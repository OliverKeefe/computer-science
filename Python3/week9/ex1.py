#a new program to test lists in Python 
#start three new lists 
list1 = ["roll", "burger", "cheese", "ketchup", "mustard"] 
list2 = [] 
list3 = [] 
#code to add ten numbers to list2 
a = 0 
print("Task 1:", *list1, sep = "\n ")
while a < 10: 
    a = a + 1 
    userdata = input("Enter a whole number: ") 
    if userdata != '':
        usernum = int(userdata) 
        list2.append(usernum) 
    print(list2)
list3.append(list2)
list3 = list2.insert(list2, list3) 
print(list3)

remove_item = int(input("Enter the value you wish to remove from list3: "))
if remove_item in list3([0]):
    list3.remove(remove_item)
else:
    print("[!] value could not be found...")  

list2_length = len(list2)
list3_length = len(list3)

if list2_length == list3_length:
    print("List2 and list3 are the same length.")
elif list2_length > list3_length:
    print("List3 is bigger")
elif list3_length > list2_length:
    print("List2 is bigger")
# Need to finish, brain hurt






