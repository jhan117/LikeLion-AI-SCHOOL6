# SQL
<details>
<summary>목차</summary>
  
- [SQL 종류](#sql_종류)
- [쿼리 순서](#쿼리_순서)
- [데이터](#데이터)
  - [1. 데이터 가져오기](#데이터_가져오기)
  - [2. 조건에 맞는 데이터 검색하기](#조건에_맞는_데이터_검색하기)
  - [3. 데이터 순서 정렬하기](#데이터_순서_정렬하기)
- [함수](#함수)
  - [문자열 자르기](#문자열_자르기)
  - [소수점 처리](#소수점_처리)

</details>

**[참고 자료]**  
w3schools tutorial : [MySQL](https://www.w3schools.com/mysql/default.asp)  
인프런 강의 : [[백문이불여일타] 데이터 분석을 위한 기초 SQL](https://inf.run/HxLC)

## SQL 종류
- SQL : 구조화된 질의 언어
  - DQL : 데이터 질의 언어 (SELECT)
  - DML : 데이터 조작 언어 (INSERT, UPDATE, DELETE)

## 쿼리 순서
1. SELECT
2. FROM
3. WHERE
4. LIMIT

## 데이터
### 1. 데이터 가져오기
```MySQL
SELECT *
FROM table
```
#### `SELECT` Statement
데이터베이스에서 데이터를 선택하는데 쓰인다. 반환된 데이터는 `result-set`이라고 불리는 result table에 저장된다.
```MySQL
SELECT * -- 모든 columns 선택
SELECT column1, column2, ... -- 특정 column 선택
```
##### `SELECT DISTINCT` Statement
고유한 값을 반환하는데 쓰인다. (중복 제거)
```MySQL
SELECT DISTINCT column1, column2, ...
```

### 2. 조건에 맞는 데이터 검색하기
#### WHERE
필터링하는데 사용된다. (조건문)
```MySQL
WHERE condition
```
##### 연산자
- 비교 연산자 (=, >, >=, <, <=, <>)  
  <> 대신 !=도 사용 가능하다.  
  문자에도 사용이 가능하다.  
  `WHERE col < 'B'` 이는, B이전 데이터들만 출력해준다.
- 논리 연산자 (AND, OR)
  ```MySQL
  WHERE condition1 AND condition2 AND condition3 ...
  WHERE condition1 OR condition2 OR condition3 ...
  WHERE NOT condition
  ```
##### LIKE
패턴을 찾는다.
```MySQL
WHERE col LIKE 'a%'
WHERE col NOT LIKE 'a%'
```
- `%` : 와일드 카드 (어떤 글자라도 상관 없다)
- `_` : 1글자 와일드 카드 (글자수 표현)
만약, 기호를 쓰고 싶다면 이스케이프 문자인 `\`를 사용한다.
##### IN
가능한 값을 여러개 지정한다. OR 한것과 같음.
```MySQL
WHERE col IN ('a', 'b')
WHERE col NOT IN ('a', 'b')
```
##### BETWEEN
특정 범위 사이.
```MySQL
WHERE col BETWEEN 3 AND 5
WHERE col NOT BETWEEN 3 AND 5
```
#### IS NULL
NULL 체크
```MySQL
WHERE col IS NULL
WHERE col IS NOT NULL
```

### 3. 데이터 순서 정렬하기
#### ORDER BY
- 오름차순 (Default) : ASC (ascending)
- 내림차순 : DESC (descending)
```MySQL
ORDER BY price DESC
```
#### LIMIT
```MySQL
LIMIT 10 -- 위에서부터 10개
```

## 함수
### 문자열 자르기
- `LEFT` : 왼쪽부터
  - LEFT(string, number_of_chars)
- `RIGHT` : 오른쪽부터
  - RIGHT(string, number_of_chars)
- `SUBSTR` : 원하는 위치부터
  - SUBSTR(string, start, length)
- `SUBSTRING` : SUBSTR와 같음
  - SUBSTRING(string, start, length)
### 소수점 처리
- `CEIL` : 올림
  - CEIL(number)
- `FLOOR` : 내림
  - FLOOR(number)
- `ROUND` : 반올림
  - ROUND(number, decimals)
