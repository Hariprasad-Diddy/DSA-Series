def _sum_of_elements_in_range(number : list[int], index_range: tuple[int, int]) -> int | None:
    """
    This function calculates the sum of elements in a range of an array
    Args:
        number (list[int]): The array to calculate the sum of elements in
        index_range (tuple[int, int]): The range of indices to calculate the sum of elements in
    Returns:
        int: The sum of elements in the range
    """
    if not number: return None
    l, r = index_range

    if l < 0 or r >= len(number) or l > r:
        return None


    prefix_sum : list[int] = [number[0]]
    for item in range(1, len(number)):
        prefix_sum.append(number[item] + prefix_sum[item -1])
    
    if l == 0:
        return prefix_sum[r]
    else:
        return prefix_sum[r] - prefix_sum[l - 1]

if __name__ == "__main__":
  print(_sum_of_elements_in_range([3, 1, 4, 1, 5],(1,3)))
