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
print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")
