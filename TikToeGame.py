from random import randint
marks = 0;
for x in range(5):
    x = eval(input("Guess number between 1 - 10 = "))
    
    y = randint(1,5)
    if x == y:
        marks = marks + 5
        print("Correct , now your marks is : ",marks)
    else:
        marks = marks -5
        print("You loose your marks is : ", marks)
        print("The correct number is : ", y)
    
print("Thank you for your time you marks is ", marks)    
if marks >= 20:
    print("Great work");
elif marks >= 10:
    print("good works")
else:
    print("You are looser")