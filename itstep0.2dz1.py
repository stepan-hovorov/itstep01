name = input("Enter your name: ")
security_level = 5
if security_level >= 3:
    print(f"Access granted, {name}")
else:
    print(f"Access denied, {name}")