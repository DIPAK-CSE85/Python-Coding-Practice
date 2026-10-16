def leef_year(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year,month):
    days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leef_year(year) and month==2:
        return 29
    else:
        return days_list[month-1]
year=int(input("enter a year="))     #2012
month=int(input("enter a month="))    #2
days=days_in_month(year,month)
print(days)


#using import function
import leep_year
def days_in_month(year,month):
    days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leep_year.leef_year(year) and month==2:
        return 29
    else:
        return days_list[month-1]
year=int(input("enter a year="))     #2012
month=int(input("enter a month="))    #2
days=days_in_month(year,month)
print(days)