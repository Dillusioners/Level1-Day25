try:
# take input from user
  numbers = input("Enter a list of numbers separated by spaces: ").split()
  
  # convert input into a list of integers
  numbers = [int(num) for num in numbers]
  
  # find the smallest number
  smallest = numbers[0]
  for num in numbers:
      if num < smallest:
          smallest = num
  
  # print the smallest number
  print("The smallest number in the list is:", smallest)
except:
  print("Enter only numbers next time.")
