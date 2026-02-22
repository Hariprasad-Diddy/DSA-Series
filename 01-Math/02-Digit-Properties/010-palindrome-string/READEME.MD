# Palindrome String (Case-Insensitive)

## Palindrome String (Case-Insensitive)
Given a string value, determine whether it is a palindrome.
A string is a palindrome if it reads the same forward and backward.
The comparison should be case-insensitive.

## Examples
Input: “HeH”
Output: True

Input: “madam”
Output: True

Input: “RaceCar”
Output: True

Input: “Hell0”
Output: False

Input: “”
Output: True

Input: “a”
Output: True

## Approach (Two-Pointer Technique)
* Convert the string to lowercase to ensure case-insensitive comparison.
* Initialize two pointers:
	•	left starting at index 0
	•	right starting at the last index
* Compare characters at both pointers.
* If characters do not match, return False.
* Move both pointers inward.
* Continue until left >= right.
* If no mismatch is found, return True.

## Complexity Analysis
Let n be the length of the string.

### Time Complexity: O(n)
* Converting to lowercase takes O(n).
* The two-pointer traversal takes O(n).
* Overall complexity remains O(n).

### Space Complexity: O(n)
* The lower() function creates a new string.
* No additional data structures are used.

## Edge Cases Covered
* Empty string → True
* Single-character string → True
* Mixed case strings → handled correctly
* Non-palindrome strings → correctly detected
