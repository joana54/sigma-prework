from datetime import datetime


def age_difference(date):
    current_date = datetime.now()
    current_year = int(current_date.year)
    input_year = int(date[6:])
    return abs(current_year - input_year)


if __name__ == "__main__":
    another_date = input("Please input a date in this format: '04-12-1990': ")
    print(age_difference(another_date))
