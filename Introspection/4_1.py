def banner_message(message, banner = "-"):
    
    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(f"{line}\n")

print(f":\n{int}\n")

banner_message("Introspecting the Global Namespace")
print(f"globals():\n\n{globals()}\n")