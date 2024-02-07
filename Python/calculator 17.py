print('''
ADDITION +
DIVISION -
MULTIPLE *
DIVISION /
modules %
''')
p1=eval(input("Enter a value:-"))
p2=eval(input("Enter a value:-"))
opr=input("Enter oper...(+,-,*,/)")
if opr=="+":
    print(p1+p2)
elif opr=="-":
    print(p1-p2)
elif opr=="*":
    print(p1*p2)
elif opr=="/":
    print(p1/p2)
elif opr=="%":
    print(p1%p2)
else:
    print("invlid opr")

