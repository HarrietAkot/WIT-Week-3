list1 = []
list2 = []
print("Enter end to exit list")
#user inputs  list 1
print("Enter list 1")
while True:
       #Ask for new items
       new_item=input("> ") 
       #Be able to exit list
       if new_item=='end':
           break

       #Add new items to list
       list1.append(new_item)
 #get length of list1
x=(len(list1)) 
print("List1 has",x,"items",)
print(list1)

#user inputs list 2
print("Enter list 2")
while True:
       #Ask for new items
       new_item2=input("> ") 
       #Be able to exit list
       if new_item2=='end':
           break

       #Add new items to list
       list2.append(new_item2)
#get length of list2      
y=(len(list2))
print("List2 has",y,"items")
print(list2)
def fizzbuzz(x,y):   

     #check if the total of lengths is divisible by 3 and 5           
    if (x+y)%3 == 0 and (x+y)%5 == 0:   
        print('fizzbuzz')   
    #check if total of lengths is divisible by 5              
    elif (x+y)%5 == 0:                
        print('buzz')
    #check if total of lengths is divisible by 3
    elif (x+y)%3 == 0:               
        print('fizz')
    #else print total number of elements
    else:
        print(x+y)                    
fizzbuzz(x,y)