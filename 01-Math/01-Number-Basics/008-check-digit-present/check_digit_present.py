def _check_digit_present(number : int, digit : int) -> bool:
    """
    This function checks if a digit is present in a number
    Args:
        number (int): The number to check if the digit is present in
        digit (int): The digit to check if it is present in the number
    Returns:
        bool: True if the digit is present in the number, False otherwise
    """
    number : int = abs(number)
    if digit < 0 or digit > 9: return False
    if number == digit: return True

    while number >0:
        if number % 10 == digit:
            return True
        number //= 10
    return False

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    digit = int(input("Enter digit to find: "))
    print(_check_digit_present(number,digit))
