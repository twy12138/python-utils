import datetime
from chinese_calendar import is_holiday

if __name__ == '__main__':
    start = datetime.date(2021,1,1)
    end = datetime.date(2021,12,31)
    arr = []
    for i in range(start.toordinal(), end.toordinal()):
        if is_holiday(datetime.date.fromordinal(i)):
            arr.append(datetime.date.fromordinal(i).strftime("%Y%m%d"))
    print(arr)