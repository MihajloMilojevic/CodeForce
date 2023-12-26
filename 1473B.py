import math

def case():
    s = input()
    t = input()
    m = s if len(s) < len(t) else t
    lcm_len = math.lcm(len(s), len(t))
    lcm = m * (lcm_len // len(m))
    lcm_s = s * (lcm_len // len(s))
    lcm_t = t * (lcm_len // len(t))
    if lcm_s != lcm or lcm_t != lcm:
        return "-1"
    else:
        return lcm

q = int(input())
rez = []
while q:
    q -= 1
    rez.append(case())
for r in rez:
    print(r)