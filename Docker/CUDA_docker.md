## Docker with GPU 
- NVIDIA Container Toolkit
  - 도커 환경에서 빌드하고 GPU를 사용하기 위해 필요한 도구이다.
  - 툴킷은 NVIDA GPU 관련 런타임 라이브러리와 유틸리티를 도커환경에 자동으로 구성해준다.
    

### 1. 환경 구축
- centos 7/8 설치
```
# 공식 도커 저장소 추가
sudo yum-config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo

# CentOS는 컨테이너의 특전 버전을 지원하지 않기 때문에 contanerd.id 패키지를 설치 후 도커 패키지를 설치 해야함.
sudo yum install -y https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.4.3-3.1.el7.x86_64.rpm

# 도커 패키지 설치
sudo yum install docker-ce -y

# 도커 서비스 실행
sudo systemctl --now enable docker

# 도커 설치 테스트 
sudo docker run --rm hello-world
```
- 그래픽카드 드라이버 확인
 - 드라이버 버전은 반드시 NVIDIA Linux drivers >= 418.81.07을 만족해야 함
   - ※ 사용하려는 그래픽 드라이버가 최소조건보다 작다면 도커 환경에서 GPU를 사용할 수 없으니 주의 한다.
 - 사용하려고 하는 CUDA버전에 맞게 그래픽 드라이버를 설치 해주도록 한다.

```
# 그래픽 드라이버 버전 확인 
nvidia-smi
```

- NVIDIA Container Toolkit 설치
```
# 저장소와 GPG 키 세팅
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.repo | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo

# nvidia-docker2 설치
sudo yum install -y nvidia-docker2

# 도커 서비스 재시작
sudo systemctl restart docker

# CUDA 컨테이너 실행 테스트
sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
```


