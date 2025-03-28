## MySQL 검색

### like
- 부분적으로 일치하는 컬럼을 조회할 때 사용
```markdown
where name like '정%' # 이름이 정으로 시작하는 모든사람 찾기
where name like '%난' # 이름이 난으로 끝나는 모든사람 찾기
where name like '%이%' # 이름 시작, 중간, 끝 어디든 '이'라는 단어를 포함한 모든사람

# 제갈량, 제갈공명
where name like '제갈_' # _는 한글자만 추가로 매칭하여 검색 -> 제갈량

```