class Students:
    group = 2929
    amout_of_student = 0;
    def __init__(self, heigh = 160):
        print(id(self))
        self.heigh = heigh
        Students.amout_of_student += 1

st1 = Students()
print(st1.heigh)
st2 = Students()
print(st2.heigh)
print(Students.amout_of_student)
print(st1.group)
print(st2.group)

st1.group = 2323
