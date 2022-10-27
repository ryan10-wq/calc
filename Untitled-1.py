nun1 = int(input())
nun2= int(input())
choice = int(input("enter 1 for multiplication 2 for division 3 for addition 4 subtraction"))

if choice ==1:
    print (nun1*nun2)
elif choice ==2:
    print(nun1/nun2)  
elif choice ==3:
    print(nun1+nun2)
elif choice ==4:
    print(nun1-nun2) 
else:
    print("not a valid choice")   