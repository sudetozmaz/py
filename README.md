# [codes](/main/)
# [others](/others/)

### interesting python stuff:

```python
class C:
    def m(self):
        return "result"

an_object = C()

class_method = getattr(C, "m")
result = class_method(an_object)

print(result)
```

```python
def f():
    return "result"

function_name = "f"
result = eval(function_name + "()")

print(result)
```

```python
# take an input of multiple inputs and convert them into
# a numpy array with all float converted

arr = np.array([i for i in (input().split() for _ in range(n))]).astype(np.float)
```

```python
>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
```

```python
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
```

```python
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
```

```python
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
```

```python
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
```
