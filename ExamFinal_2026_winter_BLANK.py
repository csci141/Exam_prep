exam_version = 1
#TODO 0A: your name






# Exam instructions
    # The only IDE allowed for this exam is Thonny.
    # Outside assistance such as using AI or other people's assistance is not allowed; those caught will fail the class and be referred to the academic honesty board.
    # Don't change any lines labeled "DO NOT CHANGE THIS LINE"
    # This exam has 16 tasks, each worth the same amount. Plan on about 7 minutes per task so you have a few minutes at the end to turn it in.
    # If you are unable to do a task in 7 minutes, get as far as you can and then move on.
    # On this exam, function argument variables are part of each function definition block; you won't need system arguments for this exam.
    # Comment out lines which cause the code to crash; code which must be hand un-crashed will receive a -1 penalty
    # If instructions are unclear, put your signed post-it note up on your monitor and move on, we'll come around and help.
    # If a substantial bug is found, let us know so we can inform the other students.
    # You are expected to be able to handle minor typos and minor, easily fixable bugs which may be present in the exam file.

    # As normal, there is a main function at the bottom with basic test cases:
    # As a course goal is writing test cases, it's expected you can modify these to make
    # sure everything is operating as required. The testing script will run a full set of tests.
    # The topics list are those the task highlights - others may be required.
    # I've provided the user choice loop code at the very bottom - you can run this if you like to
    # see how all the pieces fit together - or to actually use this study tracker after the exam :-)

# You've learned so much in CSCI 141 - now you can build useful programs for yourself! 
# For this exam, you'll ....

#######################################

# Start: 

#######################################

def pick_todo(hw_not_done, num_tasks): #DO NOT CHANGE THIS LINE
    #Assume parameters 'hw_not_done' is a string, and 'num_tasks' is an integer > 0
        
    #TODO 2_A 
        # topics: print, input, Lines of code: as few as 3

    prompt1 = "Type number of item to do:" 
    task_choice = -1
    
    #TODO 5_7_A 
        # topics: Logical operators, Lines of code: as few as 2

    return(task_choice) #DO NOT CHANGE THIS LINE2

def enter_session():#DO NOT CHANGE THIS LINE
    #TODO 2_B 
        # topics: data types, Lines of code: as few as 3
    prompt_1 = "Amazing! Lock in, and when you're study session is done, enter the number of minutes you worked:"
    prompt_2 = "How many pages did you read?"
    minutes = 0
    pages = 0.0
    
   
    return(minutes, pages, prompt_1)  #DO NOT CHANGE THIS LINE

#TODO 1_10A 
    # topics: print, functions Lines of code: as few as 3


#######################################

    # Calculate things : 
    # 

#######################################

def time_to_complete(total_pages, pages_read, avg_speed): #DO NOT CHANGE THIS LINE
    # assume parameters 'total_pages', 'pages_read' are floats >= 0, and avg_speed is an int >=0
    minutes = 0

    #TODO 3_A 
        # topics: order of operations , Lines of code: as few as 1
    
    return(minutes)    #DO NOT CHANGE THIS LINE

def calc_average_reading_speed(all_hw): 
    #assume parameter 'all_hw' is a list of dictionaries with keys 'name, start page, end page, minutes spent, done, class, pages read'

    #TODO 8_17_3A 
        # topics: for loops, dictionaries, operators, Lines of code: as few as 4
    
    total_pages_read = 0
    total_minutes_read = 0
    average_reading_speed = 0
    
    return(average_reading_speed) 

def find_hw_not_done(all_hw): #DO NOT CHANGE THIS LINE
    #assume parameter 'all_hw' is a list of dictionaries with keys 'name, start page, end page, minutes spent, done, class, pages read'

    #TODO 6_8_17A 
        #topics: for loops, conditionals, dictionaries, Lines of code: as few as 3
    
    count = 0
    hw_to_do = []
    
            
    #TODO 15A 
        # topics: lists, Lines of code: as few as 1
   
    return(count, hw_to_do) #DO NOT CHANGE THIS LINE

def todo_list_to_string(hw_to_do): #DO NOT CHANGE THIS LINE
    #assume parameter 'hw_to_do' is a list of dictionaries with keys 'name, start page, end page, minutes spent, done, class, pages read' 

    #TODO 13_A 
        # topics: strings, Lines of code: as few as 2
  
    count = 1
    todo_as_string = ""
    for hw in hw_to_do:
        name = hw["name"]
        class_name = hw["class"]

    #TODO 14A 
        # topics: strings, Lines of code: as few as 1
   
   
    return(todo_as_string)#DO NOT CHANGE THIS LINE

def draw_progress(one_hw_pages, one_hw_done): #DO NOT CHANGE THIS LINE
    #Assume parameters 'one_hw_pages' is an integer > 0 and 'one_hw_done' is a float >=0
    
    import turtle #DO NOT CHANGE THIS LINE
    
    #TODO 9_A 
        # topics: turtles, Lines of code: as few as 9

    full_length = 0
    
   
    return(full_length) #DO NOT CHANGE THIS LINE

#######################################

    # Store and organize things
    # 

#######################################

def read_todo_file(file_name):#DO NOT CHANGE THIS LINE
    #Assume parameter 'file_name' is the name of a file with text in it which is formatted as:
    #name, start page, end page, minutes spent, done, class, pages read
    
    #TODO 16A 
        # topics: file reading, Lines of code: as few as 3

    all_file_text = [] 

    #TODO 14B 
        # topics: strings, Lines of code: as few as 1
     return(all_file_text)  #DO NOT CHANGE THIS LINE

def make_hw_dict(file_line):#DO NOT CHANGE THIS LINE
    #Assume parameter 'file_line' is a comma separated string: name, start page, end page, minutes spent, done, class, pages read

    #TODO 14_15_A 
        # topics: strings, Lines of code: as few as 1
 

    todo_list = []
    #TODO 17A 
        # topics: dictionaries, Lines of code: 7 if you do each key on it's own line
   
    todo_dict = {}
 
    return(todo_list,todo_dict) #DO NOT CHANGE THIS LINE

def write_hw_file(all_hw, file_name): #DO NOT CHANGE THIS LINE
    #Assume parameters all_hw is a list of dictionaries and 'file_name' is a string ending in ".txt"
    
    #TODO 16_A 
        # topics: files, Lines of code: as few as 3

    for hw in all_hw:  
        for k,v in hw.items(): 
            print(str(v), end=",") 


    pass

def main():
    
    # main() is for testing and development purposes.
    # I've provided some basic code to help with testing,
    # however you will need to add extra test cases
    # and potentially debug the provided code.
    #
    # Nothing in main() will be graded, so you can
    # change it in any way you wish to help with debugging 

    # Optional: want to see this program actually run?
    # Uncertain about what the instructions are asking for?
    # uncomment the line below to see how things are supposed to interact
    # user_choice_loop_7()

    hw_mock_1= {"name":"Chapter 5", "start page": 40,"end page":48,"minutes spent": 5, "done":False, "class": "141", "pages read":2.5}
    hw_mock_2= {"name":"Chapter 1", "start page": 1,"end page":10,"minutes spent": 0, "done":False, "class": "Intro to CS ED SCED 205", "pages read":0}
    hw_mock_3 = {"name":"Conductive Thread", "start page": 23,"end page":30,"minutes spent": 15, "done":True, "class": "E-Textiles", "pages read":10}
    mock_all_hw = [hw_mock_1,hw_mock_2,hw_mock_3 ]

    #######################################

    # Start: Print and Input tasks

    #######################################

    print("\n----pick_todo(hw_not_done, num_tasks)...return(task)")
    num_tasks = 2
    numbered_list = "1: Chapter 5 for 141\n2: Chapter 1 for Intro to CS ED SCED 205"
    print("RETURNS:", pick_todo(numbered_list, num_tasks))
    
    print("\n----enter_session()...return(minutes, pages, prompt_1)")
    print("RETURNS:", enter_session())


    print("\n----todo_list_to_string(hw_to_do)... return(todo_as_string)")
    not_done = [hw_mock_1, hw_mock_2]
    print("RETURNS:", todo_list_to_string(not_done))

    print("You have to write your own test for the welcome message task!")
    

    #######################################

    # Calculate things : 

    #######################################

    print("\n\n----time_to_complete(total_pages, pages_read, avg_speed)...return(minutes)")
    total_pages = hw_mock_1["end page"] - hw_mock_1["start page"]
    pages_read = hw_mock_1["pages read"]
    mock_avg_speed = 5
    print("RETURNS:", time_to_complete(total_pages, pages_read, mock_avg_speed), "minutes")

    print("\n----calc_average_reading_speed(all_hw)...return(average_reading_speed)") #total pages read = 10, total minutes read = 20, minutes per page = 2 min per page
    print("RETURNS:",calc_average_reading_speed(mock_all_hw)) 

    print("\n----find_hw_not_done(all_hw)...return(count, hw_to_do)")
    print("RETURNS: ", find_hw_not_done(mock_all_hw))

    print("\n----draw_progress(one_hw_pages, one_hw_done)...return(full_length)")
    print("RETURNS: ", draw_progress(hw_mock_1["end page"] - hw_mock_1["start page"], hw_mock_1["pages read"]))


    #######################################

    # Store and organize things

    #######################################

    print("\n----read_todo_file(file_name)...return(all_file_text)")
    print("RETURNS:", read_todo_file("turtle_todo.txt"))

    print("\n----make_hw_dict(file_text)...return(todo_list,todo_dict)")
    file_line_mock = "Chapter 5,40,48,10,False,141,3"
    #name, start page, end page, minutes spent, done, class, pages read
    print("RETURNS: (todo_dict, todo_list) ", make_hw_dict(file_line_mock))

    print("\n----write_hw_file(all_hw, file_name)...no return")
    print("no return:", write_hw_file(mock_all_hw, "ExamFinal_practice_write.txt"))

# END OF EXAM 
##########################################################################

#you can run this if you want to see how all the parts fit together! 
#if you are uncertain about what the instructions are asking for, you can use this
#to see how things are supposed to interact

def user_choice_loop_7():            
    #pass


def get_version():			#DO NOT CHANGE THIS LINE
    return exam_version		#DO NOT CHANGE THIS LINE

if __name__ == "__main__":	#DO NOT CHANGE THIS LINE

    main()					#DO NOT CHANGE THIS LINE
