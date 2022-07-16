def solution(orders, course):
    answer = []
    listOrders = []
    for str in orders:
        listOrders.append([a for a in str])
    temp = []
    for i in course:
        tmp = findOrders(i, listOrders)
        if len(tmp) != 0:
            temp.append(findOrders(i, listOrders))
    #2차원배열 1차원배열로 바꾸기
    for t in temp:
        answer+=t
    answer.sort()
    return answer

def findOrders(num, listOrders):
    #num이상의 개수를 시킨 손님의 메뉴만을 찾기
    findorder = []
    for arr in listOrders:
        if len(arr) >= num:
            findorder.append(arr)
    combinationOrder = []
    for order in findorder:
        for ele in combination(order, num):
            ele.sort()
            combinationOrder.append(ele)
    #코스요리에 추가할 경우의 수가 없으므로 바로 return
    if len(combinationOrder)==0:
        return []
    courseorder = courseOrder(combinationOrder)
    if len(courseorder)==0:
        return []
    result = []
    #[('X', 'Y')] = ['XY'] 바꾸기
    for c in courseorder:
        tmp = list(c)
        result.append(''.join(tmp))
    return result

def combination(findorder, num):
    #한손님이 주문한 메뉴에서 num개수만큼 잘라서 배열에 넣기
    result = []
    if num==0:
        return [[]]
    for i in range(len(findorder)):
        element = findorder[i]
        restElement = findorder[i+1:]
        for comb in combination(restElement, num-1):
            result.append([element]+comb)
    return result

def courseOrder(combinationorder):
    orders = []
    ordersnum = []
    result = []
    for order in combinationorder:
        if combinationorder.count(order) >= 2:
            ordersnum.append(combinationorder.count(order))
            orders.append(order)
    for n in range(len(ordersnum)):
        if ordersnum[n] == max(ordersnum):
            result.append(orders[n])
    
    #중복 course조합 제거
    result = list(set(map(tuple, result)))
    
    return result
