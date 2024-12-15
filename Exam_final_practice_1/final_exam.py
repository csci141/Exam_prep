# This is a practice final exam written by a past 141 student, Lacie Pauw. 
# The Skel is final_exam.py which uses the files overtime.txt and pay_instruct.txt . 
# You can see a worked example at final_exam_answers.py . 
# This sample exam is a bit shorter than a real exam would be but will be very helpful for practicing!
# Try taking this examw using only your notesheet and time how long it takes you to do each question.
# Take notes on what slows you down so you can focus your studing on these areas:
#    - do you understand the concepts covered?
#    - do you need more syntax examples on your notesheet? 
#    - do you need more notes on what causes different error messages and how to fix them?
#    - do you need more practice debugging?
# Test file is not presented; perhaps this is something _you_ could write for extra credit?



#TODO 0A: Your Name

# Exam instructions
    # Outside assistance such as using AI or other people's assistance is not
    # allowed; those caught will fail the class and be referred to the academic honesty board.
    # Don't change any lines labeled "DO NOT CHANGE THIS LINE"
    # On this exam, function argument variables are part of each function
    # definition block; you won't need system arguments for this exam.
    # Comment out lines which cause the code to crash

def labels_456(dep_label): #DO NOT CHANGE THIS LINE
    #you are the manager of a grocery store and you are creating labels for perishable food items
    #the main departments for perishable food items are produce, deli, and bakery.
    #department labels are created by using the department binary number
    
    #TODO 456A
    #If a food item is in the produce department its number (not in binary) is 09
    #If a food item is in the deli department its number (not in binary) is 12
    #If a food item is in the bakery department its number (not in binary) is 15
    #convert these numbers to binary and save them in the variables below
    
    produce_binary = 0
    deli_binary = 0
    bakery_binary = 0
    
    #TODO 456B
    #determine if the dep_label is in the produce, deli, or bakery department
    #you can assume that dep_label is an integer in binary form that is equivalent to produce_binary, deli_binary or bakery_binary
    #print the result in of the department (for example if dep_label is in the bakery department,
    #print 'The department of dep_label is: bakery')
    

def bag_loop7(): #DO NOT CHANGE THIS LINE
    #TODO 7A
    #we want to return the number of bags a customer whishes to purchase during self checkout
    #add one to the varaible num_bags each time the customer answers 'y' in response to choice_text
    #you do not need to account for a case where the customer responds with something other than 'y' or 'n'
    
    num_bags = 0
    
    choice_text = input("Would you like to purchase a bag [y]es or [n]o: ") #DO NOT CHANGE THIS LINE
    
    return num_bags #DO NOT CHANGE THIS LINE

def bag_tracker8(num_customers): #DO NOT CHANGE THIS LINE
    #TODO 8A
    #you may assume num_customers is a positive integer of the number of customers the store has recieved
    #each customer has used an integer number of bags of 0 or higher
    #we want to calculate the number of bags used, and store this into the varaible bags_used
    #return bags_used as an integer
    #hint: use customer_bags in for loop
    
    bags_used = 0
    
    customer_bags = int(input("Enter the number of bags the customer used: "))
    
    return bags_used #DO NOT CHANGE THIS LINE


#TODO 10A
#The grocery store wants to know the average amount of money spent per hour (the store is open 10 hours each day) on a self-checkout machine 
#the function should take a single integer parameter called 'total_money' (which represents the total amount of money
#spent on that check out machine rounded up to the nearest dollar)
#calculate the average amount of money spent per hour, given the amount of money spent on that day was 'total_money'
#the function should be called 'money_per_hour10'


def exit_message13(message): #DO NOT CHANGE THIS LINE
    #TODO 13A
    #as customers exit the store, there is always a message on a screen
    #you may assume message is a string with no newline characters or leading/trailing whitespace
    #the store wants the message to be all lowercase and have an exclamation point at the end
    #return the given string in lowercase with an exclamation point at the end as friendly_message
    
    freindly_message = ""
    
    return friendly_message #DO NOT CHANGE THIS LINE

def something14(input_string): #DO NOT CHANGE THIS LINE
    #TODO 14A
    #all the employee names are stored into a single string, with the '*' character separating each name (only first names are included)
    #you may assume input_string is a string, but it may have leading/trailing whitespace or newline characters
    #we want to return a string of all the employee names with a comma and space (', ') as the separator between employee names
    #we will call the returned string employee_string
    #employee_string should have 'Employees: ' at the beginning before listing all the names, and should have no leading/trailing whitespace
    
    employee_string = ""
    return employee_string #DO NOT CHANGE THIS LINE

def get_price15(dep_price_list):#DO NOT CHANGE THIS LINE
    #TODO 15A
    #departments include bakery, deli, or produce
    #dep_price_list has an unknown number of items (but you may assume it has at least 1 item).
    #each item of dep_price_list is a tuple with two elements of the form ('food_item' , price_float)
    #you may assume food_item is a string with no leadling/trailing whitespace
    #you may assume price_float is a positive number out to two decimal spots (price_float is of type float)
    #print ('food_item costs $price_float' for each item in dep_price_list)
    #example: if the food_item is donut and the price_float is 3.50, print 'donut costs $3.50' (without quotes)
    #Hint: unpack tuples

def payroll_instructions16(file_name): #DO NOT CHANGE THIS LINE
    #TODO 16A
    #the owner of the store has created a list of instructions on how to calculate pay for overtime hours, and each step of instructions
    #is on its own line
    #the first line on the file is not a part of the instructions, so DO NOT return the first line (but return every line after)
    #return the set of instructions, (with each step on its own line) to the variable instructions
    #Hint: make sure to not return any trailing whitespace/newlines
    
    instructions = ""
    
    return instructions #DO NOT CHANGE THIS LINE

def overtime_hours16(list_names, list_hours): #DO NOT CHANGE THIS LINE
    #TODO 16B
    #we are going to write into a file on the number of overtime hours the employees worked this month
    #call this file overtime.txt
    #you may assume len(list_names) = len(list_hours)
    #the first item in list_hours corresponds to the number of overtime hours that the first employee in list_names worked in that month
    #you may assume each item in list_names is of type str
    #you may assume each item in list_hours is of type int (and that each item is non-negative)
    #at the top of the file write 'Overtime Hours Nov. 2024:' (hint: make sure to write a newline after this)
    #now print 'employee_name worked overtime_hours hours of overtime this month' for each employee (print without quotes)
    #hint: make sure each overtime statement gets its own line on the file
    #(example: 'Gilbert worked 6 hours of overtime this month' would be one overtime statement)


bakery_price_list = [('dinner rolls', 2.25) , ('bagels', 4.00) , ('potato bread' , 3.00)]
deli_price_list = [('ground beef' , 6.00) , ('chicken breast', 8.00), ('sliced ham', 4.50), ('sliced turkey' , 4.75), ('ribeye steak', 13.25)]
produce_price_list = [('apple' , 0.75) , ('banana', 1.00), ('pear', 0.75), ('carrot pack' , 1.75), ('broccoli pack', 1.00)]

employee_names = ['Alan' , 'Sue', 'Carol', 'Denny' , 'John' , 'Sarah' , 'Ellen']
overtime_hours = [2, 0, 5, 0, 15, 7, 9] 

    
    
