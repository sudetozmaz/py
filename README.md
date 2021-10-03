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
a = (1, 2, 3, 4, 5)
b = [1, 2, 3, 4, 5]
c = {1: 2, 3: 4, 5: 6}
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
print("Hello,\rWorld!")
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
print('\u0070')  # p 
```

### \U

```python
print('\U00000071')  # q
```

### \N

```python
import unicodedata

unicodedata.name('a')  # LATIN SMALL LETTER A
print('\N{LATIN SMALL LETTER A}')  # a
```

### \x

```python
print('\x41')  # A
```

### r

```python
print(r'C:\aylar\nisan\toplam masraf')  # deactivate the string syntaxing
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
b = 2 + 7j

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
a = [1, 2, 3, 4, 5]
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
print(a.replace("lo", "lol"))
```

### split()

```python
a = "hello world !"
print(a.split(" ", 1))  # ["hello", "world !"]
```

### rsplit()

```python
a = "hello world !"
print(a.rsplit(" ", 1))  # ['hello world', '!']
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
print(a.lower())  # "hello world!"
```

### upper()

```python
a = "helLo World!"
print(a.upper())  # "HELLO WORLD!"
```

### islower()

```python
a = "hello"
print(a.islower())  # True

b = "hellO"
print(b.islower())  # False
```

### isupper()

```python
a = "HELLO"
print(a.isupper())  # True

b = "HELLo"
print(b.isupper())  # False
```

### endswith()

```python
a = "hello world!"
print(a.endswith("ld!"))  # True
print(a.endswith("d!"))  # True
print(a.endswith("!"))  # True
```

### startswith()

```python
a = "hello world!"
print(a.startswith("hel"))  # True
print(a.startswith("he"))  # True
print(a.startswith("h"))  # True
```

### capitalize()

```python
a = "hello world !"
print(a.capitalize())  # Hello world !
```

### title()

```python
a = "hello world !"
print(a.title())  # Hello World !
```

### swapcase()

```python
a = "Hello World!"
print(a.swapcase())  # hELLO wORLD!
```

### casefold()

```python
print("ß".casefold())  # ss
```

### strip()

```python
a = " hello world! "
print(a.strip())  # "hello world!"
```

```python
a = "123hello world!123"
print(a.strip("123"))  # "hello world!"
```

### lstrip()

```python
a = " hello world! "
print(a.lstrip())  # "hello world! "
```

### rstrip()

```python
a = " hello world! "
print(a.rstrip())  # " hello world!"
```

### join()

```python
a = ["hello", "world", "!"]
print(" ".join(a))  # hello world !
print("".join(a))  # helloworld!

print("-".join(a))  # hello-world-!
```

### count()

```python
a = "hello world!"
print(a.count("o"))  # 2
```

```python
a = "hello world!"
print(a.count("o", 6))  # 1
```

```python
a = "hello world!"
print(a.count("o", 6, 9))  # 1
```

```python
a = "hello worlld!"
print(a.count("ll", 0, len(a)))  # 2
```

### index()

```python
a = "Hello, World!"
print(a.index("l"))  # 2
```

```python
a = "Hello, World!"
print(a.index("l", 6))  # 10
```

### rindex()

```python
a = "Hello, World!"
print(a.rindex("l"))  # 10
```

### find()

```python
a = "Hello, World!"
print(a.find("l"))  # 2
```

```python
a = "Hello, World!"
print(a.find("z"))  # -1
```

### rfind()

```python
a = "Hello, World!"
print(a.rfind("l"))  # 10
```

### center()

```python
a = "woosal"
print(a.center(10))  # "     woosal     "
```

```python
a = "woosal"
print(a.center(10, "-"))  # "--woosal--"
```

```python
a = "wosal"
print(a.center(10, "-"))  # "--wosal---"
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
print(a.partition("o"))  # ('w', 'o', 'osal')
```

```python
a = "woosal"
print(a.partition("z"))  # ('woosal', '', '')
```

### rpartition()

```python
a = "woosal"
print(a.rpartition("o"))  # ('wo', 'o', 'sal')
```

```python
a = "woosal"
print(a.rpartition("z"))  # ('', '', 'woosal')
```

### encode() [cp1254](https://en.wikipedia.org/wiki/Windows-1254)

```python
print("çilek".encode("cp1254"))  # b'\xe7ilek'
```

### expandtabs()

```python
a = "woo\tsa\tl"
print(a.expandtabs(10))  # "woo       sa        l"
```

### str.maketrans() / translate()

```python
kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"

çeviri_tablosu = str.maketrans(kaynak, hedef)

metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."

print(metin.translate(çeviri_tablosu))
```

### isalpha()

```python
a = "woosal"
print(a.isalpha())  # True
```

```python
a = "woosal1337"
print(a.isalpha())  # False
```

### isdigit()

```python
a = "1337"
print(a.isdigit())  # True
```

```python
a = "1337!"
print(a.isdigit())  # False
```

### isalnum()

```python
a = "woosal1337"
print(a.isalnum())  # True
```

```python
a = "woosal1337!"
print(a.isalnum())  # False
```

### isdecimal()

```python
a = "1337"
print(a.isdecimal())  # True
```

```python
a = "1337.1337"
print(a.isdecimal())  # False
```

### isidentifier()

```python
print("random_name".isidentifier())  # True
```

```python
print("1337name".isidentifier())  # False
```

### isnumeric()

```python
print("1337".isnumeric())  # True
```

```python
print("13.37".isnumeric())  # False
```

### isspace()

```python
print(" ".isspace())  # True
```

```python
print("           ".isspace())  # True
```

```python
print("wosoal".isspace())  # False
```

### isprintable()

```python
print("woosal".isprintable())  # True
```

```python
print("\n".isprintable())  # False
```

## `%`

### s

```python
print("my name is %s" % "vusal")
```

### d

```python
print("i am %d years old" % 19)
```

### o (octal)

```python
print("%i sayısının sekizli düzendeki karşılığı %o sayısıdır." % (10, 10))  # 12
```

### x (hexadecimal)

```python
print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." % (20, 20))  # 14
```

### X (hexadecimal)

```python
print("%i sayısının onaltılı düzendeki karşılığı %X sayısıdır." % (10, 10))  # A
```

### f (float)

```python
print("Dolar %f TL ..." % 8.567)  # 8.567000
```

### c

```python
print("%c" % 65)  # A
```

## `lists []`

### append()

```python
liste = ["elma", "armut", "çilek"]
liste.append("erik")
```

### extend()

```python
li1 = [1, 3, 4]
li2 = [10, 11, 12]
li1.extend(li2)  # [1, 3, 4, 10, 11, 12]
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
print(liste)  # ["armut", "çilek"]
```

### reverse()

```python
liste = ["elma", "armut", "çilek"]
liste.reverse()
print(liste)  # ["çilek", "armut", "elma"]
```

```python
liste = ["elma", "armut", "çilek"]
liste = liste[::-1]
print(liste)  # ["çilek", "armut", "elma"] 
```

```python
liste = ["elma", "armut", "çilek"]
reversed(liste)
print(list(liste))  # ["çilek", "armut", "elma"]

print(*liste)  # çilek armut elma
```

### pop()

```python
liste = ["elma", "armut", "çilek"]
liste.pop()
print(liste)  # ["elma", "armut"]
```

```python
liste = ["elma", "armut", "çilek"]
print(liste.pop(1))
print(liste)  # ["elma", "çilek"]
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
print(liste.index("elma"))  # 0
```

### count()

```python
liste = ["elma", "armut", "elma", "çilek"]
print(liste.count("elma"))  # 2
```

### copy()

```python
liste1 = ["ahmet", "mehmet", "özlem"]
liste2 = liste1[:]
liste2.pop()

print(liste1)  # ["ahmet", "mehmet", "özlem"]
print(liste2)  # ["ahmet", "mehmet"]
```

```python
liste1 = ["ahmet", "mehmet", "özlem"]
liste2 = list(liste1)
liste2.pop()

print(liste1)  # ["ahmet", "mehmet", "özlem"]
print(liste2)  # ["ahmet", "mehmet"]
```

```python
liste1 = ["ahmet", "mehmet", "özlem"]
liste2 = liste1.copy()
liste2.pop()

print(liste1)  # ["ahmet", "mehmet", "özlem"]
print(liste2)  # ["ahmet", "mehmet"]
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
print(bin(2)[2:])  # 10
```

### hex()

```python
print(hex(10)[2:])  # a
```

### oct()

```python
print(oct(10)[2:])  # 12
```

### int() (universal to all)

```python
print(int('1100', 2))  # 12
```

```python
print(int('1100', 16))  # 4352
```

### pow()

```python
print(pow(2, 3))  # 8
print(pow(2, 3, 8))  # (2**3) % 8 = 0
```

## `imaginary / complex values`

```python
c = 12 + 4j
print(c.imag)  # 4.0
print(c.real)  # 12.0
```

## `arithmetic ops`

### abs()

```python
a = -2
print(abs(a))  # 2
```

### divmod()

```python
print(divmod(10, 3))  # (3, 1) (a // b, a % b) 
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
            402324, 156156, 839504, 625325, 694080, 904277, 163914, 756250, 809689,
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

print(max(the_list))  # 996780
```

##### custom sorting

```python
isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah",
           "gıyaseddin", "sibel", "can", "necmettin", "savaş", "özgür"]

print(max(isimler, key=len))  # gıyaseddin
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
            402324, 156156, 839504, 625325, 694080, 904277, 163914, 756250, 809689,
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

print(min(the_list))  # 471
```

```python
isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah",
           "gıyaseddin", "sibel", "can", "necmettin", "savaş", "özgür"]

print(min(isimler, key=len))  # can
```

### sum()

```python
a = [10, 20, 43, 45, 77, 2, 0, 1]
print(sum(a))  # 198
```

```python
a = [10, 20, 43, 45, 77, 2, 0, 1]
print(sum(a, 10))  # 208
```

## `dictionaries {}`

### keys()

```python
sözlük = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}

print(sözlük.keys())  # dict_keys(['a', 'b', 'c', 'd'])
print(list(sözlük.keys()))  # ['a', 'b', 'c', 'd']
print("".join(sözlük.keys()))  # abcd
```

### values()

```python
sözlük = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}

print(sözlük.keys())  # dict_values(['0', '1', '2', '3'])
print(list(sözlük.keys()))  # ['0', '1', '2', '3']
print("".join(sözlük.keys()))  # 0123
```

### items()

```python
sözlük = {"a": '0',
          "b": '1',
          "c": '2',
          "d": '3'}

print(sözlük.items())  # dict_items([('a', '0'), ('b', '1'), ('c', '2'), ('d', '3')])
print(list(sözlük.items()))  # [('a', '0'), ('b', '1'), ('c', '2'), ('d', '3')]
```

### get()

```python
ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")
print(ing_sözlük.get(sorgu,
                     "Bu kelime veritabanımızda yoktur!"))  # False return statement: "Bu kelime veritabanımızda yoktur!"
```

### clear()

```python
lig = {"şampiyon": "Adana Demirspor", "ikinci": "Mersin İdman Yurdu",
       "üçüncü": "Adana Gençlerbirliği"}
lig.clear()
print(lig)  # {}
```

```python
lig = {"şampiyon": "Adana Demirspor", "ikinci": "Mersin İdman Yurdu",
       "üçüncü": "Adana Gençlerbirliği"}
del lig
print(lig)  # NameError: name 'lig' is not defined
```

### copy()

```python
lig = {"şampiyon": "Adana Demirspor", "ikinci": "Mersin İdman Yurdu", "üçüncü": "Adana Gençlerbirliği"}
lig2 = lig.copy()
print(lig2)  # {"şampiyon": "Adana Demirspor", "ikinci": "Mersin İdman Yurdu", "üçüncü": "Adana Gençlerbirliği"}
```

### fromkeys()

```python
elemanlar = "Ahmet", "Mehmet", "Can"
adresler = dict.fromkeys(elemanlar, "Kadıköy")
print(adresler)  # {'Ahmet': 'Kadıköy', 'Mehmet': 'Kadıköy', 'Can': 'Kadıköy'}
```

### pop()

```python
sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye"),
         "içecekler": ("su", "kola", "ayran")}

print(sepet.pop("meyveler"))  # ("elma", "armut")
print(sepet)  # {'sebzeler': ('pırasa', 'fasulye'), 'içecekler': ('su', 'kola', 'ayran')}

print(sepet.pop("meyveler",
                "There is not anything named in the dictionary!"))  # There is not anything named in the dictionary!
```

### popitem()

```python
sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}

print(sepet.popitem())  # ("sebzeler": ("pırasa", "fasulye"))
print(sepet)  # {"meyveler": ("elma", "armut")}
```

### setdefault()

```python
sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}

print(sepet.setdefault("woosal", ("1", "3", "3", "7")))  # ('1', '3', '3', '7')
print(sepet)  # {'meyveler': ('elma', 'armut'), 'sebzeler': ('pırasa', 'fasulye'), 'woosal': ('1', '3', '3', '7')}
```

### update()

```python
stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}

yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}

print(stok.update(yeni_stok))  # None
print(stok)  # {'elma': 3, 'armut': 20, 'peynir': 8, 'sosis': 4, 'sucuk': 6}
```

```python
stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}

yeni_stok = {"sucuk": 6}

print(stok.update(yeni_stok))  # None
print(stok)  # {'elma': 5, 'armut': 10, 'peynir': 6, 'sosis': 15, 'sucuk': 6}
```

## `set()`

```python
kardiz = "Python Programlama Dili"
kume = set(kardiz)

print(kume)  # {'g', 'h', ' ', 'a', 't', 'r', 'P', 'm', 'D', 'n', 'i', 'l', 'o', 'y'}
```

```python
liste = ["elma", "armut", "elma", "kebap", "şeker", "armut", "çilek", "ağaç", "şeker", "kebap", "şeker"]

print(set(liste))  # {'ağaç', 'şeker', 'çilek', 'armut', 'kebap', 'elma'}
```

```python
print(dir(set))
# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', #'__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', #'__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', #'__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', #'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
```

##### add()

```python
a = {1, 2, 3, 4, 5}
a.add(7)
a.add(6)

print(a)  # {1, 2, 3, 4, 5, 6, 7}
```

##### clear()

```python
a = {1, 2, 3, 4, 5}
a.clear()

print(a)  # set()
```

##### copy()

```python
a = {1, 2, 3, 4, 5}
b = a.copy()

print(b)  # {1,2,3,4,5}
```

##### difference()

```python
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5, 6}

print(a.difference(b))  # set()
print(b.difference(a))  # {6}
```

##### difference_update()

```python
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5, 6}

print(a.difference_update(b))  # None
print(a)  # set()
```

```python
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5, 6}

print(b.difference_update(a))  # None
print(b)  # {6}
```

##### discard()

```python
sets = set([10, 20, 26, 41, 54, 20])
sets.discard(20)

print(sets)  # {41, 10, 26, 54}
```

##### intersection()

```python
A = {2, 3, 5}
B = {1, 3, 5}

print(A.intersection(B))  # {3, 5}
```

###### intersection_update()

```python
A = {2, 3, 5}
B = {1, 3, 5}

print(A.intersection_update(B))  # None
print(A)  # {3, 5}
```

##### isdisjoint()

```python
A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))  # True
print('Are A and C disjoint?', A.isdisjoint(C))  # False
```

##### issubset()

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print(A.issubset(B))  # True
print(B.issubset(A))  # False
print(A.issubset(C))  # False
print(C.issubset(B))  # True
```

##### issuperset()

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print(A.issuperset(B))  # False
print(B.issuperset(A))  # True
print(A.issuperset(C))  # False
print(C.issuperset(B))  # False
```

##### pop()

```python
A = {1, 2, 3}
A.pop()

print(A)  # {2, 3}
```

##### remove()

```python
A = {1, 2, 3}
A.remove(2)

print(A)  # {1, 3}
```

##### symmetric_difference()

```python
A = {2, 4, 6, 8, 10}
B = {1, 3, 5, 7, 9}

print(B.symmetric_difference(A))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(A.symmetric_difference(B))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 
```

##### union()

```python
A = {2, 3, 5}
B = {1, 3, 5}

print(A | B)  # {1, 2, 3, 5} 
print(A.union(B))  # {1, 2, 3, 5}
```

##### update()

```python
A = {'a', 'b'}
B = {1, 2, 3}

print(A.update(B))  # None
print(A)  # {1, 2, 'b', 3, 'a'}
```

##### frozenset()

```python
dondurulmuş = frozenset(["elma", "armut", "ayva"])
print(dir(dondurulmuş))
# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', #'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', #'__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', #'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
```

## `built-in functions`

### abs()

```python
print(abs(-20))  # 20
```

```python
print(abs(20 + 3j))  # 20.223748416156685
```

```python
print(abs(20.0))  # 20.0
```

### round()

```python
print(round(12.4))  # 12
print(round(12.7))  # 13

print(round(1.5))  # 2
print(round(12.5))  # 12
```

##### if the integer part of the value is even, then the rounding is done to the floor not the ceil

```python
print(round(22 / 7))  # 3
```

```python
print(round(22 / 7, 0))  # 3.0
print(round(22 / 7, 1))  # 3.1
print(round(22 / 7, 2))  # 3.14
print(round(22 / 7, 3))  # 3.143
```

### all()

```python
liste = [1, 2, 3, 4]
print(all(liste))  # True
```

```python
liste = [0, 1, 2, 3, 4]
print(all(liste))  # False
```

```python
liste = ['ahmet', 'mehmet', '']
print(all(liste))  # False
```

### any()

```python
liste = ['ahmet', 'mehmet', '']
print(all(liste))  # True
```

```python
l = ['', 0, [], (), set(), dict()]
print(any(l))  # False
```

### ascii()

```python
a = 'woosal'
print(ascii(a))  # 'woosal' 
```

```python
a = 'ışık'
print(ascii(a))  # '\u0131\u015f\u0131k'
```

### repr()

```python
print(repr('şeker'))  # 'şeker'
```

### bool()

```python
print(bool(0))  # False
print(bool(1))  # True
print(bool([]))  # False
```

### bin()

```python
print(bin(12))  # '0b1100'
```

### bytes()

```python
print(bytes(10))  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```

```python
print('ışık'.encode('utf-8'))  # b'\xc4\xb1\xc5\x9f\xc4\xb1k'
print('ışık'.encode('cp857'))  # b'\x8d\x9f\x8dk'
print('ışık'.encode('cp1254'))  # b'\xfd\xfe\xfdk'
```

```python
print(bytes('ışık', 'utf-8'))  # b'\xc4\xb1\xc5\x9f\xc4\xb1k'
print(bytes('ışık', 'cp1254'))  # b'\xfd\xfe\xfdk'
print(bytes('ışık', 'cp857'))  # b'\x8d\x9f\x8dk'
```

### bytearray()

```python
a = bytes('istihza', 'ascii')
print(a[0])  # 105
```

### chr()

```python
print(chr(10))  # '\n'
print(chr(65))  # 'A'
```

### list()

```python
print(list('istihza'))  # ['i', 's', 't', 'i', 'h', 'z', 'a']
```

```python
s = {'elma': 44, 'armut': 10, 'erik': 100}
print(list(s))  # ['armut', 'erik', 'elma']
print(list(s.values()))  # [10, 100, 44]
```

### set()

```python
i = 'istihza'
print(set(i))  # {'t', 's', 'z', 'a', 'i', 'h'}
```

### tuple()

```python
print(tuple('a'))  # ('a', )
```

### frozenset()

```python
s = set('istihza')
print(frozenset(s))  # frozenset({'t', 's', 'a', 'z', 'i', 'h'})
```

### complex()

```python
print(complex(15))  # (15+0j)
print(complex(15, 2))  # (15 + 2j)
```

### float()

```python
print(float('134'))  # 134.0
print(float(12))  # 12.0
```

### int()

```python
print(int('10'))  # 10
print(12.4)  # 12
```

```python
print(int('12', 8))  # 10
```

```python
print(int('4cf', 16))  # 1231
```

### str()

```python
print(str(12))  # '12'
```

```python
print(str(b'istihza', encoding='utf-8'))  # istihza
```

```python
print(bytes('kadın', encoding='utf-8'))  # b'kad\xc4\xb1n'
```

```python
bayt = bytes('kadın', encoding='utf-8')
print(str(bayt, encoding='ascii', errors='ignore'))  # kadn
```

### dict()

```python
print(dict(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}
```

```python
print(dict((['a', 1], ['b', 2], ['c', 3])))  # {'a': 1, 'b': 2, 'c': 3}
```

### callable()

```python
print(callable(open))  # True
```

```python
x = 5
print(callable(x))  # False
```

### ord()

```python
print(ord('a'))  # 97
print(ord('ı'))  # 305
```

### oct()

```python
print(oct(10))  # '0o12'
```

### hex()

```python
print(hex(305))  # '0x131'
```

### globals()

```python
globals()['z'] = 23  # z = 23
```

### locals()

```python
def fonksiyon(param1, param2):
    x = 10
    print(locals())


fonksiyon(10, 20)  # {'param1': 10, 'param2': 20, 'x': 10}
```

### copyright() / credits() / license()

```python
copyright()

"""
Copyright (c) 2001-2021 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
"""
```

```python
license()

"""
A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see http://www.opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit: 
releases have also been GPL-compatible; the table below summarizes
the various releases.

    Release         Derived     Year        Owner       GPL-
                    from                                compatible? (1)

    0.9.0 thru 1.2              1991-1995   CWI         yes
    1.3 thru 1.5.2  1.2         1995-1999   CNRI        yes
    1.6             1.5.2       2000        CNRI        no
    2.0             1.6         2000        BeOpen.com  no
    1.6.1           1.6         2001        CNRI        yes (2)
    2.1             2.0+1.6.1   2001        PSF         no
    2.0.1           2.0+1.6.1   2001        PSF         yes
    2.1.1           2.1+2.0.1   2001        PSF         yes
    2.1.2           2.1.1       2002        PSF         yes
    2.1.3           2.1.2       2002        PSF         yes
    2.2 and above   2.1.1       2001-now    PSF         yes

Footnotes:

(1) GPL-compatible doesn't mean that we're distributing Python under
    the GPL.  All Python licenses, unlike the GPL, let you distribute
    a modified version without making your changes open source.  The
Hit Return for more, or q (and Return) to quit: 
    GPL-compatible licenses make it possible to combine Python with
    other software that is released under the GPL; the others don't.

(2) According to Richard Stallman, 1.6.1 is not GPL-compatible,
    because its license has a choice of law clause.  According to
    CNRI, however, Stallman's lawyer has told CNRI's lawyer that 1.6.1
    is "not incompatible" with the GPL.

Thanks to the many outside volunteers who have worked under Guido's
direction to make these releases possible.


B. TERMS AND CONDITIONS FOR ACCESSING OR OTHERWISE USING PYTHON
===============================================================

Python software and documentation are licensed under the
Python Software Foundation License Version 2.

Starting with Python 3.8.6, examples, recipes, and other code in
the documentation are dual licensed under the PSF License Version 2
and the Zero-Clause BSD license.

Some software incorporated into Python is under different licenses.
Hit Return for more, or q (and Return) to quit: 
The licenses are listed with code falling under that license.


PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
--------------------------------------------

1. This LICENSE AGREEMENT is between the Python Software Foundation
("PSF"), and the Individual or Organization ("Licensee") accessing and
otherwise using this software ("Python") in source or binary form and
its associated documentation.

2. Subject to the terms and conditions of this License Agreement, PSF hereby
grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
analyze, test, perform and/or display publicly, prepare derivative works,
distribute, and otherwise use Python alone or in any derivative version,
provided, however, that PSF's License Agreement and PSF's notice of copyright,
i.e., "Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021 Python Software Foundation;
All Rights Reserved" are retained in Python alone or in any derivative version
prepared by Licensee.

3. In the event Licensee prepares a derivative work that is based on
or incorporates Python or any part thereof, and wants to make
Hit Return for more, or q (and Return) to quit: 
the derivative work available to others as provided herein, then
Licensee hereby agrees to include in any such work a brief summary of
the changes made to Python.

4. PSF is making Python available to Licensee on an "AS IS"
basis.  PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON WILL NOT
INFRINGE ANY THIRD PARTY RIGHTS.

5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON
FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS
A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON,
OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any
relationship of agency, partnership, or joint venture between PSF and
Licensee.  This License Agreement does not grant permission to use PSF
trademarks or trade name in a trademark sense to endorse or promote
Hit Return for more, or q (and Return) to quit: 
products or services of Licensee, or any third party.

8. By copying, installing or otherwise using Python, Licensee
agrees to be bound by the terms and conditions of this License
Agreement.


BEOPEN.COM LICENSE AGREEMENT FOR PYTHON 2.0
-------------------------------------------

BEOPEN PYTHON OPEN SOURCE LICENSE AGREEMENT VERSION 1

1. This LICENSE AGREEMENT is between BeOpen.com ("BeOpen"), having an
office at 160 Saratoga Avenue, Santa Clara, CA 95051, and the
Individual or Organization ("Licensee") accessing and otherwise using
this software in source or binary form and its associated
documentation ("the Software").

2. Subject to the terms and conditions of this BeOpen Python License
Agreement, BeOpen hereby grants Licensee a non-exclusive,
royalty-free, world-wide license to reproduce, analyze, test, perform
and/or display publicly, prepare derivative works, distribute, and
otherwise use the Software alone or in any derivative version,
Hit Return for more, or q (and Return) to quit: 
provided, however, that the BeOpen Python License is retained in the
Software, alone or in any derivative version prepared by Licensee.

3. BeOpen is making the Software available to Licensee on an "AS IS"
basis.  BEOPEN MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, BEOPEN MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE SOFTWARE WILL NOT
INFRINGE ANY THIRD PARTY RIGHTS.

4. BEOPEN SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF THE
SOFTWARE FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS
AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THE SOFTWARE, OR ANY
DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

5. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

6. This License Agreement shall be governed by and interpreted in all
respects by the law of the State of California, excluding conflict of
law provisions.  Nothing in this License Agreement shall be deemed to
create any relationship of agency, partnership, or joint venture
between BeOpen and Licensee.  This License Agreement does not grant
Hit Return for more, or q (and Return) to quit: 
permission to use BeOpen trademarks or trade names in a trademark
sense to endorse or promote products or services of Licensee, or any
third party.  As an exception, the "BeOpen Python" logos available at
http://www.pythonlabs.com/logos.html may be used according to the
permissions granted on that web page.

7. By copying, installing or otherwise using the software, Licensee
agrees to be bound by the terms and conditions of this License
Agreement.


CNRI LICENSE AGREEMENT FOR PYTHON 1.6.1
---------------------------------------

1. This LICENSE AGREEMENT is between the Corporation for National
Research Initiatives, having an office at 1895 Preston White Drive,
Reston, VA 20191 ("CNRI"), and the Individual or Organization
("Licensee") accessing and otherwise using Python 1.6.1 software in
source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, CNRI
hereby grants Licensee a nonexclusive, royalty-free, world-wide
license to reproduce, analyze, test, perform and/or display publicly,
Hit Return for more, or q (and Return) to quit: 
prepare derivative works, distribute, and otherwise use Python 1.6.1
alone or in any derivative version, provided, however, that CNRI's
License Agreement and CNRI's notice of copyright, i.e., "Copyright (c)
1995-2001 Corporation for National Research Initiatives; All Rights
Reserved" are retained in Python 1.6.1 alone or in any derivative
version prepared by Licensee.  Alternately, in lieu of CNRI's License
Agreement, Licensee may substitute the following text (omitting the
quotes): "Python 1.6.1 is made available subject to the terms and
conditions in CNRI's License Agreement.  This Agreement together with
Python 1.6.1 may be located on the Internet using the following
unique, persistent identifier (known as a handle): 1895.22/1013.  This
Agreement may also be obtained from a proxy server on the Internet
using the following URL: http://hdl.handle.net/1895.22/1013".

3. In the event Licensee prepares a derivative work that is based on
or incorporates Python 1.6.1 or any part thereof, and wants to make
the derivative work available to others as provided herein, then
Licensee hereby agrees to include in any such work a brief summary of
the changes made to Python 1.6.1.

4. CNRI is making Python 1.6.1 available to Licensee on an "AS IS"
basis.  CNRI MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, CNRI MAKES NO AND
Hit Return for more, or q (and Return) to quit: 
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON 1.6.1 WILL NOT
INFRINGE ANY THIRD PARTY RIGHTS.

5. CNRI SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON
1.6.1 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS
A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 1.6.1,
OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

7. This License Agreement shall be governed by the federal
intellectual property law of the United States, including without
limitation the federal copyright law, and, to the extent such
U.S. federal law does not apply, by the law of the Commonwealth of
Virginia, excluding Virginia's conflict of law provisions.
Notwithstanding the foregoing, with regard to derivative works based
on Python 1.6.1 that incorporate non-separable material that was
previously distributed under the GNU General Public License (GPL), the
law of the Commonwealth of Virginia shall govern this License
Agreement only as to issues arising under or with respect to
Paragraphs 4, 5, and 7 of this License Agreement.  Nothing in this
Hit Return for more, or q (and Return) to quit: 
License Agreement shall be deemed to create any relationship of
agency, partnership, or joint venture between CNRI and Licensee.  This
License Agreement does not grant permission to use CNRI trademarks or
trade name in a trademark sense to endorse or promote products or
services of Licensee, or any third party.

8. By clicking on the "ACCEPT" button where indicated, or by copying,
installing or otherwise using Python 1.6.1, Licensee agrees to be
bound by the terms and conditions of this License Agreement.

        ACCEPT


CWI LICENSE AGREEMENT FOR PYTHON 0.9.0 THROUGH 1.2
--------------------------------------------------

Copyright (c) 1991 - 1995, Stichting Mathematisch Centrum Amsterdam,
The Netherlands.  All rights reserved.

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
Hit Return for more, or q (and Return) to quit: 
supporting documentation, and that the name of Stichting Mathematisch
Centrum or CWI not be used in advertising or publicity pertaining to
distribution of the software without specific, written prior
permission.

STICHTING MATHEMATISCH CENTRUM DISCLAIMS ALL WARRANTIES WITH REGARD TO
THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS, IN NO EVENT SHALL STICHTING MATHEMATISCH CENTRUM BE LIABLE
FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

ZERO-CLAUSE BSD LICENSE FOR CODE IN THE PYTHON DOCUMENTATION
----------------------------------------------------------------------

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
Hit Return for more, or q (and Return) to quit: 
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
"""
```

```python
credits()

"""
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
"""
```

### dir()

```python
print(dir([]))

"""
['__add__', '__class__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', 
'__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 
 'remove', 'reverse', 'sort']
"""
```

### divmod()

```python
print(divmod(3, 1))  # (3, 0)
```

### enumerate()

```python
print(list(enumerate('istihza')))  # [(0, 'i'), (1, 's'), (2, 't'), (3, 'i'), (4, 'h'), (5, 'z'), (6, 'a')]
```

```python
print(print(*enumerate('istihza')))  # (0, 'i') (1, 's') (2, 't') (3, 'i') (4, 'h') (5, 'z') (6, 'a')
```

### exit()

```python
exit("HaCker 1337")  # HaCker 1337 exit status: 1
```

### help()

```python
help(dir)

"""
Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attribut
es
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.
"""
```

### id()

```python
a = 50
print(id(a))  # 139889596095744
```

### format()

```python
print("{} is {} years old".format("Vusal", 18))  # Vusal is 18 years old
```

```python
print(format(12, '.2f'))  # '12.00'
```

### filter()

```python
l = [400, 176, 64, 175, 355, 13, 207, 298, 397, 386, 31, 120, 120, 236, 241, 123, 249, 364, 292, 153]


def tek(sayı):
    return sayı % 2 == 1


print(list(filter(tek, l)))  # [175, 355, 13, 207, 397, 31, 241, 123, 249, 153]
```

### hash()

```python
print(hash('istihza'))  # -546274348900451588
```

### isinstance()

```python
print(type('istihza'))  # <class 'str'>
```

```python
print(isinstance('istihza', str))  # True
```

### len()

```python
print(len('istihza'))  # 7
```

```python
print(len([1, 4, 5, 3, 2, 9, 10]))  # 7
```

### map()

```python
l = [1, 4, 5, 4, 2, 9, 10]


def squared(n):
    return n ** 2


print(list(map(squared, l)))  # [1, 16, 25, 16, 4, 81, 100]
```

### max()

```python
print(max(1, 2, 3))  # 3
```

```python
print(max([1, 2, 3]))  # 3
```

```python
isimler = ['ahmet', 'can', 'mehmet', 'selin', 'abdullah', 'kezban']
print(max(isimler, key=len))  # 'abdullah'
```

```python
def en_yüksek_rütbe(rütbe):
    rütbeler = {
        'er': 0,
        'onbaşı': 1,
        'çavuş': 2,
        'asteğmen': 3,
        'teğmen': 4,
        'üsteğmen': 5,
        'yüzbaşı': 6,
        'binbaşı': 7,
        'yarbay': 8,
        'albay': 9
    }

    return rütbeler[rütbe]


askerler = {
    'mehmet': 'onbaşı',
    'ali': 'teğmen',
    'cevat': 'yüzbaşı',
    'berkay': 'albay',
    'mahmut': 'üsteğmen',
    'ahmet': 'binbaşı'
}

print(max(askerler.values(), key=en_yüksek_rütbe))  # binbaşı
```

### min() (!max())

```python
print(min([1, 2, 3]))  # 1
```

### open()

```python
open("text.txt", mode='w', buffering=-1, encoding=None,
     errors=None, newline=None, closefd=True, opener=None)
```

### pow()

```python
print(pow(2, 3))  # 8
print(pow(2, 3) == 2 ** 3)  # True
```

```python
print(pow(2, 3, 2))  # 0
print(pow(2, 3, 2) == (2 ** 3 % 2))  # True
```

### quit()

```python
'''
exits the running system code 
'''
```

### reversed()

```python
isimler = ['ahmet', 'mehmet', 'veli', 'ayşe', 'çiğdem', 'ışık']
print(*reversed(isimler))  # ışık çiğdem ayşe veli mehmet ahmet
print(list(reversed(isimler)))  # ['ışık', 'çiğdem', 'ayşe', 'veli', 'mehmet', 'ahmet']
```

### sorted()

```python
print(sorted('ahmet'))  # ['a', 'e', 'h', 'm', 't']
print(sorted(('elma', 'armut', 'kiraz', 'badem')))  # ['armut', 'badem', 'elma', 'kiraz']
print(sorted(['elma', 'armut', 'kiraz', 'badem']))  # ['armut', 'badem', 'elma', 'kiraz']
```

### slice()

```python
l = ['ahmet', 'mehmet', 'ayşe', 'senem', 'salih']
dl = slice(0, 3)

print(l[dl])  # ['ahmet', 'mehmet', 'ayşe']

'''
slice(start, end, skip)
'''
```

### sum()

```python
l = [1, 2, 3]
print(sum(l))  # 6
print(sum(l, 10))  # 16
```

### type()

```python
print(type('apple'))  # <class 'str'>
```

### zip()

```python
a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']

print(zip(a1, a2))  # <zip object at 0x7f1b99ba7580>
print(*zip(a1, a2))  # ('a', 'd') ('b', 'e') ('c', 'f')
```

### vars()

```python
print(vars())

'''
{'__name__': '__main__', '__doc__': None, '__package__': None, 
'__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f4ee56904c0>, 
'__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 
'__file__': 'main.py', '__cached__': None}
'''
```

## `lambda functions`

```python
def f(param1, param2):
    return param1 + param2
```

##### converted to `lambda`:

```python
f = lambda param1, param2: param1 + param2
```

```python
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"

çevrim = {i: harfler.index(i) for i in harfler}

isimler = ["ahmet", "ışık", "ismail", "çiğdem",
           "can", "şule", "iskender"]

print(
    sorted(isimler, key=lambda x: çevrim.get(x[0])))  # ['ahmet', 'can', 'çiğdem', 'ışık', 'ismail', 'iskender', 'şule']
```

```python
is_even = lambda x: x % 2 == 0

print(is_even(4))  # True 
```

```python
print(*map(lambda x: x ** 2, [1, 2, 3, 4, 5]))  # 1 4 9 16 25
```

## `recursive`

```python
def düz_liste_yap(liste):
    if not isinstance(liste, list):
        return [liste]
    elif not liste:
        return []
    else:
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])


l = [1, 2, 3, [[[4], 5], 6], [7, 8, 9, [10, 11], 12], 13, 14]
print(düz_liste_yap(l))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

## `nested functions`

```python
def f():
    def y(x):
        print(x)

    return y


new_f = f()
new_f(1)  # 1
```

```python
def f():
    def y(x):
        print(x)

        def z(y):
            print(y)

        return z

    return y


new_f = f()
new_f(5)  # 5 
new_f(5)(6)  # 5 6
```

```python
a = 3


def f():
    global a

    def y(x=1):
        print(x)
        print(a)

        def z(y=2):
            print(y)
            print(a)

        return z

    return y


new_f = f()
new_f()  # 1 3
new_f()()  # 2 3
```

```python
def f():
    a = 5

    def y(x=1):
        print("y")

        def z(y=2):
            nonlocal a
            print("z")
            print(a)

        return z

    return y


new_f = f()
new_f()()  # y z 5
```

## `generators`

```python
a = 5


def fonksiyon_sayıcı():
    def say():
        global a
        a += 1
        return a

    return say


def üreteç_sayıcı():
    sayı = 0

    while True:
        sayı += 1
        yield sayı


f = üreteç_sayıcı()
print(next(f))  # 1
print(next(f))  # 2
print(next(f))  # 3
print(next(f))  # 4
print(next(f))  # 5
print(next(f))  # 6
```

```python
def f():
    yield 1
    yield 2
    yield 3


f = f()

print(next(f))  # 1
print(next(f))  # 2
print(next(f))  # 3
```

```python
def f():
    print("1st next here!")
    yield 1

    print("2nd next here!")
    yield 2

    print("3rd next here!")
    yield 3


f = f()

print(next(f))  # 1st next here! 1
print(next(f))  # 2nd next here! 2
print(next(f))  # 3rd next here! 3
```

```python
def f():
    c = 0
    x, y, z = 1, 0, 0

    while True:
        z = y
        y = x
        x = y + z

        yield x

        c += 1

        if c > 10:
            return


f = f()
for i in f:
    print(i)

"""
1
2
3
5
8
13
21
34
55
89
144
""" 
```

```python
def üreteç1():
    yield "üreteç1 başladı"
    yield "üreteç1 bitti"


def üreteç2():
    yield "üreteç2 başladı"
    yield from üreteç1()
    yield "üreteç2 bitti"


ur2 = üreteç2()

print(*ur2, sep="\n")
"""
üreteç2 başladı
üreteç1 başladı
üreteç1 bitti
üreteç2 bitti
"""
```

```python
def üreteç1():
    yield "üreteç1 başladı"
    yield "üreteç1 bitti"


def üreteç2():
    yield "üreteç2 başladı"
    yield next(üreteç1())
    yield "üreteç2 bitti"


ur2 = üreteç2()

print(*ur2, sep="\n")
"""
üreteç2 başladı
üreteç1 başladı
üreteç2 bitti
"""
```

```python
def üreteç1():
    yield "üreteç1 başladı"
    yield "üreteç1 bitti"


ur1 = üreteç1()


def üreteç2():
    yield "üreteç2 başladı"
    yield next(ur1)
    yield next(ur1)
    yield "üreteç2 bitti"


ur2 = üreteç2()

print(*ur2, sep="\n")
"""
üreteç2 başladı
üreteç1 başladı
üreteç1 bitti
üreteç2 bitti
"""
```

## `function decorators`

```python
def f(x):
    print("Bu f fonksiyonudur!")
    x()


def y():
    print("Bu y fonksiyonudur")


f(y)

"""
Bu f fonksiyonudur!
Bu y fonksiyonudur
"""
```

```python
def z():
    print("Bu z fonksiyonudur!")

    def nested():
        print("Bu icerideki fonskiyondur!")

    nested()


z()

"""
Bu z fonksiyonudur!
Bu icerideki fonskiyondur!
"""
```

```python
def decor(x):
    def wrapper():
        print("wrapper started")
        x()
        print("wrapper ended")

    return wrapper


def hello():
    print('hello, world!')


d = decor(hello)
d()

"""
wrapper started
hello, world!
wrapper ended
"""
```

```python
def decor(x):
    def wrapper():
        print("wrapper started")
        x()
        print("wrapper ended")

    return wrapper()


def hello():
    print('hello, world!')


decor(hello)

"""
wrapper started
hello, world!
wrapper ended
"""
```

## `oop`

### @classmethod

```python
from datetime import date


# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)
person.display()

person1 = Person.from_birth_year('John', 1985)
person1.display()

"""
Adam's age is: 19
John's age is: 36
"""
```

```python
from datetime import date


# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


class Man(Person):
    sex = 'Male'


man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))
print(isinstance(man1, Person))

"""
True
False
True
"""
```

### @staticmethod

```python
class Mathematics:

    def addNumbers(x, y):
        return x + y


# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is:', Mathematics.addNumbers(5, 10))

"""
The sum is: 15
"""
```

```python
class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if (date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")

"""
Equal
"""
```

```python
class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)


date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if (date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")

"""
Equal
"""
```

## @property

```python
# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)

"""
Setting value...
Getting value...
37
Getting value...
98.60000000000001
Setting value...
Traceback (most recent call last):
  File "<string>", line 29, in <module>
  File "<string>", line 4, in __init__
  File "<string>", line 18, in temperature
ValueError: Temperature below -273 is not possible
"""
```

## `__new__`

```python
class Sınıf():
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)
```

## `RegEx`

### match()

##### == startswith()

```python
import re

a = "python güçlü bir programlama dilidir."
print(re.match("python", a))

"""
<re.Match object; span=(0, 6), match='python'>
"""

print(re.match("Java", a))

"""
None
"""
```

### search()

```python
import re

a = "python güçlü bir programlama dilidir."
print(re.search('python', a))  # <re.Match object; span=(0, 6), match='python'>
```

```python
import re

a = "güçlü bir programlama dilidir python."
print(re.search('python', a))  # <re.Match object; span=(30, 36), match='python'>
```

### findall()

```python
import re

a = """Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani
aslında Python için nispeten yeni bir dil denebilir. Ancak Python'un çok uzun
bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı olması,
ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden
ötürü çoğu kimsenin gözdesi haline gelmiştir. Ayrıca Google'ın da Python'a özel
bir önem ve değer verdiğini, çok iyi derecede Python bilenlere iş olanağı
sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın
yaratıcısı Guido Van Rossum Google'de işe başladı..."""

print(re.findall('Python', a))  # ['Python', 'Python', 'Python', 'Python', 'Python', 'Python']
```

## metacharacters

```python
import re

a = ["özcan", "mehmet", "süleyman", "selim", "kemal", "özkan", "esra", "dündar", "esin", "esma", "özhan", "özlem"]

for i in a:
    if re.search('öz[chk]an', i):
        print(re.search('öz[chk]an', i).group(), end=" ")  # özcan özkan özhan
```

```python
import re

a = ["23BH56","TY76Z","4Y7UZ","TYUDZ","34534"]

for i in a:
    res = re.match("[0-9]", i)
    
    if res:
        print(res)

"""
<re.Match object; span=(0, 1), match='2'>
<re.Match object; span=(0, 1), match='4'>
<re.Match object; span=(0, 1), match='3'>
"""
```

```python
import re

a = ["özcan", "mehmet", "süleyman", "selim", "kemal", "özkan", "esra", "dündar", "esin", "esma", "özhan", "özlem"]

for i in a:
    res = re.match("es.a", i)

    if res:
        print(res.group())

"""
esra
esma
"""
```


##### == endswith()
```python
import re

a = ["ahmet","kemal", "kamil", "mehmet"]

for i in a:
    res = re.match(".*met", i)

    if res:
        print(res.group())

"""
ahmet
mehmet
"""
```

```python
import re

a = "python güçlü bir dildir"

print(re.search(".*güçlü", a))

"""
<re.Match object; span=(0, 12), match='python güçlü'>
"""
```

### +
```python
import re

liste = ["ahmet", "mehmet", "met", "kezban"]

for i in liste:
    res = re.match(".+met", i)

    if res:
        print(res.group())

"""
ahmet
mehmet
"""
```

```python
import re

yeniliste = ["st", "sat", "saat", "saaat", "falanca"]
for i in yeniliste:
    if re.match("sa+t",i):
        print(i)

"""
sat
saat
saaat
"""
```

# Important Libraries:
### `RegEx`
### `datetime`
### `math`
### `random`
### `Sqlite`
### `os`
### `time`
### `curses`
### `threading`
### `sched`
### `json`
### `timeit`
### `sys`
### `argparse`