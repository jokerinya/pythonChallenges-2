class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, fName, lName, id, scores=[]):
        super().__init__(fName, lName, id,)
        self.scores = scores

    def calculate(self):
        _average = sum(self.scores)/len(self.scores)
        _state = ""
        if _average >= 90:
            _state = "O"
        elif _average >= 80:
            _state = "E"
        elif _average >= 70:
            _state = "A"
        elif _average >= 55:
            _state = "P"
        elif _average >= 40:
            _state = "D"
        else:
            _state = "T"
        return _state


firstName = input("First name: ")
lastName = input("Last name: ")
idNum = int(input("ID number(Integer Please): "))
print("Enter notes with comma between each one. Exp: 34, 23, 12,")
scores = [int(i.strip()) for i in input("Scores: ").strip().split(',')]
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
