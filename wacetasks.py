# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#return max k such that k and -k are in the array
def solution(A):
    # write your code in Python 3.6
    maxSoFar = 0
    for x in A:
        y = x *-1
        if y in A:
            if abs(y)>maxSoFar:
                maxSoFar = abs(y)
                A.remove(y)
        A.remove(x)
		
    return maxSoFar
	
#return how many character removals are needed to make it so all letters have an even number of each
import string
def solution(S):
    # write your code in Python 3.6
    
    letters = string.ascii_lowercase
    removalsNeeded = 0
    
    for x in range (0,26):
        letter = letters[x]
        if S.count(letter) % 2 == 1:
           removalsNeeded+=1 

    return removalsNeeded
    
#insert '5' into a given number so that it is the laregest possible number it can be (negative inputs are possible)
 you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    S = str(N)
    if (N<0):
        for i in range(1,len(S)):
            compareWith = int(S[i])
            if compareWith >5:
                newN = S[0:i]+"5"+S[i:]
                N = int(newN) 
                break
        if str(N)==S:
            S+="5"
            N=int(S)
    else:
        for i in range(0,len(S)):
            compareWith = int(S[i])
            if compareWith <5:
                newN = S[0:i]+"5"+S[i:]
                N = int(newN) 
                break
        if str(N)==S:
            S+="5"
            N=int(S)
        
    return N

    
	