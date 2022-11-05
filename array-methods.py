array = [652, 679, 944, 502, 205, 399, 941, 27, 256, 881]
print(f'Array: {array}')

class menus:
    def addElement():
        print("Append")
        number = int(input("Enter the number you want to add: "))
        array.append(number)
        print(f'This is the new array: {array}')

    def insElement():
        print("Insert")
        index = int(input("Enter the index where you want to insert: "))
        number = int(input("Enter the number you want to insert: "))
        array.insert(index,number)
        print(f'This is the new array: {array}')
    
    def modElement():
        print("Lists are Mutable")
        index = int(input("Enter the index where you want to modify: "))
        number = int(input("Enter your new number: "))
        array[index] = number
        print(f'This is the new array: {array}')

    def delElement():
        print("Remove")
        index = int(input("Enter the index you want : "))
        array.pop(index)
        print(f'The element has been deleted.')
        print(f'This is the new array: {array}')

    def ascElement():
        print("Sort (ascending order)")
        array.sort()
        print(f"Arranged in ascending order: {array}")

    def dscElement():
        print("Sort (descending order)")
        array.sort(reverse=True)
        print(f"Arranged in descending order: {array}")
    
    def lenElement():
        print("Length")
        length = len(array)
        print(f"The length of the array is {length}.")

    def minElement():
        print("Mininum")
        smallest = min(array)
        print(f"The smallest element in the array is {smallest}.")

    def maxElement():
        print("Maximum")
        largest = max(array)
        print(f"The largest element in the array is {largest}.")

    def sumElement():
        print("Sum")
        total = sum(array)
        print(f"The sum of the elements in the array is {total}.")

class select:
    def userChoice():
        print("""Menu:
1 -> Add an element
2 -> Insert an element
3 -> Modify an element
4 -> Delete an Element
5 -> Arrange in ascending order
6 -> Arrange in descending order
7 -> Length of the array
8 -> Find the smallest element
9 -> Find the largest element
10 -> Find the sum of the elements
------------------------------------------------""")
        while True:
            try:
                item = int(input("What do you want to do? (1-10): "))
            except ValueError:
                print("Please choose from option 1-10.")
                continue
            if item >= 1 and item <= 10:
                option.chosen(item)
                break
            else:
                print("You must choose from number 1-10.")

class option:
    def chosen(item):
        if item == 1:
            menus.addElement()
        elif item == 2:
            menus.insElement()
        elif item == 3:
            menus.modElement()
        elif item == 4:
            menus.delElement()
        elif item == 5:
            menus.ascElement()
        elif item == 6:
            menus.dscElement()
        elif item == 7:
            menus.lenElement()
        elif item == 8: 
            menus.minElement()
        elif item == 9:
            menus.maxElement()
        elif item == 10:
            menus.sumElement()

select.userChoice()