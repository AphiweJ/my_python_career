#Program that takes input from user and creates two lists. Only integers are processed

list1 = []
list2 = []

#Input values for the first list from index 0 - 4
for i in range(5):
    while True:
        try:
            num1 = int(input("Please enter a number to be include in the first list: "))
            list1.append(num1)
            break

        except ValueError:
            print("This programcan only take number, please try again")

#Input values for second list from index 0 - 4
for j in range(5):
    while True:
        try:
            num2 = int(input("Please enter a number to be included in the second list: "))
            list2.append(num2)
            break

        except ValueError:
            print("This programcan only take number, please try again")

#Display both lists
print("First list: ",  list1)
print("Second list: ", list2)