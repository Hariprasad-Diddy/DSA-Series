def _check_prime(number : int) -> int:
    """
    This function checks if a number is prime
    Args:
        number (int): The number to check if it is prime
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if number <= 1: return False
    if number == 2: return True
    if number % 2 ==0: return False

    square_root_limit : int = int(number ** 0.5)    
    for counter in range(3, square_root_limit + 1, 2): 
        if number % counter == 0: return False
    return True

if __name__ == "__main__":
  number : int = int(input("Enter Number to check Prime number : "))
  print(_check_prime(number = number))
