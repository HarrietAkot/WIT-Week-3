#String of vowels
vowels='aeiou'
#User input of string
stringx=input("enter string: ")
#make a dictionary with vowels as keys and number of occurance as value
count={}.fromkeys(vowels,0)
#go through the user input
for char in stringx:
    #check for vowels    
    if char in count:

        count[char]+=1
print(count)       

      

  
   
    


