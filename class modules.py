Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class class1:
...     var1= 'i am class1"
...     
SyntaxError: unterminated string literal (detected at line 2)
>>> class class1:
...     var = "i am class1"
... 
...     
>>> 
>>> class class2:
...     var2 = "i am class2"
... 
...     
>>> 
>>> class class3(class1,class2):
...     var3= "i am class3"
... 
...     
>>> example = class3()
>>> 
>>> example.var1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    example.var1
AttributeError: 'class3' object has no attribute 'var1'. Did you mean: 'var'?
>>> example.var
'i am class1'
>>> example.var2
'i am class2'
>>> example.var3
'i am class3'
