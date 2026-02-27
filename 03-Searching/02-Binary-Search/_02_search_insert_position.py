def _search_insert_position(number : list[int],target : int) -> int:
    """
    This function performs a binary search on an array to find a target value to insert into the array.
    If the target value is not found, the function returns the index of the first element greater than the target value.
    If the target value is found, the function returns the index of the target value.
    Args:
        number (list[int]): The array to search in
        target (int): The target value to find
    Returns:
        int: The index of the target value
        or the index of the first element greater than the target value if the target value is not found
    Complexity:
        Time: O(log n)
            Best: O(1) - target is exactly at first mid.
            Worst: O(log n) - element not found or at boundary.
            Average: O(log n) - element not found or at boundary.
        Space: O(1)
    """
    if not number: return 0

    left = 0
    right = len(number) - 1

    while left <= right:
        mid : int = (left + right) // 2

        if number[mid] == target:
            return mid
        elif number[mid] < target:
            left = mid + 1
        elif number[mid] > target:
            right = mid - 1    
    return left

if __name__ == "__main__":
  number = [1,3,5,6]
  target_1 = 5
  target_2 = 2
  target_3 = 7
  target_4 = 0
  print(_search_insert_position(number,target_1))
  print(_search_insert_position(number,target_2))
  print(_search_insert_position(number,target_3))
  print(_search_insert_position(number,target_4))
