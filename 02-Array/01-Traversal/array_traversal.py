def print_elements_of_a_list(value : list[int]) -> None:
    """
    This function prints the elements of a list
    Args:
        value (list[int]): The list to print the elements of
    Returns:
        None
    """
    for item in value:
        print(item)

if __name__ == "__main__":
  list_of_number = input("Enter sequence number with space : ").split(" ")
  _print_elements_of_a_list_in_reverse(list_of_number)
