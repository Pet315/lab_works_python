us_in = input("user_input: ")
signs = "+-"

def recurs(x):
    if us_in == "" or not us_in[0].isdigit() or not us_in[len(us_in) - 1].isdigit(): # digit should be in the beginning and in the end
        return 0
    elif not us_in[x].isdigit() and us_in[x] not in signs: # not sign and not digit
        return 0
    elif us_in[x] in signs and us_in[x+1] in signs: # 5++3---
        return 0
    if x == len(us_in) - 1:
        return 1
    return recurs(x+1)


if recurs(0) == 1:
    print("True,", eval(us_in))
else:
    print("False, None")