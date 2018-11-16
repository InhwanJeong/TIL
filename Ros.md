Ros(Robot Operating System)
=====

# 굉장히 좋은 사이트
```
https://github.com/robotpilot/ros-seminar  -> 표윤석님의 오픈강의자료
```

## 원더봇
-

- red_light_green_light.py 예제
```py
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist # vector3 angular, linear (각각 float x,y,z)

cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1) 
				#토픽이름, 매개변수, 1개메세지만 버퍼링하겠다.
rospy.init_node('red_light_green_light')

red_light_twist = Twist() 
green_light_twist = Twist()
green_light_twist.linear.x = 0.5 # 초당 0.5m 직진

driving_forward = False
light_change_time = rospy.Time.now()
rate = rospy.Rate(10) # 10hz 주기

while not rospy.is_shutdown():
  if driving_forward:
    cmd_vel_pub.publish(green_light_twist)
  else:
    cmd_vel_pub.publish(red_light_twist)
  if rospy.Time.now() > light_change_time:
    driving_forward = not driving_forward
    light_change_time = rospy.Time.now() + rospy.Duration(3)
  rate.sleep() # sleep를 호출하지 않으면 코드는 계속동작하여 너무 많은 메세지를 전송 -> cpu 전체를 차지
```

```
$ ./red_light_green_light.py cmd_vel:=cmd_vel_mux/input/teleop 
#터틀봇 소프트웨어가 기대하는 토픽 Twist는 cmd_vel_mux/input/teleop이다.
```

##텔레옵 봇
- 선속도와 각속도(요 속도) 존재 
- 키보드를 이용한 터틀봇 제어

- key_publisher.py
```
#!/usr/bin/env python
import sys, select, tty, termios # 시스템, 입출력, 터미널 제어, 터미널 제어
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
  key_pub = rospy.Publisher('keys', String, queue_size=1)
  rospy.init_node("keyboard_driver")
  rate = rospy.Rate(100)
  
  old_attr = termios.tcgetattr(sys.stdin) #터미널에서 입력받는함수
  tty.setcbreak(sys.stdin.fileno()) #에코를 사용하지 않고 입력을 받아오는 명령
  
  while not rospy.is_shutdown():
    if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
    #select.select( rlist , wlist , xlist [ , timeout ])
    #		    읽는값, 쓰는값, 예외값, 시간 
      key_pub.publish(sys.stdin.read(1))
    rate.sleep()
  termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
  # termios.tcsetattr(sys.stdin termios.tcsadrain settings)
```

- keys_to_twist.py
```
#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# BEGIN KEYMAP
key_mapping = { 'w': [ 0, 1], 'x': [0, -1], 
                'a': [-1, 0], 'd': [1,  0], 
                's': [ 0, 0] }
# END KEYMAP

def keys_cb(msg, twist_pub):
  if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
    return #수백 밀리초 이내에 입력을 받지않으면 로봇 구동을 정지한다.
  vels = key_mapping[msg.data[0]]
  t = Twist()
  t.angular.z = vels[0]
  t.linear.x  = vels[1]
  twist_pub.publish(t)

if __name__ == '__main__':
  rospy.init_node('keys_to_twist')
  twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  rospy.Subscriber('keys', String, keys_cb, twist_pub)
  rospy.spin()
```
