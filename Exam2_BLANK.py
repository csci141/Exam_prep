exam_version = 2




    

#TODO 0A: your name

# Exam instructions
    # Outside assistance such as using AI or other people's assistance is not allowed; those caught will fail the class and be referred to the academic honesty board.
    # Don't change any lines labeled "DO NOT CHANGE THIS LINE"
    # This exam has 16 tasks, each worth the same amount. Plan on about 3 minutes per task so you have a few minutes at the end to turn it in.
    # If you are unable to do a task in 3 minutes, get as far as you can and then move on.
    # On this exam, function argument variables are part of each function definition block; you won't need system arguments for this exam.
    # Comment out lines which cause the code to crash

# Your store has decided to branch out to sell subscriptions to:
# a daily 'take a walk' text message reminders!
# Instead of miles, it uses leagues, where leagues are how far you can walk in an hour.
# Your patented 'secret sauce' is you take the weather and elevation into consideration.
# For this exam, you'll be writing code which helps you prepare these WindLeague (TM) messages.

def calc_wind_leagues_123(miles, wind): #DO NOT CHANGE THIS LINE
    #you can assume that the arguments 'miles' and 'wind' are are non-negative numbers (either int or float)

    
    #TODO 123A
    
    
    
    #TODO 123B
   
    wind_leagues = 0.0
    
    return(miles, wind, wind_leagues) #DO NOT CHANGE THIS LINE

def decipher_order_prefix_4():	#DO NOT CHANGE THIS LINE
    
    #TODO 4A

    ver_num  = 0

    return(ver_num)  #DO NOT CHANGE THIS LINE


def elevation_impact_56(one_way, leagues, elevation_change):           #DO NOT CHANGE THIS LINE           
    # assume the arguments 'one_way' is boolean and 'leagues' and 'elevation_change' are floats 
    
    elevation_impact = 0
       
    #TODO 56A   
    
    
    #TODO 56B

    
    #TODO 56C  

    return(elevation_impact) #DO NOT CHANGE THIS LINE

def hype_8(walk_streak): #DO NOT CHANGE THIS LINE
    # assume the argument 'walk_streak' is a positive integer greater than 0
    
    
    #TODO 8A

    pass
        

def display_progress_9(progress, goal): #DO NOT CHANGE THIS LINE
    # assume the arguments 'progress' and 'goal' are positive, non_zero integers
    # and that the argument 'goal' is greater than or equal to 'progress'
    
    #TODO 9A
    

    import turtle 

    
    
    #TODO 9B

    

#TODO 10A 

        
    


#TODO 11A
wants_km = False # our default is kilometers
def to_kilometer_11(miles):   #DO NOT CHANGE THIS LINE
    # assume 'miles' is a float or int, return a float

    km = 0
    
    return(km) #DO NOT CHANGE THIS LINE
    
def leagues_to_go_12(hours, minutes, wind_speed): #DO NOT CHANGE THIS LINE
    # assume ''hours' and 'minutes' are both integers,
    # and 'wind_speed' is a non negative number
    
    #TODO 12A
    
    time_tuple = ()
    
    #TODO 12B
   
    wind_leagues = 0
    total_minutes = hours * 60 + minutes
    miles = total_minutes / 20 #assuming the user can walk a mile every 20 minutes
    
    
    return(time_tuple, wind_leagues)  #DO NOT CHANGE THIS LINE

def user_choice_loop_7():           #DO NOT CHANGE THIS LINE          
  
    #TODO 7a

    loop_count = -1 
    

    #TODO 7b
   
    return(loop_count) #DO NOT CHANGE THIS LINE


def main(): 			        #DO NOT CHANGE THIS LINE
   
    # for testing and development purposes, here we'll call each of the functions
    # in sequence.
    # Nothing in Main will be graded, so you can use this to help with debugging 
  
    print("\n----calc__wind_leagues_123(miles, wind)...return(miles, wind, wind_leagues)...")
    print("with (3,30) returns: ", calc_wind_leagues_123(3, 30))
       
    print("\n----Running decipher_order_prefix_4() ...return(ver_num) for 0111...")
    print("returns: ", decipher_order_prefix_4() )

    print("\n----elevation_impact_56(one_way, leagues, elevation_change)...return(elevation_impact)...")
    print("with (True,9,30) returns: ", elevation_impact_56(True,9,30)) 
    
    print("\n---- hype_8(walk_streak)...returns nothing")
    print("...with 5 :")
    hype_8(5)
    print("...with 9 :")
    hype_8(9)

    
    print("\n--- TODO 10A add your own test here")
    
    print("---- to_kilometer_11(miles).., returns kilometers")
    
    print("\n---- leagues_to_go_12(hours, minutes, wind_speed)... return(time_tuple, wind_leagues)...")
    print("with (1, 30, 20) returns: ", leagues_to_go_12(1,30, 20))

    print("\n---- user_choice_loop_7()...return(loop_count)")
    count = user_choice_loop_7()
    print("the loop count was: ", count)
    
    print("\n---- display_progress_9(progress, goal)...draws with turtle, returns nothing")
    print("with 75% done: ")
    display_progress_9(75, 100)
    

    print("with 25% done: ")
    display_progress_9(25, 100)

   


# END OF EXAM 
##########################################################################

def get_version():			#DO NOT CHANGE THIS LINE
    return exam_version		#DO NOT CHANGE THIS LINE

if __name__ == "__main__":	#DO NOT CHANGE THIS LINE
    #Encode in base 64 the architecture used #DO NOT CHANGE THIS LINE
    main()					#DO NOT CHANGE THIS LINE
