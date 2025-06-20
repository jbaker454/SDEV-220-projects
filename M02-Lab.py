def GetStudentInfo():
    studentLastName = input("student last name: ")
    studentFirstName = input("student first name: ")
    studentGPA = float(input("student GPA: "))
    return studentLastName,studentFirstName,studentGPA

def StudentDeansListCheck(studentGPA):
    if studentGPA >= 3.5:
        DeanList = True
    else:
        DeanList = False
    if studentGPA >= 3.25:
        HonorRoll = True
    else:
        HonorRoll = False
    return DeanList,HonorRoll

def Main():
    while True:
        quit = input("type 'ZZZ' to quit program hit enter to continue: ")
        if quit == "ZZZ":
            break
        studentLastName,studentFirstName,studentGPA = GetStudentInfo()
        DeanList,HonorRoll = StudentDeansListCheck(studentGPA)
        print(studentFirstName,studentLastName,"has a gpa of", studentGPA)
        if DeanList == True:
            print("student has made the Deans list")
        if HonorRoll == True:
            print("student has made the honor roll")

Main()