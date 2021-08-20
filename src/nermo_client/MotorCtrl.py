""" Motor control class that builds on motor command class"""

from nermo_client.ToDefine import *

from nermo_client.MotorCmd import *

import time
import math
import numpy as np

class Motors(CMouseCom):
    """docstring for Motors"""
    MotorNum = 13
    CommandDelay = 0.015#0.015

    uFrontLegStart = -10		# x start pos. of pace
    uHindLegStart = -20
    uStepLengthF = 60			# length of one leg move on the ground
    uStepLengthH = 60			# length of one leg move on the ground
    uHWalkLevel = 0				# y walking level of init and walking
    uFWalkLevel = 10			# y walking level of init and walking
    uSitting_x = -30			# X position for foot in sitting
    uSitting_y = 30				# Y position for foot in sitting
    uPosSpineFlexRelax = 180	# - is flex  NO+!!
    uPosHeadPan = 180
    uPosHeadTilt = 202

    def __init__(self, SerialPort, BaudRate):
        super(Motors, self).__init__(SerialPort, BaudRate)
        self.labelFlag = 0
        self.motionlength = 50
        self.margin = 1
        self.motor_num = 12

        self.id_tags = np.array([ID_FORELEFT_HIP, ID_FORELEFT_KNEE, 
                                ID_FORERIGHT_HIP, ID_FORERIGHT_KNEE,
                                ID_HINDLEFT_HIP, ID_HINDLEFT_KNEE,
                                ID_HINDRIGHT_HIP, ID_HINDRIGHT_KNEE,
                                ID_TAIL, ID_HEAD_PAN, ID_HEAD_TILT, ID_SPINE])
        
        self.offset_q = np.array([ 180.0, 180.0,
                                 180.0, 180.0,
                                 180.0, 180.0,
                                 180.0, 180.0,
                                 180.0, 180.0, 180.0, 180.0])

    def ctrl(self, cmd, targetPos):

        return False

    def to_remap(self, val):
        maxPos = 4095
        maxDeg = 360
        tMap = (maxPos * val) / maxDeg
        return int(abs(tMap))

    def send_motor_msgs(self, q_values: np.ndarray):
        SetMotorPos = "SetMotorPos"
        for i in range(self.motor_num):
            angle = self.offset_q[i] + q_values[i]*180.0/np.pi
            # To Do
            # Put all the IDs into an addressable array -> self.id_tags[] 
            # Adjust the offset -> self.offset_q[] = 180 (neutral is 180)
            self.ProcessSpine(SetMotorPos, self.id_tags[i], self.to_remap(angle), 1)
            self.ProcessSpine(SetMotorPos, ID_FORELEFT_HIP, self.to_remap(q_values[A_FORELEFT_HIP]), 1)
            self.ProcessSpine(SetMotorPos, ID_FORELEFT_KNEE, self.to_remap(q_values[A_FORELEFT_KNEE]), 1)
            self.ProcessSpine(SetMotorPos, ID_FORERIGHT_HIP, self.to_remap(q_values[A_FORERIGHT_HIP]), 1)
            self.ProcessSpine(SetMotorPos, ID_FORERIGHT_KNEE, self.to_remap(q_values[A_FORERIGHT_KNEE]), 1)
            self.ProcessSpine(SetMotorPos, ID_HINDLEFT_HIP, self.to_remap(q_values[A_HINDLEFT_HIP]), 1)
            self.ProcessSpine(SetMotorPos, ID_HINDLEFT_KNEE, self.to_remap(q_values[A_HINDLEFT_KNEE]), 1)
            self.ProcessSpine(SetMotorPos, ID_HINDRIGHT_HIP, self.to_remap(q_values[A_HINDRIGHT_HIP]), 1)
            self.ProcessSpine(SetMotorPos, ID_HINDRIGHT_KNEE, self.to_remap(q_values[A_HINDRIGHT_KNEE]), 1)
            self.ProcessSpine(SetMotorPos, ID_SPINE, self.to_remap(q_values[A_SPINE]), 1)
            self.ProcessSpine(SetMotorPos, ID_TAIL, self.to_remap(q_values[A_TAIL]), 1)
            self.ProcessSpine(SetMotorPos, ID_HEAD_PAN, self.to_remap(q_values[A_HEAD_PAN]), 1)
            self.ProcessSpine(SetMotorPos, ID_HEAD_TILT, self.to_remap(q_values[A_HEAD_TILT]), 1)
            # self.ProcessSpine(SetMotorPos, ID_SPINE_FLEX, self.to_remap(q_values[A_SPINE_FLEX]), 1)