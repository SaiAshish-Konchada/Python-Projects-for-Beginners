def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days / 365.25)
    print(age)

birthday = input("Enter your birthday in dd/mm/yyyy format: ")
ageCalculator(int(birthday[6:]), int(birthday[3:5]), int(birthday[0:2]))
