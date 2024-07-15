Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> animals = ["dogs","cats","lion","tiger"]
>>> animals[]
SyntaxError: invalid syntax
>>> animals[2]
'lion'
>>> animals[-2]
'lion'
>>> example= [1,2,3,4,5,6,7,8,9,0]
>>> example[2,8]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    example[2,8]
TypeError: list indices must be integers or slices, not tuple
>>> example[2:8]
[3, 4, 5, 6, 7, 8]
>>> example[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> example[:5]
[1, 2, 3, 4, 5]
>>> example[5:]
[6, 7, 8, 9, 0]
>>> example[-1:-4]
[]
>>> example[-4:-1]
[7, 8, 9]
>>> a=[0,1,2,3]
>>> b=[4,5,6,7]
>>> a+b
[0, 1, 2, 3, 4, 5, 6, 7]
>>> a + "name"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a + "name"
TypeError: can only concatenate list (not "str") to list
>>> name ="swati"
>>> 'w' in name
True
'k' in name
False




number = [21,30,52,87,65,40]
len(number)
6
max(number)
87
min(number)
21


print("convert stirng to array")
convert stirng to array
list("swati")
['s', 'w', 'a', 't', 'i']
numbers[2] = 40
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    numbers[2] = 40
NameError: name 'numbers' is not defined. Did you mean: 'number'? Or did you forget to import 'numbers'?
number[2]= 40
print(number)
[21, 30, 40, 87, 65, 40]
print("convert stirng to array")
convert stirng to array



example = list ("simplelook")
example
['s', 'i', 'm', 'p', 'l', 'e', 'l', 'o', 'o', 'k']
len(example)
10
example[6:] = list('mike')
example
['s', 'i', 'm', 'p', 'l', 'e', 'm', 'i', 'k', 'e']
example[6:]= list('hello world")
                  
SyntaxError: unterminated string literal (detected at line 1)
example[6:]= list('hello world')
                  
exampel
                  
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    exampel
NameError: name 'exampel' is not defined. Did you mean: 'example'?
example
                  
['s', 'i', 'm', 'p', 'l', 'e', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
str(example)
                  
"['s', 'i', 'm', 'p', 'l', 'e', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']"
name = str(example)
                  
name
                  
"['s', 'i', 'm', 'p', 'l', 'e', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']"




examp  = ['computer','random','keyboard']
                  
examp.append('operation')
                  
examp
                  
['computer', 'random', 'keyboard', 'operation']



number = [1,1,1,2,2,3,3,4,45,5,6,6,7]
                  
number.count(2)
                  
2
number.count(6)
                  
2
number.count(1)
                  
3


print("extends method")
                  
extends method
numbers = examp+number
                  
numbers
                  
['computer', 'random', 'keyboard', 'operation', 1, 1, 1, 2, 2, 3, 3, 4, 45, 5, 6, 6, 7]

numbers.extend(examp)
                  
numbers
                  
['computer', 'random', 'keyboard', 'operation', 1, 1, 1, 2, 2, 3, 3, 4, 45, 5, 6, 6, 7, 'computer', 'random', 'keyboard', 'operation']
'random' in numbers
                  
True
name = "swati"
                  
'm' in name
                  
False
reverse(name)
                  
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    reverse(name)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
str.reverse(name)
                  
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    str.reverse(name)
AttributeError: type object 'str' has no attribute 'reverse'


print ("write a program tp reverse strign")
                  
write a program tp reverse strign
string  = input("enter string")
                  
enter string swati
string = string[::-1]
                  
print ("reversed string : "+ string)
                  
reversed string : itaws 
