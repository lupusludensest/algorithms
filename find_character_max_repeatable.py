# find the most repeatable char in the string

s = "gfjfgjgfjhhhhhhhhhhhhhhjjjjjjj"
def mst_rptbl_chrr(st):
    # return ([i for i, j in {s:st.count(s) for s in st}.items() if j == max({s:st.count(s) for s in st}.values())][0])
    return max(sorted(list(s)), key=sorted(list(s)).count)

print(mst_rptbl_chrr(s))


