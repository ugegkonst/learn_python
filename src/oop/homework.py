import datetime
import sys
from abc import ABC, abstractmethod


class AbcFormatter(ABC):
    @abstractmethod
    def format(self, val) -> str:
        ...


if __name__ == '__main__':
    this_mod = sys.modules[__name__]

    # Нужно реализовать класс DataFormatter который данную дату приведёт к нужному формату
    date = datetime.datetime(year=2024, month=2, day=18, hour=23, minute=59, second=59)

    data_formatter_klass = getattr(this_mod, "DataFormatter")
    assert issubclass(data_formatter_klass, AbcFormatter)

    data_formatter = data_formatter_klass()

    date_str = data_formatter.format(date)

    assert date_str == "2024-02-18 23:59:59", date_str
