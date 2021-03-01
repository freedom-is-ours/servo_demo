
import time

class servo_switch():  #舵机直接设角度 （180度伺服）
    
    def __init__(self):
        pass

    def set_angle(self,channel,angle = 0):
        print("set channel {} angle = {}".format(channel,angle))

    def read_angle(self): #可以通过读LED0_ON_H,LED0_ON_L知道当前角度,倒也没啥用
        pass  


class servo_360(): #360°电机
    
    def __init__(self):
        pass
    def stepping(self, channel, direction = 1, stepsize = 1, stepnum = 1): #步进用法：方向±1，步长[0，1]，步数正整数
        print("stepping {}-{}-{}-{}".format(channel,direction,stepsize,stepnum))

    def stepless(self,channel, direction = 1, speed = 1): #无极调速电机用法:方向-1反转，1正转，速度0到1
        print(channel,direction,speed)


class servo_state() :
    def __init__(self,len = 8) :
        self.len = len
        self.angles = [0]*self.len
        self.speed = [1]*self.len
        self.stepsize = [1]*self.len
        self.multi = [1]*self.len