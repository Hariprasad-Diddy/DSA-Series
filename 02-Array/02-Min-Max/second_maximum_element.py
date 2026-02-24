def _second_maximum_element(value : list[int]) -> int|None:
    """
    This function finds the second peak element in an array
    Args:
        value (list[int]): The array to find the second peak element in
    Returns:
        int: The second peak element in the array
    """

    first_max = float("-inf")
    second_max = float("-inf")
    
    for item in range(0,len(value)):
        if value[item] > first_max:
            second_max = first_max
            first_max = value[item]
        elif first_max > value[item] > second_max:
            second_max = value[item]
    return None if second_max == float("-inf") else second_max

if __name__ == "__main__":
    list_of_number = input("Enter sequence number with space : ").split(" ")
    print(_second_maximum_element(list_of_number))
