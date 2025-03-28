### 도커 프로그램 배포
- 빌드할 디렉토리에 Dockerfile 작성
    ```markdown
    # ./Dockerfile
    FROM python:3.9
    
    RUN mkdir -p /usr/src/app
    WORKDIR /usr/src/app
    
    ## Install packages
    COPY requirements.txt /usr/src/app
    RUN pip install -r requirements.txt
    
    ## Copy all src files
    COPY . /usr/src/app
    
    ## Run the application on the port 8000
    EXPOSE 8000
    
    # 서버 실행 명령어
    CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
    ```
- 패키지 설치가 필요하다면 requirements.txt 파일 작성
    ```markdown
    django==3.2
    boto3==1.6.19
    gunicorn
    ```
- 리눅스 명령어
```bash
# -t --tag: 컨테이너 이름에 태그를 추가할 수 있음
# container_name:version 
sudo docker build -t swagger_server:1.0.0 .

# --name: 컨테이너 이름 설정(조작의 편의성 및 중복 생성 방지)
# -d: 백그라운드 실행
# -p 포트설정
sudo docker run --name SwaggerServer -d -p 8081:8081 swagger_server:1.0.0

# -f: 실행중인 컨테이너 강제종료
sudo docker rm -f SwaggerServer
```


### 도커 컨테이너 중지, 삭제
```bash
docker stop
docker rm {container}

# stop and rm
docker rm -f {container}

# remove all exited state container
docker container prune
```

