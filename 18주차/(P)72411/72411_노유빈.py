# 각 리스트 안의 원소들에 대해 조합으로 주어진 개수 만큼 구하기

# 구한 것 중 최댓값을 return 하기


from itertools import combinations


def solution(orders, course):
    answer = [ ]
    lists = set(''.join(orders))
    orders = [set(val) for val in orders]

    for i in course:
        max_order = 0
        course_list = list()
        comb_list = list()
        for j in orders:
            comb_list.append(list(combinations(j, i)))

        comb_list = set(sum(comb_list, []))

        for val in comb_list:
            order = 0
            comb_food = set(val)

            for order in orders:
                if set.issubset(comb_food, order):
                    order += 1

            if order >= 2:
                if max_order < order:
                    course_list = [''.join(sorted(comb_food))]
                    max_order = order
                elif max_order == order:
                    course_list.append(''.join(sorted(comb_food)))

        answer += course_list

    return sorted(set(answer))
