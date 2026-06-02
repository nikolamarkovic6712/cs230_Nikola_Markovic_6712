
def write_text_to_file():
    tekst = input("Unesi tekst: ")

    with open("text.txt", "w", encoding="utf-8") as fajl:
        fajl.write(tekst)


def lowercase_wrapper(func):
    def wrapper():
        tekst = input("Unesi tekst: ").lower()

        with open("text2.txt", "w", encoding="utf-8") as fajl:
            fajl.write(tekst)

    return wrapper


write_text_to_file = lowercase_wrapper(write_text_to_file)

write_text_to_file()
