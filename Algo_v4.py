fhandle = open("pesudodata3.txt")
# timestamp1 name1
# timestamp2 name2
# timestamp3 name3
#1 a
#1 b-> {1 ,[a,b]} 
#2 c
#3 d

data=list()
name=list()
default_time=4

# Define dataset 2-D list 
for line in fhandle:
	line=line.strip()
	tmp=line.split()
	tmp[0]=int(tmp[0])
	data.append(tmp)

print(data)

dict={}
for i in data:
	if i[0] not in dict.keys():
		dict[i[0]]=[]
	dict[i[0]].append(i[1])
x=sorted(dict.items())
print(x)

# Define default name 1-D list
for i in range(default_time):
	for j in x[i][1]:
		name.append(j)
default = list(set(name))

# Search special timestamp
for i in range(len(data)):
	if data[i][1] not in default:
		print(data[i])
		

		
