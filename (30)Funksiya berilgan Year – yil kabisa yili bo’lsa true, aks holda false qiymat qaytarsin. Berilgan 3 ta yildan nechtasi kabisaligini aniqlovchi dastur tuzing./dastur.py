

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



def count_leap_years(years):
    count = 0
    for year in years:
        if is_leap_year(year):
            count += 1
    return count




year1 = int(input("1 yilni kiriting: "))
year2 = int(input("2 yilni kiriting: "))
year3 = int(input("3 yilni kiriting: "))

print(count_leap_years([year1,year2,year3]))