def main():
    groceries = {}
    try:
        while True:
            item = input().strip().lower()
            if item:
                groceries[item] = groceries.get(item, 0) + 1
    except EOFError:
        print()  # Move cursor to a new line after Ctrl+D

    for item in sorted(groceries):
        print(f"{groceries[item]} {item.upper()}")
if __name__ == "__main__":
    main()
