import time
def timeit(f):

    def wrapper(*args,**kwargs):
        start=time.time()
        ret=f(*args,**kwargs)
        print(time.time()-start)
        return ret

    return wrapper
@timeit
def my_func(x):
    time.sleep(x)

class Timer:
    def __init__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
        start=time.time()
        ret=self.func(*args,**kwargs)
        print(f"Time:{time.time()-start}")
        return ret

@Timer
def add(a,b):
    return a+b

def add_str(cls):
    def __str__(self):
        return str(self.__dict__)
    cls.__str__=__str__
    return cls
@add_str
class my_object(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b

if __name__=='__main__':
    my_func(1)
    add(2,3)
    my_object(2,3)