# 성능향상

## 전이학습
- 기존 머신러닝과 달리 딥러닝은 스스로 중요한 속성을 뽑아 학습하기 때문에 많은 양의 데이터가 필요함.
- 수만장에 달하는 기존의 이미지에서 학습한 정보를 가져와 프로젝트에 활용하는 것을 전이 학습(transfer learning)이라고 한다.


## TTA(Test Time Augmentation)
- 학습에 이미지를 증강해서 사용하는 것이 아닌 추론, 테스트 단계에서 이미지를 증강하여 각 이미지를 추론 후 하나의 결과로 반환하는 기법
    
           Input
             |           # input batch of images 
        / / /|\ \ \      # apply augmentations (flips, rotation, scale, etc.)
       | | | | | | |     # pass augmented batches through model
       | | | | | | |     # reverse transformations for each batch of masks/labels
        \ \ \ / / /      # merge predictions (mean, max, gmean, etc.)
             |           # output batch of masks/labels
           Output
- 출처: https://github.com/qubvel/ttach

- TTA 장점
    - 객체 인식 정확도 향상
    - 성능 향상
    
- TTA 단점
    - 추가 구현 비용이 발생
    - 늘어난 이미지 만큼의 검출 시간(비용, 자원) 발생
    