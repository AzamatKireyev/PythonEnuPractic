class PersonNameException(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Некорректное имя: {self.name}. Имя должно быть строкой и содержать только буквы."


class PersonAgeException(Exception):
    def __init__(self, age, minage=1, maxage=110):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"Недопустимый возраст: {self.age}. Возраст должен быть в диапазоне от {self.minage} до {self.maxage}."


class PersonGenderException(Exception):
    def __init__(self, gender):
        self.gender = gender

    def __str__(self):
        return f"Некорректный пол: {self.gender}. Пол должен быть 'male' или 'female'."


class Person:
    def __init__(self, name, age, gender):
        if not isinstance(name, str) or not name.strip() or not name.replace(" ", "").isalpha():
            raise PersonNameException(name)

        if not isinstance(age, int) or not (1 <= age <= 110):
            raise PersonAgeException(age)

        if gender not in ("male", "female", "Male", "Female"):
            raise PersonGenderException(gender)

        self.__name = name
        self.__age = age
        self.__gender = gender

    def display_info(self):
        print(f"Имя: {self.__name}  Возраст: {self.__age}  Пол: {self.__gender}")


def input_person():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    gender = input("Введите пол (male/female): ")

    return Person(name, age, gender)

    person = None

while True:
    print("\n=== МЕНЮ ===")
    print("1. Ввести данные о человеке")
    print("2. Показать информацию о человеке")
    print("0. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        try:
            person = input_person()
            print("Данные успешно введены.")
        except ValueError:
            print("Ошибка: возраст должен быть числом.")
        except PersonNameException as e:
            print(e)
        except PersonAgeException as e:
            print(e)
        except PersonGenderException as e:
            print(e)
        except Exception as e:
            print("Ошибка:", e)

    elif choice == "2":
        if person is None:
            print("Сначала введите данные о человеке.")
        else:
            person.display_info()

    elif choice == "0":
        print("Программа завершена.")
        break

    else:
        print("Ошибка: введите 0, 1 или 2.")