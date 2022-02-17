print ('find area of:- 1.Right angled triangle or 2. Find area of scalen triangle')
values=int(input('enter either 1 or 2  '))
if values == 1:
    height=float(input('enter height'))
    base=float(input('enter base'))
    print(0.5*height*base)
elif values == 2:
    side1=float(input('enter length of 1st side '))
    side2=float(input('enter length of 2nd side '))
    side3=float(input('enter length of 3rd side '))
    s=0.5*(side1+side2+side3)
    area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
    print(area)
else:
    print ('enter a valid value either 1 or 2')    