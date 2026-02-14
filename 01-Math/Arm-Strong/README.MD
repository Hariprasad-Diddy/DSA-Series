# Armstrong Number

## Problem
Given a non-negative integer n, determine whether it is an Armstrong number.

An Armstrong number (also called a Narcissistic number) is a number that is equal to the sum of its digits, where each digit is raised to the power of the total number of digits in the number.

## Mathematical Definition
If a number has d digits:

n = d_1d_2d_3...d_d

Then it is an Armstrong number if:

n = d_1^d + d_2^d + d_3^d + ... + d_d^d

## Examples
Input: 153
Digits = 3
1³ + 5³ + 3³ = 1 + 125 + 27 = 153
Output: True

Input: 370
3³ + 7³ + 0³ = 27 + 343 + 0 = 370
Output: True

Input: 123
1³ + 2³ + 3³ = 1 + 8 + 27 = 36
Output: False

Input: 0
0¹ = 0
Output: True

## Approach (Mathematical – Without String Conversion)
1.If the number is negative → return False.
2.Count the number of digits by repeatedly dividing by 10.
3.Extract each digit using modulo (% 10).
4.Raise each digit to the power of the digit count.
5.Sum the values.
6.Compare the sum with the original number.

Special handling:
	•	0 is considered an Armstrong number.
	•	Single-digit numbers are always Armstrong numbers.

## Complexity Analysis
Let d be the number of digits.
### Time Complexity: O(d)
  • Counting digits → O(d)
	•	Processing digits → O(d)
### Space Complexity: O(1)
Only constant extra space is used.
