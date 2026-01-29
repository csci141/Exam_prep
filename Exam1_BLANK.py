exam_version = 99
#TODO 0A: your name






# Exam instructions
    # The only IDE allowed for this exam is Thonny.
    # Outside assistance such as using AI or other people's assistance is not allowed; those caught will fail the class and be referred to the academic honesty board.
    # Don't change any lines labeled "DO NOT CHANGE THIS LINE"
    # This exam has 13 tasks, each worth the same amount. Plan on about 3.5 minutes per task so you have a few minutes at the end to turn it in.
    # If you are unable to do a task in 4 minutes, move on and come back later.
    # On this exam, function argument variables are part of each function definition block; you won't need system arguments for this exam.
    # Comment out lines which cause the code to crash; code which must be hand un-crashed will receive a -1 penalty
    

def welcome_customer_1():	#DO NOT CHANGE THIS LINE 
    
    #TODO 1A
    
    
def fix_date_2(day, month):	#DO NOT CHANGE THIS LINE
    # The date will be in the function arguments 'day' and 'month' 
    # the data type of 'day' and 'month' could be int, float or string
    
    #TODO 2A 

    return(day, month)	#DO NOT CHANGE THIS LINE
    
def predict_growth_3(visitors, members):		#DO NOT CHANGE THIS LINE
    # assume 'visitors' and 'members' are integers
   
    #TODO 3A

    growth = 0

    return(growth)	#DO NOT CHANGE THIS LINE
    
def new_merch_4(merch_name):	#DO NOT CHANGE THIS LINE
    # assume 'merch_name' is a string.
    
    #TODO 4A
    
    price = 0.0
    
    #TODO 4B
   
    prefix = "0000"

    return(price, prefix)  #DO NOT CHANGE THIS LINE

def events_scheduled_5(scheduled, date):    #DO NOT CHANGE THIS LINE
    # Assume 'scheduled' is an integer.
    # Assume 'date' is an integer
    
    #TODO 5a
   
    event_goal_met = True

    #TODO 5b

    start_plan = False
    
    return(event_goal_met, start_plan)  #DO NOT CHANGE THIS LINE


def guest_passes(visits, member, birthday):           #DO NOT CHANGE THIS LINE           
    # assume 'visits' is an integer; 'member' and 'birthday' are booleans
    
    #TODO 6a
  
    guest_passes = 0
        
    #TODO 6b 
   

    #TODO 6c
  
        
    #TODO 6d
   
    

    return(guest_passes) #DO NOT CHANGE THIS LINE


def user_choice_loop_7():           #DO NOT CHANGE THIS LINE          
    
    choice_text = "[f]ix date, [p]redict growth, [n]ew merch, [e]vents scheduled, [g]uest passes, or [q]uit:" #DO NOT CHANGE THIS LINE
    
    #TODO 7a
  
    
    pass_check = 0
        
   #TODO 7b  
        

    return(pass_check) #DO NOT CHANGE THIS LINE


def main(): 			        #DO NOT CHANGE THIS LINE
    
    # main() is for testing and development purposes.
    # I've provided some basic code to help with testing,
    # however you will need to add extra test cases
    # and potentially debug the provided code.
    #
    # Nothing in main() will be graded, so you can
    # change it in any way you wish to help with debugging 

    print("----Running welcome_customer_1()...")
    welcome_customer_1()
   
    print("----Running fix_date_2(day, month)....")
    print("returns: ", fix_date_2(1.0, "3") )
    
    print("----Running predict_growth_3(visitors, members)....")
    print("returns: ", predict_growth_3(30, 100))
    
    print("----Running new_merch_4(merch_name) ...")
    print("returns: ", new_merch_4("Blue Era") )

    print("----Running events_scheduled_5(scheduled, date)...")
    print("returns: ", events_scheduled_5(0,5)) #
    print("returns: ", events_scheduled_5(0,31)) #
    print("returns: ", events_scheduled_5(100,31)) #

    print("----Running guest_passes(visits, member, birthday)...")
    print("returns: ", guest_passes(3, True, False)) #
    print("returns: ", guest_passes(60, True, True)) # 
    print("returns: ", guest_passes(30, False, True)) # 
    print("returns: ", guest_passes(30, False, False)) # 
    
    print("---- user_choice_loop_7()...")
    print("returns: ", user_choice_loop_7()) 



# END OF EXAM 
##########################################################################

def get_version():			#DO NOT CHANGE THIS LINE
    return exam_version		#DO NOT CHANGE THIS LINE

if __name__ == "__main__":	#DO NOT CHANGE THIS LINE
  
    main()					#DO NOT CHANGE THIS LINE
