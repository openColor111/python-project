import sys,os,linecache
def trace(f):
    def globaltrace(frame,why,arg):
        if why == "call":return localtrace
        return None
    def localtrace(frame,why,arg):
        if why == "line":
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print("%s(%s):%s"%(bname,lineno,linecache.getline(filename,lineno)))
        return localtrace
    def _f(*args,**kwds):
        sys.settrace(globaltrace)
        result = f(*args,**kwds)
        sys.settrace(None)
        return result
    return _f

@trace
def p():
    print("xxx")
    print("yyy")
    print("zzz")

p()
