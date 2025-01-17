# T(N) = O(N)
# S(N) = O(N)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses==0:   # 0 courses return True
            return true
        st=[]
        temp=[0 for i in range(numCourses)]
        di={}
        for li in prerequisites:
            temp[li[0]]+=1
            if li[1] in di:       
                di[li[1]].append(li[0])
            else:
                di[li[1]]=[li[0]]
        for i in range(numCourses):
            if temp[i]==0:
                st.append(i)
        print(temp)
        print(di)
        while st:
            te=st.pop()
            
            if te in di:
                
                for i in di[te]:
                    temp[i]-=1
                    if temp[i]==0:
                        st.append(i)
        print(temp)
        for i in temp:
            if i!=0:
                return False
        return True
            
        
            
        