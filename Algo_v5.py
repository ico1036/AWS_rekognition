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

dict={}
for i in data:
	if i[0] not in dict.keys():
		dict[i[0]]=[]
	dict[i[0]].append(i[1])
x=sorted(dict.items())
print("############ data ################")
print(x)

# Define default name 1-D list
for i in range(default_time):
	for j in x[i][1]:
		name.append(j)
default = list(set(name))

# Search special timestamp
result=[]
sw=0
print(len(x))

for i in range(len(x)):
	for j in x[i][1]:
		if j not in default:
			if sw==0:	
				result.append(x[i-2:i])
				result.append(x[i:i+3])
				sw=1
			else:
				result.append(x[i:i+3])
print(result)
for i in range(1,len(result)-1):
	if result[i] == result[i-1]:
		del result[i]

print("############ result ##############")
time_result=[]
for i in range(len(result)):
	for j in range(len(result[i])):
		time_result.append(result[i][j][0])

print("####### conserved time-data #######")
print(result)
print("####### conserved time #######")
print(time_result)
		
