print('''
ADDITION +
SUBTRACT -
MULTIPLE *
DIVISION /
MODULES %
''')
R1=eval(input("Enter first number:-"))
R2=eval(input("Enter second number:-"))
opr=(input("Enter opr=(+,-,*,/)"))
if opr == "+":
    print(R1+R2)
elif opr == "-":
    print(R1-R2)
elif opr == "*":
    print(R1*R2)
elif opr == "/":
    print(R1/R2)
elif opr == "%":
    print(R1%R2)
else:
    ("invalid opr")