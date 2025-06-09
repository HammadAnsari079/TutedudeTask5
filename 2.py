
user_input = input("Enter at least 5 numbers separated by spaces: ")

numbers = list(map(int, user_input.split()))


if len(numbers) < 5:
    print("Please enter at least 5 numbers.")
else:
 
    extracted = numbers[:5]
    
   
    reversed_list = extracted[::-1]
    
    print("Extracted List:", extracted)
    print("Reversed List:", reversed_list)
