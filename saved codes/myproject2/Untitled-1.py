print("Started!!")

while 1:
     num1=int(input("player 1 must choose a number between 1 to 100 : "))
     if num1<100 and num1>0:
        break
     print("your number must be between 1 and 100 try again!")

pos=False
i=0
while pos==False and i<10:
    num2=int(input("Try for time " + str(i+1) + " : "))
    if num1==num2:
        print("player 2 won!!!!!!")
        pos=True
    elif num2<num1:
        print("answer is bigger,nigger")
        i=i+1
    elif num2>num1:
        print("answer is smaller")
        i=i+1
    else:
        print("Error, try again")
    if i==10:
        print("player 1 won!!")