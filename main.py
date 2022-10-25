ts = [-1, 1, -3, 4, 9, 77, 12]

def compute_closest_to_zero(ts):
    closest_to = 10000
    closest_to_minus = -10000
    if len(ts) == 0:
        return 0
    else:
        for i in ts:
            if i < closest_to and i >-1:
                closest_to = 1
            elif i < 1 and i > closest_to_minus:
                closest_to_minus = i
    ans = 10000
    #if two numbers are positive and negative but are same distance from zero take the positive
    if closest_to == (closest_to_minus*-1):
        ans = closest_to
    elif closest_to < (closest_to_minus*-1):
        ans = closest_to
    elif closest_to > (closest_to_minus*-1):
        ans = closest_to_minus
    return ans

print(compute_closest_to_zero(ts))
