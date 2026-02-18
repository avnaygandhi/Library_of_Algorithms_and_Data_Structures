class Lesson:
    def __init__(self,title,duration,require_lab):
        self.__LessonTitle=title
        self.__DurationMinutes=duration
        self.__RequireLab=require_lab
    def OutputLessonDetail(self):
        print(f"The lesson name: {self.__LessonTitle},Duration: {self.__DurationMinutes},Lab Required: {self.__RequireLab}")
class Assessment:
    def __init__(self,title,max_marks):
        self.__AssementTitle=title
        self.__MaxMarks=max_marks
        
    def OutputAssementDetail(self):
        return f"Assementment name: {self.__AssementTitle},Max marks: {self.__MaxMarks}"

class Course:
    def __init__(self,title,max_student):
        self.__CourseTitle=title
        self.__MaxStudent=max_student
        self.__NumberOfLessons=0
        self.__CourseLesson=[]
        self.__CourseAssessment=None
    def Addlesson(self,t,d,r):
         self.__NumberOfLessons+=1
         self.__CourseLesson.append(Lesson(t,d,r))

    def SetAssessment(self,title,max_marks):
        self.__CourseAssesemnet=Assessment(title,max_marks)

    def OutputCourseDetails(self):
        print(self.__CourseTitle, "max number of student:",self.__MaxStudent)
        for i in range(self.__NumberOfLessons):
            print("Lesson",i,self.__CourseLesson[i].OutputLessonDetail())
        print(self.__CourseAssesemnet.OutputAssementDetail())

MyCourse=Course("Computing",10)

MyCourse.SetAssessment("Programming",100)

MyCourse.Addlesson("Problem Solving",60,False)

MyCourse.OutputCourseDetails()
