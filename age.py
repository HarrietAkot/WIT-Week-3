yob=input("please enter year of birth")
y=int(yob)
year='2018'
x=int(year)
age=x-y
if age <= 18:
     print ("You are a Minor")
elif age > 18 and age < 36:
     print ("You are a youth")
elif age > 36:
     print ("You are an Elder")
else:
     print ("Please re-enter year of birth")