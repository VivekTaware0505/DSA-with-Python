"""
Topic : Isomorphic Strings

1. What are Isomorphic Strings?

Two strings are Isomorphic if the characters in one string can be replaced to get the second string.

Rules
Every character must map to exactly one character.
Two different characters cannot map to the same character.
The order of characters must remain the same.

Isomorphic mapping is used in:

Data Encoding
Cryptography
Pattern Matching
Compiler Design
Character Mapping Problems


Q.1 Isomorphic Strings

Input
s = "badc"

t = "baba"

Output
False
"""
def isomorphic(s, t):

    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for i in range(len(s)):

        a = s[i]
        b = t[i]

        if a in s_map and s_map[a] != b:
            return False

        if b in t_map and t_map[b] != a:
            return False

        s_map[a] = b
        t_map[b] = a

    return True


print(isomorphic("badc", "baba"))
print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Q.2 Input
Pattern = "abba"

Sentence = "dog cat cat dog"
Output
True

Explanation

a → dog

b → cat

b → cat

a → dog

This is exactly the same mapping concept as Isomorphic Strings.

"""
def word_pattern(pattern, sentence):

    words = sentence.split()

    if len(pattern) != len(words):
        return False

    p_map = {}
    w_map = {}

    for p, w in zip(pattern, words):

        if p in p_map and p_map[p] != w:
            return False

        if w in w_map and w_map[w] != p:
            return False

        p_map[p] = w
        w_map[w] = p

    return True


print(word_pattern("abba", "dog cat cat dog"))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Topic 11 : Valid Parentheses

1. What is Valid Parentheses?

A string containing only:

( ) { } [ ]

is valid if:

Every opening bracket has a matching closing bracket.
Brackets close in the correct order.
Every opening bracket is closed exactly once.


Valid Parentheses is used in:

Compilers
Code editors (VS Code, PyCharm)
HTML/XML tag validation
Expression evaluation
Calculator applications
Syntax checking


Q.1 Handle all three bracket types

"""
def valid_parentheses(s):

    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        if ch in "([{":
            stack.append(ch)

        else:

            if not stack:
                return False

            if stack[-1] != pairs[ch]:
                return False

            stack.pop()

    return len(stack) == 0


print(valid_parentheses("{[()]}"))

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Q.2 Minimum Additions to Make Parentheses Valid
Input
()))
Output
2

Explanation:

Add:

(())

or another valid arrangement requiring two insertions.

"""
def min_add(s):

    balance = 0
    additions = 0

    for ch in s:

        if ch == '(':
            balance += 1

        else:

            if balance > 0:
                balance -= 1
            else:
                additions += 1

    return additions + balance


print(min_add("()))"))

print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Topic 12 ; Roman to Integer

1. What are Roman Numerals?

Roman numerals are represented using 7 symbols.
| Symbol | Value |
| ------ | ----: |
| I      |     1 |
| V      |     5 |
| X      |    10 |
| L      |    50 |
| C      |   100 |
| D      |   500 |
| M      |  1000 |



"""
def roman_to_int(s):

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    for i in range(len(s)):

        if i < len(s) - 1 and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]

    return total


print(roman_to_int("MCMXCIV"))

print("------------------------------Vivek Learning DSA Python----------------------------------------")

roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

s = "IV"

total = 0

for i in range(len(s)):

    if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
        total -= roman[s[i]]
    else:
        total += roman[s[i]]

print(total)
print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""

Topic 13: Integer to Roman

1. What is Integer to Roman?

This problem is the reverse of the previous topic.

You are given an integer, and you need to convert it into its Roman numeral representation.





3. Why Greedy Algorithm?

At every step:

👉 Choose the largest Roman value that is less than or equal to the current number.

Example:

1994

↓

1000 → M

Remaining = 994

↓

900 → CM

Remaining = 94

↓

90 → XC

Remaining = 4

↓

4 → IV

Answer = MCMXCIV

This is exactly how the Greedy Algorithm works.

4. Algorithm
Store Roman values in descending order.
Start with the largest value.
If the number is greater than or equal to that value:
Add the Roman symbol.
Subtract the value.
Continue until the number becomes 0.




Q.1Input
58

"""
def int_to_roman(num):

    values = [
        1000,900,500,400,
        100,90,50,40,
        10,9,5,4,1
    ]

    romans = [
        "M","CM","D","CD",
        "C","XC","L","XL",
        "X","IX","V","IV","I"
    ]

    result = ""

    for i in range(len(values)):

        while num >= values[i]:

            result += romans[i]
            num -= values[i]

    return result


print(int_to_roman(58))


print("------------------------------Vivek Learning DSA Python----------------------------------------")

"""
Q.2 Input
1994
Dry Run
Number	Roman	Remaining
1994	M	994
994	CM	94
94	XC	4
4	IV	0

Answer

MCMXCIV
"""

def int_to_roman(num):

    values = [
        1000,900,500,400,
        100,90,50,40,
        10,9,5,4,1
    ]

    romans = [
        "M","CM","D","CD",
        "C","XC","L","XL",
        "X","IX","V","IV","I"
    ]

    answer = ""

    for value, symbol in zip(values, romans):

        while num >= value:
            answer += symbol
            num -= value

    return answer


print(int_to_roman(1994))
print("------------------------------Vivek Learning DSA Python----------------------------------------")


