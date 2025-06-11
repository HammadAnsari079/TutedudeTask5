numbers = [1,2,3,4,5,6,7,8,9,10]
if len(numbers) < 5:
    print("Please enter at least 5 numbers.")
else:
 
    extracted = numbers[:5]
    
   
    reversed_list = extracted[::-1]
    
    print("Extracted List:", extracted)
    print("Reversed List:", reversed_list)
