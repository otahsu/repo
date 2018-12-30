from SCons.Script import AddOption
import os, sys

print "%s offers default options!" %str(__file__)
os.environ['IHTROOT'] = "/vol0/ap/iht/x86_64_rh4.a/ihtruntime" #TODO: hard path.

# default path.
AddOption('--ihtruntime-path', dest='ihtruntime_path',
    action='store', default=os.environ.get('IHTROOT', ''),
    help='The library path of boost, gtest, glog...; default is "%default".')

# options for directories.
AddOption('--build-dir', dest='build_dir',
    action='store', default='build',
    help='Building directory; default is "%default".')
AddOption('--purify', dest='purify', action='store_true', default=False,
    help='Build purify version; default is %default.')
AddOption('--quantify', dest='quantify', action='store_true', default=False,
    help='Build quantify version; default is %default.')
AddOption('--library-dir', dest='library_dir',
    action='store', default='lib',
    help='The directory for produced library files; default is "%default".')
AddOption('--binary-dir', dest='binary_dir',
    action='store', default='bin',
    help='The directory for produced binary files; default is "%default".')

# options for compilation.
AddOption('--debug-build', dest='debug', action='store_true', default=False,
    help='Debugging build; default is %default.')
AddOption('--warnings', dest='warnings', action='store',
    default='no-deprecated,no-write-strings',
    help='Comma-separated list of warning options to the compiler; '
    'default is %default.')
AddOption('--flags', dest='flags', action='store', default='',
    help='Comma-separated list of compiler flags; default is %default.')
AddOption('--link-flags', dest='linkflags', action='store',
    default='-static-libgcc,-static-libstdc++',
    help='Comma-separated list of linker flags; default is %default.')
AddOption('--mocflags', dest='mocflags', action='store',
    default='-DQT_NO_DEBUG,-DQT_GUI_LIB,-DQT_CORE_LIB,-DQT_SHARED',
    help='Comma-separated list of moc flags; default is %default.')

from SCons.Environment import Environment
class Environment_IHT(Environment):
    def __init__(self, *args, **kw):
        print "init Environment_IHT"
        super(Environment_IHT, self).__init__(*args, **kw)
        self.SetLibrayPath()
        self.SetLibrayLink()

# vim: set ft=python ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=85:
