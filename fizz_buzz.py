def fizz_buzz(number):
    """
    Returns 'Fizz' if the number is divisible by 3,
    'Buzz' if divisible by 5,
    'FizzBuzz' if divisible by both 3 and 5,
    otherwise returns the number itself.

    Args:
        number (int): The input number to evaluate.

    Returns:
        str|int: 'Fizz', 'Buzz', 'FizzBuzz', or the original number.
    """

    # Check if divisible by both 3 and 5 first
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    
    # Check if divisible by 3 only
    elif number % 3 == 0:
        return 'Fizz'
    
    # Check if divisible by 5 only
    elif number % 5 == 0:
        return 'Buzz'
    
    # If none of the above, return the number as-is
    else:
        return number


# Entry point of the program
nummber = int(input('ENTER A NUMBER: '))

print(fizz_buzz(int(nummber)))

