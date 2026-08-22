def triangle():
  s1=int(input("Enter the first side of the triangle:"))
  s2=int(input("Enter the second side of the triangle:"))
  s3=int(input("Enter the third side of the triangle:"))
  if s1==s2 and s2==s3:
    print("The triangle is equilateral")
  elif s1==s2 or s2==s3 or s1==s3:
    print("The triangle is isoceles")
  else:
    print("The triangle is scalene")
triangle()    
