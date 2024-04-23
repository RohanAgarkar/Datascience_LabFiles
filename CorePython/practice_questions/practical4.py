# Get user input and convert to integer
userInput = int(input('Number>>> '))

# Initialize the first two Fibonacci numbers
a = 0
b = 1

# Loop from 0 to user input
for i in range(0, userInput):
  # Print the current Fibonacci number
  print(a)
  
  # Calculate the next Fibonacci number
  c = a + b

  # Update a and b for the next iteration
  a = b
  b = c