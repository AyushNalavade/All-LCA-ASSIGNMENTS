def right_triangle(side1,side2,side3):
  sides=sorted([side1,side2,side3])
  if sides[0]**2 + sides[1]**2==sides[2]**2:
    return True
  else:
    return False
a=int(input("Enter length of first side:"))
b=int(input("Enter length of second side:"))
c=int(input("Enter length of third side:"))
if right_triangle(a,b,c)==True:
  print("The triangle is a right angled triangle")
else:
  print("The triangle is not a right angled triangle")
  
