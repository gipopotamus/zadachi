def calculate_days_and_seconds(y1, m1, d1, h1, min1, s1, y2, m2, d2, h2, min2, s2):
    # Преобразование дат в секунды
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start_days = sum(months_days[:m1-1]) + d1
    end_days = sum(months_days[:m2-1]) + d2

    total_days_start = y1 * 365 + start_days
    total_days_end = y2 * 365 + end_days

    days_difference = total_days_end - total_days_start
    seconds_difference = (h2 * 3600 + min2 * 60 + s2) - (h1 * 3600 + min1 * 60 + s1)

    if seconds_difference < 0:
        seconds_difference += 86400
        days_difference -= 1

    return days_difference, seconds_difference

def main():
    # Ввод данных
    input_start = input().split()
    input_end = input().split()

    year1, month1, day1, hour1, min1, sec1 = map(int, input_start)
    year2, month2, day2, hour2, min2, sec2 = map(int, input_end)

    days, seconds = calculate_days_and_seconds(year1, month1, day1, hour1, min1, sec1, year2, month2, day2, hour2, min2, sec2)
    print(days, seconds)


if __name__ == '__main__':
    main()
