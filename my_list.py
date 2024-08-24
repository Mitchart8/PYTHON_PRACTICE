#Empty list
my_list = []

#Adding items
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#Inserting 15 to the second position
my_list.insert(1, 15)

print(my_list)

#Extending my_list with another list
my_list.extend([50, 60, 70])

print(my_list)

#Removing the last item on the list
my_list.remove(70)

print(my_list)

#Sorting list in ascending order
my_list.sort()

#Finding and printing the index of the value 30 in my_list.
index_of_30 = my_list.index(30)

print("index of 30:", index_of_30)