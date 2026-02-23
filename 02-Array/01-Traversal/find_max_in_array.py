def _find_max_in_array(value : list[int]) -> int|None:
    """
    This function finds the maximum value in an array
    Args:
        value (list[int]): The array to find the maximum value in
    Returns:
        int: The maximum value in the array
    """
    if not value: 
        return None

    max_value : int = value[0]
        
    for item in value[1:]:
        if item > max_value:
            max_value = item
    return max_value

if __name__ == "__main__":
  list_of_number = input("Enter sequence number with space : ").split(" ")
  _find_max_in_array(list_of_number)
