def solution(files):
    answer = []
    for file in files:
        answer.append(splitFileName(file))
        
    answer.sort(key = lambda x : (x[0].lower(), int(x[1])))
    answer = [head+number+tail for head, number, tail in answer]
    return answer

def splitFileName(fileName):
    head = ''
    number = ''
    tail = ''
    for i, c in enumerate(fileName):
        if '0'<=c<='9':
            if not head:
                head = fileName[:i]
            number +=c
        elif (head and number):
            if not tail:
                tail = fileName[i:]
                # tail에서 숫자가 나올 시 다시 for문이 도는 것을 방지하기 위해 break
                break
    
    return [head, number, tail]
