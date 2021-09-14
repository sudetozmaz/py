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

## counting systems
### bin()
```python
print(bin(2)[2:]) # 10
```

### hex()
```python
print(hex(10)[2:]) # a
```

### oct()
```python
print(oct(10)[2:]) # 12
```

### int() (universal to all)
```python
print(int('1100', 2)) # 12
```
```python
print(int('1100', 16)) # 4352
```

### pow()
```python
print(pow(2, 3) # 8
print(pow(2, 3, 8) # (2**3) % 8 = 0
```

## `imaginary / complex values`
```python
c = 12+4j
print(c.imag) # 4.0
print(c.real) # 12.0
```

## `arithmetic ops`
### abs()
```python
a = -2
print(abs(a)) # 2
```

### divmod()
```python
print(divmod(10, 3)) # (3, 1) (a // b, a % b) 
```

### max()
```python
the_list = [882388, 260409, 72923, 692476, 131925, 259114, 47630, 84513, 25413, 614654,
 239479, 299159, 175488, 345972, 458112, 791030, 243610, 413702, 565285,
 773607, 131583, 979177, 247202, 615485, 647512, 556823, 242460, 852928,
 893126, 792435, 273904, 544434, 627222, 601984, 966446, 384143, 308858,
 915106, 914423, 826315, 258342, 188056, 934954, 253918, 468223, 262875,
 462902, 370061, 336521, 367829, 147846, 838385, 605377, 175140, 957437,
 105779, 153499, 435097, 9934, 435761, 989066, 357279, 341319, 420455,
 220075, 28839, 910043, 891209, 975758, 140968, 837021, 526798, 235190,
 634295, 521918, 400634, 385922, 842289, 106889, 742531, 359913, 842431,
 666182, 516933, 22222, 445705, 589281, 709098, 48521, 513501, 277645,
 860937, 655966, 923944, 7895, 77482, 929007, 562981, 904166, 619260,
 616293, 203512, 67534, 615578, 74381, 484273, 941872, 110617, 53517,
 402324, 156156, 839504 , 625325, 694080, 904277, 163914, 756250, 809689,
 354050, 523654, 26723, 167882, 103404, 689579, 121439, 158946, 485258,
 850804, 650603, 717388, 981770, 573882, 358726, 957285, 418479, 851590,
 960182, 11955, 894146, 856069, 369866, 740623, 867622, 616830, 894801,
 827179, 580024, 987174, 638930, 129200, 214789, 45268, 455924, 655940,
 335481, 845907, 942437, 759380, 790660, 432715, 858959, 289617, 757317,
 982063, 237940, 141714, 939369, 198282, 975017, 785968, 49954, 854914,
 996780, 121633, 436419, 471, 776271, 91626, 209175, 894281, 417963, 624464,
 736535, 418888, 506194, 591087, 64075, 50252, 952943, 25878, 217085,
 223996, 416042, 484123, 810460, 423284, 956886, 237772, 960241, 601551,
 830147, 449088, 364567, 337281, 524358, 980387, 393760, 619710, 100181,
 96738, 275199, 553783, 975654, 662536, 979103, 869504, 702350, 174361,
 970250, 267625, 661580, 444662, 871532, 881977, 981660, 446047, 508758,
 530694, 608789, 339540, 242774, 637473, 874011, 732999, 511638, 744144,
 710805, 641326, 88085, 128487, 59732, 739340, 443638, 830333, 832136,
 882277, 403538, 441349, 721048, 32859]
 
print(max(the_list)) # 996780
```
##### custom sorting
```python
isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah",
           "gıyaseddin", "sibel", "can", "necmettin", "savaş", "özgür"]
           
print(max(isimler, key=len)) # gıyaseddin
```

### min()
```python
the_list = [882388, 260409, 72923, 692476, 131925, 259114, 47630, 84513, 25413, 614654,
 239479, 299159, 175488, 345972, 458112, 791030, 243610, 413702, 565285,
 773607, 131583, 979177, 247202, 615485, 647512, 556823, 242460, 852928,
 893126, 792435, 273904, 544434, 627222, 601984, 966446, 384143, 308858,
 915106, 914423, 826315, 258342, 188056, 934954, 253918, 468223, 262875,
 462902, 370061, 336521, 367829, 147846, 838385, 605377, 175140, 957437,
 105779, 153499, 435097, 9934, 435761, 989066, 357279, 341319, 420455,
 220075, 28839, 910043, 891209, 975758, 140968, 837021, 526798, 235190,
 634295, 521918, 400634, 385922, 842289, 106889, 742531, 359913, 842431,
 666182, 516933, 22222, 445705, 589281, 709098, 48521, 513501, 277645,
 860937, 655966, 923944, 7895, 77482, 929007, 562981, 904166, 619260,
 616293, 203512, 67534, 615578, 74381, 484273, 941872, 110617, 53517,
 402324, 156156, 839504 , 625325, 694080, 904277, 163914, 756250, 809689,
 354050, 523654, 26723, 167882, 103404, 689579, 121439, 158946, 485258,
 850804, 650603, 717388, 981770, 573882, 358726, 957285, 418479, 851590,
 960182, 11955, 894146, 856069, 369866, 740623, 867622, 616830, 894801,
 827179, 580024, 987174, 638930, 129200, 214789, 45268, 455924, 655940,
 335481, 845907, 942437, 759380, 790660, 432715, 858959, 289617, 757317,
 982063, 237940, 141714, 939369, 198282, 975017, 785968, 49954, 854914,
 996780, 121633, 436419, 471, 776271, 91626, 209175, 894281, 417963, 624464,
 736535, 418888, 506194, 591087, 64075, 50252, 952943, 25878, 217085,
 223996, 416042, 484123, 810460, 423284, 956886, 237772, 960241, 601551,
 830147, 449088, 364567, 337281, 524358, 980387, 393760, 619710, 100181,
 96738, 275199, 553783, 975654, 662536, 979103, 869504, 702350, 174361,
 970250, 267625, 661580, 444662, 871532, 881977, 981660, 446047, 508758,
 530694, 608789, 339540, 242774, 637473, 874011, 732999, 511638, 744144,
 710805, 641326, 88085, 128487, 59732, 739340, 443638, 830333, 832136,
 882277, 403538, 441349, 721048, 32859]
 
print(min(the_list)) # 471
```
```python
isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah",
           "gıyaseddin", "sibel", "can", "necmettin", "savaş", "özgür"]
           
print(min(isimler, key=len)) # can
```

### sum()
```python
a = [10, 20, 43, 45 , 77, 2, 0, 1]
print(sum(a)) # 198
```
```python
a = [10, 20, 43, 45 , 77, 2, 0, 1]
print(sum(a, 10)) # 208
```
