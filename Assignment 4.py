#Witu has tasked you to automate a simple grading system as a paython student .write a programme using to display the grades that the students will be receiving based on the mark scored in a subject.
#the grades are;
#90%-100% Grade is A
#80%-89% Grade is B
#70%-79% Grade is C
# 60-69% Grade is D
#50%-59% Grade is E
#<50% Fail

# Answers
mark= int(input("Enter the mark scored : \t"))
if mark>=90 and mark<= 100:
        print("Grade is A")
elif mark>= 80 and mark<= 89:
        print("Grade is B")
elif mark>= 70 and mark<= 79:
       print("Grade is C")
elif mark>= 60 and mark<=69:
        print("Grade is D")
elif mark>= 50 and mark<= 59:
        print("Grade is E") 
else:
        print("fail")
        


        # The volume of a sphere with radius r is (4/3 )*pie* r**2.
        #what is the volume of the spere with radius 5
        #make sure the programme enters the raduius from the key board and provide the answer in 2 decimal places
        
        #ans
radius = int(input("Enter the radious of the sphere :\t"))
pie = float(input("Enter the pie of the sphere :\t"))
volume = (4/3)*pie*radius**2
print(f"The volume of the sphere of {radius} and {pie} is {volume:.2f}")


        #create aprogramme to calculate the area of a triagle (1/2*base*height.)
        #Base and height should be entered using the keyboard. 

        #  ans
base = int(input("Enter the base  of the triangle : \t"))
height = int(input("Enter the height of the triangle : \t"))
area = (1/2)*base*height
print(F"The area of the triangle of {base} and {height} is {area}")
        
    

        #witi Academy is proposing a sacco to help students save their money.
        # Design a platform that will do the following.
        #welcome to, WITI Academy sacco.
        #1.Deposite money
        #2.Withdraw money
        #3.Check Balance
        #Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
        #if the student select 2 ,money should be withdrawn and a minimum withdrawl is 500.
        #if the student selects 3,the account balance should be displayed.
       
        #answer
accauntBlance=0
run=1

while run==1:
  print("\nWelcome to ,WITIACADEMY sacco.")

     #menu
  print("1.Deposite Money")
  print("2.Withdraw Money")
  print("3.check Blance")

studentChoice=int(input("Enter your selection(1,2,or 3):"))
 #performing the transactions basing on the student selection

if studentChoice==1:
   print("\n....processing a depost trasaction...")
depositAmount=int(input("Enter amount to be deposited:"))

     #check if deposit amount is less than 1ooo
if depositAmount < 1000:
   print("\nMinimum deposit is 1000")

else:
    accauntBlance +=depositAmount
print(f"Deposit successfully {"amount"}.Your new balance is{"Balance"}")


print("minimum deposit amount is 1000.")
"choice"==2
amount=float(input("Enter Withdraw amount:"))
if amount >=500:
    "Balance"-= amount
print(f"sucessfully withdraw {amount}.Your new account is {"Balance"}.")


print("minimum withdraw amount is 500.")
"choise"==3

          
    




