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

"""
Q.2 count volwels and consonants 

"""

text = "Programming"

vowels = "aeiouAEIOU"

vowel = 0
consonant = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel += 1
        else:
            consonant += 1

print("Vowels:", vowel)
print("Consonants:", consonant)

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Q.3 Find the first non-repeating character

"""
from collections import Counter

text = "aabbcddee"

freq = Counter(text)

for ch in text:
    if freq[ch] == 1:
        print(ch)
        break



print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Example 

longest substring without repeating characters

"""
def length_of_longest_substring(s):
    seen = {}
    left = 0
    ans = 0

    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1

        seen[s[right]] = right
        ans = max(ans, right - left + 1)

    return ans

print(length_of_longest_substring("abcabcbb"))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Interview Questions
Why are Python strings immutable?
What is the difference between positive and negative indexing?
What is the time complexity of indexing?
Why are strings considered sequence data types?
Can we change a single character in a Python string? Why?

"""


print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""

Topic 3: String Traversal
 Learning Objectives

After this topic, you will be able to:

Traverse a string using different methods.
Understand when to use each traversal technique.
Solve interview questions involving character-by-character processing.
Build a foundation for advanced string algorithms like Sliding Window, KMP, and Rabin-Karp.
1. What is String Traversal?

String Traversal means visiting each character of a string one by one to perform some operation.

Examples of operations:

Count vowels
Count digits
Reverse a string
Check palindrome
Find duplicate characters
Search for a character

Almost every string problem starts with traversal.

2. Real-Life Example

Imagine you're checking each character of a password:

Password = Vivek@123

You inspect every character:

V → Letter
i → Letter
v → Letter
e → Letter
k → Letter
@ → Special Symbol
1 → Digit
2 → Digit
3 → Digit

This is traversal.

3. Visualization
String = "Python"

Index

 0    1    2    3    4    5
 P    y    t    h    o    n
 ↑
Start Traversal

The pointer moves one position at a time until the end.

4. Methods to Traverse a String
Method 1: Using a for Loop (Recommended)

This is the simplest and most Pythonic way.

"""
" eaxample "
text = "Python"

for ch in text:
    print(ch)

print("------------------------------Vivek Learning DSA Python----------------------------------------")

" Useful when you also need the position."

text = "Python"

for i in range(len(text)):
    print(i, text[i])

print("------------------------------Vivek Learning DSA Python----------------------------------------")

" Using a while Loop"
text = "Python"

i = 0

while i < len(text):
    print(text[i])
    i += 1
print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Intermediate Example
Problem

Q.1 Count:

Uppercase letters
Lowercase letters
Digits
Special characters
Input
PyThOn@2026

"""

text = "PyThOn@2026"

upper = lower = digit = special = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special:", special)



print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Brute Force Approach

For every character:

Count its frequency.
If frequency is 1, return it.
"""
text = "aabbcdde"

for ch in text:
    if text.count(ch) == 1:
        print(ch)
        break

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Topic 4 String Immutability 


This is one of the most commonly asked Python interview concepts. Interviewers often ask:

Why are Python strings immutable?
What are the advantages of immutable strings?
How do you modify a string if it is immutable?



Learning Objectives

After this topic, you will understand:

What is immutability?
Why Python strings are immutable.
Benefits of immutable strings.
How to "modify" a string correctly.
Common interview questions.
Advanced examples.
1. What is Immutability?

Immutability means:

Once an object is created, it cannot be changed.


Why Does Python Make Strings Immutable?

Python designers made strings immutable for several important reasons.

A. Better Performance

If many variables contain the same string:

a = "Python"
b = "Python"
c = "Python"

Python can reuse the same string in memory instead of creating three separate copies.

This saves memory


Safe Data

Suppose your password is:

password = "Admin@123"

If strings were mutable, another part of the program could accidentally change it.

Immutability prevents accidental modifications.

C. Hashing

Dictionary keys must never change.

Example:

student = {
    "Vivek": 90
}

If "Vivek" could suddenly become "Rahul", the dictionary would break.

That is why strings are immutable and can safely be used as dictionary keys.

D. Thread Safety

When multiple parts of a program use the same string, 
immutability ensures that one part cannot unexpectedly change it for everyone else.
"""
a = "Python"
b = "Python"
c = "Python"


print("------------------------------Vivek Learning DSA Python----------------------------------------")

"Q.1 Replace Every Vowel With * "

text = "Programming"

vowels = "aeiouAEIOU"
result = ""

for ch in text:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print(result)

print("------------------------------Vivek Learning DSA Python----------------------------------------")


" Q.2 Remove consecutive duplicate character"

text = "aaabbbbccdaa"

result = text[0]

for i in range(1, len(text)):
    if text[i] != text[i - 1]:
        result += text[i]

print(result)

print("------------------------------Vivek Learning DSA Python----------------------------------------")
""" Q.3 Check if Two Strings are One Edit Away

Two strings are one edit away if they differ by only one insertion, deletion, or replacement."""
def one_edit_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    i = j = 0
    found = False

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if found:
                return False
            found = True

            if len(s1) == len(s2):
                i += 1
        else:
            i += 1

        j += 1

    return True

print(one_edit_away("pale", "ple"))


print("------------------------------Vivek Learning DSA Python----------------------------------------")
"q.4 Compress a String (Run-Length Encoding) "
text = "aaabbccccdd"

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result += text[i - 1] + str(count)
        count = 1

result += text[-1] + str(count)

print(result)

print("------------------------------Vivek Learning DSA Python----------------------------------------")
