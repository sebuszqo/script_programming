
from term import Term
from day import Day

class Lesson():
    def __init__(self, term: Term, name: str, teacherName: str, year: int, fullTime: bool= True ):
        self.term = term
        self.name = name 
        self.teacherName = teacherName
        self.year = year
        self.fullTime = self.typeOfStudies()

    
    def typeOfStudies(self):
        if ((self.term._day.value in [1,2,3,4] and self.term.hour <= 20) or (self.term._day.value == 5 and self.term.hour < 17)) and self.term.hour >= 8:
            return True
        else:
            return False
        
    # sprawdzam juz przesuniety w tyl lub w przod dzien
    # sprawdzam ten przesuniety dzien / godzine majac wiadomosc czy nalezy to do studiow stacjonarnych lub niestacjonranych
    # dzieki temu moge ocenic czy przesunieta juz data nalezy do przedzialu czasu ktory odpowiada jej 'rodzajowi' studiow
    # nie moze byc <= np. 20 bo 20:40 wtedy tez zostanie zaliczona
    def can_be_transferred_to(term: Term, full_time: bool) -> bool:
        if full_time and term._day.value in [1,2,3,4]:
            if term.hour >= 8 and term.hour < 20:
                return True
        elif full_time and term._day.value in [5]:
            if term.hour >= 8 and term.hour < 17:
                return True
        elif not full_time and term._day.value in [5]:
            if term.hour >= 17 and term.hour < 20:
                return True
        elif not full_time and term._day.value in [6,7]:
            if term.hour >= 8 and term.hour < 20:
                return True
        return False

    def ealierDay(self):
        new_day = Day(7 if self.term._day.value - 1 == 0 else self.term._day.value - 1)
        new_term = Term(new_day, self.term.hour, self.term.minute, self.term.duration)
        # wystarczy sprawdzenie czy nowy termin spelnia warunki dla studiow stacjonarnych lub niestacjonarnych w zaleznosci ktore wybralismy
        # true - stacjonarne false - niestacjonarne
        if self.can_be_transferred_to(new_term, self.fullTime):
            self.term = new_term
            return True
        else:
            return False
        

    def laterDay(self):
        new_day = Day(1 if self.term._day.value + 1 == 8 else self.term._day.value + 1)
        new_term = Term(new_day, self.term.hour, self.term.minute, self.term.duration)
        if self.can_be_transferred_to(new_term, self.fullTime):
            self.term = new_term
            return True
        else:
            return False

    # method to use DRY methodology
    def timeSetUp(self):
        hoursToChange = self.term.duration // 60
        minutesToChange = self.term.duration % 60
        return [hoursToChange, minutesToChange]

    def laterTime(self):
        # hoursToChange = self.term.duration // 60
        # # minutesToChange = self.term.duration - 60 * hoursToChange
        # minutesToChange = self.term.duration % 60
        arrayOfTime = self.timeSetUp()
        new_hour = self.term.hour + arrayOfTime[0]
        new_minutes = self.term.minute + arrayOfTime[1]

        if new_minutes >= 60:
            new_hour += 1
            new_minutes -= 60 

        new_term = Term(self.term._day, new_hour, new_minutes, self.term.duration)
        if self.can_be_transferred_to(new_term, self.fullTime):
            self.term = new_term
            return True
        else:
            return False

    def ealierTime(self):
        # hoursToChange = self.term.duration // 60
        # # minutesToChange = self.term.duration - 60 * hoursToChange
        # minutesToChange = self.term.duration % 60
        arrayOfTime = self.timeSetUp()
        new_hour = self.term.hour - arrayOfTime[0]
        new_minutes = self.term.minute - arrayOfTime[1]

        if new_minutes < 0:
            new_hour -=1
            new_minutes += 60 

        new_term = Term(self.term._day, new_hour, new_minutes, self.term.duration)
        if self.can_be_transferred_to(new_term, self.fullTime):
            self.term = new_term
            return True
        else:
            return False

    def __str__(self) -> str:
        # return 'pawel topa'
        # return '''Systemy operacyjne (Piątek 17:40 [90]) \n2 rok studiów niestacjonarnych \nProwadzący: Paweł Topa'''
        return f'''{"-"*50}\n{self.name} ({self.term}) \n{self.year} rok studiów {"stacjonarnych" if self.fullTime else "niestacjonarnych"} \nProwadzący: {self.teacherName}\n{"-"*50}'''

if __name__ == "__main__":
    # some manual tests before unitests
    lesson = Lesson(Term(Day.TUE, 9, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
    print(lesson)
    # lesson.earlierTime()
    # term2 = Term(Day.FRI, 9, 45, 30)
    # termafter = Lesson(term2, 'name', 'name', 2, False)
    # print(termafter)
    # print(termafter.term._day.value)
    # print(termafter.laterDay())
    # print(termafter.term._day.value)