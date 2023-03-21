

# MYSQL 개발 환경 구축


## MYSQL 설치
    1) https://dev.mysql.com/downloads/installer/ 접속
    
    2) mysql-installer-community-8.0.32 파일 다운로드
    
    3) 로그인 화면이 나올 경우 'No, thanks' 눌러주기
    
    4) 다운로드 후  installer 창이 뜨면 [License Agreement]에서 <I accept the license terms>를 체크하고 다음으로 넘어간다.
    
    5) [Choosing a Setup Type]은 설치할 유형을 선택 가능한데, 제일 아래의 <Developer Default>을 선택하고 <Next>를 클릭한다.
    
    5-1) 여기서 다른 버전(Server only, Client only, Full, Custom)들은 각각 서버만, 클라이언트 및 관련 툴, 전체, 사용자 설정 버전이다.

    6) 그 후 쭉 Next 와 excute로 넘어가다가 Accounts and Roles 화면에서 사용자의 비밀번호를 설정하고 Next로 넘어간다.

    7) 그 후 쭉 Next 와 excute로 넘어가다가 Connect To Server 에서 Password를 입력

    8) 그 후 쭉 Next 와 excute로 넘어가다가 MYSQL shell과 Workbench 창이 뜨면 설치 완료된 것이에요잉

## MYSQL 설치 확인 및 추가 설정
    1) Workbench 창에서 MYSQL Connections 밑에 클릭해서 로그인합니다.

    2) Edit에서 Preference 클릭해주세용

    3) 거기서 Query Editor 클릭하고 Use UPPERCASE keywords 및 Change keywords to UPPER CASE 체크하고 OK 클릭해줍니다.



## 샘플 데이터베이스 설치 및 추가, 확인
    1) MYSQL에서 전통적으로 'employees'라는 이름의 샘플 데이터베이스를 제공하지만 우리는 멀티캠퍼스에서 제공해주는거 쓸꺼에요잉

    2) Workbench에서 Administration에 들어가 Data Import/Restore 눌러줍니다

    3) Import from Self-Contained File 체크하고 ...클릭 해주고 다운로드한 샘플 데이터베이스 선택하고 Start Import 해줍니다

    4) Schemas 클릭하고 새로고침 버튼 클릭해줍니다.

    5) 샘플 데이터베이스인 classicmodels 확인 해줍니다

    6) 클릭해주고 Query 에디터 클릭하고 쿼리문 'SELECT * FROM customers;' 입력해주고 실행해봅니다. 번개모양 클릭해주면 됩니다.

    7) 출력 확인하면 꿑!



## 한글 입력 설정
    1) 데이터 베이스 옆에 도구 모양 스패너처럼 생긴거 클릭하고 charset/collation 부분 utf8이랑 utf8_bin으로 변경해줍니다.

    2) 마지막은 그냥 Apply 클릭해주면 됩니다요.