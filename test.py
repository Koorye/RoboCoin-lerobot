import time
from piper_sdk import C_PiperInterface_V2

arm = C_PiperInterface_V2('can_left')
arm.ConnectPort()
while not arm.EnablePiper():
    print('connect')
    time.sleep(0.1)

while True:
    arm.MotionCtrl_2(0x01, 0x00, 10, 0x00)
    print(arm.GetArmEndPoseMsgs())
    arm.EndPoseCtrl(-8000, 303, 278393, -158858, 60071, -157899)
    time.sleep(0.1)