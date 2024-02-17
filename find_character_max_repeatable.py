st="gfjfgjgfjhhhhhhhhhhhhhhjjjjjjj"

# print([i for i, j in {s:st.count(s) for s in st}.items() if j == max({s:st.count(s) for s in st}.values())][0])

def mst_rptbl_chrr(st):
    return ([i for i, j in {s:st.count(s) for s in st}.items() if j == max({s:st.count(s) for s in st}.values())][0])

print(mst_rptbl_chrr(st))


