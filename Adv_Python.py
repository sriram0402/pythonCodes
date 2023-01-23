Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

============ RESTART: /Users/sriram/Documents/Python/Adv_Practice.py ===========

============ RESTART: /Users/sriram/Documents/Python/Adv_Practice.py ===========
['a', 'b', {'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30}, 'baz': 3}, 'c', 'd']
x=['a', 'b', {'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30}, 'baz': 3}, 'c', 'd']

x
['a', 'b', {'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30}, 'baz': 3}, 'c', 'd']
x[2].items()
dict_items([('foo', 1), ('bar', {'x': 10, 'y': 20, 'z': 30}), ('baz', 3)])
x[2].get('bar')
{'x': 10, 'y': 20, 'z': 30}
x[2].get('bar').items()
dict_items([('x', 10), ('y', 20), ('z', 30)])
x[2].get('bar').get('z')
30
x[2].get('bar').add('p',100)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x[2].get('bar').add('p',100)
AttributeError: 'dict' object has no attribute 'add'
x[2].get('bar')['p']=100
x[2].get('bar')['q']=200
x[2].get('bar')['r']=300
x[2].get('bar').items()
dict_items([('x', 10), ('y', 20), ('z', 30), ('p', 100), ('q', 200), ('r', 300)])
x
['a', 'b', {'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30, 'p': 100, 'q': 200, 'r': 300}, 'baz': 3}, 'c', 'd']
x[2].values()
dict_values([1, {'x': 10, 'y': 20, 'z': 30, 'p': 100, 'q': 200, 'r': 300}, 3])
x[2].items()
dict_items([('foo', 1), ('bar', {'x': 10, 'y': 20, 'z': 30, 'p': 100, 'q': 200, 'r': 300}), ('baz', 3)])
x[2]
{'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30, 'p': 100, 'q': 200, 'r': 300}, 'baz': 3}
x[2][2]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x[2][2]
KeyError: 2
x[2].pop('baz')
3
x
['a', 'b', {'foo': 1, 'bar': {'x': 10, 'y': 20, 'z': 30, 'p': 100, 'q': 200, 'r': 300}}, 'c', 'd']
y= [10, [3.141, 20, [30, ‘baz’, 2.718]], ‘foo’]
SyntaxError: invalid character '‘' (U+2018)
y= [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
y
[10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
y[1][2]
[30, 'baz', 2.718]
y[1][2][1][2]
'z'
y[1][2][1]
'baz'
y[1][2][1] in 'z'
False
'z' in y[1][2][1]
True
y[1][2]
[30, 'baz', 2.718]
y[1][2][1:]
['baz', 2.718]
