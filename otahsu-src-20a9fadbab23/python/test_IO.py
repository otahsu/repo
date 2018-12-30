#! /usr/bin/env python2.7
import time, os, sys, re, argparse

def write_file(filename, bytes):
    if isinstance(filename, basestring) and isinstance(bytes, int):
        if os.path.isfile(filename):
            os.remove(filename)
        file = open(filename, 'a+')
        count = 0 
        while count < bytes:
            file.write("x")
            count += 1
        file.close()
    else:
        print filename, bytes
        raise RuntimeError("type of paramter of write_file(filename, bytes) is wrong!")
    
def read_file(filename, bytes):
    if isinstance(filename, basestring) and isinstance(bytes, int):
        file = open(filename, 'r')
        file.read(bytes)
        file.close()
    else:
        print filename, bytes
        raise RuntimeError("type of paramter of read_file(filename, bytes) is wrong!")

def time_diff(start, end):
    if isinstance(start, float) and isinstance(end, float):
        ms_total = int( (end - start)*1000 )
        msec = ms_total % 1000
        ms_for_sec =  int( (ms_total - msec)/1000 )
        sec =  ms_for_sec % 60
        sec_for_mins = int( ( ms_for_sec - sec )/60 )
        mins = sec_for_mins 
        print "(min, sec, msec) = (%s, %s, %s) " %(mins, sec, msec) 
    else:
        raise RuntimeError("type of paramter of time_diff(start, end) is wrong!")

def read_write_files():
    with open('w1.txt', 'w') as f1: # embeded try-expect structure inside.
        print "the current byte-position of the reading file is", f1.tell()
        f1.write('0\n1\n2')
        f1.write('\n4')
        print "the current byte-position of the reading file is", f1.tell()
        f1.close()
    with open('w1.txt', 'r') as f1:
        print "the current byte-position of the reading file is", f1.tell()
        ls = f1.readlines()
        print type(ls), ls
        print "the current byte-position of the reading file is", f1.tell()
        f1.seek(2)
        print "the current byte-position of the reading file is", f1.tell()
        print "the current byte in ACSII =", f1.read(1)
        print "the current byte-position of the reading file is", f1.tell()
        f1.close()
    with open('w1.txt', 'r+') as f1:
        # 'r+'(udpating read) can read/write and dosen't truncate(delete) the opened
        # file if it exists, but the file-pointer position is 0 at the
        # beginging.
        print "the current byte-position of the reading file is", f1.tell()
        print "the current byte in ACSII =", f1.read(1)
        f1.seek(20)
        print "the current byte-position of the reading file is", f1.tell()
        print "the current byte in ACSII =", f1.read(1) # get '\0'.
        # In Vim, ^@ represents '\0'
        f1.write('g\0\0\0\0')# '\n' will be added before 'EOF'. 
        f1.close()
    with open('w2.txt', 'w+') as f2:
        # 'w+'(udpating write) can read/write but truncate(delete) the opened
        # file if it exists. 
        f1 = open('w1.txt', 'r')
        print "the current byte-position of the file(\'w2\') is", f2.tell()
        str_f1 = f1.read()#TODO: Getting EOF by brute-force. What's the best approach?
        f1.close()
        f2.write(str_f1)
        print "the current byte-position of the file(\'w2\') is", f2.tell()
        f2.write("\ne1\ne2\ne3\n")
        print "the current byte-position of the file(\'w2\') is", f2.tell()
        # file.seek( [, os.SEEK_SET(absolute file position|os.SEEK_CUR|os.SEEK_END)]) 
        #print os.SEEK_SET, os.SEEK_CUR, os.SEEK_END
        f2.seek(-3, 1) # os.SEEK_CUR == 1
        print "the current byte-position of the file(\'w2\') is", f2.tell()
        print "the current byte in ACSII =", f2.read(1) 
        f2.seek(-3, 2) # os.SEEK_END == 2
        print "the current byte-position of the file(\'w2\') is", f2.tell()
        print "the current byte in ACSII =", f2.read(1)
        
        try:
            f2.seek(-1, 0) # os.SEEK_SET == 0. It' an invalid statement.
        except Exception as e:
            print e
        f2.close()
    
    with open('w2.txt', 'a') as f:
        # 'a' is to append to EOF of the file it exit, but cant't read.
        print "the current byte-position of the file(\'w2\') is", f.tell()
        f.write('a1')
        print "the current byte-position of the file(\'w2\') is", f.tell()
        #print "the current byte in ACSII =", f.read(1) #
        f.close()
    
    with open('w3.txt', 'a') as f:
        print "the current byte-position of the file(\'w3\') is", f.tell()
        f.write('a1')
        print "the current byte-position of the file(\'w3\') is", f.tell()
        f.close() 
    
    with open('w2.txt', 'a+') as f:
        # 'a+' is to append to EOF of the file it exit, and can read.
        # TODO: But the file-pointer postion at the 1st time is confusion!
        print "the current byte-position of the file(\'w2\') is", f.tell() #TODO: Why is it 0, not 37?
        print "the current byte in ACSII =", f.read(1)
        f.write('a2')
        print "the current byte-position of the file(\'w2\') is", f.tell()
        
    #with open('w2.txt', 'w') as f3:
    #    # truncate(delete) the opened file if it exists,
    #    f3.close()
    
def test_io():
    time_start = time.time()
    bytes = 10 * 1024 * 1024 # 10 MBytes
    write_file(".temp", bytes)
    time_end = time.time()
    print "write %s bytes take " %bytes ,
    time_diff(time_start, time_end)
    
    time_start = time.time()
    read_file(".temp", bytes)
    time_end = time.time()
    print "read %s bytes take " %bytes ,
    time_diff(time_start, time_end)

def test_file():
    read_write_files()

def test_re():
    pass

if __name__ == "__main__":
    # Argument Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--test_key', dest='test_key', action='store',
                default='file', type=str,
                help='Choose to test either \'io\',\'file\',\'re\' module; default is %(default)s.')
    #parser.add_argument('-o', '--outputCSV', dest='outputCSV', action='store',
    #            default='DesignGauge.csv', type=str,
    #            help='Design-Gauge\'s CSV; default is %(default)s.')
    cmd_args = parser.parse_args()
    print cmd_args, type(cmd_args), cmd_args.__dict__
    # http://openhome.cc/Gossip/Python/LambdaExpression.html
    # The inimated "switch structure" : 
    key = 'io' # 'io' / 'file' / 're' 
    
    flow_ctl_dict = { 'io': (lambda : test_io()), 'file': (lambda : test_file()),
                      're': (lambda : test_re()) }
    func_obj = flow_ctl_dict.get(cmd_args.test_key, None)
    #print func_obj # <function <lambda> at 0x2af378887410>
    func_obj() #TODO: excute a fuction-object?

# vim: set ft=python ff=unix fenc=utf8 ai et sw=4 ts=4 tw=79: