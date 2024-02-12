print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

true_list = ['t', 'r', 'u', 'e']
love_list = ['l','o', 'v', 'e']

name1_list = list(name1.lower())
name2_list = list(name2.lower())
names_combined_list = name1_list + name2_list

true_count = 0
for pos in true_list:
    value = names_combined_list.count(pos)
    true_count += value

love_count = 0
for pos in love_list:
    value = names_combined_list.count(pos)
    love_count += value

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')

elif love_score >= 40 and love_score <= 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
