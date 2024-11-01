
#TODO 0A: your name

# Exam instructions
 
def print_calculated_profit123(buy_price, sell_price):
    
    #TODO 123A
       
    #TODO 123B
      
    #TODO 123C
   
   return(percent_profit)

def set_barcode_4(product_name):	#DO NOT CHANGE THIS LINE
      
    #TODO 4A

    return(prefix)  #DO NOT CHANGE THIS LINE

def reorder_56(inventory_amount, order_amount, holiday):           #DO NOT CHANGE THIS LINE           
   
    #TODO 56A   
      
    #TODO 56B  
    
    #TODO 56C

    return(order_quantity) #DO NOT CHANGE THIS LINE

def hype_8(num):
    #TODO 8A
    
def turtle_9(super_time):
    
    import turtle
    t = turtle.Turtle()
    #TODO 9A
      
    #TODO 9B
      
#TODO 10A

time_zone = "PST"
def time_zone_11(zone):
    
    #TODO 11A
    
    return(time_zone)
    
def time_in_super_time_12(time_tuple):
    
    #TODO 12A
      
    #TODO 12B use the to_super_10 function to 
     
    return(standard_min, standard_sec, super_time)

def user_choice_loop_7():           #DO NOT CHANGE THIS LINE          
    
    print_1() #DO NOT CHANGE THIS LINE
    choice_text = "[f]ix prices, [c]alc profits, set [b]arcode, [i]nventory check, [s]et sale, or [q]uit:" #DO NOT CHANGE THIS LINE
    
    #TODO 7a
      
    #TODO 7b
         
    return(loop_count) #DO NOT CHANGE THIS LINE


def main(): 			        #DO NOT CHANGE THIS LINE
   
    # this program will run from a 'user choice loop' you'll build inside user_choice_7
    # but for testing and development purposes, here we'll call each of the functions
    # in sequence.
    # Nothing in Main will be graded, so you can use this to help with debugging 
    
    print("----print_calculated_profit123...")
     print("returns: ", print_calculated_profit123(10, 30))
   
    print("----Running set_barcode_4() ...")
    print("returns: ", set_barcode_4("E-Bike") )

    print("----reorder_56()...")
    print("returns: ", reorder_56(5,10 , True))

    print("----Running set_sale_6()...")
    print("returns: ", set_sale_6(3, 20))
     
    print("---- user_choice_loop_7()...")
    user_choice_loop_7()
    
    print("----  hype_8...")
    hype_8(5)

    print("----  turtle_9...")
    turtle_9(80)
    
    print("---- time_zone_11()...")
    print("returns: ", time_zone_11("CST"))
    
    print("---- time_in_super_time_12()...")
    print("returns: ", time_in_super_time_12((10,35)))


# END OF EXAM 
##########################################################################

def get_version():			#DO NOT CHANGE THIS LINE
    return exam_version		#DO NOT CHANGE THIS LINE

if __name__ == "__main__":	#DO NOT CHANGE THIS LINE
    #Encode in base 64 the architecture used #DO NOT CHANGE THIS LINE
    main()					#DO NOT CHANGE THIS LINE
