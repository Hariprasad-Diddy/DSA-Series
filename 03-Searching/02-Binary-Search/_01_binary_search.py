def _binary_search(number : list[int],target : int) -> int|None:
    """
    This function performs a binary search on an array to find a target value.
    It checks the middle element of the array and compares it to the target value.
    If the target value is found, the function returns the index of the target value.
    If the target value is not found, the function returns None.
    Args:
        number (list[int]): The array to search in
        target (int): The target value to find
    Returns:
        int: The index of the target value
        or None if the target value is not found
    Complexity:
        Time: O(log n)
            Best: O(1) - target is exactly at first mid.
            Worst: O(log n) - element not found or at boundary.
            Average: O(log n) - element not found or at boundary.
        Space: O(1)
    """
    if not number: return None
        
    left = 0
    right = len(number) - 1

    while left <= right:
        mid = (left + right) // 2
        if number[mid] == target:
            return mid
        elif number[mid] < target:
            left = mid + 1
        elif number[mid] > target:
            right = mid - 1
        
    return None

if __name__ == "__main__":      
    
    print(_binary_search([1,2,3,4,5,],3))
    print(_binary_search([1,2,3,4,5,],1))
    print(_binary_search([1,2,3,4,5,],5))
    print(_binary_search([1,2,3,4,5,],6))
