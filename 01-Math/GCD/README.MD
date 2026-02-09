# GCD / HCF of Two Numbers

## Problem
Given two integers `a` and `b`, find their **Greatest Common Divisor (GCD)**  
(also known as **Highest Common Factor – HCF**).

The GCD of two numbers is the largest positive integer that divides both numbers without leaving a remainder.

---

## Examples
Input:  a = 36, b = 24
Output: 12

Input:  a = 17, b = 13
Output: 1

Input:  a = 0, b = 5
Output: 5

## Approach (Euclidean Algorithm)

The algorithm is based on the principle:

> **GCD(a, b) = GCD(b, a % b)**

### Steps
1. While `b` is not zero:
   - Replace `a` with `b`
   - Replace `b` with `a % b`
2. When `b` becomes `0`, `a` contains the GCD.

This works because the GCD does not change when the larger number is replaced by its remainder.

---

## Python Implementation
**Source Code:**  
[gcd_or_hcf.py](./gcd_or_hcf.py)
