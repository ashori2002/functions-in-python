
def test1():
    print("Hello world!")

test1()
###################################################################
def test2(name):
    print(f"Welcome {name}")

test2(input())
####################################################################
def test3(name):
    print(f"Welcome {name}")

name="mohammad"

test3(name)
####################################################################
def test4(first_name , last_name):
    print(f"Welcome {first_name} {last_name}")

#test4(input("Whats your first name?"),input("Whats your last name?"))
F_N=input("Whats your first name?")
L_N=input("Whats your last name?")
test4(F_N , L_N)
