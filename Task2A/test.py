import sim
import cv2
import numpy as np
import os, sys
import traceback
import time
sim.simxFinish(-1)
client_id = sim.simxStart('127.0.0.1',19997,True,True,5000,5)
sim.simxStartSimulation(client_id,sim.simx_opmode_oneshot)
return_code,vhandle=sim.simxGetObjectHandle(client_id,'vision_sensor_1',sim.simx_opmode_blocking)
print(vhandle)
return_code,imgres,imgarr=sim.simxGetVisionSensorImage(client_id,15,0,sim.simx_opmode_streaming)
return_code,vhandle=sim.simxGetObjectHandle(client_id,'vision_sensor',sim.simx_opmode_blocking)
return_code,imgres,imgarr=sim.simxGetVisionSensorImage(client_id,15,0,sim.simx_opmode_buffer)
return_code,vhandle=sim.simxGetObjectHandle(client_id,'vision_sensor',sim.simx_opmode_blocking)
return_code,depthres,bufferarr=sim.simxGetVisionSensorDepthBuffer(client_id,15,sim.simx_opmode_streaming)
return_code,vhandle=sim.simxGetObjectHandle(client_id,'vision_sensor',sim.simx_opmode_blocking)
return_code,depthres,bufferarr=sim.simxGetVisionSensorDepthBuffer(client_id,15,sim.simx_opmode_buffer)
#print(bufferarr)
buffernp=np.array(bufferarr,dtype=np.float64)
imgnp=np.array(imgarr,dtype=np.uint8)
#print(imgarr)
#print(buffernp)
#print(depthres)
buffernp.resize([depthres[0],depthres[1]])
imgnp.resize([imgres[0],imgres[1],3])
imgnp=cv2.cvtColor(imgnp,cv2.COLOR_BGR2RGB)
flippedimg=cv2.flip(imgnp,0)
flippedbuffer=cv2.flip(buffernp,0)
hsv=cv2.cvtColor(flippedimg,cv2.COLOR_BGR2HSV)
gray=cv2.cvtColor(flippedimg,cv2.COLOR_BGR2GRAY)
colours=['Blueberry','Strawberry','Lemon']
lowrange=[[110,50,50],[159,50,70],[25,50,50]]
highrange=[[130,255,255],[180,255,255],[32,255,255]]
return_code,thres = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
contours,return_code = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print(contours)
c=0
#print(flippedbuffer)
berries_dictionary={'Strawberry':[],'Blueberry':[],'Lemon':[]}
berry_position_dictionary={'Strawberry':[],'Blueberry':[],'Lemon':[]}
for contour in contours:
    '''if(c==0):
        c=1
        continue'''
    M=cv2.moments(contour)
    if(M['m00']!=0.0):
        x=int(M['m10']/M['m00'])
        y=int(M['m01']/M['m00'])
    for i in range(0,3):
        mask=cv2.inRange(hsv,np.array(lowrange[i]),np.array(highrange[i]))
        if(mask[y,x]==255):
            berrytype=colours[i]
    #print(berrytype)
    for i in range(1,imgres[1]):
        for j in range(1,imgres[0]):
            '''if(i==x and j==y):
                z1=bufferarr[i*depthres[0]+j]
                z2=bufferarr[i+j*depthres[0]]
                z3=bufferarr[i*depthres[1]+j]'''
            if(i==y and j==x):  
                #print(i*j)
                z=flippedbuffer[i][j]
    #print(x,y,z)
    
    #print("3D coordinates: ")
    newx=-0.5+(x/512)*(0.5+0.5)
    newy=-0.5+(y/512)*(0.5+0.5)
    newz=0.01+z*2
    #print(newx,newy,newz)
    berries_dictionary[berrytype].append((round(x,3),round(y,3),round(z,3)))
    berry_position_dictionary[berrytype].append((round(newx,3),round(newy,3),round(newz,3)))
print("Berries Dictionary: ",berries_dictionary)
print("Berry Positions Dictionary: ",berry_position_dictionary)



'''cv2.imshow('img',flippedbuffer)
cv2.imshow('vision',flippedimg)

cv2.waitKey(0)'''

    

#time.sleep(10)
sim.simxGetPingTime(client_id)
sim.simxStopSimulation(client_id,sim.simx_opmode_oneshot)
sim.simxFinish(client_id)
#cv2.destroyAllWindows()

#cv2.imshow('vision',imgnp)


