import time  # Import the time module to use time.sleep for delays.

# def recursion(x):  # Define a recursive function named 'recursion' that takes one argument 'x'.
#     if x > 0:  # Check if 'x' is greater than 0.
#         # If 'x' is positive, call the recursion function again with 'x - 1'.
#         result = x + recursion(x - 1)  
        
#         time.sleep(1)  # Pause execution for 1 second to slow down the output.
        
#         print(result)  # Print the result of the current recursion level after it has been calculated.
#     else:  # This is the base case for the recursion.
#         result = 0  # When 'x' is 0 or less, set result to 0.
        
#     return result  # Return the result back to the previous call in the stack.

# # Call the recursion function with an initial value of 5.
# recursion(5)

def factorial(n):
    # Check if the input is 0 or 1 (base case)
    if n == 0 or n == 1:
        return 1  # The factorial of 0 and 1 is 1
    else:
        # Recursive case: n * factorial of (n - 1)
        return n * factorial(n - 1)

# Example usage:
result = factorial(5)  # Calculate the factorial of 5
print(result)  # Output: 120
