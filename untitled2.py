w=float(input("enter weight:"))
h=float(input("enter hight:"))
b=w/(h**2)
if b<=18.5:
    print("underweight")
elif 18.5<b<=25:
    print("normalweight")
elif 25<b<=30:
    print("slightlyoverweight")
elif 30<b<=35:
    print("obese")
else:
    print("clinicaly obese")