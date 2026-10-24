name = input("Enter your name: ")
security_level = int(input(f"Enter your security level: "))
if security_level >= 3:
    print(f"Access granted, {name}")
else:
    print(f"Access denied, {name}")