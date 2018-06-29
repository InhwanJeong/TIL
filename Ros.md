Ros(Robot Operating System)
=====

# 굉장히 좋은 사이트
```
https://github.com/robotpilot/ros-seminar  -> 표윤석님의 오픈강의자료
```

## 로봇 운영체제
- 무료 오픈소스!!
- Ros는 메타 운영체제
- 로봇 소프트웨어를 개발하기 위한 소프트웨어 프레임워크
- 노드(node)와 연결선(edge)으로 그래프 구성
@노드: POSIX 프로세스, 연결선 : TCP연결

## 준비사항
#### roscore
- Ros의 핵심
- 노드가 노드의 위치을 찾을 수 있도록 한다.
- 모든 Ros시스템에서는 roscore가 필요하다.(심지어 gazebo, Rviz에서도)

#### 캣킨(catkin)
- 캣킨은 Ros의 빌드 시스템이다.
- CMakeLists.txt와 package.xml을 알아야 한다.

###### 작업공간

```
$ source /opt/ros/kinetic/setup.bash
```
-> Ros설정 파일에 실행되도록 추가

```
$ mkdir -p ~/catkin_ws/src
$ cd ~catkin_ws/src
$ catkn_init_workspace
```
-> 캣킨 작업 공간을 만들고 초기화

```
$ cd ~/catkin_ws
$ catkin_make
```
-> catkin_ws라는 디렉터리 안에 CMakeLists.txt파일을 생성한다.

```
$ source devel/setup.bash
```
-> 작업공간 생성완료, 앞으로의 모든 코드는 이곳의 src 디렉터리에 넣도록한다.

#### Message
- 노드들은 Message를 통해 노드간의 데이터를 주고 받는다.
- 메세지는 int, float, point, bool같은 변수 형태이다.

#### ROS 패키지
- 하나 이상의 노드, 노드 실행을 위한 정보를 묶어 놓은 것
```
$ cd ~/catkin_ws/src
$ catkin_create_pkg my_awesome_code rospy
```
-> rospy패키지에 의존하는 새로운 패키지 my_awesome_code라는 새로운 패키지 생성

#### rosrun
- ros 노드단위로 실행시켜주는 명령어

```
rosrun 패키지 노드
```

#### roslaunch
- ros 파일단위로 실행시켜주는 명령어 
```
roslaunch 패키지 launch파일
```

## rostopic
- 노드간 데이터 교환 방법중 하나이다.
- 발행/구독(Publisher -> topic -> Subscriber)
- 목적에 따라 1:1. 1:N, N:N 통신도 가능

#### 토픽 발행
```python
#! /usr/bin/env python     #쉬뱅이라는 인터프리터 지시어이다. 운영체제에게 python파일이라고 알려주는 역할
import rospy               
from std_msgs.msg import Int32

rospy.init_node('topic_publisher') #노드 선언 및 초기화, 한개의 파일에 하나만 생성 가능

pub = rospy.Publisher('counter', Int32, queue_size = 10)  #퍼블리셔 생성, 광고 (이름 , 자료형, 큐사이즈) 
#래치된 토픽  ('map', nav_msgs/OccupancyGrid, latched=True) -> 한번만 발행 및 구독자에게 바로전달
rate = rospy.Rate(2) # 퍼블리시 주기 = 2Hz

count = 0
while not rospy.is_shutdown():    #파일이 종료 될 때 까지
	pub.publish(count)
	count += 1
	rate.sleep()
```  
- 실행 권한 부여
```
$ chmod u+x topic_publisher.py
```

- rostopic list : 현재 사용가능한 토픽 리스트
- rostopic -h : rostopic 명령어 목록을 보여준다.
- rostopic echo counter -n 5 : 5개의 메시지만 출력
- rostopic info : 토픽의 타입, 발행자와 구독자 정보를 확인 할 수 있다. 
- rostopic find std_msgs/Int32 : 해당 타입의 자료형을 발행하는 노드를 찾아준다.

#### 토픽 구독
```python
#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
	print msg.data


rospy.init_node('topic_subscriber')   # 노드 선언,초기화 , 이름은 ' '


sub = rospy.Subscriber('counter', Int32, callback)   # 구독자 생성, (구독할 토픽이름, 타입, 콜벡함수지정) 

rospy.spin() #구독이 시작되면 이것을 불러 Ros에게 제어를 넘긴다.
```

## Service
- 노드간 데이터 교환 방법중 하나이다.
- 동기식
- 서버/클라이언트 구조
- 1회만 접속되고 통신완료후 통신을 끊는다.

#### 서비스 구현
```python
#! /usr/bin/env python

import rospy
from service.srv import WordCount, WordCountResponse

def count_words(request):     #콜벡함수
    return WordCountResponse(len(request.words.split()))   # WordCountRequest 타입의 인자를 받고, WordCountResponse 타입의 인자 반환

rospy.init_node('service_server') 

service = rospy.Service('word_count', WordCount, count_words) # 서비스를 광고(서비스이름, 타입, 콜백함수)

rospy.spin()
```

#### 서비스 사용
```python
#! /usr/bin/env python

import rospy
from service.srv import WordCount
import sys

rospy.init_node('service_client')

rospy.wait_for_service('word_count')  #서버에서 서비스가 광고되기를 기다린다.

word_counter = rospy.ServiceProxy('word_count', WordCount)  # 서비스가 광고되면 포컬프록시를 생성

words = ' '.join(sys.argv[1:])

word_count = word_counter(words)

print words, '->', word_count.count
```

#### 서비스의 단점
- 동기식 이므로 요청에 대한 응답을 받기 전까지 client는 대기 상태다.
- 행위가 일어나는 중간중간의 상황 정보를 알 수 없다.


## Action(액션)
- 노드간 데이터 교환 방법중 하나이다.
- 비동기식
- time-extended 행위에 적합

#### 액션 정의
- action 패키지 안에 action 디렉터리를 만든다.
```python
duration time_to_wait     # goal      client -> server  행위를 시작할 때
---
duration time_elapsed

uint32 updates_sent       # result    server  -> client goal이 완료될 때
---
duration time_elapsed

duration time_remaining   # feedback  server  -> client 행위의 진행상황 제공, goal을 취소함
```

#### 액션 서버 구현
```python
#! /usr/bin/env python
import rospy
import time
import actionlib
from action.msg import TimerAction, TimerGoal, TimerResult

def do_timer(goal):           # goal을 매개변수로하는 콜백함수
    start_time = time.time()
    time.sleep(goal.time_to_wait.to_sec())    # goal의 time_to_wait만큼 sleep
    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)  #시간의 차이를 result에 저장
    result.updates_sent = 0
    server.set_succeeded(result)    # result를 클라이언트에게 전달
    
rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()         #서버 객체생성, (서버이름, 액션타입, 콜백함수, 자동시작여부)
rospy.spin()
```

#### 액션 클라이언트 구현
```python
#! /usr/bin/env python
import rospy
import actionlib
from action.msg import TimerAction, TimerGoal, TimerResult

rospy.init_node('timer_action_client')
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()    #서버가 준비 되기를 기다림
goal = TimerGoal()          # goal 객체 생성
goal.time_to_wait = rospy.Duration.from_sec(5.0)   #goal의 time_to_wail값 입력
client.send_goal(goal)                             #server로 goal 전달
client.wait_for_result()                           # result를 기다림
print('time elapsed: %f' %(client.get_result().time_elapsed.to_sec())) #result를 출력
```

## 원더-봇
- 가제보 설치
```
$ sudo apt-get install ros-kinetic-turtlebot-gazebo
```
- 주행 예제
```python
#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist   #vector3 타입의 linear, angular을 가지는 msg // 각각 x,y,z 방향의 속도를 표현

cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)  
rospy.init_node('red_light_green_light')

red_light_twist = Twist()          #메시지 생성
green_light_twist = Twist()
green_light_twist.linear.x = 0.5   # x 방면의 속도 0.5m/s

driving_forward = False            # 운행 여부를 표현 
light_change_time = rospy.Time.now()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    if driving_forward:
        cmd_vel_pub.publish(green_light_twist) #운행 여부 true시 green을 퍼블리시
    else:
        cmd_vel_pub.publish(red_light_twist)   #운행 여부 false시 red를 퍼블리시
    if light_change_time < rospy.Time.now():   #운행 여부를 바꿔주며, 시간을 갱신한다. 
        driving_forward = not driving_forward
        light_change_time = rospy.Time.now() + rospy.Duration(3)
    rate.sleep()    # 이 부분이 빠진다면 너무 많은 메시지를 전송하고, 전체 cpu코어를 차지 할 것이다.
```
- 실행
```
$ chmod +x red_light_green_light.py  #파일 실행권한
$ roslaunch turtlebot_gazebo turtlebot_world.launch  #가제보 실행
$ ./red_light_green_light.py cmd_vel:=cmd_vel_mux/input/telop  #터틀봇이 원하는 토픽을 퍼블리시하기위해 remapping 필요
```

- 센서 예제
```python
#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    range_ahead = msg.ranges[len(msg.ranges)/2]
    print "range ahead: %0.1f" % range_ahead      #장애물 거리를 출력
    
rospy.init_node('range_ahead')
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
rospy.spin()    
```


