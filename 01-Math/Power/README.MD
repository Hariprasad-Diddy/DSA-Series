# Power of a Number

## Problem
Given two integers `base` and `exponent`, compute:

base ^ exponent

That is, multiply the base number by itself `exponent` times.

---

## Examples
Input:  base = 2, exponent = 3
Output: 8

Input:  base = 5, exponent = 0
Output: 1

Input:  base = 3, exponent = 4
Output: 81


## Approach (Iterative Multiplication)

We compute the result by multiplying the base number repeatedly:

1. Initialize `result = 1`
2. Multiply `result` by `base` exactly `exponent` times
3. Return the final result

This directly follows the mathematical definition:
a^n = a × a × a … (n times)

## Python Implementation

📄 **Source Code:**  
👉 [power_of_a_number.py](./power_of_a_number.py)


## Complexity Analysis
	•	Time Complexity: O(n)
	•	Space Complexity: O(1)
Only a constant amount of extra space is used.
