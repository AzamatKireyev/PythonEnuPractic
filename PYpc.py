class SmartPhone:
    def __init__(self, manufacturer, model, memory, powerBattery):
        self.manufacturer = manufacturer
        self.model = model
        self.memory = memory
        self.power = min(100, max(0, powerBattery))

    def use(self, amount):
        if amount < 0:
            print("Қуат мөлшері теріс болмауы керек!")

            return 
        self.power = max(0, self.power - amount)
        print(f"Қолданылған {amount}% қуат. Қазіргі қуаты : {self.power}%")

    def charge(self, amount):
        if amount < 0:
            print("Қуат мөлшері теріс болмауы керек!")
            return
        self.power = min(100, self.power + amount)
        print(f"Қуатталды {amount}%. Қазіргі қуаты : {self.power}%")

    def __str__(self):
        return f"Өндіруші: {self.manufacturer}, Моделі: {self.model}, Память: {self.memory} ГБ, Заряды: {self.power}%"


phone = SmartPhone("Apple", "iPhone 13", 128, 100)

while True:
    print("\n=== MENU ===")
    print("1. Телефон туралы ақпаратты көрсету")
    print("2. Телефонмен қолдану")
    print("3. Телефон қуатын зарядтау")
    print("0. Шығу")
    
    choice = input("Әрекетті таңдаңыз: ")

    if choice == "1":
        print(phone)
    elif choice == "2":
        try:
            percent = float(input("Қанша % қуат жұмсау керек? "))
            phone.use(percent)
        except ValueError:
            print("Қате: сан енгізу керек!")
    elif choice == "3":
        try:
            percent = float(input("Қанша % зарядтау керек? "))
            phone.charge(percent)
        except ValueError:
            print("Қате: сан енгізу керек!")
    elif choice == "0":
        print("Программа жұмысы аяқталды.")
        break
    else:
        print("Енгізілген мән 0 мен 3 арасында болуы керек.")