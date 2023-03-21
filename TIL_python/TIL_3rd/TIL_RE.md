# TIL_3rd

# 3일차 수업 정리

## 원격저장소 활용 개요
1. Push: 로컬 저장소의 버전을 원격 저장소로 보낸다.
2. Pull: 원격 저장소의 버전을 로컬 저장소로 가져온다.


## 초기 원격저장소 설정하는 법
1. GitHUb 로그인 후 +버튼 누르고 New Repository
2. 저장소 설정
    - repository 이름 설정
    - 저장소 설명(필수 아님)
    - 공개 여부 설정
3. URL 확인하기
4. 로컬 저장소에 원격 저장소 정보 설정하기
    - $ git remote add origin https://github.com/github username/저장소이름.git
5. 원격 저장소의 정보를 확인함


## 로컬 저장소의 버전을 원격 저장소로 Push하기
1. $ git push <원격저장소이름><브랜치이름>
    - 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push), 원격 저장소는 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)을 관리하는 것

2. Push 주의 사항
    - Push할 때는 인증 정보가 필수적
    - 윈도우는 아래의 화면에서 인증을 해야 함.


## 로컬 저장소의 버전을 원격 저장소로 Pull하기
1. $ git pull <원격저장소이름><브랜치이름>
    - 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함

2. git clone
    - $ git clone <원격저장소주소>, 원격 저장소를 복제하여 가져온다.

3. Pull과 clone의 차이: pull은 원격저장소 커밋을 가져오는 것이고, clone은 전체 복제다.


## 명령어 간단 정리
1. git clone <url>: 원격 저장소 복제

2. git remote -v: 원격 저장소 정보 확인

3. git remote add <원격저장소><url>: 원격저장소 추가(일반적으로 origin)

4. git remote rm <원격저장소>: 원격저장소 삭제

5. git push <원격저장소><브랜치>: 원격저장소에 push

6. git pull <원격저장소><브랜치>: 원격저장소로부터 pull


# 추가 내용 정리


## 협업 간 변경사항 충돌
1. git push origin master
    - 협업에서 푸시했을 때, error: failed to push some refs to 'https://github.com/kdt-live/test1.git'라는 내용이 뜨면서 힌트에 updates were rejected because the remote contains work that you do not have locally. 라고 명시된다면 이미 공동작업파일에 변경사항이 있으니 그것을 Pull로 받아오라는 뜻이다. 병합 후에 다시 Push를 시도해야 한다.
    - 이 과정은 merge commit이라고 칭한다.

## git ignore?
    - 버전 관리랑 상관없는 파일을 무시하는 것으로, 이미 커밋된 것은 무시하지 못한다.
    - 미리 gitignore을 설정해야 하며 그 전에 입력된 것은 삭제해도 되지만 삭제 이력 커밋이 남아있기 때문에 처음부터 잘 설정하는 것이 좋다.
    - 파이썬: venv/, 자바: nodemodules/ 등 존재한다.
    - gitignore.io/ 사이트에서 내 조건에 맞추어 찾아 복붙하면 편하다.

## 열심히 하자