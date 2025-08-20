Angle1=int(input("enter Angle1: "))
Angle2=int(input("enter Angle2: "))
Angle3=int(input("enter Angle3: "))
if Angle1==90 or Angle2==90 or Angle3==90:
    print("it is a right angle")
elif Angle1>90 or Angle2>90 or Angle3>90:
    print("it is not a obsute angle")
elif Angle1<90 or Angle2<90 or Angle3<90:
    print("it is a Acute angle")
else:
    print("invalid triangle")