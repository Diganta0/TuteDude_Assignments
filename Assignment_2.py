#Task 1
#Check if a Number is Even or Odd

num=int(input("Enter any number:"))

if num%2==0:
    print("The number is even")
else:
    print("The number is odd")

#Task 2
#Sum of Integers from 1 to 50 Using a Loop
total=0
for i in range(1,51):
    total+=i
print(total)