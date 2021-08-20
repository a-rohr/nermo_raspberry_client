""" Motor control class that builds on motor command class"""

from nermo_client.ToDefine import *

from nermo_client.MotorCmd import *

import time
import math
import numpy as np

class Motors(CMouseCom):
    """docstring for Motors"""

    def __init__(self, SerialPort, BaudRate):
        super(Motors, self).__init__(SerialPort, BaudRate)
        self.init_motor_parameters()
        print("Motor Control Initialized")

    def init_motor_parameters(self):
        """ Initialize all overall motor control parameters"""
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

    def shutdown_ctrl(self):
        self.ProcessSpine("MPwrOff",0)
        self.shutdown()

    def to_remap(self, val):
        maxPos = 4095
        maxDeg = 360
        tMap = (maxPos * val) / maxDeg
        return int(abs(tMap))

    def rad_to_deg(self, val):
        return val*180.0/np.pi

    def send_motor_msgs(self, command: str, q_values: np.ndarray):
        
        for i in range(self.motor_num):
            angle = self.offset_q[i] + self.rad_to_deg(q_values[i])
            # To Do
            # Put all the IDs into an addressable array -> self.id_tags[] 
            # Adjust the offset -> self.offset_q[] = 180 (neutral is 180)
            self.ProcessSpine(command, self.id_tags[i], self.to_remap(angle), 1)

            """ Outdated, now running these commands inside a loop
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
            """
            # self.ProcessSpine(SetMotorPos, ID_SPINE_FLEX, self.to_remap(q_values[A_SPINE_FLEX]), 1)