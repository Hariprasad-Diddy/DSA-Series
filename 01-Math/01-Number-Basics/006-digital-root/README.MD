# Digital Root

## Problem
Given an integer n, compute its digital root.
The digital root of a number is obtained by repeatedly summing its digits until a single-digit number remains.

## Examples
Input: 9875
Step 1: 9 + 8 + 7 + 5 = 29
Step 2: 2 + 9 = 11
Step 3: 1 + 1 = 2
Output: 2

Input: 99
9 + 9 = 18
1 + 8 = 9
Output: 9

Input: 10
1 + 0 = 1
Output: 1

Input: 0
Output: 0

Input: -987
9 + 8 + 7 = 24
2 + 4 = 6
Output: 6

## Approach (Recursive Digit Summation)
* If the number is 0, return 0.
* Convert the number to its absolute value to ignore the sign.
* Extract digits using number % 10.
* Sum all digits.
* If the sum is a single digit, return it.
* Otherwise, recursively compute the digital root of the sum.

## Complexity Analysis
Let d be the number of digits in the number.

### Time Complexity: O(d)
* Each digit is processed once per recursion.
* Since the number of digits is approximately log₁₀(n), the complexity can also be written as:
O(log n)

### Space Complexity: O(d)
* Due to recursion stack.
* However, recursion depth is very small in practice (usually ≤ 2 or 3).

## Edge Cases Covered
* Negative numbers (sign ignored)
* Number = 0
* Single-digit numbers
* Large integers
