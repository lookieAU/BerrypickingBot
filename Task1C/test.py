import cv2
import numpy as np
import os, sys
import traceback
import sim
import time
sim.simxFinish(-1)
client_id = sim.simxStart('127.0.0.1',19997,True,True,5000,5)
return_code=sim.simxStartSimulation(client_id,sim.simx_opmode_oneshot)
'''
err_code,ps_handle = sim.simxGetObjectHandle(client_id,"distance_sensor_1", sim.simx_opmode_blocking)
err_code,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.simxReadProximitySensor(client_id,ps_handle,sim.simx_opmode_streaming)
distance=np.linalg.norm(detectedPoint)
print(distance)
'''
return_code,detectionState1,detectedPoint1,detectedObjectHandle1,detectedSurfaceNormalVector1=sim.simxReadProximitySensor(client_id,34,sim.simx_opmode_streaming)
distance1=np.linalg.norm(detectedPoint1)
print(distance1)
print(detectionState1)
c=0
return_code,diff_handle=sim.simxGetObjectHandle(client_id,'Diff_Drive_Bot_Visible',sim.simx_opmode_blocking)
return_code,eulerAngles=sim.simxGetObjectOrientation(client_id,diff_handle,-1,sim.simx_opmode_blocking)
print(abs(eulerAngles[2])*180/3.14)
#print(eulerAngles)
#lj=sim.simxGetObjectHandle(client_id, 'left_joint', sim.simx_opmode_blocking)
#rj=sim.simxGetObjectHandle(client_id, 'right_joint', sim.simx_opmode_blocking)
#print(lj)
#time.sleep(12)
while(1):
    #return_code,ps_handle = sim.simxGetObjectHandle(client_id,"distance_sensor_1", sim.simx_opmode_blocking)
    #return_code,ps_handle2=sim.simxGetObjectHandle(client_id,'distance_sensor_2',sim.simx_opmode_blocking)
    return_code,detectionState1,detectedPoint1,detectedObjectHandle1,detectedSurfaceNormalVector1=sim.simxReadProximitySensor(client_id,34,sim.simx_opmode_blocking)
    return_code1,detectionState2,detectedPoint2,detectedObjectHandle2,detectedSurfaceNormalVector2=sim.simxReadProximitySensor(client_id,35,sim.simx_opmode_blocking)
    distance1=np.linalg.norm(detectedPoint1)
    distance2=np.linalg.norm(detectedPoint2)
    print(distance2)
    print(distance1)
    #print(detectionState)
    #time.sleep(1)
    #c+=1
    return_code,eulerAngles=sim.simxGetObjectOrientation(client_id,diff_handle,-1,sim.simx_opmode_streaming)
    print('Euler',abs(eulerAngles[2])*180/3.14)
    if(detectionState1==False and distance1>0.15):
        sim.simxSetJointTargetVelocity(client_id,21,+0.2648,sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(client_id,24,+0.2648,sim.simx_opmode_streaming)
    #if(detectionState1==True and distance1<=0.15):
        #if(detectionState1==False and distance2<=0.14):
            #sim.simxSetJointTargetVelocity(client_id,21,+0.6648,sim.simx_opmode_streaming)
            #sim.simxSetJointTargetVelocity(client_id,24,+0.6648,sim.simx_opmode_streaming)
    if(detectionState1==True and distance1<=0.15):
        c+=1 
        if(c==1):
            while((abs(eulerAngles[2])*180/3.14)<88):
                return_code,eulerAngles=sim.simxGetObjectOrientation(client_id,diff_handle,-1,sim.simx_opmode_buffer)
                print('Euler',abs(eulerAngles[2])*180/3.14)
                sim.simxSetJointTargetVelocity(client_id,21,-0.0648,sim.simx_opmode_streaming)
                sim.simxSetJointTargetVelocity(client_id,24,+0.0648,sim.simx_opmode_streaming)
        elif(c==2):
            while((abs(eulerAngles[2])*180/3.14)<179):
                return_code,eulerAngles=sim.simxGetObjectOrientation(client_id,diff_handle,-1,sim.simx_opmode_buffer)
                print('Euler',abs(eulerAngles[2])*180/3.14)
                sim.simxSetJointTargetVelocity(client_id,21,-0.0648,sim.simx_opmode_streaming)
                sim.simxSetJointTargetVelocity(client_id,24,+0.0648,sim.simx_opmode_streaming)
        elif(c==3):
            while((abs(eulerAngles[2])*180/3.14)>92):
                return_code,eulerAngles=sim.simxGetObjectOrientation(client_id,diff_handle,-1,sim.simx_opmode_buffer)
                print('Euler',abs(eulerAngles[2])*180/3.14)
                sim.simxSetJointTargetVelocity(client_id,21,-0.0648,sim.simx_opmode_streaming)
                sim.simxSetJointTargetVelocity(client_id,24,+0.0648,sim.simx_opmode_streaming)
        elif(c==4):
            sim.simxStopSimulation(client_id,sim.simx_opmode_oneshot)
            sim.simxGetPingTime(client_id)
            sim.simxFinish(client_id)
            break
        

    #if(detectionState1==True and distance1<=0.25):
        
    
    #print(eulerAngles)
    #time.sleep(1)

    #if(c==10):
        #break
        
    
    #time.sleep(1)
        
    
'''
emptyBuff=bytearray()
return_code,ints,floats,strings,outBuffer=sim.simxCallScriptFunction(client_id,'distance_sensor_1',sim.sim_scripttype_customizationscript,'getDistance',[],[],[],emptyBuff,sim.simx_opmode_blocking)
return_code=sim.simxStopSimulation(client_id,sim.simx_opmode_oneshot)
print(ints)
print(floats)
print(strings)
'''
#time.sleep(5)
#sim.simxGetPingTime(client_id)
#sim.simxFinish(client_id)