
import sys

def addCorse(course):
    listOfCoursesAndStudents[course] = []
    return listOfCoursesAndStudents

def removeCourse(course):
    listOfCoursesAndStudents.pop(course)
    return

def addPersonToCourse(name, course):
    return listOfCoursesAndStudents[course].append(name)

def removePersonFromCourse(name,course):
   print(listOfCoursesAndStudents[course])
   return listOfCoursesAndStudents[course].remove(name)


if __name__ == '__main__':
   maxNumOfCourses = sys.argv[1]
   maxNumOfStudents = sys.argv[2]
   listOfCoursesAndStudents = {'kurs1': ['studentA']}
   while True:
    try:
        print(f'Aktualny stan kursu: {listOfCoursesAndStudents}')
        print('Wybierz co chcesz zrobic?')
        try:
            x = int(input('1.Zapisz osobe na kurs\n 2.Wypisz osobe z kursu\n 3.Dodaj kurs \n 4.Usun kurs\n'))
        except ValueError:
            print('Zlego wyboru dokonales!')
        if x == 1:
            numOfPeople = int(input('ile osob chcesz wpisac?'))
            for _ in range(numOfPeople):
                name = input('Podaj imie: ')
                course = input('Podaj nazwe kursu: ')
                addPersonToCourse(name, course)
        elif x == 2:
            name = input('Podaj imie: ')
            course = input('Podaj nazwe kursu: ')
            removePersonFromCourse(name, course)
        elif x == 3:
            course = input('Podaj nazwe nowego kursu: ')
            addCorse(course)
        elif x == 4:
            course = input('Podaj nazwe kursu do usuniecia: ')
            removeCourse(course)
    except EOFError:
        print(f'\nLISTA KURSOW I KURSANTOW {listOfCoursesAndStudents}')
        break
    except KeyError:
        print(' \n Podales zlą nazwe kursu  Sprobuj jeszcze raz!\n')
    except ValueError:
        print(' \n Podales zle imie osoby!  Sprobuj jeszcze raz!\n')
            



