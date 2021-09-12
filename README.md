# [blog](https://www.woosal.com/)
# [codes](/main/)
# [others](/others/)

# ▬▬ι═══════ﺤ

## `print()`
### sep
```python
print("http://", "www.", "google.", "com", sep=" ")
```

### end
```python
print("http://", "www.", "google.", "com", end="\n")
```

### file
```python
print("http://", "www.", "google.", "com", file="custom_text.txt")
```

### flush
```python
f = open("custom_text.txt", "a")
print("http://", "www.", "google.", "com", file=f, flush=True)
```

### *
```python
a = (1,2,3,4,5)
b = [1,2,3,4,5]
c = {1:2, 3:4, 5:6}
print(*a, *b, *c)
```

## `\`
### \
```python
print("\"It was said by him.\" - Sun Tzu")
```

### \n
```python
print("Hello, World!\n")
```

### \t
```python
print("Hello,\tWorld!")
```

### \a (bell noise might be incompatible on some devices)
```python
print("Hello,\aWorld!")
```

### \r
```python
print("Hello,\rWorld!)
```

### \v
```python
print("Hello, World\vSun Tzu")
```

### \b
```python
print("google.com\b.uk")
```

### \u
```python
print('\u0070') #p 
```

### \U
```python
print('\U00000071') #q
```

### \N
```python
import unicodedata
unicodedata.name('a') # LATIN SMALL LETTER A
print('\N{LATIN SMALL LETTER A}') #a
```

### \x
```python
print('\x41') #A
```

### `r`
```python
print(r'C:\aylar\nisan\toplam masraf') #deactivate the string syntaxing
```
