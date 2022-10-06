#User function Template for python3

class Solution:
    def divide(self, a, b):
        #code here
        sign = 1
        if a < 0:
           sign *= -1
           a = -a
        if b < 0:
           sign *= -1
           b = -b
        return (a//b)*sign


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        ob=Solution()
        
        print(ob.divide(a,b))
        
# } Driver Code Ends
