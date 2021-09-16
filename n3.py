numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
signs = {'-', '+'}

def res(i):
    if ((us_in[i] in signs and us_in[i+1] in signs) 
    # '2++12--3'
        or (us_in[i] not in numbers and us_in[i] not in signs)):
    # 'hello+12'
        return False, None
    if i == len(us_in)-2:
        if us_in[i+1] not in signs and us_in[i+1] not in numbers:
            return False, None
        else:
            return True, eval(us_in)
            # '1+2+4-2+5-1', '123'
    return res(i+1)

us_in = str(input("us_in: "))
if (us_in[0] in signs) or (us_in[len(us_in) - 1] in signs) or (us_in == ""):
# ''
    print((False, None))
    exit(1)
print("result:", res(0))
