from encodings import mac_latin2

from numpy.ma.core import true_divide

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2

        s3=student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1=student(56,45)
s2=student(51,54)

s3=s1+s2
print(s3)

if s1 > s2:
    print("s1 wins ")
else:
    print("s2 wins ")
print(s1)
print(s2)