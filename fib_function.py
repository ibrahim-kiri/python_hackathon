def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  if n <= 1:
    # If n is 0 or 1, return n itself
    return n
  else:
    # Initialize the first two terms of the sequence
    a, b = 0, 1
    # Initialize a list to store the Fibonacci sequence
    fibonacci_sequence = [a, b]
    # Generate the rest of the sequence
    for _ in range(2, n):
      c = a + b
      a, b = b, c
      fibonacci_sequence.append(c)
    return fibonacci_sequence
  
# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)