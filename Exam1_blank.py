exam_version = 1
#TODO 0A: name date

# Exam instructions
    # Outside assistance such as using AI or other people's assistance is not allowed; those caught will fail the class and be referred to the academic honesty board.
    # Don't change any lines labeled "DO NOT CHANGE THIS LINE"
    # This exam has 12 tasks, each worth the same amount. Plan on about 4 minutes per task so you have a few minutes at the end to turn it in.
    # If you are unable to do a task in 4 minutes, get as far as you can and then move on.
    # Comment out lines which cause the code to crash
    

def print_1():	#DO NOT CHANGE THIS LINE 
    
    #TODO 1A

    
def fix_prices_2(buy_price, sell_price):	#DO NOT CHANGE THIS LINE

    #TODO 2A
    print()
    
    return(buy_price, sell_price)	#DO NOT CHANGE THIS LINE
    
def calculate_profit_3(buy_price, sell_price):		#DO NOT CHANGE THIS LINE
    
    #TODO 3A
    answer3a = 0
   
    return(answer3a)	#DO NOT CHANGE THIS LINE
    
def set_barcode_4(product_name):	#DO NOT CHANGE THIS LINE
      
    #TODO 4A
    prod_num = "" 
    
    
    #TODO 4B
    prefix = 0000


    return(prod_num, prefix)  #DO NOT CHANGE THIS LINE

def check_inventory_5(have_amount, want_amount):    #DO NOT CHANGE THIS LINE
    
    #TODO 5a
    have_enough = True


    #TODO 5b
    reorder = False
   

    return(have_enough, reorder)  #DO NOT CHANGE THIS LINE


def set_sale_6(days_since, last_sale):           #DO NOT CHANGE THIS LINE          
     # assume days_since and last_sale are integers

    sale_percent = 0
    
    #TODO 6a
    
   
    #TODO 6b


    #TODO 6c
   

    return(sale_amount) #DO NOT CHANGE THIS LINE


def user_choice_loop_7():           #DO NOT CHANGE THIS LINE          
    
    print_1() #DO NOT CHANGE THIS LINE
    choice_text = "[f]ix prices, [c]alc profits, set [b]arcode, [i]nventory check, [s]et sale, or [q]uit:" #DO NOT CHANGE THIS LINE
    
    #TODO 7a
    
    #TODO 7b
    loop_count = 0  
  

    return(loop_count) #DO NOT CHANGE THIS LINE


def main(): 			        #DO NOT CHANGE THIS LINE
   
    # this program will run from a 'user choice loop' you'll build inside user_choice_7
    # but for testing and development purposes, here we'll call each of the functions
    # in sequence.
    # Nothing in Main will be graded, so you can use this to help with debugging 
    

    print("----Running print_intro_1...")
    print_1()
   
    print("----Running data_type_2....")
    print("returns: ", fix_prices_2(1, "3") )
    
    print("----Running calculate_profit_3....")
    print("returns: ", calculate_profit_3(1.0, 2.0))
    
    print("----Running set_barcode_4() ...")
    print("returns: ", set_barcode_4("E-Bike") )

    print("----Running check_inventory_5...")
    print("returns: ", check_inventory_5(10,5))

    print("---- set_sale_6...")
    set_sale_6(3, 20)
    
    print("---- user_choice_loop_7...")
    user_choice_loop_7()


# END OF EXAM 
##########################################################################

def get_version():			#DO NOT CHANGE THIS LINE
    return exam_version		#DO NOT CHANGE THIS LINE

if __name__ == "__main__":	#DO NOT CHANGE THIS LINE
    main()					#DO NOT CHANGE THIS LINE
