import re
import sys
def main():
    print(convert(input("Hours: ")))
def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))?\s(AM|PM) to (\d{1,2})(?::(\d{2}))?\s(AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")
    h1, m1, ampm1, h2, m2, ampm2 = match.groups()
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    h1 = int(h1)
    h2 = int(h2)
    if not (1 <= h1 <= 12) or not (0 <= m1 <= 59):
        raise ValueError("Invalid start time")
    if not (1 <= h2 <= 12) or not (0 <= m2 <= 59):
        raise ValueError("Invalid end time")
    h1 = to_24_hour(h1, ampm1)
    h2 = to_24_hour(h2, ampm2)
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
def to_24_hour(hour, ampm):
    if ampm == "AM":
        return 0 if hour == 12 else hour
    else:  # PM
        return 12 if hour == 12 else hour + 12
if __name__ == "__main__":
    main()
