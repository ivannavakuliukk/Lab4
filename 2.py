days_31 = {1, 3, 5, 7, 8, 10, 12}
days_30 = {4, 6, 9, 11}


class Calendar:

    def __init__(self, day, month, year):
        self.month = month
        self.day = day
        self.year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError
        if self.month in days_31:
            if not 0 < day < 32:
                raise ValueError
        if self.month in days_30:
            if not 0 < day < 31:
                raise ValueError
        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError
        if not 0 < month < 13:
            raise ValueError
        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError
        if not 0 < year < 2023:
            raise ValueError
        self._year = year

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


date_1 = Calendar(31, 6, 2012)
print(date_1)