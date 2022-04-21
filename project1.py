#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy 


# In[2]:


mycolor = [[74,188,35,179,255,255],
          [113,91,139,179,255,255],
          [59,107,98,86,250,223],
          [0,161,187,179,218,255]]
colorval=[[255,153,51],
          [102,102,255],
          [0,255,0],
          [0,128,255]]
points=[]


# In[3]:


def findcolor(img,mycolor,colorval):
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    newpoints=[]
    for color in mycolor:
        lower = numpy.array(color[0:3])
        upper = numpy.array(color[3:6])
        mask  = cv2.inRange(imghsv,lower,upper)
        x,y=getcountour(mask)
        cv2.circle(imgres,(x,y),10,colorval[count],cv2.FILLED)
        if x!=0 and y!=0:
            newpoints.append([x,y,count])
        count+=1
        
    return newpoints


# In[4]:


def getcountour(img):
    countour,h=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in countour:
        area=cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgres,cnt, -1,(255,255,0), 3)
            peri=cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y
        


# In[5]:


def draw(points,colorval):
    for point in points:
        cv2.circle(imgres,(point[0],point[1]),10,colorval[point[2]],cv2.FILLED)
        


# In[6]:


vid = cv2.VideoCapture(0)
#vid.set(3,640)
#vid.set(4,240)
while True:
    success,img = vid.read()
    imgres =img.copy()
    newpoints= findcolor(img,mycolor,colorval)
    if len(newpoints)!=0:
        for np in newpoints:
            points.append(np)
    if len(points)!=0:
        draw(points,colorval)
    cv2.imshow("result", imgres)
    if cv2.waitKey(1)& 0XFF== ord('q'):
        break;


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




