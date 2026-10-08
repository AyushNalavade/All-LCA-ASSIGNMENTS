#Assignment 1

student_list=["Amit","Priya","Rahul"]
student_list.append("Ishaan")
print(student_list)
student_list.remove("Amit")
print(student_list)
student_list[1]="Isha"
print(student_list)

student_tuple=("Aaryan","Rohan","Sneha")
converted_list=list(student_tuple)
converted_list.append("Ishita")
student_tuple=tuple(converted_list)
print(student_tuple)
converted_list.remove("Rohan")
student_tuple=tuple(converted_list)
print(student_tuple)
converted_list[1]="Aniket"
student_tuple=tuple(converted_list)
print(student_tuple)

student_dict={20:"Amit",21:"Priya",22:"Rahul"}
student_dict[23]="Ishaan"
print(student_dict)
del student_dict[22]
print(student_dict)
student_dict.update({22:"Sneha",23:"Ayush"})
print(student_dict)
              
