# Write your code here
def print_result():
    print('The coffee machine has:')
    print(str(resources[0]) + ' of water')
    print(str(resources[1]) + ' of milk')
    print(str(resources[2]) + ' of coffee beans')
    print(str(resources[3]) + ' of disposable cups')
    print(str(total_money) + ' of money')


ingredients = [[250, 0, 16, 1], [350, 75, 20, 1], [200, 100, 12, 1]]
resources = [400, 540, 120, 9]
stock = ['water', 'milk', 'coffee', 'cups']
price = [4, 7, 6]
total_money = 550

while True:
    action = input('Write action (buy, fill, take, remaining, exit):\n')
    if action == 'buy':
        n = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if n == 'back':
            continue
        else:
            n = int(n)
            for i in range(4):
                if ingredients[n - 1][i] > resources[i]:
                    print('Sorry, not enough ' + stock[i] + '!')
                    break
            else:
                print('I have enough resources, making you a coffee!\n')
                for i in range(4):
                    resources[i] -= ingredients[n - 1][i]
                total_money += price[n - 1]
    elif action == 'fill':
        resources[0] += int(input('Write how many ml of water do you want to add:\n'))
        resources[1] += int(input('Write how many ml of milk do you want to add:\n'))
        resources[2] += int(input('Write how many grams of coffee beans do you want to add:\n'))
        resources[3] += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    elif action == 'take':
        print('I gave you ' + str(total_money) + '\n')
        total_money = 0
    elif action == 'remaining':
        print_result()
    elif action == 'exit':
        break
