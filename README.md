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

### r
```python
print(r'C:\aylar\nisan\toplam masraf') #deactivate the string syntaxing
```

## `input()`
### input()
```python
name = input("please, enter your name: ")
```

### int()
```python
input_arg = input("please, enter your age: ")
input_arg = int(input_arg)
```

### str()
```python
a = 15
a = str(a)
print(a)
```

### complex()
```python
a = 1 + 5j
b = 2 +7j

print(complex(a) + complex(b))
```

### eval()
```python
a = 5
b = 10

print(eval("a + b"))
print(eval("a - b"))
print(eval("a * b"))
print(eval("a / b"))
```

### exec()
```python
exec("a=5")
exec("b=10")

print(eval("a + b"))
print(eval("a - b"))
print(eval("a * b"))
print(eval("a / b"))
```

### format()
```python
print("My name is {1} and I am {0} years old".format(19, "Vusal"))
```

## others
### dir()
```python
print(dir(str))
```

### enumerate()
```python
a = [1,2,3,4,5]
for i in enumerate(a):
    print(i)
```

### help()
```python
help(int)
```
```python
help()
```

## string manipulations
### replace()
```python
a = "hello"
print(a.replace("lo", "lol")
```

### split()
```python
a = "hello world !"
print(a.split(" ", 1)) #["hello", "world !"]
```

### rsplit()
```python
a = "hello world !"
print(a.rsplit(" ", 1) #['hello world', '!']
```

### splitlines() a.k.a split("\n") (a bit different)
```python
a = """hello
world
!
"""
print(a.splitlines())
```

### lower()
```python
a = "HeLLo WorlD!"
print(a.lower()) # "hello world!"
```

### upper()
```python
a = "helLo World!"
print(a.upper()) # "HELLO WORLD!"
```

### islower()
```python
a = "hello"
print(a.islower()) # True

b = "hellO"
print(b.islower()) # False
```

### isupper()
```python
a = "HELLO"
print(a.isupper()) # True

b = "HELLo"
print(b.isupper()) # False
```

### endswith()
```python
a = "hello world!"
print(a.endswith("ld!")) # True
print(a.endswith("d!")) # True
print(a.endswith("!")) # True
```

### startswith()
```python
a = "hello world!"
print(a.startswith("hel")) # True
print(a.startswith("he")) # True
print(a.startswith("h")) # True
```

### capitalize()
```python
a = "hello world !"
print(a.capitalize()) # Hello world !
```

### title()
```python
a = "hello world !"
print(a.title()) # Hello World !
```

### swapcase()
```python
a = "Hello World!"
print(a.swapcase()) # hELLO wORLD!
```

### casefold()
```python
print("ß".casefold()) # ss
```

### strip()
```python
a = " hello world! "
print(a.strip()) # "hello world!"
```
```python
a = "123hello world!123"
print(a.strip("123")) # "hello world!"
```

### lstrip()
```python
a = " hello world! "
print(a.lstrip()) # "hello world! "
```

### rstrip()
```python
a = " hello world! "
print(a.rstrip()) # " hello world!"
```

### join()
```python
a = ["hello", "world", "!"]
print(" ".join(a)) # hello world !
print("".join(a)) # helloworld!

print("-".join(a)) # hello-world-!
```

### count()
```python
a = "hello world!"
print(a.count("o")) # 2
```
```python
a = "hello world!"
print(a.count("o", 6)) # 1
```
```python
a = "hello world!"
print(a.count("o", 6, 9)) # 1
```
```python
a = "hello worlld!"
print(a.count("ll", 0, len(a))) # 2
```

### index()
```python
a = "Hello, World!"
print(a.index("l")) # 2
```
```python
a = "Hello, World!"
print(a.index("l", 6) # 10
```

### rindex()
```python
a = "Hello, World!"
print(a.rindex("l")) # 10
```


### find()
```python
a = "Hello, World!"
print(a.find("l")) # 2
```
```python
a = "Hello, World!"
print(a.find("z")) # -1
```

### rfind()
```python
a = "Hello, World!"
print(a.rfind("l")) # 10
```

### center()
```python
a = "woosal"
print(a.center(10)) # "     woosal     "
```
```python
a = "woosal"
print(a.center(10,"-")) # "--woosal--"
```
```python
a = "wosal"
print(a.center(10, "-")) # "--wosal---"
```

### rjust()
```python
for i in dir(""):
    print(i.rjust(20))
```

### ljust()
```python
for i in dir(""):
    print(i.ljust(20))
```

### zfill()
```python
for i in range(11):
    print(str(i).zfill(3))
    
# 000
# 001
# 002
# 003
# 004
# 005
# 006
# 007
# 008
# 009
# 010
```

### partition()
```python
a = "woosal"
print(a.partition("o")) # ('w', 'o', 'osal')
```
```python
a = "woosal"
print(a.partition("z")) # ('woosal', '', '')
```

### rpartition()
```python
a = "woosal"
print(a.rpartition("o")) # ('wo', 'o', 'sal')
```
```python
a = "woosal"
print(a.rpartition("z")) # ('', '', 'woosal')
```

### encode() [cp1254](https://en.wikipedia.org/wiki/Windows-1254)
```python
print("çilek".encode("cp1254")) # b'\xe7ilek'
```

### expandtabs()
```python
a = "woo\tsa\tl"
print(a.expandtabs(10)) # "woo       sa        l"
```

### str.maketrans() / translate()
```python
kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"

çeviri_tablosu = str.maketrans(kaynak, hedef)

metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."

print(metin.translate(çeviri_tablosu))
```

### isalpha()
```python
a = "woosal"
print(a.isalpha()) # True
```
```python
a = "woosal1337"
print(a.isalpha()) # False
```

### isdigit()
```python
a = "1337"
print(a.isdigit()) # True
```
```python
a = "1337!"
print(a.isdigit()) # False
```

### isalnum()
```python
a = "woosal1337"
print(a.isalnum()) # True
```
```python
a = "woosal1337!"
print(a.isalnum()) # False
```

### isdecimal()
```python
a = "1337"
print(a.isdecimal()) # True
```
```python
a = "1337.1337"
print(a.isdecimal()) # False
```

### isidentifier()
```python
print("random_name".isidentifier()) # True
```
```python
print("1337name".isidentifier())) # False
```

### isnumeric()
```python
print("1337".isnumeric()) # True
```
```python
print("13.37".isnumeric()) # False
```

### isspace()
```python
print(" ".isspace()) # True
```python
print("           ".isspace()) # True
```
```python
print("wosoal".isspace()) # False
```

### isprintable()
```python
print("woosal".isprintable()) # True
```
```python
print("\n".isprintable()) # False
```

## `%`
### s
```python
print("my name is %s" %"vusal")
```

### d
```python
print("i am %d years old" %19)
```

### o (octal)
```python
print("%i sayısının sekizli düzendeki karşılığı %o sayısıdır." %(10, 10)) # 12
```

### x (hexadecimal)
```python
print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." %(20, 20)) # 14
```

### X (hexadecimal)
```python
print("%i sayısının onaltılı düzendeki karşılığı %X sayısıdır." %(10, 10)) # A
```

### f (float)
```python
print("Dolar %f TL ..." %8.567) # 8.567000
```

### c
```python
print("%c" %65) # A
```

## `lists []`
### append()
```python
liste = ["elma", "armut", "çilek"]
liste.append("erik")
```

###  extend()
```python
li1 = [1, 3, 4]
li2 = [10, 11, 12]
li1. extend(li2) # [1, 3, 4, 10, 11, 12]
```

### insert()
```python
liste = ["elma", "armut", "çilek"]
liste.insert(0, "erik")
print(liste)
```

### remove()
```python
liste = ["elma", "armut", "çilek"]
liste.remove("elma")
print(liste) # ["armut", "çilek"]
```

### reverse()
```python
liste = ["elma", "armut", "çilek"]
liste.reverse()
print(liste) # ["çilek", "armut", "elma"]
```
```python
liste = ["elma", "armut", "çilek"]
liste = liste[::-1]
print(liste) # ["çilek", "armut", "elma"] 
```
```python
liste = ["elma", "armut", "çilek"]
reversed(liste)
print(list(liste)) # ["çilek", "armut", "elma"]

print(*liste) # çilek armut elma
```

### pop()
```python
liste = ["elma", "armut", "çilek"]
liste.pop()
print(liste) # ["elma", "armut"]
```
```python
liste = ["elma", "armut", "çilek"]
print(liste.pop(1))
print(liste) # ["elma", "çilek"]
```

### sort()
```python
members = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep',
          'Abdullah', 'Kadir', 'Kemal', 'Kamil', 'Selin', 'Senem',
          'Sinem', 'Tayfun', 'Tuna', 'Tolga']
members.sort()
print(members)
```
```python
digits = [1, 0, -1, 4, 10, 3, 6]
digits.sort()
print(digits)
```
```python
digits = [1, 0, -1, 4, 10, 3, 6]
digits.sort(reverse=True)
print(digits)
```
```python
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {harf: harfler.index(harf) for harf in harfler}

isimler = ["ahmet", "ışık", "ismail", "çiğdem", "can", "şule"]
isimler.sort(key=lambda x: çevrim.get(x[0]))

print(isimler)
```

### index()
```python
liste = ["elma", "armut", "çilek"]
print(liste.index("elma")) # 0
```

### count()
```python
liste = ["elma", "armut", "elma", "çilek"]
print(liste.count("elma")) # 2
```

### copy()
```python
liste1 = ["ahmet", "mehmet", "özlem"]
liste2 = liste1[:]
liste2.pop()

print(liste1) # ["ahmet", "mehmet", "özlem"]
print(liste2) # ["ahmet", "mehmet"]
```
```python
liste1 = ["ahmet", "mehmet", "özlem"]
liste2 = list(list1)
liste2.pop()

print(liste1) # ["ahmet", "mehmet", "özlem"]
print(liste2) # ["ahmet", "mehmet"]
```
```python
liste1 = ["ahmet", "mehmet", "özlem"]
liste2 = liste1.copy()
liste2.pop()

print(liste1) # ["ahmet", "mehmet", "özlem"]
print(liste2) # ["ahmet", "mehmet"]
```

### clear()
```python
liste = [1, 2, 3, 5, 10, 20, 30, 45]
liste.clear()
print(liste)
```

### count()
```python
demet = ("elma", "armut", "elma", "çilek")
print(demet.count("elma"))
```
