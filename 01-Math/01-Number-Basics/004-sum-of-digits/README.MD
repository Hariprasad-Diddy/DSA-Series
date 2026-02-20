# Sum of Digits

## Problem
Given an integer n, calculate the sum of its digits.
The function should handle both positive and negative numbers.

## Examples
Input: 123
Output: 6

Input: -456
Output: 15

Input: 0
Output: 0

Input: 1002
Output: 3

## Approach
* Convert the number to its absolute value to ignore the sign.
* Extract the last digit using number % 10.
* Add the digit to a running total.
* Remove the last digit using integer division number //= 10.
* Repeat until the number becomes 0.
* Return the total sum.

## Complexity Analysis
Let d be the number of digits in the number.
### Time Complexity: O(d)
Since the algorithm processes each digit exactly once.
Because the number of digits in n is approximately log₁₀(n), we can also express the time complexity as:
O(log n)

### Space Complexity: O(1)
Only a constant amount of extra space is used.

## Edge Cases Covered
* Negative numbers (sign ignored)
* Number = 0
* Numbers with trailing zeros
* Large integers
