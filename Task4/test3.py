def qrdetect():
    return_code,imgres,imgarr=sim.simxGetVisionSensorImage(client_id,vhandle,0,sim.simx_opmode_blocking)
    imgnp=np.array(imgarr,dtype=np.uint8)
    imgnp.resize([imgres[0],imgres[1],3])
    imgnp=cv2.cvtColor(imgnp,cv2.COLOR_BGR2RGB)
    flippedimg=cv2.flip(imgnp,0)
    # cv2.imshow("Image",imgnp)
    # cv2.waitKey(0)1
    data=(0,0)
    qrcodes=decode(flippedimg)
    for qrcode in qrcodes:
        data=qrcode.data.decode("utf-8")
        data=ast.literal_eval(data)
        # print(data)
        # print(type(data))
    return data
def gostraight():
    sim.simxSetJointTargetVelocity(client_id,jointfl,3.5,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointfr,3.5,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointrl,3.5,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointrr,3.5,sim.simx_opmode_oneshot)
def rotateright():
    sim.simxSetJointTargetVelocity(client_id,jointfl,0.8,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointfr,-0.8,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointrl,0.8,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointrr,-0.8,sim.simx_opmode_oneshot)
def rotateleft():
    sim.simxSetJointTargetVelocity(client_id,jointfl,-0.8,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointfr,0.8,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointrl,-0.8,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointrr,0.8,sim.simx_opmode_oneshot)
def zerovel():
    sim.simxSetJointTargetVelocity(client_id,jointfl,0,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointfr,0,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointrl,0,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(client_id,jointrr,0,sim.simx_opmode_oneshot)

if __name__=="__main__":
    import cv2
    import numpy as np
    import math
    import time
    from pyzbar.pyzbar import decode
    import sim
    import ast
    sim.simxFinish(-1)
    client_id=sim.simxStart('127.0.0.1',19997,True,True,5000,5)
    sim.simxStartSimulation(client_id,sim.simx_opmode_oneshot)
    return_code,vhandle=sim.simxGetObjectHandle(client_id,'vision_sensor_1',sim.simx_opmode_blocking)
    # print(vhandle)
    # return_code,imgres,imgarr=sim.simxGetVisionSensorImage(client_id,vhandle,0,sim.simx_opmode_blocking)
    # print(imgarr)
    # print(imgres)
    return_code,jointfl=sim.simxGetObjectHandle(client_id,'rollingJoint_fl',sim.simx_opmode_blocking)
    return_code,jointfr=sim.simxGetObjectHandle(client_id,'rollingJoint_fr',sim.simx_opmode_blocking)
    return_code,jointrl=sim.simxGetObjectHandle(client_id,'rollingJoint_rl',sim.simx_opmode_blocking)
    return_code,jointrr=sim.simxGetObjectHandle(client_id,'rollingJoint_rr',sim.simx_opmode_blocking)
    # print(jointfl)
    # print(jointfr)
    # print(jointrl)
    # print(jointrr)
    # nav=(5,0)
    # x=nav[0]
    # y=nav[1]
    # print(y)
    zerovel()
    init=(0,0)
    navcoor=[(2,3),(3,6),(11,11),(0,0)]
    print("Navigation co-ordinates: ",navcoor)
    c=0
    for i in range(0,len(navcoor)):
        for j in range(0,(len(navcoor)-1)):
            if(navcoor[j][1]>navcoor[j+1][1]):
                store=navcoor[j]
                navcoor[j]=navcoor[j+1]
                navcoor[j+1]=store
                c+=1 
        if(c>0):
            c=0
        else:
            break


    data=qrdetect()
    # print(type(data[0]))
    # print(type(data[1]))
    a=data[0]
    for n in navcoor:
        x=n[0]
        y=n[1]
        # print(x," ",y,"cooridinates for navigation")
        xi=init[0]
        yi=init[1]
        # print(xi," ",yi,"Initial")
        if(y>yi and x>xi):
            # print("first loop")
            while(int(data[1])<y or data==(0,0)):
                data=qrdetect()
                # print(data[1])
                gostraight()
            rotateright()
            time.sleep(15.2)
            while(int(data[0])<x or data==(0,0)):
                data=qrdetect()               
                gostraight()
            data=qrdetect()
            rotateleft()
            time.sleep(15.5)
        elif(y>yi and x<xi):
            # print("2nd loop")
            while(int(data[1])<y or data==(0,0)):
                data=qrdetect()
                # print(data[1])
                gostraight()
            rotateleft()
            time.sleep(15.2)
            while(int(data[0])>x or data==(0,0)):
                data=qrdetect() 
                gostraight()
                # print(data[0])              
                # if(int(data[0])>x or data==(0,0) ):
                #     gostraight()
                #     print("continuing")
                #     continue
                
                # else:
                #     print("broke")
                #     break
            
            data=qrdetect()
            rotateright()
            time.sleep(15.5)

        elif(y==yi and x>xi):
            rotateright()
            time.sleep(15.2)
            # print(data)
            # print(type(data))
            # print(type(data[0]))
            # print(data[0])
            while(int(data[0])<x or data==(0,0)):
                data=qrdetect()
                gostraight()
            rotateleft()
            time.sleep(15.5)
        elif(y==yi and x<xi):
            rotateleft()
            time.sleep(15.2)
            # print(data)
            # print(type(data))
            # print(type(data[0]))
            # print(data[0])
            while(int(data[0])>x or data==(0,0)):
                data=qrdetect()
                gostraight()
            rotateright()
            time.sleep(15.5)
        elif(y>yi and x==xi):
            while(int(data[1])<y or data==(0,0)):
                data=qrdetect()
                gostraight()
        zerovel()
        init=n
        


    print("REACHED ALL COORDINATES SUCCESSFULLY!!!")
    # sim.simxGetPingTime(client_id)
    return_code=sim.simxStopSimulation(client_id,sim.simx_opmode_oneshot)
    sim.simxGetPingTime(client_id)
    sim.simxFinish(client_id)
