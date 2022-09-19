from pyPS4Controller.controller import Controller
import pickle

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.LeftX = 0
        self.LeftY = 0  
        self.RightX = 0
        self.RightY = 0
        self.Motor1 = 0
        self.Motor2 = 0  
        self.Motor3 = 0
        self.Motor4 = 0

    def updateControl(self):
        #print(list([self.LeftX, self.LeftY, self.RightX, self.RightY]))
        if self.LeftX<16384 and self.LeftX>-16384:
            self.Motor1=round(-self.LeftY/32768*265)
            self.Motor4=round(-self.LeftY/32768*265)
        if self.LeftX>=16384:
            self.Motor1=round(self.LeftX/32768*265)
            self.Motor4=round(-self.LeftX/32768*265)
        if self.LeftX<=-16384:
            self.Motor1=round(self.LeftX/32768*265)
            self.Motor4=round(-self.LeftX/32768*265)
        if self.RightX<16384 and self.RightX>-16384:
            self.Motor2=round(-self.RightY/32768*265)
            self.Motor3=round(-self.RightY/32768*265)
        if self.RightX>=16384:
            self.Motor2=round(self.RightX/32768*265)
            self.Motor3=round(-self.RightX/32768*265)
        if self.RightX<=-16384:
            self.Motor2=round(self.RightX/32768*265)
            self.Motor3=round(-self.RightX/32768*265)
        StrNum=",".join([str(self.Motor1),str(self.Motor2),str(self.Motor3),str(self.Motor4)])
        print("p:", StrNum)
        file=open('motorspeed.ps4','wb')
        pickle.dump(StrNum, file)
        file.close()
        #print(StrNum)
    

    def on_L3_up(self, value):
        self.LeftY=value
        self.updateControl()
    def on_L3_down(self, value):
        self.LeftY=value
        self.updateControl()
    def on_L3_left(self, value):
        self.LeftX=value
        self.updateControl()
    def on_L3_right(self, value):
        self.LeftX=value
        self.updateControl()
    def on_L3_y_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        self.LeftY=0
        self.updateControl()
    def on_L3_x_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        self.LeftX=0
        self.updateControl()
    def on_R3_up(self, value):
        self.RightY=value
        self.updateControl()
    def on_R3_down(self, value):
        self.RightY=value
        self.updateControl()
    def on_R3_left(self, value):
        self.RightX=value
        self.updateControl()
    def on_R3_right(self, value):
        self.RightX=value
        self.updateControl()
    def on_R3_y_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        self.RightY=0
        self.updateControl()
    def on_R3_x_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        self.RightX=0
        self.updateControl()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
