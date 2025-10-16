class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        def is_leap(year):
            return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def total_days(date):
            y, m, d = map(int, date.split('-'))

            days = (y - 1) * 365 + (y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400
            
            for i in range(m - 1):
                days += month_days[i]

            if is_leap(y) and m > 2:
                days += 1
        
            days += d
        
            return days

        return abs(total_days(date1) - total_days(date2))   
        