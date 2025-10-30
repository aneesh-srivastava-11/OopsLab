# Custom exceptions must derive from the built-in Exception class (or a subclass)
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is large"""
    pass
  

while(True):
    try:
        num = int(input("Enter any value in 10 to 50 range: "))
        if num < 10:
            # Raise the custom exception if the value is too small
            raise ValueTooSmallError
        elif num > 50:
            # Raise the custom exception if the value is too large
            raise ValueTooLargeError
        
        # If no exception is raised (i.e., 10 <= num <= 50), the loop breaks
        break 

    except ValueTooSmallError:
        # Handle the custom exception for small values
        print("Value is below range..try again")
    except ValueTooLargeError:
        # Handle the custom exception for large values
        print("value out of range...try again")

print("Great! value in correct range.")

# Example Output:
# Enter any value in 10 to 50 range: 5
# Value is below range..try again
# Enter any value in 10 to 50 range: 60
# value out of range...try again
# Enter any value in 10 to 50 range: 11
# Great! value in correct range.