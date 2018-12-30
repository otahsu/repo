#!/usr/bin/env python2.7
import sys, os, glob, re

class Reg_IHT(object):
    
    def __init__(self, *arg, **kw):
        super(Reg_IHT, self).__init__()
        self.reg_dir = os.getenv("REG_ROOT")
        self.log_dir = str(self.reg_dir) + "/Test_Arena"
        self.project = kw.get("project", "griffey")
        self.email_list = kw.get("email_list", [])

    def find_log(self):
        if os.path.exists(self.log_dir):
            # find and save file names in unix-style by a path.
            log_list = glob.glob(self.log_dir + "/*.log")
            if len(log_list) is 0:
                sys.exit("~/Test_Arena/*.log doesn't exist!")
            else:
                self.log_file = log_list[0]
        else:
            sys.exit("~/Test_Arena doesn't exist!")
    
    def send_notification(self):
        import subprocess
        
        email_str = ""
        for i in self.email_list:
           email_str += str(i) + " "
        sCmd4Send = 'echo "Please take a look at Jenkins!"|mail -s "%s regression failed!" %s'\
                    %(self.project, email_str)
        print len(sCmd4Send), sCmd4Send
        p = subprocess.Popen( sCmd4Send, shell = True, stdout = subprocess.PIPE)
        out, err = p.communicate()
        print "stdout = ", out
        print "stderr = ", err

    def check_report(self):
        file = open(self.log_file, "r")
        lines = file.readlines()
        status = lines[-2].rstrip('\n') # strip '\n' by end reversely.
        status = status.split('\t')
        print status
        error = int(status[2][7:])
        fail = int(status[3][6:])
        if (error != 0) or (fail != 0):
            msg = "Regrssions have " + "errors = %d, fails = %d!" %(error, fail)
            self.send_notification()
            # raise exception by passing non-zero argument.
            sys.exit(msg)

class Reg_Purify(Reg_IHT):
   
    def __init__(self, *arg, **kw):
        super(Reg_Purify, self).__init__()
        self.log_dir = os.getcwd() # get `pwd`.
        self.keylist = ['UMR', 'SBR', 'SBW', 'ABR', 'ABW', 'NPR', 'NPW', 'FMM',
        'FMR', 'FMW', 'FNH', 'FUM', 'MLK', 'Memory leaked']
        self.keylines = []
        self.log_list = []

    def find_log(self):
        # find and save file names in unix-style by a path.
        if os.path.exists(self.log_dir + "/purify.output"):
            self.log_list.append(self.log_dir + "/purify.output") 
        else:
            opt =  os.getenv("PURIFYOPTIONS")
            opt_list = opt.split()
            idx = -1
            for i in opt_list:
                print i
                idx = i.find("-log-file=")
                if idx != -1:
                    break
            if idx == -1:
                sys.exit("Find no Purify log file!!")
            else:
                self.log_dir =  os.path.dirname( opt_list[idx].split("=")[-1] )
                print self.log_dir
                self.log_list = glob.glob(self.log_dir + "/*.plog")
                print self.log_list
                if len(self.log_list) == 0:
                    sys.exit("Find no Purify log file!!")

    def extract_keylines(self):
        for i in self.log_list:
            file = open(i, "r")        
            while 1 :
                line = file.readline()
                if not line :
                    break
                head = line.split(':', 1)[0]
                if head in self.keylist:
                    self.keylines.append(line)
            file.close()
    
    def filter_keylines(self):
        print len(self.keylines)
        for line in self.keylines:
            head = line.split(':', 1)[0]
            if head == "Memory leaked" :
                # \d means a decimal char, + means more than 1.
                key_num = re.findall('\d+', line)
                condition = (int(key_num[0]) == 0 and int(key_num[2]) == 0)
                if condition:
                    self.keylines.remove(line)

    def check_report(self):
        self.filter_keylines()
        if len(self.keylines) > 0:
            str = ''.join(self.keylines)
            msg = "*** There is %d key error lines as list below *** \n%s "\
                    %( len(self.keylines), str )
            self.send_notification()
            # raise exception by passing non-zero argument.
            sys.exit(msg)
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    if 1:
        parser.add_argument('--type', dest='type', action='store',
                default='IHT', type=str,
                help='Key-in the regression type; default is %(default)s.')
        parser.add_argument('--project', dest='project', action='store',
                default='griffey', type=str,
                help='project name; default is %(default)s.')
        parser.add_argument('--emails', dest='emails', action='store',
                default='hsuting_huang@tsmc.com,yhuangza@tsmc.com,jhchenzg@tsmc.com,fatien@tsmc.com,yhhsuz@tsmc.com,shlozb@tsmc.com,tclint@tsmc.com,chhsuzt@tsmc.com,xinzhou@tsmc.com',
                type=str, help='email list seperated by ","; default is %(default)s.')
    else:
        parser.add_argument('type', choices=['griffey', 'purify'],
                help='choose one type of regresion.')
    cmd_args = parser.parse_args()
    email_list = cmd_args.emails.split(',')
    project = "\'" + cmd_args.project + "\'" 
    if cmd_args.type == 'IHT':
        reg_obj = Reg_IHT(project=project, email_list=email_list)
        reg_obj.find_log()
        reg_obj.check_report()
    elif cmd_args.type == 'purify':
        reg_obj = Reg_Purify(project=project, email_list=email_list)
        reg_obj.find_log()
        reg_obj.extract_keylines()
        reg_obj.filter_keylines()
        reg_obj.check_report()
    else :
        msg = "The regrssion type is not defined yet!"
        sys.exit(msg)

# vim: set ft=python ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=85:
