from itertools import combinations #조합 쓰는거는 제 머리속이 아니라 구글에서 나왔어요 .. 

def solution(orders, course):

    temp = dict() # 각 코스 요리 조합의 맞는 개수를 세기 위해, 딕셔너리 구조를 이용하였습니다. 

    for num in course:
        temp[num] = []

    for order in orders:
        for num in course:
            if num > len(order): #모든 손님은 두개이상의 메뉴를 주문해야한다.
                break
            else:
                temp[num] += list(combinations(sorted(list(order)),num))

    result = []
    for menus in temp.values():
        max_num = 2 # 2명이상이 고른 메뉴 조합이어야 함으로.
        for menu in menus:
            cnt = menus.count(menu)
            if cnt>max_num:
                max_num = cnt

        for menu in menus:
            m = ''.join(menu)
            if max_num == menus.count(menu) and m not in result:
                result.append(m)

    return sorted(result)