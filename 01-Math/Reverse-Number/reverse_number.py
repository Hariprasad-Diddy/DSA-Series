def _reverse_number(number : int) -> int:
    """
    This function reverses a number
    Args:
        number (int): The number to reverse
    Returns:
        int: The reversed number
    """
    sign : int = -1 if number < 0 else 1
    number = abs(number)
    reversed_number : int = 0
    
    if number == 0: return 0

    while number > 0:        
        reversed_number = reversed_number * 10 + number % 10        
        number //= 10   
    return sign * reversed_number
    

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(_reverse_number(number))
