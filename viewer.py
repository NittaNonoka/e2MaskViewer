# e2MaskZ用
# Arduinoで読み取ったセンサの値をシリアル通信によってPythonで可視化
import serial
import datetime
import numpy as np
from time import time
import pygame 
from datetime import datetime 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#色を返す
def color(data_byte):
    sp = 1024/4
    if 0<data_byte<sp:
        return (0,0+data_byte,255)
    elif sp<=data_byte<sp*2:
        return(0,255,255-(data_byte-256))
    elif sp*2<=data_byte<sp*3:
        return(0+(data_byte-512),255,0)
    elif sp*3<=data_byte<sp*4:
        return (255,255-(data_byte-768),0)
    else:
        return(255,255,255)


class HMDSerialRead():

    def __init__(self, comnum, rate):
        self.com = comnum
        self.ser = serial.Serial(comnum, rate)
        self.values = [0 for i in range(20)]   
    
    def UpdateSensorData(self):
        # When micro computer receives the "b", it sends back the sensor data.
        # This system receive the 24 bytes which include the sensor data and start stop character
        
        # self.ser.write(b"b")
        byteBuffer = self.ser.read_until(terminator="Z".encode("utf-8"))
        SensorList = byteBuffer
      
        # print("SensorList = ", SensorList)
        # print(byteBuffer)
        if(len(SensorList) == 27):
            # print(SensorList[0])
            self.values[0] = (((SensorList[1]) & 0xff) << 2) + (((SensorList[21]) & 0xc0) >> 6)	    
            self.values[1] = (((SensorList[2]) & 0xff) << 2) + (((SensorList[21]) & 0x30) >> 4)
            self.values[2] = (((SensorList[3]) & 0xff) << 2) + (((SensorList[21]) & 0x0c) >> 2)
            self.values[3] = (((SensorList[4]) & 0xff) << 2) + ((SensorList[21]) & 0x03)
            self.values[4] = (((SensorList[5]) & 0xff) << 2) + (((SensorList[22]) & 0xc0) >> 6)	
            self.values[5] = (((SensorList[6]) & 0xff) << 2) + (((SensorList[22]) & 0x30) >> 4)
            self.values[6] = (((SensorList[7]) & 0xff) << 2) + (((SensorList[22]) & 0x0c) >> 2)
            self.values[7] = (((SensorList[8]) & 0xff) << 2) + ((SensorList[22]) & 0x03)
            self.values[8] = (((SensorList[9]) & 0xff) << 2) + (((SensorList[23]) & 0xc0) >> 6)
            self.values[9] = (((SensorList[10]) & 0xff) << 2) + (((SensorList[23]) & 0x30) >> 4)
            self.values[10] = (((SensorList[11]) & 0xff) << 2) + (((SensorList[23]) & 0x0c) >> 2)
            self.values[11] = (((SensorList[12]) & 0xff) << 2) + ((SensorList[23]) & 0x03)
            self.values[12] = (((SensorList[13]) & 0xff) << 2) + (((SensorList[24]) & 0xc0) >> 6)
            self.values[13] = (((SensorList[14]) & 0xff) << 2) + (((SensorList[24]) & 0x30) >> 4)
            self.values[14] = (((SensorList[15]) & 0xff) << 2) + (((SensorList[24])& 0x0c) >> 2)
            self.values[15] = (((SensorList[16]) & 0xff) << 2) + ((SensorList[24]) & 0x03)
            self.values[16] = (((SensorList[17]) & 0xff) << 2) + (((SensorList[25]) & 0xc0) >> 6)
            self.values[17] = (((SensorList[18]) & 0xff) << 2) + (((SensorList[25]) & 0x30) >> 4)
            self.values[18] = (((SensorList[19]) & 0xff) << 2) + (((SensorList[25]) & 0x0c) >> 2)
            self.values[19] = (((SensorList[20]) & 0xff) << 2) + ((SensorList[25]) & 0x03)
            # print(self.values)

        else:
            print("sensor data error")

    def getSensorData(self):
        self.UpdateSensorData()
        return self.values 

class SensorData:
    def __init__(self):
        self.commandType = -1
        self.strength = 0
        self.sensorValues = []
    
    def setSensorValues(self, sensorValues):
        self.sensorValues = sensorValues
    
    def getSensorValues(self):
        return self.sensorValues

# Arduinoを繋げたCOMポートを開く 
# * ポート名は環境に合わせて適宜変えること
ser = HMDSerialRead("/dev/tty.usbserial-DN03ZVUJ", 57600) # e2mask left
ser2 = HMDSerialRead("/dev/tty.usbserial-DN040KE7", 57600) # e2mask right

#ser = HMDSerialRead("/dev/tty.usbserial-DN0404LS", 57600)
# ser = HMDSerialRead("COM5", 57600)


sensorData = SensorData()
sensorData2 = SensorData()
# print("getSensorData = ", ser.getSensorData())
sensorDataList = []

#描画
pygame.init()

WIDTH = 528
HEIGHT = 639

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Viewer')

#画像の挿入、1がセンサもついた画像、2が顔だけの画像
# img1 = pygame.image.load("sensor.jpg")
# img2 = pygame.image.load("face_resize.jpg")
    
#SCREEN.blit(img1, (0, 0))
# SCREEN.blit(img2, (0, 0))  
SCREEN.fill(WHITE)

is_running = True
while is_running:
    # SensorData Update
    ser.UpdateSensorData()
    ser2.UpdateSensorData()
    sensorData.setSensorValues(ser.getSensorData())
    sensorData2.setSensorValues(ser.getSensorData())
    data = sensorData.getSensorValues()+sensorData2.getSensorValues()
    #print(sensorData.getSensorValues())
    print(data)
    
       
    #right
    # pygame.draw.rect(SCREEN,color(data[18]),(60,210,25,40))#18
    # pygame.draw.rect(SCREEN,color(data[19]),(100,210,25,40))#19
    # pygame.draw.rect(SCREEN,color(data[16]),(140,210,25,40))#16
    # pygame.draw.rect(SCREEN,color(data[17]),(185,210,25,40))#17
    # pygame.draw.rect(SCREEN,color(data[15]),(230,210,25,40))#15

    pygame.draw.rect(SCREEN,color(data[0]),(60,210,30,30))#
    pygame.draw.rect(SCREEN,color(data[21]),(125,210,30,30))#
    pygame.draw.rect(SCREEN,color(data[22]),(190,210,30,30))#
    
    pygame.draw.rect(SCREEN,color(data[23]),(50,320,30,30))#7
    pygame.draw.rect(SCREEN,color(data[24]),(110,320,30,30))#11
    pygame.draw.rect(SCREEN,color(data[25]),(170,320,30,30))#13
    
    pygame.draw.rect(SCREEN,color(data[26]),(35,370,30,30))#10
    pygame.draw.rect(SCREEN,color(data[27]),(105,370,30,30))#12
    pygame.draw.rect(SCREEN,color(data[28]),(170,370,30,30))#8
        
    pygame.draw.rect(SCREEN,color(data[20]),(60,420,30,30))#9
    pygame.draw.rect(SCREEN,color(data[30]),(110,420,30,30))#1
    pygame.draw.rect(SCREEN,color(data[31]),(165,420,30,30))#2
        
    pygame.draw.rect(SCREEN,color(data[32]),(80,470,30,30))#0
    pygame.draw.rect(SCREEN,color(data[33]),(130,470,30,30))#4
    pygame.draw.rect(SCREEN,color(data[34]),(180,470,30,30))#5
        
    pygame.draw.rect(SCREEN,color(data[35]),(100,520,30,30))#3
    pygame.draw.rect(SCREEN,color(data[36]),(150,520,30,30))#14
    pygame.draw.rect(SCREEN,color(data[37]),(200,520,30,30))#6

    pygame.draw.rect(SCREEN,color(data[38]),(130,570,30,30))#3
    pygame.draw.rect(SCREEN,color(data[39]),(180,570,30,30))#14

    #left
    # pygame.draw.rect(SCREEN,BLUE,(280,210,25,40))#
    # pygame.draw.rect(SCREEN,BLUE,(325,210,25,40))#
    # pygame.draw.rect(SCREEN,BLUE,(370,210,25,40))#
    # pygame.draw.rect(SCREEN,BLUE,(415,210,25,40))#
    # pygame.draw.rect(SCREEN,BLUE,(460,210,25,40))#

    pygame.draw.rect(SCREEN,color(data[14]),(330,210,30,30))#ok
    pygame.draw.rect(SCREEN,color(data[16]),(395,210,30,30))#
    pygame.draw.rect(SCREEN,color(data[17]),(460,210,30,30))#
    
    pygame.draw.rect(SCREEN,BLUE,(330,320,30,30))#?
    pygame.draw.rect(SCREEN,color(data[13]),(390,320,30,30))#
    pygame.draw.rect(SCREEN,color(data[19]),(450,320,30,30))#
    
    pygame.draw.rect(SCREEN,color(data[28]),(340,370,30,30))#
    pygame.draw.rect(SCREEN,color(data[11]),(400,370,30,30))#
    pygame.draw.rect(SCREEN,color(data[18]),(460,370,30,30))#
    
    pygame.draw.rect(SCREEN,color(data[9]),(350,420,30,30))#
    pygame.draw.rect(SCREEN,color(data[10]),(400,420,30,30))#
    pygame.draw.rect(SCREEN,BLUE,(450,420,30,30))#?
    
    pygame.draw.rect(SCREEN,BLUE,(340,470,30,30))#
    pygame.draw.rect(SCREEN,BLUE,(390,470,30,30))#
    pygame.draw.rect(SCREEN,BLUE,(440,470,30,30))#
    
    pygame.draw.rect(SCREEN,BLUE,(310,520,30,30))#?
    pygame.draw.rect(SCREEN,color(data[2]),(360,520,30,30))#
    pygame.draw.rect(SCREEN,color(data[3]),(410,520,30,30))#

    pygame.draw.rect(SCREEN,color(data[25]),(330,570,30,30))#
    pygame.draw.rect(SCREEN,color(data[3]),(380,570,30,30))#


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:#右クリックするとスクリーンショットを保存する
            if event.button == 1:
                print("スクリーンショットを保存しました。")
                # pygame.image.save(SCREEN,"screenshot%s.jpg"%datetime.today().strftime("%Y%m%d-%H%M%S"))
    
pygame.quit()
    