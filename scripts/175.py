from fractions import Fraction
target = Fraction(123456789, 987654321)
# target = Fraction(101, 266)
# target = Fraction(13, 17)
target
from fractions import Fraction
class SternBrocot:
    def __init__(self):
        pass

    def traverse(self, t: Fraction):
        self.sb = []
        self.last = None
        self.cnt = 0
        self.l = (0, 1)
        self.m = (1, 1)
        self.r = (1, 0)
        self.level = 0
        self.pos = 0
        def iter():
            m_f = Fraction(*self.m)
            if t == m_f:
                if self.last != "L":
                    if self.last != None:
                        self.sb.append(self.cnt)
                    self.last = "L"
                    self.cnt = 0
                self.cnt += 1
                self.sb.append(self.cnt)
                return ",".join([str(e) for e in reversed(self.sb)])
            elif m_f < t:
                if self.last != "R":
                    if self.last != None:
                        self.sb.append(self.cnt)
                    self.last = "R"
                    self.cnt = 0
                self.cnt += 1
                self.l = self.m
                self.m = (self.l[0] + self.r[0], self.l[1] + self.r[1])
            else:
                # print("Going Left!")
                if self.last != "L":
                    if self.last != None:
                        self.sb.append(self.cnt)
                    self.last = "L"
                    self.cnt = 0
                self.cnt += 1
                self.r = self.m
                self.m = (self.l[0] + self.r[0], self.l[1] + self.r[1])
            # assert(Fraction(*self.l) <= t and t <= Fraction(*self.r))
            return 0
        while True:
            r = iter()
            if r:
                print(r)
                return r
s = SternBrocot()
s.traverse(target)