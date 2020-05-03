import datetime


def welcome_screen():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Hello, welcome to my second game!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def birthday_one():
    print('Player one, when is your birthday?')
    year1 = int(input('Year? [YYYY]'))
    month1 = int(input('Month? [MM]'))
    day1 = int(input('Day? [DD]'))
    return datetime.date(year1, month1, day1)


def birthday_two():
    print('Player {0}, when is your birthday?'.format("2"))
    year2 = int(input('Year? [YYYY]'))
    month2 = int(input('Month? [MM]'))
    day2 = int(input('Day? [DD]'))
    return datetime.date(year2, month2, day2)


def middle_date(date1, date2):
    date1_same_year = datetime.date(date2.year, date1.month, date1.day)
    averagedate = date1_same_year + (date2 - date1_same_year) / 2
    return str(averagedate.month) + ' ' + str(averagedate.day)


def main():
    welcome_screen()
    bdayone = birthday_one()
    bdaytwo = birthday_two()
    celebration_day = middle_date(bdayone, bdaytwo)
    print('You should have your joint birthday party on {0}!'.format(celebration_day))

main()
