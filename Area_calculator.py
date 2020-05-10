#first of all I will begin with taking valid inputs from user
#This should include whether it's a Circle or a Triangle
Object= (str(input("Enter C for circle and T for Triangle:    "))
if(Object==C):
  r= float(input("Enter the Radius"))
  area= 3.14 * r *r
  print("Area:",area)
elif(Object==T):
  base=float(input("ENter the value of base"))
  height=float(input("Enter the value of Height"))
  Area= 1/2 * base * height
  print("Area:",Area)
