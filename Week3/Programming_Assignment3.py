name1 = input()
date1 = input()
name2 = input()
date2 = input()
day1, month1, year1 = map(int, date1.split('-'))
day2, month2, year2 = map(int, date2.split('-'))
if year1 < year2:
    print(name2,end='')
elif year1 > year2:
    print(name1,end='')
else:
    if month1 < month2:
        print(name2,end='')
    elif month1 > month2:
        print(name1,end='')
    else:
        if day1 < day2:
            print(name2,end='')
        elif day1 > day2:
            print(name1,end='')
        else:
            if name1 >= name2:
              print(name2)
            else:
              print(name1)