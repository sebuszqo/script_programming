from day import Day

class Term():
    def __init__(self, day = Day.MON ,hour: int = 0, minute: int = 0 , duration = 90):
        self._day = day
        if not isinstance(self._day, Day):
            raise ValueError('Wrong day type')
        self.hour = hour
        self.minute = minute
        self.duration = duration

    # finding what day _day.value means
    def __str__(self):
        day = {      1: "Poniedziałek",
                     2: "Wtorek",
                     3: "Środa",
                     4: "Czwartek",
                     5: "Piątek",
                     6: "Sobota",
                     7: "Niedziela",
         }[self._day.value]
        return f'{day} {self.hour}:{self.minute} [{self.duration}]'
    
    #DRY method -- to check if given hour minute and day is ealier or later 
    @classmethod
    def isTrueOrFalse(cls, termToCheck, termin):
        if termin.hour < termToCheck.hour:
            return False
        elif (termin.hour == termToCheck.hour and termin.minute < termToCheck.minute):
            return False
        return True

    #DRY method -- to check if given days are the same, days hours and minutes
    @classmethod
    def sameDay(cls, termToCheck, termin):
        if (termin.hour == termToCheck.hour and termin.minute == termToCheck.minute and termin._day.value == termToCheck._day.value and termin.duration == termToCheck.duration):
            return True
        return False

    #function to check is terms are ealier, gives False or True
    def earlierThan(self, termin):
        # creating new instance of Term class 
        termToCheck = Term(self._day, self.hour, self.minute)
        if (Term.sameDay(termToCheck, termin)):
            return bool(False)
        result = Term.isTrueOrFalse(termToCheck,termin)
        return bool(result)

    #function to check is terms are later, gives False or True
    def laterThan(self, termin):
        # creating new instance of Term class -- cuz I had problems with t
        termToCheck = Term(self._day, self.hour,self.minute)
        if (Term.sameDay(termToCheck,termin)):
            return bool(False)
        result = Term.isTrueOrFalse(termToCheck,termin)
        #using same DRY method to check F/T so in return has to be 'not'
        return not bool(result)


        # if termin.hour > self.hour:
        #     return False
        # elif (termin.hour == self.hour and termin.minute > self.minute):
        #     return False
        #return True
        # print(self._day.value)

    def equals(self, termin):
        termToCheck = Term(self._day, self.hour, self.minute, self.duration)
        return bool(Term.sameDay(termToCheck,termin))

    # Overloading Functions and Operators in Python
    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    def __gt__(self, termin):
        return not self.earlierThan(termin)

    def __ge__(self, termin):
        return not self.earlierThan(termin) or self.equals(termin)

    def __eq__(self, termin):
        return self.equals(termin)

    def __sub__(self, termin):
        duration = ((self.hour + 1)- termin.hour)*60 + ((self.minute + 30) - termin.minute) + ((self._day.value - termin._day.value) * 24)*60
        # newTerm = Term(termin._day, termin.hour, termin.minute, duration)
        return Term(termin._day, termin.hour, termin.minute, duration)
        
if __name__ == "__main__":
    term1 = Term(Day.MON, 8, 30)
    term2 = Term(Day.TUE, 9, 45, 30)
    term3 = Term(Day.TUE, 9, 45, 90)
    print("term1 < term2:", term1 < term2)   # Ma się wypisać True
    print("term1 <= term2:", term1 <= term2) # Ma się wypisać True
    print("term1 > term2:", term1 > term2)   # Ma się wypisać False
    print("term1 >= term2:", term1 >= term2) # Ma się wypisać False
    print("term2 == term2:", term2 == term2) # Ma się wypisać True
    print("term2 == term3:", term2 == term3)
    term4 = term3 - term1
    print(term4)
    # term1 = Term(Day.TUE, 9, 45)
    # print(term1)                     
    # term2 = Term(Day.WED, 10, 15)
    # print(term2)                     
    # print(term1.earlierThan(term2)); 
    # print(term1.laterThan(term2));  
    # print(term1.equals(term2)); 

        
# try:
#     term1 = Term(Day.TUE, 9, 45)
#     term2 = Term(Day.TUE, 10, 15)
# except:
#     print('Podales zle dzien')
# term1.__str__()
# print(term1.earlierThan(term2))
# print(term1.laterThan(term2))
# print(term1.equals(term2))

# klasa.earlierThan(secondclass)