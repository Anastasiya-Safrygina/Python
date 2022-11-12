class Time:
    def __init__(self, *args):
        if len(args) == 1:
            items = list(map(int, str(args[0]).split(':')))
            self._seconds = int(items[2])
            self._minutes = int(items[1])
            self._hours = int(items[0])
        if len(args) == 3:
            self._seconds = int(args[2])
            self._minutes = int(args[1])
            self._hours = int(args[0])

    def __str__(self):
        return f'{self._hours}:{self._minutes}:{self._seconds}'


class NewTime:
    def __init__(self, *, seconds=0, minutes=0, hours=0, str=None):
        if str is None:
            self._seconds = seconds
            self._minutes = minutes
            self._hours = hours
        else:
            items = list(map(int, str.split(':')))
            self._seconds = int(items[2])
            self._minutes = int(items[1])
            self._hours = int(items[0])

    def __str__(self):
        return f'{self._hours}:{self._minutes}:{self._seconds}'


t2 = NewTime(str='13:15:00')
t1 = NewTime(hours=13, minutes=15, seconds=00)
print(t1)
print(t2)
