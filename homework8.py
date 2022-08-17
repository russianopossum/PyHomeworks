# Task 1
class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        print(cls, date_as_string)
        return date1
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 3999:
            print(date_as_string)
            return day, month, year
        else:
            print('Ошибка ввода данных')
d = '32-08-2022'
date2 = Date.from_string(d)
is_date = Date.is_date_valid(d)

# Task 2
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
def div():
    try:
        user_num_1 = int(input('Введите делимое: '))
        user_num_2 = int(input('Введите делитель: '))
        if user_num_2 == 0:
            raise OwnError("Ошибка, деление на ноль запрешено.")
        else:
            res = user_num_1 / user_num_2
            return res
    except ValueError:
        return "Ошибка, введено не число."
    except OwnError as err:
        return err
print(div())

# Task 3
class MyError(Exception):
    def __init__(self):
        pass
class TypeCheck:
    def __init__(self):
        self.my_list = []
    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите число в список: '))
                    ex = input(f'Добавляем число "{user_val}" в список. Продолжить? y/n: ').lower()
                    self.my_list.append(user_val)
                    if ex == 'n':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Ошибка, введено не число. Продолжить? y/n: ").lower()
                if ex == 'n':
                    print(self.my_list)
                    break
                else:
                    self.check_value()
a = TypeCheck()
a.check_value()

# Task 7
class MyComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)
    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return MyComplex(new_a, new_b)
    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return MyComplex(new_a, new_b)
z1 = MyComplex(1, 2)
z2 = MyComplex(2, 3)
print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)

# Task 4-6
class Storage:
    pass
class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
            color: str,
            purchase_price: float,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.color = color
        self.purchase_price = purchase_price
        self.printable = True if self.type in ("printer", "xerox") else False
        self.scannable = True if self.type in ("scanner", "xerox") else False
    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate
    @property
    def wholesale_price(self):
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)
    def __str__(self):
        return f"{self.type} {self.vendor} {self.model} ({self.color})"
class Printer(OfficeEquipment):
    printable = True
    scannable = False
    def __init__(self, *args):
        super().__init__('Принтер', *args)
class Scanner(OfficeEquipment):
    printable = False
    scannable = True
    def __init__(self, *args):
        super().__init__('scanner', *args)
class Xerox(OfficeEquipment):
    printable = True
    scannable = True
    def __init__(self, *args):
        super().__init__('xerox', *args)
if __name__ == '__main__':
    p1 = Printer("Epson", "XP-400", "white", 4000)
    print(p1)
class StorageError(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text
class AddStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"
class TransferStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"
class Storage:
    def __init__(self):
        self.__storage = []
    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorageError(f"{item} не оргтехника")
        self.__storage.append(item)
    def transfer(self, idx: int, department: str, item=None):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")
        item: OfficeEquipment = self.__storage[idx]
        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")
        item.department = department
    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        return self.__storage[key]
    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        del self.__storage[key]
    def __iter__(self):
        return self.__storage.__iter__()
    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"
class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            vendor: str,
            model: str,
    ):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.department = None
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"
class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Принтер', *args)
class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('scanner', *args)
class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('xerox', *args)
if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer("Epson", "XP-400"))
    storage.add(Scanner("OKI", "5367-AD"))
    storage.add(Xerox("Xerox", "F123"))
    print(storage)
    last_idx = None
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
        last_idx = idx
    print("Передаем 1 устройство")
    storage.transfer(last_idx, 'Отдел ЯФ')
    for idx, itm in storage.filter_by(department=None):
        print(idx, itm)
    print(storage)
    print("Удаляем 1 устройство")
    del storage[last_idx]
    print(storage)
class AppError(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text
class AcceptStorageError(AppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"
class TransferStorageError(AppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"
AddStorageError = AcceptStorageError
class ValidateEquipmentError(AppError):
    pass
class Storage:
    def __init__(self):
        self.__storage = []
    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddStorageError(f"Вы пытаетесь добавить на склад не оргтехнику")
        self.__storage.extend(equipments)
    def transfer(self, idx: int, department: str, item=None):
        if not isinstance(idx, int):
            raise TransferStorageError(f"Недопустимый тип '{type(item)}'")
        item: OfficeEquipment = self.__storage[idx]
        if item.department:
            raise TransferStorageError(f"Оборудование {item} уже закреплено за отделом {item.department}")
        item.department = department
    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        return self.__storage[key]
    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        del self.__storage[key]
    def __iter__(self):
        return self.__storage.__iter__()
    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"
class OfficeEquipment:
    __required_props = ("eq_type", "vendor", "model")
    def __init__(self, eq_type: str = None, vendor: str = "", model: str = ""):
        self.type = eq_type
        self.vendor = vendor
        self.model = model
        self.department = None
    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")
        object.__setattr__(self, key, value)
    def __str__(self):
        return f"{self.type} {self.vendor} {self.model}"
    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")
    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]
class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Printer', **kwargs)
class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Scanner', **kwargs)
class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Xerox', **kwargs)
if __name__ == '__main__':
    storage = Storage()
    storage.add(Printer.create(4, vendor="Epson", model="XP-400"))
    storage.add(Scanner.create(3, vendor="OKI", model="5367-AD"))
    storage.add(Scanner.create(2, vendor="OKI", model="5368-AD"))
    storage.add(Xerox.create(6, vendor="Xerox", model="F123"))
    print(storage)
    for idx, itm in storage.filter_by(department=None, vendor="OKI", model="5367-AD"):
        print(f"Резервируем {itm} в 'Отдел ЯФ'")
        storage.transfer(idx, 'Отдел ЯФ')
    for idx, itm in storage.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам")
    print(storage)
    print("Списываем 1 устройство")
    del storage[0]
    print(storage)