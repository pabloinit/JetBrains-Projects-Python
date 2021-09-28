# Write your code here
class CoffeeMachine:
    def __init__(self):
        self.ingredients = [[250, 0, 16, 1], [350, 75, 20, 1], [200, 100, 12, 1]]
        self.resources = [400, 540, 120, 9]
        self.stock = ['water', 'milk', 'coffee', 'cups']
        self.price = [4, 7, 6]
        self.total_money = 550

    def print_result(self):
        print('The coffee machine has:')
        print(str(self.resources[0]) + ' of water')
        print(str(self.resources[1]) + ' of milk')
        print(str(self.resources[2]) + ' of coffee beans')
        print(str(self.resources[3]) + ' of disposable cups')
        print(str(self.total_money) + ' of money')

    def run(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):\n')
            if action == 'buy':
                n = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
                if n == 'back':
                    continue
                else:
                    n = int(n)
                    for i in range(4):
                        if self.ingredients[n - 1][i] > self.resources[i]:
                            print('Sorry, not enough ' + self.stock[i] + '!')
                            break
                    else:
                        print('I have enough resources, making you a coffee!\n')
                        for i in range(4):
                            self.resources[i] -= self.ingredients[n - 1][i]
                        self.total_money += self.price[n - 1]
            elif action == 'fill':
                self.resources[0] += int(input('Write how many ml of water do you want to add:\n'))
                self.resources[1] += int(input('Write how many ml of milk do you want to add:\n'))
                self.resources[2] += int(input('Write how many grams of coffee beans do you want to add:\n'))
                self.resources[3] += int(input('Write how many disposable cups of coffee do you want to add:\n'))
            elif action == 'take':
                print('I gave you ' + str(self.total_money) + '\n')
                self.total_money = 0
            elif action == 'remaining':
                x.print_result()
            elif action == 'exit':
                break

x = CoffeeMachine()
x.run()
