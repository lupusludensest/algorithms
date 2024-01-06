# find min and max and second min and max elements of the list

l = [0, 99, -99, 7, -7, 5, 4, 3]

def mn_mx_smn_smx(l):
    mn = mx = l[0]
    smn = smx = l[1]

    for i in l:
        if i < mn:
            mn, smn = i, mn
        elif i > mx:
            mx, smx = i, mx
        elif mn < i < smn:
            smn = i
        elif mx > i > smx:
            smx = i

    return mn, mx, smn, smx

print(mn_mx_smn_smx(l))
