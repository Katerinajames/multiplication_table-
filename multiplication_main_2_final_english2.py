print("MULTIPLICATION TABLE")

counter=1
n=int(input("Enter an  integer between 1 and  10 or  0 for exit :\n"))
while n<0:
   n=int(input("Try again !! !!\n "))
   
if n==0 :
	  print("Exit  ")

else: 
 while n!=0:	 
	 for counter in range (1,11):
	  result = counter * n 	 
	  print(f"{counter} x {n} = {result}")
	 counter += 1
	 n=int(input("Enter an  integer between 1 and  10 or  0 for exit :\n"))
	 if n==0:
	
        
		 print("Exit  ")
		 break  
	  
	   	 
	
		 
     
		 
	    
     
    
    
    	 
           
			
			
		 		   
              
             
       


 	 


#https://www.geeksforgeeks.org/multiplication-table-using-while-loop-in-python/
