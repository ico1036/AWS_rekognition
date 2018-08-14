fhandle = open('pesudodata2.txt')

data=[]

for line in fhandle:
	line=line.strip()
	data.append(line.split())

print(data)

'''
for i in range(1,len(data)):
		
	if data[i-1][0] != data[i][0]:
		print(data[i])
'''
