import random

play = True
list = []
while play:
    count = 0
    sum = 0
    average = 0
    diceTimes = int(input("How many times would you like to roll?\n"))
    print("============")
    while (count < diceTimes):
        num = random.randint(1, 6)
        list.append(num)
        count += 1

    # Print out all stored rolls in the list
    def list_function(list):
        for x in list:
            print(x)

    # Add all stored rolls up
    def sum_function(list):
        sum = 0
        for x in list:
            sum += x
        return sum

    # Get the average of the stored rolls in the list
    def ave_function(sum, list):
        average = round(sum/len(list), 2)
        return average

    list_function(list)
    sum = sum_function(list)
    print("The sum of the stored rolls is ",sum)
    average = ave_function(sum, list)
    print("The average of the stored rolls is ",average)

    print("============")
    answer = input("Would you like to roll again? Y/N\n")
    print("============")
    if answer.lower() == "n":
        play = False
        print("Thank you!")
