"""
Memory representation:

+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+

Visual Representation
Word = " python"
"""

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
String Indexing 
python index start from 0 

"""
word = " python"
print(word[0])
print(word[1])

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Negative / or reverse  indexing 
Python also supports negative indexing.

 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1

"""

print(word[-1])
print(word[-3])

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
after creating a string you cannot change indivisual characters

python creates a new string instead of mofdifying the old one 

name = " Vivek"
name[0] = "S"
"""


print("------------------------------Vivek Learning DSA Python----------------------------------------")
"loop in python  "


for ch in "Python":
    print(ch)
print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""
Q.1 count volwels in a string 

"""
text = "Python Programming"

vowels = "aeiouAEIOU"

count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Total Vowels:", count)



print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
