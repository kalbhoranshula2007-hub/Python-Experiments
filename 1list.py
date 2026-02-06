
my_list = [10, 5, 20, 15, 30]
print("Original List:", my_list)

print("First element:", my_list[0])
print("Last element:", my_list[-1])

my_list.append(25)          
print("After adding 25:", my_list)

my_list.insert(2, 12)       
print("After inserting 12 at index 2:", my_list)

my_list.remove(5)           
print("After removing 5:", my_list)

my_list.pop()            
print("After removing last element:", my_list)

my_list.sort()
print("Sorted List:", my_list)

my_list.reverse()
print("Reversed List:", my_list)