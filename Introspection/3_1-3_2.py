
def banner_message(message, banner = "-"):
    
    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(f"{line}\n")

print(f":\n{int}\n")

banner_message("Introspecting Objects")

a = 42
print(f"a = 42:\n")

print(f"dir(a):\n{dir(a)}\n")

print(f"getattr(a, 'denominator'):\n{getattr(a, 'denominator')}\n")

print(f"a.denominator):\n{a.denominator}\n")

print(f"getattr(a, 'conjugate'):\n{getattr(a, 'conjugate')}\n")

print(f"callable(getattr(a, 'conjugate')):\n{callable(getattr(a, 'conjugate'))}\n")

print(f"a.conjugate.__class__.__name__:\n{a.conjugate.__class__.__name__}\n")

try:
    print("Expecting Error when calling funtion on non-existent field")
    print(f"getattr(a, 'index'):")
    print(f"{getattr(a, 'index')}")
except Exception as e:
    print(e)
    pass

print("")
print(f"hasattr(a, 'bit_length')\n{hasattr(a, 'bit_length')}\n")
print(f"hasattr(a, 'length')\n{hasattr(a, 'length')}\n")

