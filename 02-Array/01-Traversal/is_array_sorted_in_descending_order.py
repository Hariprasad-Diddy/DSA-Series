def _is_array_sorted_in_descending_order(number : list[int]) -> bool:
    """
    This function checks if an array is sorted in ascending order
    Args:
        number (list[int]): The array to check if it is sorted in ascending order
    Returns:
        bool: True if the array is sorted in ascending order, False otherwise
    """

    if not number: return False
    if len(number) == 1: return True

    for item in range(0,len(number) - 1):
        if number[item + 1] > number[item]:
            return False
    return True

if __name__ == "__main__":    
    print(_is_array_sorted_in_descending_order([2,5,6,3,9,1,10]))
    print(_is_array_sorted_in_descending_order([2,5,6]))
    print(_is_array_sorted_in_descending_order([6,5,2]))
