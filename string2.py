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
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")

