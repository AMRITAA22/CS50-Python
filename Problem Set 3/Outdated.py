def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            elif "," in date:
                month_str, rest = date.split(" ", 1)
                day, year = rest.replace(",", "").split()
                month = months.index(month_str) + 1
                day = int(day)
                year = int(year)
            else:
                raise ValueError
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError
            print(f"{year:04}-{month:02}-{day:02}")
            break
        except (ValueError, IndexError):
            continue
if __name__ == "__main__":
    main()
