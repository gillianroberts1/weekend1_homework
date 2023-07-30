# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for num in (numbers):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)



# # 2. Print the difference between the largest and smallest value:
num_ordered = sorted(numbers)
print(num_ordered)

answer = num_ordered[-1] - num_ordered[0]

print(answer)



# # 3. Print True if the list contains a 2 next to a 2 somewhere.
def adjacent2s(numbers):
    for num in (range(len(numbers) - 1)):  # stops at length of list -1 as index starts at 0
        # if current number being looped over is 2 and number next to it is 2
      if(numbers[num] == 2 & numbers[(num + 1)] == 2):
          return True
    return False
        
result = adjacent2s(numbers)
print(result)

# # 4. Print the sum of the numbers, 
# #    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
# #    
# #    So [11, 6, 4, 99, 7, 11] would have sum of 22
def sum_except67(numbers):
    # tracking the index and total
    index = 0
    total = 0

    while index < len(numbers):
        if numbers[index] == 6:
            # this starts at the next index and then stop once reached the end of the list
            for index in range(index + 1, len(numbers)): # start index +1, stop at length of list in this case index 10
                if numbers[index] == 7:
                    break
        else:
            total += numbers[index]

        index += 1

    return total            
print(sum_except67(numbers))  

    
# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

def unlucky_13(numbers):
    index = 0
    total = 0

    while index < len(numbers):
        if numbers[index] == 13:  
            for index in range(index +1, len(numbers)):# if it finds 13 then move on one without adding
                break
            
        else:
         total += numbers[index]

        index += 1

    return total
print(unlucky_13(numbers))





