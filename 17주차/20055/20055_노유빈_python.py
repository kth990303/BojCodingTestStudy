# 왜 계속 무한루프인지 모르겠네요.. 문제 이해를 잘못한것 같기도 합니다.

a = list(map(int, input().split(" "))) # 길이, K input
b = list(map(int, input().split(" "))) # 내구도 input

answer = 1

# 내구도 1 이상인 것들 1씩 제거 해주는 함수

def delete(list):
    for i in range(0,int(len(list)/2)):
        if list[i]>0:
            list[i] = list[i]-1

    return list

# 리스트가 한번 회전하는 함수

def rotate(list):

    list[0]=list[-1]

    for i in range(1,len(list)):
        list[i] = list[i-1]

    return list



while True:
    if b.count(0) >= a[1]:
        break
    else:
        b=delete(b)
        b=rotate(b)
        answer+=1
        
        

print(answer)