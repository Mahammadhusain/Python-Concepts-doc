# Python Deep copy & shallow copy

---- > Shallow copy makes a new object but reference is an original object (affected the original object)
---- > Deep copy makes a new object with a new reference (not affecting the original object)


# ------------------- EXAMPLE -------------------
import copy
# Shallow copy example
original_list = [1, [2, 3,[9,10]], 4]
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)
# Modify the first element of the shallow copy
shallow_copy[1][0] = "C"
shallow_copy[1][2].append("P") 
# Both the original and shallow copy will reflect the change
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)
