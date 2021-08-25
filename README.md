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
