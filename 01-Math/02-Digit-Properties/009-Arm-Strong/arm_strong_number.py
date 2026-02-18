def _is_arm_strong(number : int) -> bool:
    """
    This function checks if a number is an Armstrong number
    Args:
        number (int): The number to check if it is an Armstrong number
    Returns:
        bool: True if the number is an Armstrong number, False otherwise
    """
    if number < 0: return False
    
    length_of_number : int = 0
    original_number : int = number
    sum_of_digits : int = 0
    final_number : int = number
    # counting number of digits in the number
    if number == 0: length_of_number = 1
    while number > 0:
        number //=10
        length_of_number += 1
        
    while original_number > 0:
        sum_of_digits += (original_number % 10) ** length_of_number 
        original_number //= 10
    
    return sum_of_digits == final_number

if __name__ == '__main__':
  number : int = int(input("Enter a number :"))
  print(_is_arm_strong(number))
  
