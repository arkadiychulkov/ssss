class Students:
    group = 2929
    amout_of_student = 0;
    def __init__(self, heigh = 160):
        self.heigh = heigh
        Students.amout_of_student += 1
    def grow (self, heigh = 1):
        self.heigh += heigh


st1 = Students()
st1.grow(heigh=25)
st2 = Students()
print(st1.heigh)
