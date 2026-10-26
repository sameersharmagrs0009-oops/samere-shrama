c= float (input("enter cost:"))
r= float (input("enter revenue:"))
if c==r:
    print("breakeven")
elif c>r:
    print("loss")
else:
    print("profit")