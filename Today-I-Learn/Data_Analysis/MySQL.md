# MySQL

<details>
<summary>목차</summary>

- [데이터베이스](#데이터베이스)
  - [DB의 기본 기능](#db의-기본-기능)
  - [DB 종류](#db-종류)
- [순서](#순서)
  - [문법 순서](#문법-순서)
  - [실행 순서](#실행-순서)
- [데이터](#데이터)
  - [1. 데이터 가져오기](#1-데이터-가져오기)
  - [2. 조건에 맞는 데이터 검색하기](#2-조건에-맞는-데이터-검색하기)
  - [3. 보고싶은 데이터 요약하기](#3-보고싶은-데이터-요약하기)
  - [4. 데이터 순서 정렬하기](#4-데이터-순서-정렬하기)
- [함수](#함수)
  - [문자열 자르기](#문자열-자르기)
  - [소수점 처리](#소수점-처리)

</details>

<details>
<summary><bold>[참고 자료]</bold></summary>

블로그 : [SELECT 쿼리 문법 순서 및 실행 순서](https://nohriter.tistory.com/129), [Tech Interview](https://gyoogle.dev/blog/computer-science/data-base/SQL%20&%20NOSQL.html)  
W3SCHOOLS : [MySQL](https://www.w3schools.com/mysql/default.asp)  
인프런 강의 : [[백문이불여일타] 데이터 분석을 위한 기초 SQL](https://inf.run/HxLC)

</details>

---

## 데이터베이스

- 데이터베이스 = 데이터를 관리하는 프로그램 + 그 안에 저장된 데이터
- DBMS = 데이터를 관리하는 프로그램

### DB의 기본 기능

1. 데이터
   - 검색
     - 질의 (SELECT)
   - 갱신
     - 등록 (INSERT)
     - 수정 (UPDATE)
     - 제거 (DELETE)
2. 동시성 제어 (누군가 이미 파일을 열고 있을 때)
   - 파일을 열 수 없다.
   - 읽기 전용으로만 열 수 있다.
   - 파일을 수정할 수 있다. (Dirty write으로 선호하지 않는다.)
3. 장애 대응  
   데이터베이스는 데이터를 한 곳이 아니라 복수의 장소에 분산해서 저장하는 등 데이터를 보호하고, 장애에 대응할 수 있어야 한다.
4. 보안  
   데이터베이스에 보존된 데이터를 어떻게 숨길 것인가?

### DB 종류

데이터베이스의 종류는 다양하지만 주로 SQL과 NoSQL이 사용된다.

1. SQL 관계형 데이터베이스 (주류)

- 장점
  - 명확하게 정의된 스키마, 데이터 무결성 보장
  - 관계는 각 데이터를 중복없이 한번만 저장
- 단점
  - 덜 유연함. 데이터 스키마를 사전에 계획하고 알려야 함. (나중에 수정하기 힘듬)
  - 관계를 맺고 있어서 조인문이 많은 복잡한 쿼리가 만들어질 수 있음
  - 대체로 수직적 확장만 가능함

2. NoSQL 비관계형 데이터베이스 (최근 자주 사용됨)  
   말 그대로 관계형 DB의 반대이다.

- 장점
  - 스키마가 없어서 유연함. 언제든지 저장된 데이터를 조정하고 새로운 필드 추가 가능
  - 데이터는 애플리케이션이 필요로 하는 형식으로 저장됨. 데이터 읽어오는 속도 빨라짐
  - 수직 및 수평 확장이 가능해서 애플리케이션이 발생시키는 모든 읽기/쓰기 요청 처리 가능
- 단점
  - 유연성으로 인해 데이터 구조 결정을 미루게 될 수 있음
  - 데이터 중복을 계속 업데이트 해야 함
  - 데이터가 여러 컬렉션에 중복되어 있기 때문에 수정 시 모든 컬렉션에서 수행해야 함 (SQL에서는 중복 데이터가 없으므로 한번만 수행이 가능)

## 순서

### 문법 순서

1. SELECT
2. FROM
3. WHERE
4. GROUP BY
5. HAVING
6. ORDER BY

### 실행 순서

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY

## 데이터

### 1. 데이터 가져오기

#### `SELECT`

데이터베이스에서 데이터를 선택하는데 쓰인다.

```MySQL
-- 모든 columns 선택
SELECT *
-- 특정 column 선택
SELECT column1, column2, ...
-- 중복 제거
SELECT DISTINCT column1, column2, ...
```

### 2. 조건에 맞는 데이터 검색하기

#### `IS NULL`

NULL 체크

```MySQL
WHERE col IS NULL
WHERE col IS NOT NULL
```

#### `WHERE`

필터링하는데 사용된다. (조건문)

```MySQL
WHERE condition
```

##### - 연산자

- 비교 연산자 (=, >, >=, <, <=, <>)  
  <> 대신 !=도 사용 가능하다.  
  문자에도 사용이 가능하다.  
  `WHERE col < 'B'` -> B이전 데이터들만 출력해준다.
- 논리 연산자 (AND, OR)
  ```MySQL
  WHERE condition1 AND condition2 AND condition3 ...
  WHERE condition1 OR condition2 OR condition3 ...
  WHERE NOT condition
  ```

##### - `LIKE`

패턴을 찾는다.

- `%` : 와일드 카드 (어떤 글자라도 상관 없다)
- `_` : 1글자 와일드 카드 (글자수 표현)

만약, 기호를 쓰고 싶다면 이스케이프 문자인 `\`를 사용한다.

```MySQL
WHERE col LIKE 'a%'
WHERE col NOT LIKE 'a%'
```

##### - `IN`

가능한 값을 여러개 지정한다. OR 한것과 같음.

```MySQL
WHERE col IN ('a', 'b')
WHERE col NOT IN ('a', 'b')
```

##### - `BETWEEN`

특정 범위 사이

```MySQL
WHERE col BETWEEN 3 AND 5
WHERE col NOT BETWEEN 3 AND 5
```

### 3. 보고싶은 데이터 요약하기

### 4. 데이터 순서 정렬하기

#### `ORDER BY`

- 오름차순 (Default) : ASC (ascending)
- 내림차순 : DESC (descending)

```MySQL
ORDER BY price ASC
ORDER BY price DESC
```

#### `LIMIT`

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
