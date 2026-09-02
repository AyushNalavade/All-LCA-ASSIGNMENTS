# Program to perform Add, Delete and Update
# operations on List, Tuple and Dictionary

# ---------------- LIST ----------------

students_list = ["Rahul", "Amit", "Sneha", "Priya"]

print("Original List:")
print(students_list)

# Add
students_list.append("Rohan")
print("\nAfter Adding Rohan:")
print(students_list)

# Delete
students_list.remove("Amit")
print("\nAfter Deleting Amit:")
print(students_list)

# Update
students_list[1] = "Neha"
print("\nAfter Updating:")
print(students_list)


# ---------------- TUPLE ----------------

students_tuple = ("Rahul", "Amit", "Sneha", "Priya")

print("\nOriginal Tuple:")
print(students_tuple)

# Add using concatenation
students_tuple = students_tuple + ("Rohan",)
print("\nAfter Adding Rohan:")
print(students_tuple)

# Delete using slicing
students_tuple = students_tuple[:1] + students_tuple[2:]
print("\nAfter Deleting Amit:")
print(students_tuple)

# Update by creating a new tuple
students_tuple = ("Rahul", "Neha", "Sneha", "Priya", "Rohan")
print("\nAfter Updating:")
print(students_tuple)


# ---------------- DICTIONARY ----------------

students_dict = {
    101: "Rahul",
    102: "Amit",
    103: "Sneha",
    104: "Priya"
}

print("\nOriginal Dictionary:")
print(students_dict)

# Add
students_dict[105] = "Rohan"
print("\nAfter Adding Rohan:")
print(students_dict)

# Delete
students_dict.pop(102)
print("\nAfter Deleting Amit:")
print(students_dict)

# Update
students_dict[103] = "Neha"
print("\nAfter Updating:")
print(students_dict)
