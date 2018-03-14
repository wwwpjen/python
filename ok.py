# print 'hello world'
# names=['a','b','c']
# mark='::::::'
# for name in names:
#     names= name+mark
#     print names
# def ask_ok(prompt,retries=4,complaint='again'):
#     while 1:
#         ok=raw_input(prompt)
#         if ok in ('y','ye','yes'):return 1
#         if ok in ('no'):return 0
#         retries=retries-1
#         if retries<0:raise IOError,'refusenik error'
#         print complaint
# ask_ok('Really?')

# def timecal(date1,date2):
#     print 'please type the first date'
#     date1=raw_input()
#     datestart=date1.split('.')
#     yearstart,monthstart,daystart=int(datestart(0)),int(datestart(1)),int(datestart(2))
#     print 'please type the second date'
#     date2=raw_input()
#     dateend = date2.split('.')
#     yearend, monthend, dayend = int(dateend(0)), int(dateend(1)), int(dateend(2))

def isComYear(year):  # judge the case of common year
    if year % 100 == 0:
        if (year / 100) % 4 == 0:
            return 0
        else:
            return 1
    else:
        if year % 4 == 0:
            return 0
        else:
            return 1


def daysMonth(year, month):  # days in month
    month1 = [1, 3, 5, 7, 8, 10, 12]
    if month in month1:
        return 31
    elif month == 2:
        if isComYear(year):
            return 28
        else:
            return 29
    else:
        return 30


def daysYear(year):  # calculate the total days in a certain year
    if isComYear(year):
        return 365
    else:
        return 366


def distance(date1, date2):  # first sort the two date
    list1 = []
    list2 = []
    result = 0
    for num in date1.split('/'):
        list1.append(int(num))
    for num in date2.split('/'):
        list2.append(int(num))
    list1, list2 = min(list1, list2), max(list1, list2)

    if list1[0] == list2[0]:  # equal year
        if list1[1] == list2[1]:  # equal month
            result = list1[2] - list2[2]
        else:
            result1 = 0
            for month in range(list1[1], list2[1]):
                result1 += daysMonth(list1[0], month)
            result = result1 - list1[2] + list2[2]
    else:
        # if year is not equal,we won't care if the month is equal.We will only
        # care the first year's remaining days,the last year's passed days and the total days between the two years
        result2 = 0
        result3 = 0
        result4 = 0
        for year in range(list1[0], list2[0]):
            result2 += daysYear(year)
        if list1[1] == 1:
            result3 = list1[2] - 1
        else:
            for month in range(1, list1[1]):
                result3 += daysMonth(list1[0], month)
            if list2[1] == 1:
                result4 = list[2]
            else:
                for month in range(1, list2[1]):
                      result4 += daysMonth(list2[0], month)
        result = result2 - result3 + result4
    return result

def main():
        date1 = raw_input('input the first date in the format YY/MM/DD : ')
        date2 = raw_input('input the second date in the format YY/MM/DD: ')
        dist = (distance(date1, date2)**2)**0.5
        print 'the distance between the two date is:', dist

if __name__ == '__main__':
        main()

