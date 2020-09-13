score_number = input("How many days of scores? ")
sum_num = 0
for score in range(int(score_number)):
    score = input("Enter score for day : ")
    sum_num += int(score)

print("The total score of the 4 days is", sum_num)
