from PCA9685 import PCA9685
import time

#这个版本用于给http调用，channel要在调用方法时直接提供

class servo_switch(PCA9685):  #舵机直接设角度 （180度伺服）
    
    def __init__(self, address, debug):
        super().__init__(address=address, debug=debug)
        self.setPWMFreq(50)

    def set_angle(self,channel,angle = 0):
        channel = 2*channel #只用了偶数通道
        if angle <= 180:
            pulse = angle/180*2000 + 500 #根据角度设定脉冲   
        else:
            pulse = 500
        self.setServoPulse(channel,pulse)

    def read_angle(self): #可以通过读LED0_ON_H,LED0_ON_L知道当前角度,倒也没啥用
        pass  


class servo_360(PCA9685): #360°电机
    
    def __init__(self, address, debug):
        super().__init__(address=address, debug=debug)
        self.setPWMFreq(50)

    def stepping(self, channel, direction = 1, stepsize = 1, stepnum = 1): #步进用法：方向±1，步长[0，1]，步数正整数
        channel = 2*channel #
        pulse = 1500 - direction * stepsize * 500 
        timedelay = 0.02 * stepnum #延时
        self.setServoPulse(channel,1500)               #停止
        self.setServoPulse(channel,pulse) #转动
        time.sleep(timedelay)                  #延时
        self.setServoPulse(channel,1500)               #停止

    def stepless(self, channel,direction = 1, speed = 1): #无极调速电机用法:方向-1反转，1正转，0停止,速度0到1
        pulse = 1500 - direction * speed * 500
        self.setServoPulse(channel,pulse)

class servo_state() :
    def __init__(self,len = 8) :
        self.len = len
        self.angles = [0]*self.len
        self.speed = [1]*self.len
        self.stepsize = [1]*self.len
        self.multi = [1]*self.len

if  __name__ == "__main__":
    pass
