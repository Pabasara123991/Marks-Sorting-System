# Code
# Part 2

User_option=int(input("User Option:\n\tEnter number 1 for STUDENT VERSION\n\tEnter number 2 for STAFF VERSION\nEnter the User Option: "))
if User_option == 1:
    print("STUDENT VERSION")
    
    while True:              #to get multiple inputs
    
        while True:             #loop until a valid input is given
            try:
                valid_credits=[0, 20, 40, 60, 80, 100, 120]
                Pass=int(input("Please enter your credits at pass: "))
            except ValueError:
                print("Integer required")
                continue
            if Pass not in valid_credits:
                print("Out of range")
                continue
            break
        while True:
            try:
                valid_credits=[0, 20, 40, 60, 80, 100, 120]
                Defer=int(input("Please enter your credits at defer: "))
            except ValueError:
                print("Integer required")
                continue
            if Defer not in valid_credits:
                print("Out of range")
                continue
            break

        while True:
            try:
                valid_credits=[0, 20, 40, 60, 80, 100, 120]
                Fail=int(input("Please enter your credits at fail: "))
            except ValueError:
                print("Integer required")
                continue
            if Fail not in valid_credits:
                print("Out of range")
                continue
            break
           

        total= Pass+Defer+Fail
        if total != 120:       #check whether credit total equal to 120
            print("Total incorrect")
        elif Pass == 120 and Defer == 0 and Fail == 0:
            print("Progress")
        elif Pass == 100 and Defer <= 20 and Fail <= 20:
            print("Module trailer")
        elif Pass <=80 and Defer <= 80 and Fail <= 60:
            print("Module retriever")
        elif Pass <=40 and Defer <= 40 and Fail <= 120:
            print("Excluded")
            break
        break
    
            
       
           

#if User_option != 1 then comes to this            
elif User_option == 2:
    print("STAFF VERSION")
    Progress_count= Trailer_count= Retriever_count= Excluded_count= 0
    Progress_list= []
    Trailer_list= []
    Retriever_list= []
    Excluded_list= []
    Dictionary={}
    #create def to print histogram
    def Histogram(Progress_count, Trailer_count, Retriever_count, Excluded_count):
        print("-"*50)
        print("Histogram")
        print("Progress",Progress_count,":",Progress_count * "*")
        print("Trailer",Trailer_count,":",Trailer_count * "*")
        print("Retriever",Retriever_count,":",Retriever_count * "*")
        print("Excluded",Excluded_count,":",Excluded_count * "*")
        outcome_count=Progress_count+Trailer_count+Retriever_count+Excluded_count
        print(outcome_count,"outcomes in total.")
        print("-"*50)
    
        
    
    while True:
        UoW_Number = input("Enter the UoW number: ")
        UoW_Number = UoW_Number.lower()
   
        while True:
            try:
                valid_credits=[0, 20, 40, 60, 80, 100, 120]
                Pass=int(input("Please enter your credits at pass: "))
            except ValueError:
                print("Integer required")
                continue
            if Pass not in valid_credits:
                print("Out of range")
                continue
            break
        while True:
            try:
                valid_credits=[0, 20, 40, 60, 80, 100, 120]
                Defer=int(input("Please enter your credits at defer: "))
            except ValueError:
                print("Integer required")
                continue
            if Defer not in valid_credits:
                print("Out of range")
                continue
            break

        while True:
            try:
                valid_credits=[0, 20, 40, 60, 80, 100, 120]
                Fail=int(input("Please enter your credits at fail: "))
            except ValueError:
                print("Integer required")
                continue
            if Fail not in valid_credits:
                print("Out of range")
                continue
            break
        
        
        

        total= Pass+Defer+Fail
        if total != 120:        #check whether credit total equal to 120
            print("Total incorrect")
        elif Pass == 120 and Defer == 0 and Fail == 0:
            print("Progress")
            Progress_list.append([Pass,Defer,Fail])
            Progress_count += 1

            Dictionary[UoW_Number] = f"Progress - {Pass}, {Defer}, {Fail}"
            
        elif Pass == 100 and Defer <= 20 and Fail <= 20:
            print("Module trailer")
            Trailer_list.append([Pass,Defer,Fail])
            Trailer_count += 1

            Dictionary[UoW_Number] = f"Module trailer - {Pass}, {Defer}, {Fail}"
            
        elif Pass <=80 and Defer <= 80 and Fail <= 60:
            print("Module retriever")
            Retriever_list.append([Pass,Defer,Fail])
            Retriever_count += 1

            Dictionary[UoW_Number] = f"Module retriever - {Pass}, {Defer}, {Fail}"
            
        else:
            print("Excluded")
            Excluded_list.append([Pass,Defer,Fail])
            Excluded_count += 1

            Dictionary[UoW_Number] = f"Excluded - {Pass}, {Defer}, {Fail}"
            
        print("Would you like to enter another set of data?")    
        while True:
            answer=input("Enter 'y' for yes or 'q' to quit : ")
            answer=answer.lower()

            if answer in('y','q'):
                break
            else:
                print("Invalid Input. Try Again!!!")       
                continue
            
        if answer=='y':
            continue
        
        if answer=='q':
            Histogram(Progress_count, Trailer_count, Retriever_count, Excluded_count)
            print()

            # Part 4 - Dictionary
            for key in Dictionary:
                value = Dictionary[key]
                print("{} : {}".format(key, value), end=" ")
            break
                
        
        

 



        
        
    
            






    
       
       
             

              
    

     
             


               
                    
