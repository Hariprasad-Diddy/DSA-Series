def _two_sum(number : list[int],target:int) -> list[int]:
    """
    This function finds two numbers in an array that add up to a target value and the array should be in sorted / ascending order
    Args:
        number (list[int]): The array to find the two numbers in
        target (int): The target value to add up to
    Returns:
        list[int]: The indices of the two numbers that add up to the target value
        or an empty list if no two numbers are found
    Complexity:
        Time: O(n)
        Space: O(1)
    """
    if not number: return []
    left = 0
    right = len(number) -1
    
    while left < right:
        current_sum : int = number[left] + number[right]
        if current_sum == target:
            return [left, right]
            
        elif current_sum < target:
            left += 1
        
        elif current_sum > target:
            right -= 1
    return []

if __name__ == "__main__":
  list_of_number = input("Enter sequence number with space : ").split(" ")
  print(_two_sum(list_of_number))
