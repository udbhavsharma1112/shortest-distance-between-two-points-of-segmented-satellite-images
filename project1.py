
import cv2
import numpy 
from queue import Queue


img = cv2.imread("17878885_15.tiff") # example image



img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert into gray scale


for i in range(1500):
    for j in range(1500):
        if img[i][j]>0:
            img[i][j]=1


def valid(i,j):
    if i<0 or j<0 or i>=1500 or j>=1500:
        return 0
    return 1


q = Queue()
INF=1000000001
st=[1133,872]   #starting point example
en=[666,253]    #ending point
dx=[0,0,1,-1]
dy=[1,-1,0,0]
dis=[]
for i in range(1501):
    col=[]
    for j in range(1501):
        col.append(INF)
    dis.append(col)
path={}
q.put(st)
dis[st[0]][st[1]]=0


for i in range(1501):
    for j in range(1501):
        sit=str(i)+' '+str(j)
        path[sit]=sit


h=0
while q.empty()==False:
    x=q.get()
    for i in range(4):
        nx=x[0]+dx[i]
        ny=x[1]+dy[i]
        if valid(nx,ny):
            if dis[nx][ny]>dis[x[0]][x[1]]+1 and img[nx][ny]==1:
                dis[nx][ny]=dis[x[0]][x[1]]+1
                q.put([nx,ny])
                s1t=str(nx)+' '+str(ny)
                stt=str(x[0])+' '+str(x[1])
                path[s1t]=stt
                h+=1
            
            
        
dis[en[0]][en[1]]
s2t=str(en[0])+' '+str(en[1])



path[s2t]




path['667 253']


# In[36]:



ans=[]
ans.append(en)
while path[s2t]!=s2t:
    s2t=path[s2t]
    inp = list(map(int, s2t.split()))
    ans.append(inp)



imgres = cv2.imread("img.tiff")
ans.reverse()
len(ans)


for i in range(len(ans)):
    cv2.circle(imgres,(ans[i][1],ans[i][0]),10,(255,0,0),cv2.FILLED)



cv2.imshow("final",imgres)
cv2.waitKey(0)




