a=[[1],[2],[4,4],[1],[44],[4,4],[4]]

b_set = set(map(tuple,a))
print(b_set)
b = map(list,b_set)
b.sort()
print(b)
