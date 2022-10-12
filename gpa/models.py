from django.db import models

# Create your models here.

class Faculty(models.Model):
    pass

class Department(models.Model):
    name = models.CharField(max_length=200)
    faculty = ""

class Program(models.Model):
    name = models.CharField(max_length=200)
    department = ""

    #findByProgram(program)

class Course(models.Model):
    code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=1) #ForeignKey to Status
    load = models.IntegerField()

    #findByCode(code)
    #addCourse(code, title, status, load)
    #totalMark(ca, exam, resit)
    #getGrade(total)

    #Students
    #Programs
    #Semesters
    #Results
class Student(models.Model):
    matnum = models.CharField(max_length=8)
    #first_name
    #last_name
    program = ""
    cumgpa = models.DecimalField()
    honours = models.CharField(max_length=20)

    #findByAccId(acc_id)
    #fullName(first_name, last_name)
    #getEnrollmentYear(matnum)
    #getLevel(matnum)
    #getFaculty(matnum)

    #Accounts
    #Courses
    #Programs

class Result(models.Model):
    student = ""
    semester = ""
    level = ""
    course = ""
    grade = models.CharField(max_length=2)

    #findBySemester(student_id, semester, level)
    #viewResults()

    #Semesters
    #Courses
    #Constants


class Semester(models.Model):
    student_id = ""
    semester = models.IntegerField(1)
    level = models.IntegerField(30)
    gpa = models.DecimalField()

    #findBySemester(acc_id, semester, level)
    #viewSemesterGPA()
    #calculateSemesterGPA(semester, level)
    #getMark(code)
    #inputMark(code, mark)
    #getSemesterGPA()
    #getSemesterResults()

    #Courses
    #Results

class Constant(models.Model):
    constant = models.CharField(max_length=2, default="F")
    value = models.DecimalField(max_digits=2, default=0.0)

    #findByConstant(constant)
    #setGradePoint(total)
    #getGradePoint(grade)
    #findAll()

    #Result

    
