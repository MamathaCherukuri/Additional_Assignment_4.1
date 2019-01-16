
1.Write a Python program which accepts a list named : randomList = ['a', 0,2] Use exception handling using try-catch which gives the output as:


```python
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)
```

    The entry is a
    Oops! <class 'ValueError'> occured.
    Next entry.
    
    The entry is 0
    Oops! <class 'ZeroDivisionError'> occured.
    Next entry.
    
    The entry is 2
    The reciprocal of 2 is 0.5
    


```python

```


```python

```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-2-eefe155c0e87> in <module>()
    ----> 1 import fibo
    

    ModuleNotFoundError: No module named 'fibo'



```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
