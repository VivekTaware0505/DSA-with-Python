 DSA in Python

Welcome!

This repository contains my solutions to Data Structures and Algorithms problems written in Python.

## Topics Covered

- Arrays
- Strings
- Linked Lists
- Stack
- Queue
- Trees
- Graphs
- Recursion
- Dynamic Programming

## Goal

✔ Solve 100+ Interview Questions

✔ Improve Problem Solving

✔ Prepare for Software Engineer Interviews

## Language

Python

## Platforms

- LeetCode
- HackerRank
- GeeksforGeeks
- CodeStudio
 

## Array notes 

# Arrays in Python (DSA Notes)

## Introduction

Array is one of the most important topics in Data Structures and Algorithms (DSA). Almost every coding interview starts with array problems because arrays help us understand searching, sorting, pointers, sliding window, prefix sum, and many other concepts.

In Python, we generally use **Lists** to represent arrays because Python does not have a built-in fixed-size array like C or Java.

Example:

```python
numbers = [10, 20, 30, 40, 50]
```

Here, `numbers` is an array (list) containing five elements.

---

# What is an Array?

An array is a collection of elements stored one after another in memory.

Each element has its own position called an **index**.

Example:

```text
Array = [10, 20, 30, 40, 50]

Index

0   1   2   3   4
```

* First element → Index 0
* Second element → Index 1
* Third element → Index 2

Python always starts indexing from **0**.

---

# Why Do We Use Arrays?

Arrays are used because they allow us to store multiple values inside a single variable.

Instead of writing:

```python
a = 10
b = 20
c = 30
d = 40
```

We can simply write:

```python
numbers = [10, 20, 30, 40]
```

This makes the program easier to read and manage.

---

# Real-Life Example

Think of a classroom.

Suppose there are 40 students.

Instead of giving each student a separate variable, we store all marks inside one array.

```python
marks = [75, 88, 91, 60, 85]
```

Now we can easily access any student's marks.

---

# Characteristics of an Array

* Stores multiple values.
* Elements are stored in order.
* Every element has an index.
* Duplicate values are allowed.
* Different data types can be stored in Python lists, although in DSA we usually use the same type.

Example:

```python
arr = [5, 10, 15, 20]
```

---

# Array Indexing

Example:

```python
arr = [10, 20, 30, 40, 50]
```

Access elements:

```python
print(arr[0])    # 10
print(arr[2])    # 30
print(arr[4])    # 50
```

Negative indexing:

```python
print(arr[-1])   # 50
print(arr[-2])   # 40
```

Negative indexing starts from the end.

---

# Array Traversal

Traversal means visiting every element one by one.

Example:

```python
arr = [10,20,30,40]

for num in arr:
    print(num)
```

Using index:

```python
for i in range(len(arr)):
    print(arr[i])
```

Traversal is one of the most common operations in DSA.

Time Complexity: **O(n)**

---

# Common Operations on Arrays

## 1. Access

```python
print(arr[2])
```

Time Complexity: **O(1)**

---

## 2. Update

```python
arr[1] = 100
```

Time Complexity: **O(1)**

---

## 3. Insert

```python
arr.insert(2, 50)
```

Time Complexity: **O(n)**

Because elements after the insertion position must shift.

---

## 4. Delete

```python
arr.remove(30)
```

or

```python
arr.pop()
```

Time Complexity: **O(n)** (except removing the last element with `pop()` which is usually **O(1)**)

---

## 5. Searching

### Linear Search

Check every element one by one.

```python
for num in arr:
    if num == 50:
        print("Found")
```

Time Complexity:

**O(n)**

---

### Binary Search

Works only on a **sorted array**.

Time Complexity:

**O(log n)**

---

# Array Length

```python
len(arr)
```

Example:

```python
arr = [5,10,15]

print(len(arr))
```

Output

```
3
```

---

# Array Slicing

Example

```python
arr = [10,20,30,40,50]
```

```python
arr[1:4]
```

Output

```
[20,30,40]
```

Other examples

```python
arr[:3]

arr[2:]

arr[::-1]
```

`arr[::-1]` reverses the array.

---

# Important Python Functions

```python
append()

insert()

remove()

pop()

sort()

reverse()

index()

count()

len()

max()

min()

sum()
```

Example

```python
arr = [5,3,8]

arr.sort()

print(arr)
```

Output

```
[3,5,8]
```

---

# Time Complexity Summary

| Operation           | Complexity |
| ------------------- | ---------- |
| Access              | O(1)       |
| Update              | O(1)       |
| Search              | O(n)       |
| Insert at End       | O(1)       |
| Insert at Beginning | O(n)       |
| Delete Last         | O(1)       |
| Delete Middle       | O(n)       |
| Traversal           | O(n)       |

---

# Advantages of Arrays

* Easy to use.
* Fast access using index.
* Stores multiple values.
* Memory efficient.
* Useful for many algorithms.

---

# Disadvantages of Arrays

* Insertion in the middle is slow.
* Deletion in the middle is slow.
* Binary search works only on sorted arrays.
* Fixed-size arrays exist in many programming languages (Python lists automatically resize).

---

# Common Array Patterns Used in Interviews

These patterns help solve most array problems.

## 1. Traversal

Visit every element.

Example:

* Find maximum element
* Find minimum element
* Calculate sum

---

## 2. Two Pointers

Use two indexes to solve problems efficiently.

Examples:

* Reverse Array
* Move Zeroes
* Remove Duplicates
* Two Sum (sorted array)

---

## 3. Sliding Window

Used when dealing with continuous subarrays.

Examples:

* Maximum sum subarray
* Longest substring
* Fixed-size window problems

---

## 4. Prefix Sum

Store cumulative sums to answer range sum queries quickly.

---

## 5. HashMap

Store previously seen values.

Examples:

* Two Sum
* Frequency Count
* Duplicate Detection

---

## 6. Sorting

Sort first, then solve the problem.

Examples:

* Merge Intervals
* Meeting Rooms
* Three Sum

---

# Common Interview Questions

Beginner

* Largest Element
* Smallest Element
* Second Largest
* Reverse Array
* Check Sorted
* Move Zeroes
* Rotate Array
* Missing Number
* Two Sum

Intermediate

* Kadane's Algorithm
* Best Time to Buy and Sell Stock
* Majority Element
* Product of Array Except Self
* Merge Intervals
* Longest Consecutive Sequence

Advanced

* Trapping Rain Water
* Median of Two Sorted Arrays
* First Missing Positive
* Maximum Product Subarray

---

# Tips for Solving Array Problems

* Read the question carefully.
* Identify the input and expected output.
* Solve using a simple (brute-force) approach first.
* Then think about how to optimize it.
* Dry run your algorithm with a small example.
* Always calculate Time Complexity and Space Complexity.
* Practice regularly because arrays are the foundation of DSA.

---

# Key Takeaways

* Arrays store multiple values in one variable.
* Indexing starts from **0**.
* Accessing an element is very fast (**O(1)**).
* Traversing an array takes **O(n)** time.
* Two Pointers, Sliding Window, Prefix Sum, Sorting, and HashMap are the most important patterns for array problems.
* Mastering arrays makes learning Strings, Linked Lists, Trees, Graphs, and Dynamic Programming much easier.

---

## My Learning Summary

While learning arrays, I realized that most interview questions are not about memorizing code. They are about recognizing the correct pattern. The more problems I solve, the easier it becomes to identify whether a question requires traversal, two pointers, hashing, sorting, or another approach. Building a strong foundation in arrays will make learning the rest of DSA much easier.
