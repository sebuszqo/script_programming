from DeanerySystem.term import Term


from term import Term

class Lesson():
    def __init__(self, term: Term, name: str, teacherName: str, year: int, fullTime: bool ) -> None:
        self.term = term
        self.name = term 
        self.teacherName = teacherName
        self.year = year
        self.fullTime = fullTime
        