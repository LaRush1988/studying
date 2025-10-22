from datetime import datetime, date

class Store:

    def __init__(self, address):
        self.address = address

    def get_info(self, text_date) -> str:
        date_object = datetime.strptime(text_date, '%d.%m.%Y')
        if self.__is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {text_date} {info}'

    def __is_open(self,date) -> bool:
        pass

class MiniStore(Store):

    def _Store__is_open(self, date: datetime) -> bool:
        if date.weekday() !=5 and date.weekday() !=6:
            return True
        else:
            return False



class WeekendStore(Store):

    def _Store__is_open(self, date: datetime) -> bool:
        if date.weekday() ==5 or date.weekday() ==6:
            return True
        else:
            return False


class NonStopStore(Store):

    def _Store__is_open(self, date: datetime) -> bool:
        return True


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))