# 单调栈

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        leftMins, rightMins= [0]*len(arr), [0]*len(arr)
        
        st = []
        for i, num in enumerate(arr):
            while st and arr[st[-1]] > num:
                st.pop()
            if len(st) == 0:
                leftMins[i] = -1
            else:
                leftMins[i] = st[-1]
            st.append(i)
        
        st = []
        for i in range(len(arr)-1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if len(st) == 0:
                rightMins[i] = len(arr)
            else:
                rightMins[i] = st[-1]
            st.append(i)
        
        ans = 0
        for i in range(len(arr)):
            ans = (ans + arr[i] * (i - leftMins[i]) * (rightMins[i] - i)) % (1e9 + 7)
        
        return int(ans)