def _count_frequency_of_elements(number : list[int]) -> dict[int, int]:
    """
    This function counts the frequency of elements in a list
    Args:
        number (list[int]): The list to count the frequency of elements in
    Returns:
        dict[int, int]: A dictionary with the frequency of elements in the list or None if the list is empty
    """
    if not number: return {}
    dict_qs : dict[int, int] = {}
    
    for item in number:
        if item not in dict_qs:
            dict_qs[item] = 1
        else:
            dict_qs[item] += 1
    return dict_qs

if __name__ == "__main__":
    list_of_number = input("Enter sequence number with space : ").split(" ")
    print(_count_frequency_of_elements(list_of_number))
