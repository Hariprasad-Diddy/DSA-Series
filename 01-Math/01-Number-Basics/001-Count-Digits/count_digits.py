def _count_digits(number : int) -> int:
  """
    This function counts the digits of a number
    Args:
        number (int): The number to count the digits of
    Returns:
        int: The number of digits in the number
  """
  counter : int = 0
  number : int = abs(number)

if number == 0: return 1

while number > 0:
  counter += 1
  number //= 10
return counter

if __name__ == '__main__':
  number : int = int(input("Enter a number :"))
  print(_count_digits(number))
