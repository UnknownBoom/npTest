import itertools
from calendar import monthcalendar

# logging.basicConfig(level=logging.CRITICAL)
#
# def sample_t():
#     while True:
#         get = requests.get("http://localhost:1277", data={'name': uuid.uuid4()}, headers={'content-type':'application/json'})
#         print('Get new response:', get.text)
#         time.sleep(2)
#
#
# sample_t()

# res = {}


# def mc(iterable):
#     if iterable[-3] == 13:
#         return True
#     return False
#
#
# def add(iterable):
#     months = res.get(iterable[0], [])
#     months.append(iterable[1])
#     res[iterable[0]] = months
#
#
# def pp(iterable):
#     for i in iterable:
#         print(i)
#         print('---------------------')
#
#
# month_calendar_map = map(lambda x: (x[0], x[1], monthcalendar(x[0], x[1])),
#                          itertools.product(range(1900, 2023), range(1, 13)))
# pp(month_calendar_map)
# map_ = map(lambda x: x[2], month_calendar_map)
# f = filter(lambda x: print('q', x), map_)
# pp(f)
# map2 = map(lambda x: (x[0], x[1], x[2]), filter(lambda x: x[-3] == 13, month_calendar_map))
# pp(map2)

# list(map(add, list(map2)))
# for year in range(1900, 2023):
#     for month in range(1, 13):
#         month_calendar = monthcalendar(year, month)
#         m = map(lambda x: (year, month, x), filter(lambda x: x[-3] == 13, month_calendar))
#         list(map(add, list(m)))

# print(res)
