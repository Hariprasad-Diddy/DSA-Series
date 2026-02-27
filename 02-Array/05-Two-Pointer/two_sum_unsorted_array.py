def _two_sum_unsorted_array(number : list[int],target : int) -> list[int]:
    """
    This function finds two numbers in an unsorted array that add up to a target value
    Args:
        number (list[int]): The array to find the two numbers in
        target (int): The target value to add up to
    Returns:
        list[int]: The indices of the two numbers that add up to the target value
        or an empty list if no two numbers are found
    Complexity:
        Time: O(n)
        Space: O(n)
    """
    if not number: return []
    lookup : dict[int,int] = {}

    for item in range(0,len(number)):
        complement : int = target - number[item]
        if complement in lookup:
            return [lookup[complement],item]
        lookup[number[item]] = item
    return []

if __name__ == "__main__":
  list_of_number = input("Enter sequence number with space : ").split(" ")
  print(_two_sum_unsorted_array(list_of_number))
