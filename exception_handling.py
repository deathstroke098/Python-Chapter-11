#for i in range(1,6):
  #  for j in range(1 ,i+1):
    #    print('*' , end="  ")
    #print()
            

#try :
   # f = open("test3.txt", "w")
   # f.write("there is something in here")
   # print("I have to return some video tapes")
#except:
 #   print("This is how you handle an error in exception block")
#else:
   # print("Now the else will be executed , coz there is no error in the try block")  
   # f.close()
#finally:
    #print("This will execute all the damn time ") #


#def askint():
   # try:
       # a=int(input("enter something here please :"))
       # return a

   # except Exception:
       # print("the error has been handled" )
    
#askint()    

# WRITE A FUNCTION WHICH KEEPS ON EXECUTING UNTILL AN INTEGER IS PROVIDED.
#def interger():
   # while True:
     #   """Function asks for an integer unless provided"""
      #  try:
        #    x = int(input("enter something "))
         #   break
       # except Exception:
           # print("please input no. only")
    

#interger()        

#try:    
  #  age = int(input("Enter the age:"))    
   # if(age<18):    
     #   raise ValueError   
  #  else:    
      #  print("the age is valid")    
#except ValueError:    
   # print("The age is not valid") 


#def askint():
   # while True:
       # try:
            #x= int(input("Enter the no. "))
           # break
     #   except Exception:
          #  print("error occured , please try again ")
          #  continue
            
        

#askint()  


try:
    a=8
    b=0
    c=a/b
    print("error occured")
except ZeroDivisionError:
    c=0
    print("error handled")
print(c)