for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
        i-=1
    print()

'''
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 


'''

'''

More optimised
for i in range(1,6):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()
'''