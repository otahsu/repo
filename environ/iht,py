import os, sys
from SCons.Script import AddOption, GetOption

def search_src(env, source_dirs, extfn='.cpp', **kw):
    """
    Inside-scope function.
    Find src files, copy them to a variant dir, return FileNodes list.
    """
    build_dir = kw.get('build_dir', env['BUILD_DIR'])
    source_files = list()
    for spath in source_dirs:
        if not os.path.isdir(str(spath)):
            raise OSError('"%s" should be a directory but is a file'%spath)
        dst = '%s/%s' % (build_dir, str(spath))
        env.VariantDir(dst, spath) # build .o in another dir, be saved within env in .sconsign
        if isinstance(extfn, basestring):
            source_files.extend(env.Glob('%s/*%s' % (dst, extfn))) # find subdir/xx.cpp
        else:
            for thisextfn in extfn: #TODO: what's its intention?
                source_files.extend(env.Glob('%s/*%s' % (dst, thisextfn)))
    
    return source_files

def search_library(env, libname): 
    """
    Return a file node by the full path of a lib.
    """
    libfile = None
    for dir in env['LIBPATH']:
        libpath = os.path.join(dir, libname)
        if os.path.exists(libpath):
            libfile = env.File(libpath)
            break
    print libname, libfile
    
    return libfile

def custom_compiler(env, source_dirs, extfn='.cpp', **kw):
    """
    Generate .o files.
    """
    build_dir = kw.get('build_dir', env['BUILD_DIR'])
    source_files = search_src(env, source_dirs, extfn='.cpp', **kw)
    
    # clone and modify the environment.
    env = env.Clone()
    
    return env.Object(source_files)

def moc_make(env, source_dirs, **kw):
    """
    Generate moc_xxx.cpp from xxx.h .
    """
    source_files = search_src(env, source_dirs, extfn='.h', **kw)
    results = [] 
    for fNode in source_files:
        fPath = str(fNode)
        base = os.path.basename(fPath)
        targetFileName = 'moc_%s.cpp' % os.path.splitext(base)[0]
        targetFileName = os.path.join(os.path.dirname(fPath), targetFileName)
        results.extend(env.Moc(targetFileName, fPath))
    
    return results

def custom_linker( env, target_name, nodes=None, libs=None, **kw):
    """
    To support link stage.
    """
    library_dir = kw.get('library_dir', env['LIBRARY_DIR'])
    binary_dir = kw.get('binary_dir', env['BINARY_DIR'])
    purify_on= kw.get('purify_on', env['PURIFY_ON'])
    quantify_on = kw.get('quantify_on', env['QUANTIFY_ON'])
    results = list()
    
    # clone and modify the environment.
    env = env.Clone()
    if libs is not None:
        env.Prepend(LIBS=libs) #TODO: use Prepend or Append?
        # resolve the link order automatically.
        env['_LIBFLAGS'] = ' -Wl,--start-group ' + env['_LIBFLAGS'] + ' -Wl,--end-group '

    # link stage.
    if kw.get('want_static', False):
        env.Append(LINKFLAGS=['-static-libgcc', '-static-libstdc++'])
        results.extend(env.StaticLibrary(
            '%s/%s' % (library_dir, target_name), nodes))
    if kw.get('want_shared', False):
        results.extend(env.SharedLibrary(
            '%s/%s' % (library_dir, target_name), nodes))
    if kw.get('want_pywrap', False):
        shlibprefix = env['SHLIBPREFIX']
        env['SHLIBPREFIX'] = ''
        results.extend(env.SharedLibrary(
            '%s/%s' % (library_dir, target_name), nodes))
        env['SHLIBPREFIX'] = shlibprefix
    if kw.get('want_executable', False):
        env.Append(LINKFLAGS=['-static-libgcc', '-static-libstdc++'])
        if purify_on:
            env['LINK'] = 'purify -best-effort -locking=no -always-use-cache-dir %s' %env['LINK']
            target_name = target_name + '.pur'
        elif quantify_on:
            env['LINK'] = 'quantify -best-effort -locking=no -always-use-cache-dir %s' %env['LINK']
            target_name = target_name + '.qua'
        results.extend(env.Program(
            '%s/%s' % (binary_dir, target_name), nodes))
    
    return results

def custom_make(env, target_name, source_dirs,
        extfn='.cpp', libs=None, do_static=False, **kw):
    
    # grab environment settings.
    build_dir = kw.get('build_dir', env['BUILD_DIR'])
    library_dir = kw.get('library_dir', env['LIBRARY_DIR'])
    binary_dir = kw.get('binary_dir', env['BINARY_DIR'])
    purify_on= kw.get('purify_on', env['PURIFY_ON'])
    quantify_on = kw.get('quantify_on', env['QUANTIFY_ON'])
    
    # clone and modify the environment.
    env = env.Clone()
    if libs is not None:
        env.Prepend(LIBS=libs) #TODO: use Prepend or Append?
        # resolve the link order automatically.
        env['_LIBFLAGS'] = ' -Wl,--start-group ' + env['_LIBFLAGS'] + ' -Wl,--end-group '

    if do_static:
        env.Prepend(LINKFLAGS='-static')
    
    # prepare build directory.
    source_files = list()
    for spath in source_dirs:
        if not os.path.isdir(str(spath)):
            raise OSError('"%s" should be a directory but is a file'%spath)
        dst = '%s/%s' % (build_dir, str(spath))
        env.VariantDir(dst, spath) # build target files in a separate dir from src.
        if isinstance(extfn, basestring):
            source_files.extend(env.Glob('%s/*%s' % (dst, extfn)))
        else:
            for thisextfn in extfn:
                source_files.extend(env.Glob('%s/*%s' % (dst, thisextfn)))
        
        if kw.get('with_moc', False): #TODO: libQtKit.a may has dublicate .o
            for fn in env.Glob('%s/*.h' % dst):
                fn = str(fn)
                mainfn = os.path.basename(fn)
                cfn = 'moc_%s.cpp' % os.path.splitext(mainfn)[0]
                cfn = os.path.join(os.path.dirname(fn), cfn)
                source_files.extend(env.Moc(cfn, fn))
    
    results = list()
    # link.
    if kw.get('want_static', False):
        env.Prepend(LINKFLAGS=['-static-libgcc', '-static-libstdc++'])
        results.extend(env.StaticLibrary(
            '%s/%s' % (library_dir, target_name), source_files))
    if kw.get('want_shared', False):
        results.extend(env.SharedLibrary(
            '%s/%s' % (library_dir, target_name), source_files))
    if kw.get('want_pywrap', False):
        shlibprefix = env['SHLIBPREFIX']
        env['SHLIBPREFIX'] = ''
        results.extend(env.SharedLibrary(
            '%s/%s' % (library_dir, target_name), source_files))
        env['SHLIBPREFIX'] = shlibprefix
    if kw.get('want_executable', False):
        env.Prepend(LINKFLAGS=['-static-libgcc', '-static-libstdc++'])
        if purify_on:
            env['LINK'] = 'purify -best-effort -locking=no -always-use-cache-dir %s' % env['LINK']
            target_name = target_name + '.pur'
        elif quantify_on:
            env['LINK'] = 'quantify -best-effort -locking=no -always-use-cache-dir %s' % env['LINK']
            target_name = target_name + '.qua'
        results.extend(env.Program(
            '%s/%s' % (binary_dir, target_name), source_files))
    
    return results

def quick_make(env, target_name, extfn='.cpp', libs=None, do_static=False, **kw):
    """
    Support flattern reposirory(no build/, src/, inc/ ...etc.)
    """
    # grab environment settings.
    purify_on= kw.get('purify_on', env['PURIFY_ON'])
    quantify_on = kw.get('quantify_on', env['QUANTIFY_ON'])
    
    # clone and modify the environment.
    env = env.Clone()
    if libs is not None:
        env.Prepend(LIBS=libs) #TODO: use Prepend or Append?
        # resolve the link order automatically.
        env['_LIBFLAGS'] = ' -Wl,--start-group ' + env['_LIBFLAGS'] + ' -Wl,--end-group '

    if do_static:
        env.Prepend(LINKFLAGS='-static')
    
    # prepare build directory.
    source_files = list()
    if isinstance(extfn, basestring):
        source_files.extend(env.Glob("*%s" %extfn))
        print "The found src files: ",
        for i in source_files:
            print str(i),
        print "\n"
    else:
        raise RuntimeError("%s is not a basestring extension." % str(extfn))

    results = list()
    # link.
    if kw.get('want_static', False):
        env.Append(LINKFLAGS=['-static-libgcc', '-static-libstdc++'])
        results.extend(env.StaticLibrary(
            '%s' % (target_name), source_files))
    if kw.get('want_shared', False):
        results.extend(env.SharedLibrary(
            '%s' % (target_name), source_files))
    if kw.get('want_executable', False):
        env.Append(LINKFLAGS=['-static-libgcc', '-static-libstdc++'])
        if purify_on:
            env['LINK'] = 'purify -best-effort -locking=no -always-use-cache-dir %s' % env['LINK']
            target_name = target_name + '.pur'
        elif quantify_on:
            env['LINK'] = 'quantify -best-effort -locking=no -always-use-cache-dir %s' % env['LINK']
            target_name = target_name + '.qua'
        results.extend(env.Program('%s' %(target_name), source_files))
    
    return results

def set_libray_path(env):
    if GetOption('ihtruntime_path'):
        # include iht runtime lib - boost, gtest, glog ...
        env.Append(CPPPATH=['%s/include' % GetOption('ihtruntime_path')])
        env.Append(LIBPATH=['%s/lib' % GetOption('ihtruntime_path')])
        env.Append(LIBPATH=['%s/lib64' % GetOption('ihtruntime_path')])
        # include python.
        env.Append(CPPPATH=['%s/include/python2.7' %GetOption('ihtruntime_path')])
        env.Append(CPPPATH=['%s/lib/python2.7/site-packages/numpy/core/include'
                            %GetOption('ihtruntime_path')])
        
        for name in env['LIB_LINK_LIST']:
            # include Qt4.
            if name == "Qt":
                env.Append(CPPPATH=[
                    '%s/include' % GetOption('ihtruntime_path'),
                    '%s/include/QtCore' % GetOption('ihtruntime_path'),
                    '%s/include/QtGui' % GetOption('ihtruntime_path'),
                    '%s/include/QtNetwork' % GetOption('ihtruntime_path'),
                    '%s/include/QtXml' % GetOption('ihtruntime_path'),
                ])
            # include OpenCV.
            elif name == "opencv":
                env.Append(CPPPATH = '%s/include/opencv' %GetOption('ihtruntime_path'))
                env.Append(LIBPATH = '%s/share/OpenCV/3rdparty/lib' %GetOption('ihtruntime_path'))

    # other default library path, ordered by significance.
    # needed by RH4.
    env.Append(LIBPATH=['/usr/X11R6/lib64', '/usr/lib64'])
    
    # import comipler flag "-fPIC" for building .so
    env.Append(CPPFLAGS="-fPIC")
    # additional moc flags.
    env.Append(MOCFLAGS=GetOption('mocflags').split(','))
    # comipler flag for debugging.
    if GetOption('debug'):
        env.Append(CPPFLAGS=['-g'])
    else:
        env.Append(CPPFLAGS=['-DNDEBUG'])
        env.Append(CPPFLAGS=['-O2']) #default optimize level, the latest option could overwrite it.
    # comipler flag for warning. 
    env.Append(CPPFLAGS = ['-Wall'])
    # comipler flag for c++ new standard.
    env.Append(CPPFLAGS=['--std=c++0x'])
    # additional compiler flags.
    for key in GetOption('flags').split(','):
        env.Append(CPPFLAGS=['%s' % key])
    # linker flag for rpath Qt.
    env.Append(LIBPATH=['/vol0/ap/iht/qt_app_res/lib'])
    env.Append(LINKFLAGS=[
        '-Wl,-rpath,%s'%os.path.join(GetOption('ihtruntime_path'), path) for path in
        ('lib', 'lib64')
    ])

def set_libray_link(env):
    """
    import lib keywords.
    """
    for name in env['LIB_LINK_LIST']:
        if name == "basic":
            yamlcpp = env.SearchLibrary('libyaml-cpp.a')
            boost_opt = env.SearchLibrary('libboost_program_options.a')
            env.Append(LIBS=['gtest',
                 'glog', yamlcpp, boost_opt, 'gthread-2.0', 'glib-2.0', 'pthread',
                 'm', 'rt', 'z', 'dl'])
        elif name == "ssl":
            ssl = env.SearchLibrary('libssl.a')
            crypto = env.SearchLibrary('libcrypto.a')
            env.Append(LIBS= [ssl, crypto])
        elif name == "mysqlclient":
            mysqlclient = env.SearchLibrary('libmysqlclient.a')
            env.Append(LIBS= [mysqlclient])
        elif name == "opencv":
            opencv_highgui = env.SearchLibrary('libopencv_highgui.a')
            opencv_core = env.SearchLibrary('libopencv_core.a')
            opencv_imgproc = env.SearchLibrary('libopencv_imgproc.a')
            CVpng = env.SearchLibrary('liblibpng.a') 
            jasper = env.SearchLibrary('liblibjasper.a')
            OpenCV_lib = [opencv_highgui, opencv_imgproc, opencv_core, jasper, CVpng]
            env.Append(LIBS=OpenCV_lib)
        elif name == "Qt":
            QtGui = env.SearchLibrary('libQtGui.a')
            QtNetwork = env.SearchLibrary('libQtNetwork.a')
            QtCore = env.SearchLibrary('libQtCore.a')
            QtXml = env.SearchLibrary('libQtXml.a')
            tiff = env.SearchLibrary('libtiff.a')
            jpeg = env.SearchLibrary('libjpeg.a')
            Qt_lib = ['IhtQtRes', QtGui, QtNetwork, QtCore, QtXml, jpeg, tiff, 'png', 'SM',
              'ICE', 'X11', 'Xrender', 'Xext', 'freetype', 'fontconfig'] 
            env.Append(LIBS=Qt_lib)
        elif name == "fftw3":
            fftw3 = env.SearchLibrary('libfftw3.a')
            env.Append(LIBS=[fftw3])

    print "default lib list", [ str(i) for i in env['LIBS'] ]

def call_moc(env, target, source):
    ''' 
    Use QT Meta-Object Compiler(MOC).
    '''
    moccmd = ' '.join(['moc',
        ' '.join(env['MOCFLAGS']),
        ' '.join(['-I%s' % str(path) for path in env['CPPPATH']]),
        '$SOURCE',
        '-o $TARGET',
    ])
    
    return env.Command(target, source, moccmd)

def exists(env):
    return True

def generate(env):
    env.AddMethod(call_moc, 'Moc')
    env.AddMethod(custom_make, 'CustomMake')
    env.AddMethod(custom_linker, 'CustomLinker')
    env.AddMethod(custom_compiler, 'CustomCompiler')
    env.AddMethod(moc_make, 'MocMake')
    env.AddMethod(search_library, 'SearchLibrary')
    env.AddMethod(quick_make, 'QuickMake')
    env.AddMethod(set_libray_path, 'SetLibrayPath')
    env.AddMethod(set_libray_link, 'SetLibrayLink')
    return env

# vim: set ft=python ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=105:
