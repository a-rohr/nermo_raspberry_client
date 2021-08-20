import numpy as np
import rospy 

from std_msgs.msg import Float32MultiArray
import socket

from nermo_client.MotorCmd import *
from nermo_client.MotorCtrl import Motors
from nermo_client.ToDefine import *

class Low_Level_Controller:

    def __init__(self):
        print("Low level controller init")
        self.init_parameters()
        self.main()

    def init_parameters(self):
        """ Initialize the important class parameters here """
        self.q_values = np.zeros((12,))
        SerialPort = "/dev/ttyAMA0"
        BaudRate = 1000000
        self.motor_ctrl = Motors(SerialPort, BaudRate)

    def callback_q_values(self, data):
        """ Callback for the q_values topic and written to the internal q_values """
        self.q_values = np.array((data.data))

    def shutdown_callback(self):
        print("Closing UART connection & motor power off")
        self.motor_ctrl.shutdown_ctrl()
        print("Shutting down ros node")

    def low_level_controller_loop(self, rate: int) -> None:
        """ Low level controller ROS loop """

        rospy.init_node("low_level_controller", anonymous=True)
        r = rospy.Rate(rate)

        rospy.Subscriber('q_values', Float32MultiArray, self.callback_q_values, queue_size = 1)
        count = 0
        while(not rospy.is_shutdown(self.shutdown_callback)):         
            # Main loop
            self.motor_ctrl.send_motor_msgs("SetMotorPos", self.q_values)
            r.sleep()

    def main(self):
        """ Main function - try to run the ROS node, otherwise pass """
        try:
            rate = 50
            self.low_level_controller_loop(rate)
        except rospy.ROSInterruptException:
            pass


if __name__ == "__main__":
    low_level_control = Low_Level_Controller()