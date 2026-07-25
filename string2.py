"""
 
Topic 5 : Reverse String

1. What is Reverse a String?

Reversing a string means arranging its characters in the opposite order.

String reversal is used in:

Checking Palindromes
Text Processing
Encryption and Decryption
Data Compression
Compiler Design
DNA Sequence Analysis
Interview Problems




Q.1 Although Python strings are immutable, 
the two-pointer algorithm is an important interview pattern. We first convert the string into a list.



 """
text = "Python"

chars = list(text)

left = 0
right = len(chars) - 1

while left < right:
    chars[left], chars[right] = chars[right], chars[left]
    left += 1
    right -= 1

result = "".join(chars)

print(result)

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Q.1 Reverse Only Letters
Kepp numbers and Special Characters in The same Position

"""
def reverse_only_letters(s):
    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:

        if not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha():
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)


print(reverse_only_letters("a,b$c"))


print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Topic 6 : check Palindrome
1. What is a Palindrome?

A Palindrome is a word, number, or sentence that reads the same forward and backward.
Palindrome checking is used in:

DNA sequence analysis
Natural Language Processing (NLP)
Text editors
Search algorithms
Data validation
Coding interviews


Q.1 This is the most preferred interview solution
"""
text = "madam"

left = 0
right = len(text) - 1

is_palindrome = True

while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")


print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""

Q.1 Valid Palindrome (Ignore Spaces & Special Characters)

"""
text = "A man, a plan, a canal: Panama"

clean = ""

for ch in text:
    if ch.isalnum():
        clean += ch.lower()

left = 0
right = len(clean) - 1

while left < right:
    if clean[left] != clean[right]:
        print(False)
        break

    left += 1
    right -= 1
else:
    print(True)


print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""

Q.2Find the maximum length of a palindrome that can be formed using the characters.

"""
from collections import Counter

text = "abccccdd"

freq = Counter(text)

length = 0
odd = False

for count in freq.values():
    length += (count // 2) * 2

    if count % 2 == 1:
        odd = True

if odd:
    length += 1

print(length)


print("------------------------------Vivek Learning DSA Python----------------------------------------")

