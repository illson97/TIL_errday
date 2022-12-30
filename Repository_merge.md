# Repository_merge

## 1. Remote Repository 생성
- 깃허브에서 새로운 레포지토리 생성
- 새로운 레포지토리는 부모, merge되는 레포지토리는 자식이라 칭함

## 2. Local이랑 Remote Repository 연결
- $ git init: 깃 초기화
- $ git clone <url>: 부모 레포지토리 클론

## 3. Remote 추가
- $ git remote add <리모트명> <레포지토리 url>
- 자식 레포지토리를 추가해야함 

## 4. Subtree 생성
- $ git subtree add --prefix=<저장할 폴더명> <자식 레포지토리의 remote명> <부모레포지토리의 브랜치>

- fatal: ambiguous argument 'HEAD': unknown revision or path not in the working tree...
이와 같은 오류가 발생했다면

- 방금 생성한 부모 레포지토리에 아무것도 존재하지 않는다면 Dummy File을 생성하고 커밋한다. 물론 커밋 밑 푸시까지 마쳐야 한다.

- remote를 add만 하고 fetch만 받아 내용이 없는 상태기 때문에 ""$ git fetch <remote명> <브랜치 명>"" 으로 내용을 받아오자

## 5. Push 진행
- $ git push <부모 레포지토리의 remote명> <브랜치명>

#
## END!