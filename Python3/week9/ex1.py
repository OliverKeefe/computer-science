#a new program to test lists in Python 
#start three new lists 
list1 = ["roll", "burger", "cheese", "ketchup", "mustard"] 
list2 = [] 
list3 = [] 

#code to add ten numbers to list2 
a = 0 
print("Task 1:", *list1, sep = "\n")
while a < 10: 
    a = a + 1 
    userdata = input("Enter a whole number: ") 
    if userdata != '':
        usernum = int(userdata) 
        list2.append(usernum) 
    print(list2)
    list3 = list2
    print(list3)

odd_numbers = [x for x in list3 if x % 2 == 0]
even_numbers = [x for x in list2 if x % 2 != 0]
print("List2 with even numbers removed:", even_numbers, "List3 with odd numbers removed:", odd_numbers)

list2_length = len(list2)
list3_length = len(list3)

if list2_length == list3_length:
    print("List2 and list3 are the same length.")
elif list2_length > list3_length:
    print("List3 is bigger")
elif list3_length > list2_length:
    print("List2 is bigger")
# Need to finish, brain hurt






