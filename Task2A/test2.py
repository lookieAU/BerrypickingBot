import sim
import cv2
import numpy as np
import os, sys
import traceback
import time
sim.simxFinish(-1)
client_id = sim.simxStart('127.0.0.1',19997,True,True,5000,5)
sim.simxStartSimulation(client_id,sim.simx_opmode_oneshot)
return_code,vhandle=sim.simxGetObjectHandle(client_id,'vision_sensor',sim.simx_opmode_blocking)
return_code,imgres,imgarr=sim.simxGetVisionSensorImage(client_id, vhandle, 0, sim.simx_opmode_streaming)
return_code,vhandle=sim.simxGetObjectHandle(client_id,'vision_sensor',sim.simx_opmode_blocking)
return_code,imgres,imgarr=sim.simxGetVisionSensorImage(client_id, vhandle, 0, sim.simx_opmode_buffer)
#print(imgarr)
imgarr=np.array(imgarr,dtype=np.float32)
imgarr=np.resize(imgarr, [imgres[0],imgres[1],3])
cv2.imshow('window', imgarr)


time.sleep(10)
sim.simxGetPingTime(client_id)
sim.simxStopSimulation(client_id,sim.simx_opmode_oneshot)
sim.simxFinish(client_id)