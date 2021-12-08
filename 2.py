days_31 = {1, 3, 5, 7, 8, 10, 12}
days_30 = {4, 6, 9, 11}


class Calendar:

    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError("Should have type int")
        if not 0 < day <= self.amount_of_days():
            raise ValueError("Outside the number of days in the month")
        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError("Should have type int")
        if not 0 < month < 13:
            raise ValueError("Outside the number of months")
        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("Should have type int")
        if not 0 < year < 5000:
            raise ValueError
        self._year = year

    def leap_check_year(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            return True
        else:
            return False

    def amount_of_days(self):
        if self.month in days_30:
            return 30
        elif self.month in days_31:
            return 31
        elif self.month == 2:
            if self.leap_check_year():
                return 29
            return 28

    def __iadd__(self, other):
        day = self.day
        month = self.month
        year = self.year
        day += other.day
        month += other.month
        year += other.year

        if month > 12:
            month = month - 12
            year += 1
        if day > self.amount_of_days():
            day -= self.amount_of_days()
            month += 1
        self.day = day
        self.month = month
        self.year = year
        return self

    def __isub__(self, other):
        day = self.day
        month = self.month
        year = self.year
        day -= other.day
        month -= other.month
        year -= other.year

        if year < 0:
            raise ValueError("This is the date before our era")
        if month < 1:
            month += 12
            year -= 1
        if day < 1:
            month -= 1
            if month == 0:
                months = 12
            day += self.amount_of_days()
        self.day = day
        self.month = month
        self.year = year
        return self

    def __lt__(self, other):
        if self.year < other.year:
            return True
        else:
            if self.month < other.month:
                return True
            else:
                if self.day < other.day:
                    return True
        return False

    def __le__(self, other):
        if self.year <= other.year:
            return True
        else:
            if self.month <= other.month:
                return True
            else:
                if self.day <= other.day:
                    return True
        return False

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __eq__(self, other):
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        return False

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


date_1 = Calendar(30, 6, 1804)
date_2 = Calendar(30, 12, 1603)
date_3 = Calendar(1, 12, 2000)
date_1 -= date_2
date_2 += date_1
print(date_1)
print(date_2)
print(date_1 > date_2)
print(date_1 < date_2)
print(date_2 <= date_3)
print(date_3 >= date_1)
print(date_1 == date_2)
print(date_1 != date_3)