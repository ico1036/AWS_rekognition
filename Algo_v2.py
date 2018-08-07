fhandle = open("pesudodata2.txt")


data=list()
name=list()
default_time=3

# Define dataset 2-D list 
for line in fhandle:
    line=line.strip()
    data.append(line.split())

# Define default name 1-D list
for i in range(default_time):
	name.append(data[i][1])
default = list(set(name))

# Search special timestamp
for i in range(len(data)):
	if data[i][1] not in default:
		print(data[i])
 


		
