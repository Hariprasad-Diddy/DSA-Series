# Check Digit Present in a Number

## Problem

Given an integer `n` and a digit `d` (0 to 9), check whether the digit `d` is present in the number.

## Examples

Input: n = 12345, d = 3  
Output: True

Input: n = 1010, d = 5  
Output: False

Input: n = 0, d = 0  
Output: True

Input: n = -987, d = 8  
Output: True

## Approach

1. Convert `n` to absolute value to ignore the sign.
2. Handle the special case: if `n == 0`, then digit 0 is present only if `d == 0`.
3. While `n > 0`:
   - Extract last digit using `n % 10`
   - If it equals `d`, return True
   - Remove last digit using `n //= 10`
4. If loop ends, return False.

## Complexity Analysis
Let digits be the number of digits in n.

### Time Complexity: O(digits)
We may scan all digits once.

### Space Complexity: O(1)
Only constant extra space is used.

## Edge Cases Covered
* n = 0
* d = 0
* Negative numbers
* Digit present multiple times
* Digit not present
