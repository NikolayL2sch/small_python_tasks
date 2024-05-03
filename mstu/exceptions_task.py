import json
import datetime
from api import register_booking


class Booking:
    def __init__(self, room_name: str, start: datetime.datetime = None, end: datetime.datetime = None):
        if start is None or end is None or start > end:
            raise ValueError
        self.room_name = room_name
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        if value > self.end:
            raise ValueError
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if value < self.start:
            raise ValueError
        self._end = value

    @property
    def duration(self) -> int:
        return (self.end - self.start).total_seconds() // 60

    @property
    def start_date(self) -> str:
        return self.start.strftime("%Y-%m-%d")

    @property
    def end_date(self) -> str:
        return self.end.strftime("%Y-%m-%d")

    @property
    def start_time(self) -> str:
        return self.start.strftime("%H-%M")

    @property
    def end_time(self) -> str:
        return self.start.strftime("%H-%M")


def create_booking(room_name, start, end) -> str:
    print('Начинаем создание бронирования')
    try:
        booking = Booking(room_name, start, end)
    except ValueError:
        raise ValueError

    try:
        booking_info = {'room_name': room_name, 'duration': booking.duration,
                        'start_date': booking.start_date, 'end_date': booking.end_date,
                        'start_time': booking.start_time, 'end_time': booking.end_time}
        created = register_booking(booking)
    except KeyError:
        booking_result = {'created': False, 'msg': 'Комната не найдена', 'booking': booking_info}
    else:
        if created:
            booking_result = {'created': created, 'msg': 'Бронирование создано', 'booking': booking_info}
        else:
            booking_result = {'created': created, 'msg': 'Комната занята', 'booking': booking_info}
    finally:
        print('Заканчиваем создание бронирования')
    return json.dumps(booking_result)
