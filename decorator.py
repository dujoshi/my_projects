import time, pdb


"""
Prog has two function square and cube
it takes an array or 1000 numbers and do cube or square of each one of them
we are having a decorator time_it function which will be called to calculate time python took
in cube and Square .

"""
def time_it(func):
     def wrapper_func(*args,**kwargs):
           start=time.time()
           result=func(*args, **kwargs)
           end=time.time()
           print 'Func {} took {} msec time '.format(func.__name__,(end-start))
           return result
     return wrapper_func

@time_it
def square(x):
    result=[]
    for item in x:
        result.append(item*item)
    return result

@time_it
def cube(x):
    result=[]
    for item in x:
        result.append(item*item*item)
    return result

array=range(1,1000)
square(array)
cube(array)

"""
output
======
$ python dec1.py
Func square took 0.000102996826172 msec time
Func cube took 9.89437103271e-05 msec time
$
"""
