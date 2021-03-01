from PCA9685 import PCA9685
import time

#1.0版本，channel在初始的时候设定，优点是能直接在建立示例的时候跟用途一一对应，方便单个调用

class servo_switch(PCA9685):  #舵机直接设角度 （180度伺服）
    
    def __init__(self, address, debug, channal):
        super().__init__(address=address, debug=debug)
        self.channal = channal
        self.setPWMFreq(50)

    def set_angle(self,angle = 0):
        if angle <= 180:
            pulse = angle/180*2000 + 500 #根据角度设定脉冲   
        else:
            pulse = 500
        self.setServoPulse(self.channal,pulse)

    def read_angle(self): #可以通过读LED0_ON_H,LED0_ON_L知道当前角度,倒也没啥用
        pass  


class servo_360(PCA9685): #360°电机
    
    def __init__(self, address, debug, channal):
        super().__init__(address=address, debug=debug)
        self.channal = channal
        self.setPWMFreq(50)

    def stepping(self, direction = 1, stepsize = 1, stepnum = 1): #步进用法：方向±1，步长[0，1]，步数正整数
        pulse = 1500 - direction * stepsize * 500 
        timedelay = 0.02 * stepnum #延时
        self.setServoPulse(1500)               #停止
        self.setServoPulse(self.channal,pulse) #转动
        time.sleep(timedelay)                  #延时
        self.setServoPulse(1500)               #停止

    def motor(self, direction = 1, speed = 1): #无极调速电机用法:方向-1反转，1正转，速度0到1
        pulse = 1500 - direction * speed * 500
        self.setServoPulse(self.channal,pulse)


if  __name__ == "__main__":

    ionization_shutter = servo_switch(channal=0) #测试
    ionization_shutter.set_angle(0)
    time.sleep(1)
    ionization_shutter.set_angle(90)
    time.sleep(1)
    ionization_shutter.set_angle(0)

    ablation_shutter = servo_switch(channal=1) #测试
    ablation_shutter.set_angle(0)
    time.sleep(1)
    ablation_shutter.set_angle(90)
    time.sleep(1)
    ablation_shutter.set_angle(0)

    detect_switch = servo_switch(channnal=2) # 测试
    angles = [0,45,90,135,180,0]
    for theta in angles:
        detect_switch.set_angle(theta)
        time.sleep(1)
    
    atten_motor = servo_360(channal=3)
    atten_motor.motor(1,1) #正转
    time.sleep(1)
    atten_motor.motor(1,0) #停转
    time.sleep(1)
    atten_motor.motor(-1,1) #反转
    time.sleep(1)
    atten_motor.motor(-1,0) #停转

    print("测试完毕！！")
