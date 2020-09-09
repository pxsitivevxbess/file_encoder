Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.array([1,2,3,4,5],[7,6,8,9,0])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = np.array([1,2,3,4,5],[7,6,8,9,0])
TypeError: Field elements must be 2- or 3-tuples, got '7'
>>> a.shape
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.shape
NameError: name 'a' is not defined
>>> a = np.array([[1,2,3,4,5],[7,6,8,9,0]])
>>> a.shape
(2, 5)
>>> b = np.array([[6,7,8,9,2],[1,2,3,4,8]])
>>> np.dot(a,b)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    np.dot(a,b)
  File "<__array_function__ internals>", line 5, in dot
ValueError: shapes (2,5) and (2,5) not aligned: 5 (dim 1) != 2 (dim 0)
>>> np.dot(a,b)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    np.dot(a,b)
  File "<__array_function__ internals>", line 5, in dot
ValueError: shapes (2,5) and (2,5) not aligned: 5 (dim 1) != 2 (dim 0)
>>> b.shape
(2, 5)
>>> 