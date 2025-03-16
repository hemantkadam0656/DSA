class Grades:
    def __init__(self, grades):
        self.grades = grades
        
    def Print_grades(self):
        return grades

    def add_New_grade(self):
        num = int(input())
        grades.append(num)
        return grades

    def Totle_grades(self):
        n = len(grades)
        tot = int(sum(grades)/n)
        return tot


if __name__ == '__main__':
    grades = [83,86,90,78,90,95]
    grd = Grades(grades)
    print(grd.Print_grades())
    print(grd.add_New_grade())
    print(grd.Totle_grades())
