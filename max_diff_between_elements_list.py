# max diff between elements list

l_a = [8, 7, 1, 2, 6, 9]

def mx_dfr(l_a):
	mn = l_a[0]
	mx = 0
	for i in range(1, len(l_a)):
		mn = min(mn, l_a[i])
		mx = max(mx, l_a[i] - mn)
	return mx
	
print(mx_dfr(l_a))

def bg_df(l_a):
	mn = l_a[0]
	mx_df = 0
	for i in l_a[1:len(l_a)]:
		mn = min(mn, i)
		mx_df = max(mx_df, i - mn)

	return mx_df

print(bg_df(l_a))


