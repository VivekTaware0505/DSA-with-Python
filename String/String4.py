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
print("------------------------------Vivek Learning DSA Python----------------------------------------")







