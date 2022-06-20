def banner_message(message, banner = "-"):
    
    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(f"{line}\n")

print(f":\n{int}\n")
banner_message("Introspecting types")
i = 7
print(f" i = {i}\n")

print(f"type(i):\n{type(i)}\n" )

print("returning 'int' at the repl will produce the same thing as repr(int)\n")
print(f"repr(int):\n{repr(int)}\n")

print(f"type(i) is int:\n {type(i) is int}\n")

print(f"type(i)(78):\n{type(i)(78)}\n")

print(f"type(type(i)):\n{type(type(i))}")
print(f"i.__class__:\n{i.__class__}")
print(f"i.__class__.__class__:\n{i.__class__.__class__}")
print(f"i.__class__.__class__.__class__:\n{i.__class__.__class__.__class__}\n")

print(f"type(type(int)):\n{type(type(int))}")

banner_message(f"issubclasss()")
print("Determines if its first arguement is a subclass of the second\n")

print("The Second argument can be a single class\n")

print("Or it can be a tuple of classes")
print("Then it checks if its first arguement is a subclass of any of the elements of the second\n")

print(f"issubclass(type, object):\n{issubclass(type, object)}\n")

print(f"type(object):\n{type(object)}\n")

banner_message(f"isinstance")

print("Determines if its first arguerment is an instance of a class")
print("The first arguement can be an object of any type\n")

print("The second arguement can be a single class or a tuple of classes\n")

print("When type checks are necessary, prefer isinstance() and issubclass() over direct comparision of type objects\n")

print(f"isinstance(i, int):\n{isinstance(i, int)}\n")