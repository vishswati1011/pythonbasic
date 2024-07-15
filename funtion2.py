Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def printname(name)
SyntaxError: expected ':'

def printname(name):
    print(name)

...     
>>> printname("Swati")
Swati
>>> printname("Swati","Nisha")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    printname("Swati","Nisha")
TypeError: printname() takes 1 positional argument but 2 were given
>>> def printname(*name):
...     print(name)
... 
...     
>>> printname("Swati","Nisha")
... 
('Swati', 'Nisha')
>>> 
>>> def printname(*name):
...     print(name[0]);
... 
...     
>>> printname("Swati","nisha","sharad")
Swati
>>> printname("Swati","nisha","sharad",22,23,24)
Swati
>>> def printname(name,age)
SyntaxError: expected ':'
>>> def printname(name,age):
...     print(name)
...     print(age)
... 
...     
>>> pritnname("Swati",22)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    pritnname("Swati",22)
NameError: name 'pritnname' is not defined. Did you mean: 'printname'?
>>> printname("swati",22)
swati
22
