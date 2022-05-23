def solution(N, build_frame):
    pillar = {} # 0
    bridge = {} # 1

    def check(y, x, c):
        if c == 0:
            if y == 0 or (y, x-1) in bridge or (y, x) in bridge or (y-1, x) in pillar:
                return True
            else: return False
        else:
            if (y-1, x) in pillar or ((y, x-1) in bridge and (y, x+1) in bridge) or (y-1, x+1) in pillar:
                return True
            else: return False

    for x, y, a, b in build_frame:
        if not b:
            if a == 0:
                pillar.pop((y, x))
            else:
                bridge.pop((y, x))

            flag = True

            for ty, tx in pillar:
                if pillar[(ty, tx)]:
                    flag &= check(ty, tx, 0)

            for ty, tx in bridge:
                if bridge[(ty, tx)]:
                    flag &= check(ty, tx, 1)

            if not flag:
                if a == 0:
                    pillar[(y, x)] = 1
                else:
                    bridge[(y, x)] = 1


        elif check(y, x, a):
            if a == 0:
                pillar[(y, x)] = 1
            else:
                bridge[(y, x)] = 1

    ans = [(x, y, 0) for y, x in pillar] + [(x, y, 1) for y, x in bridge]
    ans.sort()
    return ans
