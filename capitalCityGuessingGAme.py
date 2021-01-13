quetion =['What is the capital city of Rwanda : ',
           'What is the capital city of Uganda : ',
           'What is the Capital city of  Burundi : ',
           'What is The Capital city of Kenya  : ',
           'What is The capital city of Tanzania : ']
answers =['Kigali','Kampala','Bujumbura','Nairobi','Dodoma']
marks = 0
for i in range(len(quetion)):
    guess = input(quetion[i])
    if guess.lower() ==answers[i].lower():
        marks = marks + 5
        print("Correct ")
    else:
        print("you FAil the Capital city is ",answers[i])
        marks = marks -1
print("Your marks is ",marks ,"Thanks for you Time")
