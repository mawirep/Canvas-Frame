 

def approxTime():
    #This is a function designed to tell time to the nearest quater-hour.
    hours = dict() 
    #Hours is the dictionary that will convert the hours from intergers to words
    hours[1] = "0ne"
    hours[2] = "Two"
    hours[3] = "Three"
    hours[4] = "Four"
    hours[5] = "Five"
    hours[6] = "Six"
    hours[7] = "Seven"
    hours[8] = "Eight"
    hours[9] = "Nine"
    hours[10] = "Ten"
    hours[11] = "Eleven"
    hours[12] = "Twelve"
    hours[13] = "Thirteen"
    

    hrs = input(" Please enter the hour ")
    #Input for the hours
    if int(hrs)<1 and int(hrs)>12:
        raise ValueError("hrs range is (1,12)")
        # Raise error massege when the wronge values are entered for the hours
    minutes = input(" Please enter the minutes ")
    if int(minutes)<1 and int(minutes)>59:
        #input for the minutes
        raise ValueError("minutes ranges from 1 to 59")
        # Raise error massege when the wrong numbers are entered for the minutes
    
    


   
    
    if int(minutes)>=1 and int(minutes)<=7:
        print(" The time is ", hours[int(hrs)], "O'Clock")

    elif int(minutes)>=8 and int(minutes)<=22:
        print("the time is quater past", hours[int(hrs)])

    elif int(minutes)>=23 and int(minutes)<=37:
        print('The time is halfpast', hours[int(hrs)])

    elif int(minutes)>=38 and int(minutes)<=52:
        print('The time is quater to', hours[int(hrs)+1])
        
         
    elif int(minutes)>=53 and int(minutes)<=59:
        print('The time is',  hours[int(hrs)+1],  'Oclock')
        

        

    

approxTime()    
    
