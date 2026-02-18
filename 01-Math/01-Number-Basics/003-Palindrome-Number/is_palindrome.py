def _is_palindrome(value : int|str) -> bool:
    """
    This function checks if a number or string is a palindrome
    Args:
        value (int|str): The value to check if it is a palindrome
    Returns:
        bool: True if the value is a palindrome, False otherwise
    """
        
    if isinstance(value, int):
        reverse_value : int = 0
        input_value : int = value

        if value < 0 : return False
        while value > 0:
            reverse_value = reverse_value * 10 + value % 10
            value //=10
        return reverse_value == input_value

    elif isinstance(value, str):        
        left,right = 0, len(value) - 1
        while left < right:
            if value[left] != value[right]:
                return False
            left += 1
            right -=1
        return True
    

if __name__ == "__main__":
    print(_is_palindrome(121))    
    print(_is_palindrome("HeH"))
    print(_is_palindrome("Hell0"))
