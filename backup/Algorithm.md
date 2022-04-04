Algorithm
============


# 1. qsort()

```c
#include <stdlib.h>    // qsort()를 사용하기 위해 선언

int compare(const void *first, const void *second){  
//현재 이 qsort는 오름차순으로 정렬 return값 1,-1을 서로 바꿔주면 내림차순으로 정렬
    if(*(int*)first > *(int*)second)
        return 1;
    if(*(int*)first < *(int*)second)
        return -1;
    else
        return 0;       //비교가 끝나면 main으로 돌아감
}

void main(){
    
    ...
    
    qsort( P, N, sizeof(int), compare)    // qsort(데이터의 시작주소, 리스트의 개수, 배열의 길이 , 비교함수)
    
}

```
