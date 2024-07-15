Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> white True:
...     
SyntaxError: invalid syntax
>>> while True:
...     text = input("Enter something:")
... 
...     
Enter something:12
Enter something:123
Enter something:dfasdf
Enter something:
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    text = input("Enter something:")
KeyboardInterrupt
>>> while True:
...     text = input("Enter something");
...     if(text == 'exit'):
...         break
... 
...     
Enter somethingw
Enter somethingwerwer
Enter somethingexit
>>> 
======= RESTART: /Users/macbookair/Desktop/pythonproject/infinite_loop.py ======
enter somethingadfd
enter somethingadsfasdf
enter somethingdfasdf
enter somethingadsfsadf
enter somethingasdfasdf
enter somethingsdfasd
enter somethingexit
