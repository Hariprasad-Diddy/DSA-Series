def _print_elements_of_a_list_in_reverse(value : list[int]) -> None:
    """
    This function prints the elements of a list in reverse
    Args:
        value (list[int]): The list to print the elements of in reverse
    Returns:
        None
    """
    for i in range(len(value) - 1, -1, -1):
        print(value[i])

if __name__ == "__main__":
  list_of_number = input("Enter sequence number with space : ").split(" ")
  _print_elements_of_a_list_in_reverse(list_of_number)
