#print the output of while loop in the same line 
# i=1
# while i<4:
#     print(f"Hellow Tony {i}", end=" ")
#     i+=1

#print star pattern using loops 
# n=5
# for i in range(1,n+1):     #for rows 
#     for j in range(1,i+1): #for coloums
#         print("*",end="")
#     print()

n=5
for i in range(0,n+1):
    for j in range(1,i):
        print("*",end="")
    print()