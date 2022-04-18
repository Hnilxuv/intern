import math


class Student:

    def __init__(self, sid, name, age, math, physical, chemistry, avg, rank):
        self._id = sid
        self._name = name
        self._age = age
        self._math = math
        self._physical = physical
        self._chemistry = chemistry
        self._avg = avg
        self._rank = rank


class ManagerStudent:
    list_student = []

    def generate_id(self):
        sid = 1
        if self.student_quantity() > 0:
            sid = self.list_student[0]._id
            for s in self.list_student:
                if sid < s._id:
                    sid = s._id
            maxId = sid + 1
        return sid

    def student_quantity(self):
        return self.list_student.__len__()

    def avg_mark(self, s: Student):
        avg = (s._math + s._physical + s._chemistry) / 3
        # làm tròn điểm trung binh với 2 chữ số thập phân
        s.avg = math.ceil(avg * 100) / 100

    def rank(self, s: Student):
        if (s._avg >= 8):
            s._rank = "Gioi"
        elif (s._avg >= 6.5):
            s._rank = "Kha"
        elif (s._avg  >= 5):
            s._rank = "Trung Binh"
        else:
            s._rank = "Yeu"

    def find_by_name(self, keyword):
        rs = None
        if self.student_quantity() > 0:
            for s in self.list_student:
                if keyword.upper() in s._name.upper():
                    rs = s
        return rs

    def find_by_rank(self, rank):
        rs = []
        if self.student_quantity() > 0:
            for s in self.list_student:
                if s._rank == rank:
                    rs.append(s)
        return rs

    def sortByName(self):
        self.list_student.sort(key=lambda x: x._name, reverse=False)
        self.list_student.sort(key=lambda x: x.avg, reverse=False)


