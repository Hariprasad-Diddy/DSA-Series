def _prefix_sum(number : list[int]) -> int:
    """
    This function calculates the prefix sum of an array
    Args:
        number (list[int]): The array to calculate the prefix sum of
    Returns:
        list[int]: The prefix sum of the array
    """
    if not number: return []
    if len(number) == 1: return number
    prefix_sum : list[int] = [number[0]]

    for item in range(1,len(number)):
        prefix_sum.append(number[item] + prefix_sum[item - 1])
    return prefix_sum

if __name__ == "__main__":
  list_of_number = input("Enter sequence number with space : ").split(" ")
  print(_prefix_sum(list_of_number))
