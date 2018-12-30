#!/usr/bin/env python2.7
import sys, os, glob, re, subprocess, shutil, time
import threading


#######################################
# Global Function
#######################################
def check_file_size(filepath):
    """
    return in bytes.
    """
    process = subprocess.Popen("ls -l " + filepath + " | awk '{print $5}'", 
                               shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out, err = process.communicate()
    if not err == '':
        sys.stdout.flush()
        print "out= ", out, "err=", err
        raise RuntimeError("check_file_size() fail!")
    return int(out)

def get_localtime_string():
    """
    Get the formatted local time string.
    """
    time_sturct = time.localtime() # get system local time. 
    time_string  = time.strftime("%y-%m-%d-%H-%M-%S", time_sturct)
    #print time_string
    return time_string

def format_walltime(start_walltime, end_walltime):
    """
    input: get from time.time(), which return wall time in sec.
    ouput: return in the format - "hr:%s min:%s sec:%s"
    """
    spend_time = int(end_walltime - start_walltime)
    sec = spend_time % 60
    spend_time = (spend_time - sec)/60
    min = spend_time % 60
    hr = (spend_time - min)/60 
    spend_time_str = "hr:%s min:%s sec:%s" %(hr, min, sec)
    return spend_time_str

###########################################
# Class Definition
###########################################
class dpLogFilter(object):
    """
    This is for parsing the latest IHT-DP log file in ./dp_log
    """
    def __init__(self, *args, **kw):
        super(dpLogFilter, self).__init__()
        self.dpLog_dir = os.path.abspath(kw.get("dir", "./dp_log"))
        self.long_runtime = kw.get("long_runtime", 1200)
        # global containers
        self.keywords = ["***", "DROP"]
        self.EPE_violation_line_list = []
        self.EPE_violation_yaml_list = []
        self.DROP_line_list = []
        self.DROP_yaml_list = []
        self.long_runtime_yaml_list = []
        self.dpLog_path = ""

        # prepare params.
        self.find_newest_dplog()
        self.parse_line()
        self.process_line_list()

    def find_newest_dplog(self):
        process = subprocess.Popen( "ls -t " + self.dpLog_dir + "/*" + "status*",
                                    shell = True, stdout = subprocess.PIPE)
        out, err = process.communicate()
        out_list = out.split('\n')
        self.dpLog_path = out_list[0]
        return self.dpLog_path
    
    def parse_line(self): #TODO: parse line between "" 
        file = open(self.dpLog_path, "r") 
        while 1 :
            line = file.readline()
            if not line:
                break
            self.parse_long_runtime_line(line)
            for key in self.keywords:
                if key not in line:
                    continue
                #print key, line
                # switch cases for different keys.
                if key == "***":
                    self.EPE_violation_line_list.append(line)
                elif key == "DROP":
                    self.DROP_line_list.append(line)
        file.close()
        #print self.EPE_violation_line_list
        #print self.DROP_line_list
    
    def parse_long_runtime_line(self, line):
        """
        Hard-parse dp_log/status_ line when it status is "FINISH/PROCESS" and Run_Time > 1200.
        """
        test_line_list = line.strip().split(' ')
        test_line_list = [i for i in test_line_list if i != ''] # remove '' in the list.
        #self.long_runtime_line_list
        try:
            status = test_line_list[1]
            if "FINISH" != status and "PROCESS" != status:
                return
            if int(test_line_list[3]) >= self.long_runtime:
                self.long_runtime_yaml_list.append(test_line_list[-1])
        except Exception as e:
            pass #print str(e)
    
    def process_line_list(self):
        for key in self.keywords:
        # switch cases for different keys
            yamlpath = None
            if key == "***":
                for i in self.EPE_violation_line_list:
                    yamlpath = i.strip(' ').split(' ')[0]
                    #print yamlpath
                    self.EPE_violation_yaml_list.append(yamlpath)
            elif key == "DROP":
                for i in self.DROP_line_list:
                    yamlpath = i.strip().split(' ')[-1]
                    self.DROP_yaml_list.append(yamlpath)
        #print self.EPE_violation_yaml_list
        #print self.DROP_yaml_list

    def do_grep(self, dir):
        INFO_list = glob.glob(dir + "/" + "*INFO*")
        print INFO_list
        ERROR_list = glob.glob(dir + "/" + "*ERROR*")
        print ERROR_list
        
        outEPE = open(".grep_EPE_violation", 'w')
        for yaml in self.EPE_violation_yaml_list :
            for INFO in INFO_list :
                sCMD = "grep -irn " + " %s "%yaml + INFO
                #print sCMD
                #TODO: multi-process write the same file have no race issue or lose line?
                #TODO: bufsize matters?
                process = subprocess.Popen( sCMD, shell = True, stdout = outEPE)#, bufsize=4096)
                #ret = process.wait()
        outEPE.close()
        
        outDROP = open(".grep_DROP", 'w')
        for yaml in self.DROP_yaml_list :
            for INFO in INFO_list :
                sCMD1 = "grep -irn " + " %s "%yaml + INFO
                process = subprocess.Popen( sCMD1, shell = True, stdout = outDROP)
            for ERROR in ERROR_list:
                sCMD2 = "grep -irn " + " %s "%yaml + INFO
                process = subprocess.Popen( sCMD2, shell = True, stdout = outDROP)

        outDROP.close()
    
    def do_summary(self):
        summary = open("summary.log", 'w')

        # cat "1. [Summary]" part 
        #TODO: How to extract line 0 to line 10
        dpLog = open(self.dpLog_path, 'r')
        for line in dpLog:
            if "2. [Task List]" in line :
                break
            summary.write(line)
        
        dpLog.close()
        
        # write lines for EPE_violation_line_list
        for line in self.EPE_violation_line_list:
            print line
            summary.write(line)
        
        # cat  .grep_EPE_violation and .grep_DROP
        if 0:
            grep1 = open(".grep_EPE_violation")
            summary.write("## EPE_violation ##\n")
            for line in grep1 :
                summary.write(line)
            grep2 = open(".grep_DROP")
            summary.write("\n ## DROP ##\n")
            for line in grep2 :
                summary.write(line)
            grep1.close()
            grep2.close()

        summary.close()
    
class JobSubmmiter(object):
    """
    140509 :
        + INPUT : It only support given a "opc_recipe_iht" repository(dir), and a "yaml_list.txt".
        + yaml_list.txt : 
            ++ It should list "*.yaml" in the "opc_recipe_iht" repository.
            ++ It support comment sign '#' of the star-of-line.
        + Can monitor the finnished yaml jobs in "./finished_yaml_jobs.txt" immediately.
    140512 :
        + check_dirs_IsEmpty(): use sleep() to pause the main-thread.
    140529 :
        + bacup the newest dp_log/status_ .
    140603 :
        + Write start-time and end-time to fininshed_yaml_jobs.txt
        + Can remove temp files explicitly.
        + TODO: Copy yaml/oas to ./BACKUP_time/long_runtime/ (xxx/out_of_spec, xxx/drop) (BACKUP can be
        softlink) and keep the file hierachy by parsing newest ./dp_log/status_. Ensure the action is done then do remove.
        + TODO: How to ensure copy dir/file has finished?
    140606:
        + TODO: Esmitate runtime of left cases in "yaml_list" by "input" oas filesize: the formula may be
                golden_runtime/golden_fileSize/cpu_num_golden * cpu_num_golen * (sum of all filesize of the left cases).
    140609:
        + Backup function for 3 categories has tested.
    140613:
        + parse only "Drop" in 2. [] section - clearify Drop meanings for 1. / 2. /3.  
    """
    def __init__(self, *args, **kw) :
        super(JobSubmmiter, self).__init__()
        # pass parameters 
        self.dir = os.path.abspath(kw.get("dir", None))
        if not os.path.isdir(self.dir) :
            raise RuntimeError("\"%s\" is not a dir!!" %self.dir)

        self.config = os.path.abspath(kw.get("config", None))
        if not os.path.isfile(self.config) :
            raise RuntimeError("\"%s\" is not a file!!" %self.config)

        # member data 
        self.yaml_list = []
        self.job_name = None
        #print self.dir, self.config
        self.temp_subdir_list = ['log', 'dp_log', 'IHT_OPC_hier', 'SimParaFiles']
        self.temp_file_list = ['eu_dp.log', 'eu_dp_pre.log']

        # prepare flow
        self.parse_cofigure(self.config)
   
        # prepare backup dir. #TODO: it should support symlink.
        self.backup_path = os.path.abspath(kw.get("backup_dir", "BACKUP"))
        if not os.path.exists(self.backup_path): 
            os.mkdir(self.backup_path)
        else:
            raise RuntimeError("./%s does already exist, please mv it!!" %self.backup_path)
            
    def __del__(self) : # destructor
        print "~JobSubmmiter()"

    def parse_cofigure(self, config) :
        file = open(config, 'r')
        while 1 :
            line = file.readline()
            if not line : #EOF
                break
            line = line.strip()
            if line[0] == '#' : # comment sign '#' for start-of-line.
                continue    
            self.yaml_list.append(line)
        file.close()
        #print "yaml_list = ", self.yaml_list
        #sys.stdout.flush()
    
    def run(self) :
        
        cwd_ori = os.getcwd() 
        os.chdir(self.dir)
        for yaml in self.yaml_list:
            if not os.path.exists(yaml):
                print "\"%s\" doesn't exist!!" %os.path.abspath(yaml)
                continue
            start_time = get_localtime_string()
            start_walltime = time.time() # wall-time in sec since epoch.
            self.job_name = (os.path.basename(yaml)).split('.')[0]
            #print self.job_name

            sCMD = "iht_opc %s" %(yaml)
            #print "run CMD =", sCMD
            if 1:
                process = subprocess.Popen( sCMD, shell = True)
            else: # redirct stderr/out to PIPE object.
                process = subprocess.Popen( sCMD, shell = True, stdout = subprocess.PIPE,
                                            stderr = subprocess.PIPE)
            out, err = process.communicate()
            
            end_time = get_localtime_string()
            end_walltime = time.time() # wall-time in sec since epoch.
            self.do_backup()
            self.clean_temp()
            spend_time_str = format_walltime(start_walltime, end_walltime)
            line = "%s : start at %s, end at %s, spending %s\n" %(self.job_name, start_time, end_time, spend_time_str)
            fstatus = open("finished_yaml_jobs.txt", 'a+')
            self.write_line_immediately(fstatus, line)
            fstatus.close() # append one line immediately.
        
        os.chdir(cwd_ori)
    
    def write_line_immediately(self, file, line):
        # fflush in libc.a -> write data to kernel buffer
        # fsync in kernal -> write data from kernal to disk
        try: 
            file.write(line)
            file.flush() 
            file_id = file.fileno() # get file descriptor id.
            os.fsync(file_id)
        except Exception as e:
            print str(e)
    
    def copy_to_dir_by_yaml_list(self, yaml_list, target_dir):
        """
        mkdir -p and cp -p for the tile yaml/oas and keep dir hierachy.
        """
        for yaml_path in yaml_list:
            basefname = os.path.basename(yaml_path)
            no_ext_fname = basefname.split('.')[0]
            dirname = os.path.dirname(yaml_path)
            #print basefname, dirname
            # mkdir -p, --parents: no error if existing, make parent directories as needed
            process = subprocess.Popen( "mkdir -p %s/%s" %(target_dir, dirname),
                                        shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            out, err = process.communicate()
            if not (out == '' and err == ''):
                sys.stdout.flush()
                print "out= ", out, "err=", err
            cp_src = os.path.join(self.dir, dirname, no_ext_fname)+'*' # use wildcard in fname.
            cp_target = os.path.join(target_dir, dirname)
            # cp -p: preserve the specified attributes (default:mode,ownership,timestamps)
            process = subprocess.Popen( "cp -p %s %s" %(cp_src, cp_target),
                                        shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            out, err = process.communicate()
            if not (out == '' and err == ''):
                sys.stdout.flush()
                print "out= ", out, "err=", err

    def do_backup(self):
        """
        Backup interest files per job. 
        """
        #TODO: ensure backup has been finished, then do next.
        # prepare stage.
        time_string  = get_localtime_string()
        job_backup_dir_path =  "%s/%s-%s" %(self.backup_path, self.job_name, time_string)
        os.mkdir(job_backup_dir_path)
        
        if 0:
            shutil.copy2(dp_log_file_path, job_backup_dir_path) #TODO: keep the file property.
            time.sleep(120) #TODO: not use this!
       
        if 1:
            logger = dpLogFilter(dir="%s/dp_log" %self.dir, long_runtime=1200) #TODO: into argpars?
            print "long_runtime_yaml_list", logger.long_runtime_yaml_list
            print "EPE_violation_yaml_list", logger.EPE_violation_yaml_list
            print "DROP_yaml_list", logger.DROP_yaml_list
        
        # copy the newest summary. 
        process = subprocess.Popen( "cp -p %s %s" %(logger.dpLog_path, job_backup_dir_path),
                                    shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        out, err = process.communicate()
        if not (out == '' and err == ''):
            sys.stdout.flush()
            print "out= ", out, "err=", err
        
        # copy splitted yaml/oas into ./long_runtime
        target_dir = os.path.join(job_backup_dir_path, "long_runtime")
        self.copy_to_dir_by_yaml_list(logger.long_runtime_yaml_list, target_dir) 
        # copy splitted yaml/oas into ./out_of_spec 
        target_dir = os.path.join(job_backup_dir_path, "out_of_spec")
        self.copy_to_dir_by_yaml_list(logger.EPE_violation_yaml_list, target_dir) 
        # copy splitted yaml/oas into ./drop
        target_dir = os.path.join(job_backup_dir_path, "drop")
        self.copy_to_dir_by_yaml_list(logger.DROP_yaml_list, target_dir) 
    
    def clean_temp(self):
        # clean temp files.
        for file in self.temp_file_list:
            sys.stdout.flush()
            try:
                os.remove(file)
            except Exception as e:
                print str(e)

        # clean temp dirs.
        for dir in self.temp_subdir_list:
            self.remove_dir_files(dir)
        
        self.remove_dir_files('IHT_OPC_hier') #TODO: need to parse it from yaml.
        self.check_dirs_IsEmpty(self.temp_subdir_list)
    
    def remove_dir_files(self, dir): # keep the top dir.
        try:
            dirpath = os.path.realpath(dir)
            for file in os.listdir(dirpath):
                file_path = os.path.join(dirpath, file)
                if os.path.isdir(file_path) :
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
        except: #TODO: need to understand exception mechanism more!
            sys.stdout.flush()
            print "ignore exception"
    
    def check_dirs_IsEmpty(self, dir_list): # pending if the dir is not empty.
        for dir in self.temp_subdir_list:
            sec_elasped = 0
            try:
                while os.listdir(dir):
                    time.sleep(0.001)
                    sec_elasped += 1
                    sys.stdout.flush()
                    print "waiting %d msec for removing %d by OS..." %(sec_elasped, dir)
            except:
                sys.stdout.flush()
                print "ignore exception for %s" %dir

class DirMonitor(threading.Thread):
    def __init__(self, *args, **kw):
        super(DirMonitor, self).__init__()
        self.dir = kw.get("dir", "./")
        print self.dir
        self.event = threading.Event() #TODO: how can it relate to the parant class obj?
        self.ran_time = 0 
        self.start()
        print "deault thread name =", self.name 

    def run(self):
        print os.listdir(self.dir)
        # check is the dir is None.
        while (not self.event.isSet()) and os.listdir(self.dir): #TODO: change it to function obj.
            time.sleep(1)
            self.ran_time += 1
            print "thread is running for %d sec" %(self.ran_time)

    def exit(self):
        print "now the thread is to exit!"
        self.event.set() # exit thread.
        

###############################################
# Test Flow
###############################################
def test_dpLogFilter(dir):
    # do log filter and summary.
    obj = dpLogFilter(dir="dp_log.my", long_runtime=1200)
    print obj.long_runtime_yaml_list
    print obj.EPE_violation_yaml_list
    print obj.DROP_yaml_list
    #obj.do_grep("fatien_140507/log")
    #obj.do_summary()

def test_DirMonitor(dir):
    thread = DirMonitor(dir="blank")
    time.sleep(2)
    thread.exit()

def test_load_yaml():
    import yaml
    yaml_dict = yaml.load(open("n10V1Tv1Vmk_tb06288600.yml"))
    print yaml_dict.keys()
    cut_design_dir = yaml_dict["split"]["cut_design_dir"]
    print type(cut_design_dir), cut_design_dir
    main_list = yaml_dict["global"]["main"]
    print type(main_list), main_list
    NR_DRC_set = yaml_dict["NR_DRC"]["Set"]
    print type(NR_DRC_set), NR_DRC_set

def test_sum_oas_size(oas_dir, prefix):
    flist = glob.glob("%s/%s*.oas" %(oas_dir, prefix))
    size_bytes = 0
    for fpath in flist:
        size_bytes += check_file_size(fpath)
     
    sum_mb = float(size_bytes)/1.e+6
    print "%s/%s*.oas size in MB is %f" %(oas_dir, prefix, sum_mb)
    return sum_mb


if __name__ == "__main__":
    # TODO: BUG- the default is wrong "./run_ihtopc_jobs.py"
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', nargs=1, help = "the path of \"yaml_list.txt\"", default="yaml_list.txt")
    parser.add_argument('-d', nargs=1, help = "the path of \"iht_recipe_opc\" repos.",
                        default="iht_recipe_opc")
    parser.add_argument('-b', nargs=1, help = "the path of \"backup\" dir.", default="BACKUP")
    
    args_namespace = parser.parse_args()
    args_dict = vars(args_namespace)
    #print args_dict['d']
    if 0:
        # run "iht_opc" serveral times.
        jobs = JobSubmmiter(dir=args_dict['d'][0], config=args_dict['i'][0], backup_dir=args_dict['b'][0])
        jobs.run()
    else:
        #test_DirMonitor("temp")
        #test_load_yaml()#"Job5.yml")
        #shutil.copytree('./srcdir/', './temp/')
        #test_dpLogFilter('./dp_log.my')
        test_sum_oas_size("/vol0/opcmask/140116_tmfj86_778a/gdsin", "tb")


# vim: set ft=python ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=105:
