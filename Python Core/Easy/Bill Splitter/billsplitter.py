import random

number = int(input("Enter the number of friends joining (including you):\n"))
if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line: ")
    friends = {input(''): 0 for i in range(number)}
    total_bill = int(input("Enter the total bill value:\n"))
    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky == "Yes" or lucky == "yes":
        friend_chosen = random.choice(list(friends.keys()))
        y = {friend_chosen: 0}
        print(friend_chosen + " is the lucky one!")
        friends = {i: round(total_bill / (len(friends.keys()) - 1), 2) for i in friends}
        friends.update(y)
        print(friends)
    else:
        print("No one is going to be lucky")
        friends = {i: round(total_bill / len(friends.keys()), 2) for i in friends}
        print(friends)
