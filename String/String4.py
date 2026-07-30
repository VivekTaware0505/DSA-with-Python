"""

Topic 14 : Longest Substring Without Repeating Characters


What is a Substring?

A substring is a continuous sequence of characters from a string.


String = "Python"

Substrings:
"P"
"Py"
"Pyt"
"yth"
"thon"
"Python"




Q.1 given a string find the length of the longest substring without repeating character

"""


def longest_substring(s):

    maximum = 0

    for i in range(len(s)):

        seen = set()

        for j in range(i, len(s)):

            if s[j] in seen:
                break

            seen.add(s[j])

            maximum = max(maximum, j - i + 1)

    return maximum


print(longest_substring("abcabcbb"))

print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""

What is Sliding Window?

Imagine a window moving across the string.

If the next character is unique, expand the window.

If it's already present, shrink the window from the left until the duplicate is removed.


"""


def longest_substring(s):

    left = 0

    seen = set()

    maximum = 0

    for right in range(len(s)):

        while s[right] in seen:

            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        maximum = max(maximum, right - left + 1)

    return maximum


print(longest_substring("abcabcbb"))








print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Return the Actual Longest Substring

Instead of returning the length, return the substring itself.

"""


def longest_string(s):

    left = 0
    seen = set()

    best = ""

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        if right - left + 1 > len(best):
            best = s[left:right + 1]

    return best


print(longest_string("abcabcbb"))


print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""

Longest palindromic substring


What is a Palindrome?

A palindrome is a string that reads the same from left to right and right to left.


What is Longest Palindromic Substring?

Find the longest continuous substring that is a palindrome.

Example 1
Input:
babad

Output:
bab

Note: "aba" is also a correct answer.


Idea
Generate every possible substring.
Check if it is a palindrome.
Keep the longest one.

"""
def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome(s):

    answer = ""

    for i in range(len(s)):
        for j in range(i, len(s)):

            temp = s[i:j+1]

            if is_palindrome(temp):

                if len(temp) > len(answer):
                    answer = temp

    return answer

print(longest_palindrome("babad"))

print("------------------------------Vivek Learning DSA Python----------------------------------------")


"""
Every palindrome has a center.

There are two types:





"""

def expand(s, left, right):

    while left >= 0 and right < len(s) and s[left] == s[right]:

        left -= 1
        right += 1

    return s[left+1:right]


def longest_palindrome(s):

    answer = ""

    for i in range(len(s)):

        # Odd length palindrome
        p1 = expand(s, i, i)

        # Even length palindrome
        p2 = expand(s, i, i+1)

        if len(p1) > len(answer):
            answer = p1

        if len(p2) > len(answer):
            answer = p2

    return answer


print(longest_palindrome("babad"))


print("------------------------------Vivek Learning DSA Python----------------------------------------")



"""

count all palindromic substrings

"""
def count_palindromes(s):

    count = 0

    def expand(left, right):
        nonlocal count

        while left >= 0 and right < len(s) and s[left] == s[right]:

            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):

        expand(i, i)
        expand(i, i+1)

    return count

print(count_palindromes("aaa"))


print("------------------------------Vivek Learning DSA Python----------------------------------------")
print("------------------------------Vivek Learning DSA Python----------------------------------------")








