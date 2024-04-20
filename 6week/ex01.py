myList = [1, 'a', [5, 6, 7]]
print(myList)
print((len(myList)))

print(myList[2][1])

numList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for n1 in numList:
    for n2 in n1:
        print(n2,end=' ')
    print(' ')

# for n1 in range(len(numList)):
#     for n2 in range(len(numList[n1])):
#         print(numList[n1][n2],end=' ')
#     print(' ')