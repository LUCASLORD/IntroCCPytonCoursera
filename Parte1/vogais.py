def vogal(v):
    v = v.upper()
    if (v == "A") or (v == "E") or (v == "I") or (v == "O") or (v == "U"):
        return True
    else:
        return False

print(vogal("a"))