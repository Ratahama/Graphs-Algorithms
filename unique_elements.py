list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Elements in list1 but not in list2
unique_to_list1 = list(set(list1) - set(list2))

# Elements in list2 but not in list1
unique_to_list2 = list(set(list2) - set(list1))

print("Elements unique to list1:", unique_to_list1)  # Elements unique to list1: [1, 2]
print("Elements unique to list2:", unique_to_list2)  # Elements unique to list2: [6, 7]




# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# # Elements in list1 but not in list2
# unique_to_list1 = [elem for elem in list1 if elem not in list2]
#
# # Elements in list2 but not in list1
# unique_to_list2 = [elem for elem in list2 if elem not in list1]
#
# print("Elements unique to list1:", unique_to_list1)  # Elements unique to list1: [1, 2]
# print("Elements unique to list2:", unique_to_list2)  # Elements unique to list2: [6, 7]
