import inflect
def main():
    p = inflect.engine()
    names = []
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        print()
    formatted_names = p.join(names)
    print(f"Adieu, adieu, to {formatted_names}")
if __name__ == "__main__":
    main()
