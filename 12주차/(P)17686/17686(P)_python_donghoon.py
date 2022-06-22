import re
def solution(files):
    return [''.join(x) for x in sorted(
        [re.split(
            "("+re.match(r'^[^\d]*(\d{1,5})', s).group(1)+")", s
        ) for s in files], 
        key=lambda x: (x[0].lower(), int(x[1]))
    )]

    """
    p = r'^[^\d]*(\d{1,5})'
    f = [re.split("("+re.match(p, s).group(1)+")", s) for s in files]
    f.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(x) for x in f]
    """