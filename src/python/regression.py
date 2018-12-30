# -*- coding: UTF-8 -*-
#
# Copyright (C) 2012 Bella Chang <fjchangf@tsmc.com> and Yung-Yu Chen
# <yychenzv@tsmc.com>.  All rights reserved.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
###########################################################
# you should know: 
# 1. setenv REG_ROOT = */reg_griffey/
# 2. make sure your tag is in */reg_griffey/tag_list.txt
###########################################################
"""
This module represents the entities in regression testing.
"""
class Runtime(object):
    """
    Runtime environment for regression tests.

    :ivar wdir: working directory.  It is made always absolute path.
    :itype wdir: str
    """
    def __init__(self):
        import os, sys
        self.args_list = sys.argv
        self.logfile = None
        self.args_dict = self.get_args_dict()
        self.reg_path = os.getenv('REG_ROOT')
        self.tagfile = os.path.join(self.reg_path, "tag_list.txt")
        self.yaml_list = self.get_yaml_list()
        self.cmd_list = [" "]
        self.wdir = os.path.join(os.getcwd(), str(os.getpid())+"_test")
        self.logname = os.path.join(os.getcwd(), str(os.getpid())+".log")
        if not '-c' in sys.argv and self.yaml_list:
            os.mkdir(self.wdir)
            self.logfile = open(self.logname,'w')

    def __del__(self):
        if self.logfile is not None:
            self.logfile.close()

    def echo(self, msg, write_log = False, stdout = True):
        import sys
        if stdout == True:
            sys.stdout.write(msg+'\n')
            sys.stdout.flush()
        if write_log == True:
            self.logfile.write(msg+'\n')

    def is_ysev_OK(self, ysev):
        if not ysev in ['H', 'M', 'L']:
            self.echo("severity:\t%s --> sould be H/M/L" %ysev)
            return 0
        else:
            return 1

    def is_ytags_OK(self, ytag_list, tag_list):
        undef_tags = [i for i in ytag_list if i not in tag_list]
        if undef_tags:
            self.echo('tag:     \t%s does not exist' %undef_tags)
            return 0
        else:
            return 1

    def is_ygolden_OK(self, y_dict, y_dir):
        import os
        '''
        undef_g : undefined golden_file list
        y_dir : the dir path of this yaml file
        '''
        golden = [i for i in y_dict if i[0] == 'g' and y_dict[i] ]
        for i in golden:
            if y_dict[i]:
                undef_g = [i for i in y_dict[i] if not
                    os.path.exists(os.path.join(y_dir,'golden',i))]
                if undef_g:
                    self.echo("golden:  \t%s \t does not exist in %s" %(undef_g,
                        os.path.join(y_dir,'golden')))
            if i == golden[-1]:
                return 0
        return 1

    def is_ycomment_OK(self, y_comment):
        if y_comment == None:
            self.echo("comment:\tempty")
            return 0
        else:
            return 1
        
    def is_yaml_OK(self, fyaml):
        import os
        from yaml import load
        if os.path.exists(fyaml):
            taglist_file = open(self.tagfile)
            tag_list = taglist_file.read().split("\n")
            taglist_file.close()
            yaml_file = open(fyaml)
            y_dict = load(yaml_file)
            yaml_file.close()
            if self.is_ysev_OK(y_dict['severity']) *\
                self.is_ytags_OK(y_dict['tags'], tag_list) *\
                self.is_ygolden_OK(y_dict,os.path.dirname(fyaml))*\
                self.is_ycomment_OK(y_dict['comment']) == 1:
                self.echo("OK:     \t%s" %'/'.join(fyaml.split("/")[-3:]))
                return True
            else:
                self.echo("Fail:   \t%s" %'/'.join(fyaml.split("/")[-3:]))
                return False
        else:
            self.echo("%s\tdoes not exist" %'/'.join(fyaml.split("/")[-3:]))
            return False

    def get_yaml_list(self):
        if self.is_cf_opt_OK():
            if '-c' in self.args_list:
                self.is_yaml_OK(self.args_list[2])
                return None
            else:
                return self.get_fyaml_list()
        else:
            return None

    def get_args_dict(self):
        import sys
        import argparse
        description = "Code Regression: "
        description += """1. setenv REG_ROOT = */reg_griffey/\n2. make sure your
    tag is in */reg_griffey/tag_list.txt\n3. you can only turn on 'one' option
    or ('-s' and '-t' 2 options) """
        parser = argparse.ArgumentParser(description=description)
        group1 = parser.add_mutually_exclusive_group()
        group1.add_argument('-c', nargs=1, help='check the yaml format')
        group1.add_argument('-f', nargs='+', help='run the yaml(s)')
        group1.add_argument('-a', action='store_true', help='run all yamls in */REG_ROOT/tag_list.txt')
        parser.add_argument('-s', nargs='+', choices='HML',
                            help="""run the yaml(s) with any of severities
                            flags. Ex. -s H M""")
        parser.add_argument('-t', nargs='+',
                            help="""run the yaml(s) with any of tag flags. Ex.
                            -t A B C""")
        g1 = ['-a', '-c', '-f']
        if '-s' in self.args_list or '-t' in self.args_list:
            if set(g1) & set(self.args_list):
                self.echo("argument -t or -s: not allowed with argument\
                        -a, -c, -f")
        elif len(self.args_list) == 1:
            self.echo(str(parser.print_help()))
        return vars(parser.parse_args())

    def is_cf_opt_OK(self):
        import os
        #check -c --> should be "-c yamlpath"
        if '-c' in self.args_list:
            if self.args_dict['c'][0][-4:] != '.rgr':
                self.echo("[Usage]: runReg.py -c *.rgr")
                return False
            elif not os.path.exists(self.args_dict['c'][0]):
                self.echo("%s does not exist" %self.args_dict['c'])
                return False
            else:
                return True
        #check -f --> should be "-f yamlpaths"
        elif '-f' in self.args_list:
            for i in self.args_dict['f']:
                if i[-4:] != '.rgr':
                    self.echo("[Usage]: runReg.py -f *.rgr")
                    return False
                elif not os.path.exists(i):
                    self.echo("%s does not exist" %i)
                    return False
            return True
        else:
             return True
    
    def get_filtered_file_list(self, dir, ext):
        import fnmatch, os
        matches = []
        # usage: fyaml_list_all = self.get_filtered_file_list(self.reg_path, "*.rgr")
        # it will get all rgr files no matter the deep of hierachy
        for root, dirnames, filenames in os.walk(dir):
            for filename in fnmatch.filter(filenames, ext):
                matches.append(os.path.join(root, filename))
        return matches

    def get_fyaml_list(self):
        import os, glob
        from yaml import load
        fyaml_list = []
        if '-a' in self.args_list:
            fyaml_list = glob.glob(os.path.join(self.reg_path, "*", "*",
                        "*.rgr"))+ glob.glob(os.path.join(self.reg_path, "*", "*", "*", "*.rgr"))
            if 1: # run only cases that have any tag in tag_list.txt
                taglist_file = open(self.tagfile)
                tag_list = taglist_file.read().split("\n")
                taglist_file.close()
                print tag_list
                fyaml_list_filtered = [] 
                for fyaml in fyaml_list:
                    yaml_file = open(fyaml)
                    y_dict = load(yaml_file)
                    yaml_file.close()
                    for i in range(len(tag_list)):
                        if tag_list[i] in y_dict["tags"]:
                            fyaml_list_filtered.append(fyaml)
                fyaml_list = fyaml_list_filtered
                #print fyaml_list
        elif '-f' in self.args_list:
            fyaml_list = [os.path.abspath(path) for path in self.args_list[2:]]
        elif '-s' in self.args_list or '-t' in self.args_list:
            fyaml_list_all = glob.glob(os.path.join(self.reg_path, "*", "*",
                        "*.rgr")) + glob.glob(os.path.join(self.reg_path, "*", "*", "*", "*.rgr"))
            for fyaml in fyaml_list_all:
                yaml_file = open(fyaml,'r')
                yaml_dict = load(yaml_file)
                yaml_file.close()
                if self.is_allopts_match(self.args_dict['t'], yaml_dict["tags"],
                        self.args_dict['s'], [yaml_dict["severity"]]):
                    fyaml_list.append(fyaml)
        sorted(fyaml_list)
        return fyaml_list

    def is_allopts_match(self, iptag_list, tags, ipsev_list, sevs):
        ans, check_ans = 0, 0
        if iptag_list:
            ans += 1
        if ipsev_list:
            ans += 1
        if iptag_list and list(set(iptag_list) & set(tags)): 
            check_ans += 1
        if ipsev_list and list(set(ipsev_list) & set(sevs)): 
            check_ans += 1
        if check_ans == ans:
            return True
        else:
            return False

    def status_report(self):
        import os, sys
        self.logfile.close()
        logfile = open(os.path.join(os.path.dirname(self.wdir), str(os.getpid()) + ".log"))
        logdata = logfile.readlines()
        logfile.close()
        self.logfile = open(os.path.join(os.path.dirname(self.wdir),
                    str(os.getpid()) + ".log"), 'a')
        ok_num, err_num, fail_num, line_num= 0, 0, 0, 0
        for i in logdata:
            if i[:2] == 'OK':
                ok_num += 1
            elif i[:2] == 'Fa':
                fail_num += 1
            elif i[:2] == 'Er':
                err_num += 1
            else:
                line_num +=1
        self.echo("\ncode regression folder: %s_test" %str(os.getpid()), True)
        self.echo("Total: %s\tOK: %s\tError: %s\tFail: %s\n" % (
            len(logdata)-line_num, ok_num, err_num, fail_num), True)

default_runtime = Runtime()

class Executable(object):
    """
    The executable for regression tests.

    :ivar runtime: the runtime environment for this executable.  Must be set
        through the constructor.
    :itype runtime: Runtime
    """
    def __init__(self, runtime):
        self.runtime = runtime

    @staticmethod
    def link_needs(funcase_path):
        import os
        for i in os.listdir(funcase_path):
            os.symlink(os.path.abspath(os.path.join(funcase_path,i)),i)

    @staticmethod
    def run_lvl(new, fullgolden_stream, tmp_path):
        import os
        from .lvl import Run_LVL_Auto
        old_files = os.listdir(tmp_path)
        lvl_ans = Run_LVL_Auto(new, fullgolden_stream)
        new_items = list(set(os.listdir(tmp_path)) - set(old_files))
        # Run_LVL_Auto returns "nDiffCnt"
        if lvl_ans == 0:
            os.remove(os.path.join(tmp_path, new))
            for item in new_items:
                os.remove(os.path.join(tmp_path, item))
            return 1
        elif lvl_ans == 1:
            return 0
        else:
            return -1

    @staticmethod
    def run_diff(new, fullgolden_log, tmp_path):
        import os
        from difflib import unified_diff
        new_file = open(new)
        golden_file = open(fullgolden_log) 
        diff = unified_diff(new_file.readlines(), golden_file.readlines(),
            fromfile = new, tofile = fullgolden_log)
        diff = [i for i in diff]
        new_file.close()
        golden_file.close()
        if diff != []:
            diff_file = open(os.path.basename(fullgolden_log)+"_diff.log", 'w')
            for line in diff:
                diff_file.writelines(line)
            diff_file.close()
            return 0
        else:
            os.remove(os.path.join(tmp_path, new))
            return 1

    @staticmethod
    def get_pathtails(path, num):
        import os
        split_sig = path.rstrip(os.path.basename(path))[-1]
        split_path_list = path.split(split_sig)
        return os.path.join(*split_path_list[num:])

    def get_runtime(self, seconds):
        sec = seconds%60
        min = seconds/60
        hr  = min/60
        day = hr/24
        if day >= 1:
            runtimeMsg = "\trun time: %d days %d:%d:%.0f seconds." %(day, hr, min, sec)
        else:
            runtimeMsg = "\trun time: %d:%d:%.0f seconds." %(hr, min, sec)
        return runtimeMsg

    def __call__(self, tmp_path, yaml_dict, REG_logfile, yamlpath):
        import os, shutil, commands, time
        from subprocess import Popen, PIPE
        from dirProcessor import TGZ_dir
        REG_logfile.write('in Executable.call temp path: %s\n' %tmp_path)
        os.mkdir(tmp_path)
        os.chdir(tmp_path)
        self.link_needs(os.path.dirname(yamlpath))
        maincmd = yaml_dict['command'].split(' ')[0]
        if 1:
            # run regression with Purify build.
            if ( os.getenv("REG_PURIFY") == 'yes' ):
                str_list = yaml_dict['command'].split(' ', 1)
                if not '.' in str_list[0]:
                    str_0 = str_list[0] + '.pur'
                    str_1 = str_list[1]
                    # overwrite command string and dict.
                    yaml_dict['command'] = str_0 + ' ' + str_1
                    maincmd = str_0
                    print self.runtime.args_dict
            print self.runtime.args_dict
        
        if maincmd != self.runtime.cmd_list[-1]:
            self.runtime.cmd_list.append(maincmd)
            self.runtime.echo("which\t%s:\t%s\n" %(maincmd,
                commands.getoutput('which %s' %maincmd)), True)
        self.startTime = time.time()
        Popen(yaml_dict['command'], shell=True, stdout=PIPE).stdout.read()
        runTimeMsg = self.get_runtime(time.time() - self.startTime)
        outputs = [i for i in os.listdir(tmp_path) if i in
        yaml_dict['golden_streams'] or i in yaml_dict['golden_logs']]

        golden_nol = len(yaml_dict['golden_streams']) + \
                     len(yaml_dict['golden_logs'])
        check_ans = err_num = 0
        msg = ''
        if len(outputs) == 0 or len(outputs) != golden_nol:
            if len(outputs) == 0:
                msg += "No outputs"
            else:
                miss_golden_list = [i for i in yaml_dict['golden_streams']\
                                   if not i in outputs]
                miss_golden_list.extend([i for i in yaml_dict['golden_logs']\
                                        if not i in outputs])
                msg += "Missing file %s" %miss_golden_list
            self.runtime.echo('Error' + '\t' +
                    self.get_pathtails(yamlpath, -3) + '\t' + msg+ runTimeMsg, True)
            os.chdir("..")
            TGZ_dir(self.get_pathtails(tmp_path, -1))
            shutil.rmtree(tmp_path)
        else:
            for o in outputs:
                if o.split('.')[-1] == 'oas' or o.split('.')[-1] == 'gds':
                    gs = yaml_dict['golden_streams']
                    golden_path = os.path.join(os.path.dirname(yamlpath), 'golden', o)
                    if o in gs and os.path.exists(golden_path):
                        run_lvl_ans = self.run_lvl(o, os.path.join(
                            os.path.dirname(yamlpath), "golden", gs[gs.index(o)]), tmp_path)
                        check_ans += run_lvl_ans
                        if run_lvl_ans < 0:
                            msg += "%s is not a valid file" %o
                            err_num += 1
                    else:
                        msg += '%s does not exist in golden dir' %o
                        err_num += 1
                else:
                    gl = yaml_dict['golden_logs']
                    golden_path = os.path.join(os.path.dirname(yamlpath), 'golden', o)
                    if o in gl and os.path.exists(golden_path):
                        check_ans += self.run_diff(o, os.path.join(
                            os.path.dirname(yamlpath), "golden", gl[gl.index(o)]), tmp_path)
                    else:
                        msg += '%s does not exist in golden dir' %o
                        err_num += 1
            os.chdir("..")
            if err_num > 0:
                TGZ_dir(self.get_pathtails(tmp_path, -1))
                shutil.rmtree(tmp_path)
                self.runtime.echo('Error' + '\t' + 
                    self.get_pathtails(yamlpath, -3) + '\t' + msg + runTimeMsg, True)
            elif check_ans < len(outputs):
                TGZ_dir(self.get_pathtails(tmp_path, -1))
                shutil.rmtree(tmp_path)
                self.runtime.echo('Fail' + '\t' + 
                    self.get_pathtails(yamlpath, -3) + '\t' + msg + runTimeMsg, True)
            elif check_ans == len(outputs):
                shutil.rmtree(tmp_path)
                self.runtime.echo('OK' + '\t' + 
                    self.get_pathtails(yamlpath, -3) + '\t' + msg + runTimeMsg, True)
            else:
                TGZ_dir(self.get_pathtails(tmp_path, -1))
                shutil.rmtree(tmp_path)
                self.runtime.echo('Error' + '\t' + 
                    self.get_pathtails(yamlpath, -3) + '\t' + msg + runTimeMsg, True)

class Regression(object):
    """
    This class represent the runtime and status of a regression test.

    :ivar runtime: the runtime environment for this regression test.  Must be
        set through the constructor.
    :itype runtime: Runtime
    :ivar yamlpath: the path to the yaml file for this regression test.  It is
        made always an absolute path.  Must be set through the constructor.
    :itype yamlpath: str
    :ivar tags: a list of tags for the regression test.
    :itype tags: list
    :ivar status: the status of this regression test.
    :itype status: str
    """
    
    def __init__(self, yamlpath, runtime=None):
        import os
        if runtime is None:
            runtime = default_runtime
        self.runtime = runtime
        self.yamlpath = yamlpath
        if not os.path.isabs(self.yamlpath):
            self.yamlpath = os.path.abspath(yamlpath)
        self.tags = list()
        self.status = None

    @property
    def wdir(self):
        return self.runtime.wdir

    @property
    def logfile(self):
        return self.runtime.logfile

    def get_epath(self):
        # get tmp path
        import os, re
        split_sig = self.yamlpath.rstrip(os.path.basename(self.yamlpath))[-1]
        fname = "_".join([self.yamlpath.split(os.sep)[-3],
                self.yamlpath.split(os.sep)[-2]])
        epath = os.path.join(self.wdir,fname)
        epath = re.sub(" ", "",epath)
        return epath

    def run(self):
        """
        Run the regression test.

        :return: the status of execution.
        :rtype: str
        """
        import os, sys
        from yaml import load
        # epath: execute in this path. (tmp_path)
        if self.yamlpath == self.runtime.yaml_list[0]:
            self.runtime.echo("command:  " + ' '.join(self.runtime.args_list),
                    True, False)
            self.runtime.echo('\ncode regression folder: %s_test'
                    %str(os.getpid()), True)
        epath = self.get_epath()
        self.runtime.logfile.write('in Regression.run temp path: %s\n' %epath)
        yaml_file = open(self.yamlpath)
        yaml_data = load(yaml_file)
        yaml_file.close()
        executable = Executable(runtime=self.runtime)
        return executable(epath, yaml_data, self.logfile, self.yamlpath)

# vim: set ft=python ff=unix fenc=utf8 ai et sw=4 ts=4 tw=79:
