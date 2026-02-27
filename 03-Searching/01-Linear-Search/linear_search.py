def _linear_search(number : list[int],target : int) -> int|None:
    """
    This function performs a linear search on an array to find a target value.
    It checks each element of the array one by one until the target value is found or the end of the array is reached.
    If the target value is found, the function returns the index of the target value.
    If the target value is not found, the function returns None.    
    Args:
        number (list[int]): The array to search in
        target (int): The target value to find
    Returns:
        int: The index of the target value
        or None if the target value is not found
    Complexity:
        Time: O(n)
            Best: O(1) - first element
            Worst: O(n) - last element
            Average: O(n) - middle element
        Space: O(1)
    """
    if not number: return None
    for index in range(0,len(number)):
        if number[index] == target:
            return index
    return None
if __name__ == "__main__":      
    print(_linear_search([1,2,3,4,5,],5))
    print(_linear_search([1,2,3,4,5,],9))
