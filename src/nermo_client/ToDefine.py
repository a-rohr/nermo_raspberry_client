""" Define class with important constants """
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
#defines for Motors in Array
A_TIMESTAMP = 0
A_FORELEFT_HIP = 0
A_FORELEFT_KNEE = 1
A_FORERIGHT_HIP = 2
A_FORERIGHT_KNEE = 3
A_HINDLEFT_HIP = 4
A_HINDLEFT_KNEE = 5
A_HINDRIGHT_HIP = 6
A_HINDRIGHT_KNEE = 7
A_TAIL = 8
A_HEAD_PAN = 9
A_HEAD_TILT = 10
A_SPINE = 11
A_SPINE_FLEX = 12

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
#defines for Motors in File Array
F_TIMESTAMP = 0
F_TIME = 1
F_FORELEFT_HIP = 2
F_FORELEFT_KNEE = 3
F_FORERIGHT_HIP = 4
F_FORERIGHT_KNEE = 5
F_HINDLEFT_HIP = 6
F_HINDLEFT_KNEE = 7
F_HINDRIGHT_HIP = 8
F_HINDRIGHT_KNEE = 9
F_SPINE = 10
F_TAIL = 11
F_SPINE_FLEX = 12
F_HEAD_PAN = 13
F_HEAD_TILT = 14

# motion is created via motionarray
# speed is done via amount of points to be published (old setup: 100 values at 500hz?!)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
ID_HINDLEFT_HIP=1
ID_HINDLEFT_KNEE=0
ID_FORELEFT_HIP=3
ID_FORELEFT_KNEE=2
ID_HINDRIGHT_HIP=11
ID_HINDRIGHT_KNEE=10
ID_FORERIGHT_HIP=13
ID_FORERIGHT_KNEE=12
ID_SPINE_FLEX=20
ID_SPINE=21
ID_TAIL=22
ID_HEAD_PAN=23
ID_HEAD_TILT=24
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////


class InitCoil(object):
	"""docstring for InitCoil"""
	def __init__(self, lhl=180, lfl=180, rhl=180, rfl=180):
		super(InitCoil, self).__init__()
		self.lhl = lhl
		self.lfl = lfl
		self.rhl = rhl
		self.rfl = rfl

initCoil = [InitCoil()]