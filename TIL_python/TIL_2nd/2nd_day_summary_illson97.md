# 2일차 정리

## 버전관리란?
    - 버전관리란 동일한 정보에 대한 여러 버전을 관리하는 것을 말한다.
    - ex) Google document 버전관리, Markdown, git 등등

## Git이란?
    - Git은 분산버전관리시스템으로 코드의 버전을 관리하는 도구
    - 리눅스 커널을 위한 도구로 리누스 토르발스가 개발
    - 컴퓨터 파일의 변경사항 추적 및 여러 명 사용자 간 해당 파일들의 작업 조율

## 분산버전관리시스템(DVCS)
    - 중앙집중식버전관리시스템은 중앙에서 버전을 관리하고 파일 받아서 사용
    - 분산버전관리시스템은 원격 저장소를 통하여 협업하고, 모든 히스토리를 클라이언트들이 공유

## git의 기본 흐름
1. 작업한 파일이 놓이는 곳은 Working directory
2. Working directory에서 git add를 거치면 Staging area로 이동
3. git commit -m '<커밋메시지>'을 통해 HEAD로 이동되면서 버전 기록


## Git 기본 명령어

1. git init
    - 특정 폴더를 git 저장소를 만들어 git로 관리
    - git 폴더 생성되며, git bash에서 (master)라는 표기 확인 가능

2. git add <file>
    - Working directory 상의 변경 내용을 Staging area에 추가하기 위해 사용
    - untracked 상태 -> Staged 변경
    - modified 상태 -> Staged 변경    

3. git commit -m '<커밋메시지>'
    - Staged 상태 파일들 커밋통해 버전으로 기록
    - SHA-1 해시를 사용하여 40자 길이의 체크섬 생성, 고유한 커밋 표기
    - 커밋 메시지는 명확히 작성할 것

4. git log
    - 현재 저장소에 기록된 커밋 조회(3통 상태에서 사용)
    - 다양한 옵션으로 로그 조회 가능
    - git log-1 최근 1개, git log -- oneline 한줄로, git log -2 -- oneline 최근 2개를 한줄로

5. git status
    - Git 저장소에 있는 파일의 상태를 확인하기 위해 사용(1, 2통에서 사용)

## 파일 라이프 사이클

1. 1통에서 사용되는 용어
    - Untracked files: 트래킹되지 않은 파일들, 파일 만들고 add하지 않았을 때
    - Changes not staged for commit: 커밋을 위해 staged가 아닌 변경 사항들, 커밋된적 있는 파일을 수정한 상태,수정되고 add되지 않음

2. 2통에서 사용되는 언어
    - Changes to be committed: 커밋될 변경사항들, 파일 만들고 add된 상태

3. Nothing to commit, working tree clean
    - 모두 add, commit된 상태

4. Tracked
    - Unmodified: git status에 나타나지 않음
    - Modified: Changes not staged for commit
    - Staged: Changes to be committed

5. Untracked
    - 버전으로 관리된 적 없는 파일(파일을 새로이 만드는 경우)
