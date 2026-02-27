# Searching – DSA Series

## Overview
Searching is a fundamental concept in Data Structures and Algorithms.
After mastering arrays, the next logical step is learning how to efficiently search within sorted and unsorted data.
Searching problems focus on optimization — especially reducing time complexity from O(n) to O(log n).
This section covers the most important searching patterns required for interviews.

## Topics Covered

### 1. Linear Search
Linear search checks each element one by one until the target is found.
Used for:
* Searching in unsorted arrays
* Simple lookup operations
* Small datasets

Time Complexity: O(n)

### 2. Binary Search
Binary search works only on sorted arrays.
It repeatedly divides the search space in half.
Used for:
* Searching efficiently in sorted arrays
* Finding target elements
* Optimization problems

Time Complexity: O(log n)

### 3. Lower Bound & Upper Bound
Lower bound:
* First position where element ≥ target.
Upper bound:
* First position where element > target.
Used for:
* Counting occurrences
* Range queries
* Binary search variants

Time Complexity: O(log n)

### 4. First & Last Occurrence
Find the first and last position of a target element in a sorted array.
Used for:
* Counting duplicates
* Frequency problems in sorted arrays

Time Complexity: O(log n)

### 5. Search in Rotated Sorted Array
Array is sorted but rotated at some pivot.
Used for:
* Advanced binary search variations
* Identifying sorted halves

Time Complexity: O(log n)

### 6. Binary Search on Answer
Instead of searching for an element, we search for the correct answer range.

Used for:
* Square root problems
* Minimum capacity problems
* Allocation problems
* Optimization under constraints

Time Complexity: O(log n)

## Problems List

| # | Problem Name | Topic | Folder |
|---|-------------|-----------|--------|
| 1 | Linear Search | Linear Search | [View](./Count-Digits) |
| 2 | Binary Search (Iterative) | Binary Search | [View](./Reverse-Number) |
| 3 | Binary Search (Recursive) | Binary Search | [View](./Palindrome-Number) |
| 4 | Lower Bound | Binary Search Variant | [View](./GCD) |
| 5 | Upper Bound | Binary Search Variant | [View](./LCM) |
| 6 | First Occurrence of Element | Binary Search Variant | [View](./Prime-Check) |
| 7 | Last Occurrence of Element | Binary Search Variant | [View](./Arm-Strong) |
| 8 | Count Occurrences in Sorted Array | Binary Search Variant | [View](./Factors) |
| 9 | Search in Rotated Sorted Array | Binary Search Variant | [View](./Power) |
| 10 | Find Peak Element | Binary Search Variant | [View](./Power) |
| 11 | Search Insert Position | Binary Search Variants | [View](./Power) |
| 12 | Find Minimum in Rotated Array | Binary Search Variant | [View](./Power) |
| 13 | Square Root using Binary Search | Binary Search on Answer | [View](./Power) |
| 14 | Allocate Minimum Pages | Binary Search on Answer | [View](./Power) |
| 15 | Koko Eating Bananas (Classic) | Binary Search on Answer | [View](./Power) |

