def eulerCycle(graph):
    checkedList = []
    #Gets all connections and puts them in checkedList
    for i in range(len(graph)):
        for b in range(len(graph[i])):
            if( graph[i][b]==1 ) : checkedList.append([i,b])


    index2 = 1
    ties=[]
    indicator = False
    sortedcheckedList = [checkedList.pop(0)]
    numberOfIterations =0
    while(len(checkedList)!=0):
        if(len(sortedcheckedList)==0):
            sortedcheckedList = [checkedList.pop(0)]
            l = sortedcheckedList[len(sortedcheckedList)-1][index2]
        else:
            l = sortedcheckedList[len(sortedcheckedList) - 1][index2]
        oldCheckedListLength = len(checkedList)

        for n in range (len(checkedList)-1) :
            if(checkedList[n][0]==l and checkedList[n][1] ==l) :
                sortedcheckedList.append(checkedList.pop(n))

        for i in range (len(checkedList)) :
           if(checkedList[i][0] == l) :
                sortedcheckedList.append(checkedList.pop(i))

                break
        if(oldCheckedListLength == len(checkedList)) :
            checkedList.append(sortedcheckedList.pop(len(sortedcheckedList) - 1))
            checkedList.append(sortedcheckedList.pop(len(sortedcheckedList) - 1))

        numberOfIterations+=1
        if(numberOfIterations > 1000):
            for d in range(len(sortedcheckedList)-2):
                if(sortedcheckedList[d][0] == sortedcheckedList[d][1]):
                    ties.append(sortedcheckedList.pop(d))
            for d in range (len(checkedList)-2):
                if(checkedList[d][0]==checkedList[d][1]):
                    ties.append(checkedList.pop(d))
        if (numberOfIterations > 2000):
            sortedcheckedList = "У графа  нема Ейлерового циклу"
            indicator = True
            break


    print("Ейлерів цикл: ", sortedcheckedList)
    print(ties)


    if(indicator):
        printCircuit(graph)

def printCircuit(adj):
    print('Ейлерів шлях: ')
    if len(adj) == 0:
        return
    curr_path = [0]
    circuit = []
    while curr_path:
        curr_v = curr_path[-1]
        if adj[curr_v]:
            next_v = adj[curr_v].pop()
            curr_path.append(next_v)
        else:
            circuit.append(curr_path.pop())

    for i in range(len(circuit) - 1, -1, -1):
        print(circuit[i], end="")
        if i:
            print(" -> ", end="")
    print('\n')







