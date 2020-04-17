from collections import defaultdict,deque

cityCode = []
graph = []      #Graph: LINKED CITIES
vTable = []     #VISITED TABLES
prev = []       #LINK TO PREVIOUS NODE (BACKTACK NODE TO DISPLAY SHORTEST PATH)
adjList = defaultdict(list)
q = deque()

#Generate: CITY CODE
print 'City List: ',
print 'Enter Cities in order:    A  B  C  D.....'
while len(cityCode) < 3:
    print 'Enter Cities for GRAPH: ',
    city = raw_input().upper()
    cityCode = map(str,city.split())
    if len(cityCode) < 3:
        print 'Atlease 3 Cities must be entered.\n\n'


#LINK CITIES
print 'LINK Cities: (True/False)'
for i in range(len(cityCode)):
    for j in range(len(cityCode)):
        if i < j:
            print '{0} - {1}: '.format(cityCode[i],cityCode[j]),
            lCheck = raw_input().capitalize()
            if lCheck == 'True':
                graph.append([i,j])

for edge in graph:
    adjList[edge[0]].append(edge[1])
    adjList[edge[1]].append(edge[0])

for edge in range(10):      #Initialize Visited Table[vTable] and prev
    vTable.append(False)
    prev.append(-1)

#Calculate: SHORTEST PATH
s = cityCode.index(raw_input('Enter Source: ').upper())
q.append(s)
vTable[s] = True
while q:
    u = q.popleft()
    for i in adjList[u]:
        if vTable[i] == False:
            q.append(i)
            vTable[i] = True
            prev[i] = u

#Display: PATH COST & PATH
count = 0
itr = []
v = cityCode.index(raw_input('Enter Destination: ').upper())
while prev[v] != -1:
    itr.append(v)
    v = prev[v]
    count += 1

print 'Path: {0}'.format(cityCode[s]),
for value in reversed(itr):
    print ' ---> ',cityCode[value],
print '\nPath Cost: ',count

############################ SAMPLE - OUTPUT ########################
'''
City List:
Enter Cities in order:    A  B  C  D.....
Enter Cities for GRAPH:  pune mumbai patna delhi
LINK Cities: (True/False)
PUNE - MUMBAI:  true
PUNE - PATNA:  false
PUNE - DELHI:  false
MUMBAI - PATNA:  false
MUMBAI - DELHI:  true
PATNA - DELHI:  true
Enter Source: pune
Enter Destination: patna
Path: PUNE ---> MUMBAI --->  DELHI --->  PATNA
Path Cost:  3
'''