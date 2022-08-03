mylist = (4,5,6,3,2,1)
print(" The maximum score is ", (max(mylist)))
new_list = set(mylist)
new_list.remove(max(new_list))
print("The runner up score is : ", max(new_list) )

