def _count_trailing_zeros(number : int) -> int:
    """
    This function calculates the trailing data of a number
    Args:
        number (int): The number to calculate the trailing data of
    Returns:
        int: The trailing data of the number
    """
    number : int = abs(number)
    counter : int = 0
    if number == 0: return 1

    while number % 10 == 0:        
        counter += 1
        number //= 10
    return counter


if __name__ == "__main__":
  number = int(input("Enter the number : "))
  print(_count_trailing_zeros(number))
