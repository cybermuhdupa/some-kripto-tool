import inspect, re

DEFAULT = 'kingkong'

def vvv(p = DEFAULT):
    if p == DEFAULT:
        print()
        return

    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvvv\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            print(m.group(1) + ' =', p)
            return

def vvvbytes(p):
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvvvbytes\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            print(m.group(1) + ' =', bbb(p))
            return

def bbb(p):
    ans = []
    for i in p:
        res = hex(i)[2:].zfill(2).upper()
        ans.append(res)
    return ' '.join(ans)

def varnameandval(p):
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvarnameandval\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1), p