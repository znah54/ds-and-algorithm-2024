# file : ds04_orderedList.py
# desc : 선형리스트 프로그램

kakaotalk=[] # 빈 배열 생성

#데이터 추가 함수
def add_data(friend):
    kakaotalk.append(None) # 배열 빈자리 생성
    size = len(kakaotalk) # 배열 전체 크기
    kakaotalk[size-1] = friend

#데이터 삽입함수
def insert_data(pos, friend):
    if pos < 0 or pos > len(kakaotalk):
        print('데이터 삽입범위 초과')
        return # 함수를 빠져나감
    
# 정상적인 처리시작
    kakaotalk.append(None) # 빈칸추가
    size=len(kakaotalk) # 배열 현재 크기
    # 데이터 삽입 위치 데이터 하나씩 뒤로 보냄
    for i in range(size-1, pos, -1): # 역순으로 맨뒤에서 부터
        kakaotalk[i] = kakaotalk[i-1]
        kakaotalk[i-1] = None
    kakaotalk[pos] = friend

#데이터 삭제함수
def delete_data(pos): # 데이터 삭제시는 위치값만
    if pos < 0 or pos > len(kakaotalk):
        print('데이터 삽입범위 초과')
        return
    
    size = len(kakaotalk)
    kakaotalk[pos] = None # 데이터 삭제

    for i in range(pos+1, size):
        kakaotalk[i-1] = kakaotalk[i] # 뒤에 값을 앞으로
        kakaotalk[i] = None

    del(kakaotalk[size-1])