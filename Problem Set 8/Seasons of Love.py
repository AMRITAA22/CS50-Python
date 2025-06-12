import sys
import inflect
from datetime import datetime, date

def main():
    birthdate = input("Date of Birth: ")
    try:
        birth = datetime.strptime(birthdate, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")
    print(minutes_to_words(birth))

def minutes_to_words(birthdate: date) -> str:
    today = date.today()
    diff = today - birthdate
    minutes = diff.days * 24 * 60
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()
