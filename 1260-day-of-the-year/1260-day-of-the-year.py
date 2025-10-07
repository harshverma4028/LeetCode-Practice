class Solution:
    def dayOfYear(self, date: str) -> int:
        y_str, m_str, d_str = date.split('-')
        y, m, d = int(y_str), int(m_str), int(d_str)

        def is_leap(year: int) -> bool:
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if is_leap(y):
            month_days[1] = 29 
        
        
        return sum(month_days[:m-1]) + d
