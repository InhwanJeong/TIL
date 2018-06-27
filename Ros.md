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




