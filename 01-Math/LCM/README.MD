# LCM of Two Numbers

## Problem
Given two integers, find their **Least Common Multiple (LCM)**.

The LCM of two numbers is the smallest positive integer that is divisible by both numbers.

---

## Examples
Input:  a = 12, b = 18
Output: 36

Input:  a = 5, b = 10
Output: 10

Input:  a = 7, b = 13
Output: 91

## Approach

The LCM of two numbers can be calculated using the relationship between **LCM** and **GCD**:
LCM(a, b) = (a × b) / GCD(a, b)

### Steps
1. Compute the GCD of the two numbers using the **Euclidean Algorithm**.
2. Apply the formula to compute the LCM.
3. Use integer arithmetic to ensure the result is an integer.

---

## Python Implementation
📄 **Source Code:**  
👉 [lcm.py](./lcm.py)
