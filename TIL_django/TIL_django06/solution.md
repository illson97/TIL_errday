

"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)

solution
todo = Todo(content='실습 제출', deadline='2023-03-28', priority='2', completed='False')
"""

"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)

solution
todo = Todo(content='데일리 설문(오후) 제출', deadline='2023-03-28')
"""

"""
3. 임의의 할 일 5개 생성

solution
todo = Todo(content='금일 내용 복습', deadline='2023-03-28', priority='4')
todo = Todo(content='점프 투 장고 책 학습', deadline='2023-03-28', priority='4')
todo = Todo(content='방 청소', deadline='2023-03-28', priority='2')
todo = Todo(content='docker 학습', deadline='2023-03-28', priority='3')
todo = Todo(content='필요 기술 스택 조사', deadline='2023-03-28', priority='1')
"""

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회

solution
Todo.objects.order_by('pk').values()
"""

"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회

solution
Todo.objects.order_by('-priority').values()
"""

"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)

solution
Todo.objects.filter(pk=1).values()
"""