def banner_message(message, banner = "-"):
    
    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(f"{line}\n")

print(f":\n{int}\n")

banner_message("Introspecting the Global Namespace")

print(f"globals():\n\n{globals()}\n")

a =42
print("a = 42")
print("Notice the variable 'a' now shows in the return\n")

print(f"globals():\n\n{globals()}\n")

print(f"The dictionary returned by globals() doesn't just represent the global namespace, it actually is the globals namespace!\n")

globals()['tau'] = 6.283185
print(f"globals()['tau'] = 6.283185:\n")

print(f"print(tau):\n{tau}\n")
print(f"print(tau / 2):\n{tau / 2}\n")

banner_message("Introspecting the Global Namespace")
print(f"locals():\n{locals()}\n")

def report_scope(arg):
    message = (f"The script {__name__} has finished")
    from pprint import pprint as pp
    x = 496
    pp(locals(), width=10)
    return message

print("See relative code for function to better understand the step that took place\n")
print(f"report_scope(42):")
print(report_scope(42))
