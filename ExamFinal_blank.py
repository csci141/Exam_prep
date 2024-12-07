#TODO 0A: save your name in the 'variable name'
name = "your name for 1 point"

# Exam instructions
    # The only IDE allowed for this exam is Thonny.
    # Outside assistance such as using AI or other people's assistance is not allowed; those caught will fail the class and be referred to the academic honesty board.
    # Don't change any lines labeled "DO NOT CHANGE THIS LINE"
    # This exam has 12 tasks, each worth the same amount. Plan on about 4 minutes per task so you have a few minutes at the end to turn it in.
    # If you are unable to do a task in 4 minutes, get as far as you can and then move on.
    # On this exam, function argument variables are part of each function definition block; you won't need system arguments for this exam.
    # Comment out lines which cause the code to crash; code which must be hand un-crashed will receive a -1 penalty


#Your store is going to get in on a dynamic new market: travel agents for Aliens!
#turns out Aliens are big poetry fans, and they want a tour of the top poetry cities, starting with the best.

#######################################

# Start: enters user name, welcome user, read in city data, makes city dictionary 

#######################################

def welcome_message_1(name): #DO NOT CHANGE THIS LINE
    #TODO 1_A
    
    # solvable in this many lines of code: 1

    pass

def get_name_1_2(num): #DO NOT CHANGE THIS LINE
    #TODO 1_2_A
    name = ""

    # solvable in this many lines of code: 1
    
    return name #DO NOT CHANGE THIS LINE

def read_city_data_file_15_16(file_name):#DO NOT CHANGE THIS LINE
    
    #TODO 15_16_A
    
    all_cities =[]
   
    # solvable in this many lines of code: 2

    return(all_cities)  #DO NOT CHANGE THIS LINE
  
def make_city_dict_15_16_17(city_text):#DO NOT CHANGE THIS LINE
    
    #TODO 15_16_17_A
   
    city = {}
    
    #solvable in this many lines of code: 5

    return(city) #DO NOT CHANGE THIS LINE

#######################################

# Making tour : use average poem review to determine best_poem_city_not_visited , add that city to the tour, toggled visited 

#######################################

def average_poem_review_3_10_15(review_list):  #ANSWER DELETE 
#TODO 3_10_15_A

    average_review = -1
  
    #solvable in this many lines of code: 1

    return average_review

def best_poem_city_not_visited_5_6_8_15_21(list_of_city_dicts): #DO NOT CHANGE THIS LINE
   
    #TODO 5_6_8_15_21_A
    max_poem_val = 0
    best_city = {}
    
    #solvable in this many lines of code: 5

    return(best_city)

def add_city_to_tour_15_19(tour, city): #DO NOT CHANGE THIS LINE

    #TODO 15_19
    
    old_tour = []

    #solvable in this many lines of code: 2

    return(old_tour)

def toggle_visited_5_17(one_city): #DO NOT CHANGE THIS LINE
    
    #TODO 5_17_A

    #solvable in this many lines of code: 1
    
    pass
        
#######################################

# give user tour information: Get barcode, draw barcode, print tour itinerary 

#######################################

def ticket_barcode_4(): #DO NOT CHANGE THIS LINE
    
    #TODO 4A
    
    barcode = -1
    
    #solvable in this many lines of code: 1

    return(barcode) #DO NOT CHANGE THIS LINE

def draw_barcode_9(barcode): #DO NOT CHANGE THIS LINE
    
    import turtle #DO NOT CHANGE THIS LINE
    
    #TODO 9_A

    #solvable in this many lines of code: 6
    
    turtle.exitonclick() 

def printable_itinerary_14(tour_list): #DO NOT CHANGE THIS LINE
    
    #TODO 14_A
    tour_string = ""

    #solvable in this many lines of code: 1
    
    return tour_string #DO NOT CHANGE THIS LINE


#######################################
    
# saving tour: save file, exit message

#######################################

def write_tour_file_16(tour_string, file_name): #DO NOT CHANGE THIS LINE
    
    #TODO 16_A

    #solvable in this many lines of code: 3

    pass
 
def exit_message_13(message): #DO NOT CHANGE THIS LINE
    #TODO 13_A
  
    friendly_message = ""
    
    #solvable in this many lines of code: 1

    return friendly_message #DO NOT CHANGE THIS LINE

def main():
        
    #######################################

    # Start: enters user name, welcome user, read in city data, makes city dictionary

    #######################################

    print("\n----get_name_1_2...")
    num = 2 
    print(get_name_1_2(num)) #comment this out once it works to make testing faster

    print("\n----welcome_message_1...")
    name = 3.14
    welcome_message_1(name)
    
    print("\n----read_city_data_file_15_16...")
    print("data file: ", read_city_data_file_15_16("cities_"+str(exam_version)+".txt"))

    print("\n----make_city_dict_15_16_17...")
    city = "Bellingham, .44, 10,8,7"
    print("city dict: ", make_city_dict_15_16_17(city))

    #######################################

    # Making tour : use average poem review to determine best_poem_city_not_visited , add that city to the tour, toggled visited 

    #######################################

    print("\n----average_poem_review_3_10_15...")
    average_is_2 = [1,2,3]
    print("average: ", average_poem_review_3_10_15(average_is_2))

    print("\n----best_poem_city_not_visited_5_6_8_15_21...")
    one_city = {"name": "Bellingham", "visit price" : .44, "poem reviews": [10,9,8,7], "average review": 4.13}
    two_city = {"name": "Paris", "visit price" : 5.00, "poem reviews": [6,5,4,3],"average review": 2.4}
    three_city =  {"name": "New York", "visit price" : 2.00, "poem reviews": [3,2,1,0],"average review": 1.1}
    cities = [one_city, two_city, three_city]
    print("best city: ", best_poem_city_not_visited_5_6_8_15_21(cities))

    print("\n----add_city_to_tour_15...")
    tour = ["Bellingham", "Paris"]
    add_city_to_tour_15_19(tour, "New York")
    print("tour =",tour)

    print("\n----toggle_visited_5_17...")
    one_city = {"name": "Bellingham", "visit price" : .44, "poem reviews": [4,7,9,2]}
    one_city["visited"] = False
    toggle_visited_5_17(one_city)
    print("Was False, set to True", one_city)    
    one_city["visited"] = True
    toggle_visited_5_17(one_city)
    print("Was True, set to False", one_city)  

    #######################################

    # give user tour information: Get barcode, draw barcode, print tour itinerary 

    #######################################

    print("\n ---- ticket_barcode_4...")
    print("returns: ", ticket_barcode_4() )

    print("\n----draw_barcode_9...")
    barcode = 12
    draw_barcode_9(barcode) #comment this out once it works to make testing faster

    print("\n----printable_itinerary_14...")
    tour = ["Bellingham", "Paris"] 
    print("returns: ", printable_itinerary_14(tour))

    #######################################
    
    # saving tour: save file, exit message

    #######################################

    print("\n----write_tour_file_16...")
    tour = "Bellingham and then Paris and then New York" 
    write_tour_file_16(tour, "ExamFinal_practice_write.txt")

    print("\n----message_13...")
    message = "THANK YOU for planning with us"
    print("returns: ", exit_message_13(message))

    #######################################

    #putting it all together

    #######################################

    # supplemental: user_choice_loop_7() has been completed for you
    # if you are uncertain about what the instructions are asking for, you can use user_choice_loop_7
    # to see how things are supposed to interact
    # user_choice_loop_7() #un-comment this to run it

# END OF EXAM 
##########################################################################

def user_choice_loop_7():           #DO NOT CHANGE THIS LINE      

    #Start: enters user name, welcome user, read in city data, makes city dictionary
    
    
    #Making tour : use average poem review to determine best_poem_city_not_visited , add that city to the tour, toggled visited 
    

    # give user tour information: Get barcode, draw barcode, print tour itinerary 
    

    # saving tour: save file, exit message
    pass

def get_version():			#DO NOT CHANGE THIS LINE
    return exam_version		#DO NOT CHANGE THIS LINE

if __name__ == "__main__":	#DO NOT CHANGE THIS LINE
  
    main()					#DO NOT CHANGE THIS LINE
