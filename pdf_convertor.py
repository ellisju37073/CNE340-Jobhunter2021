import pdftables_api
from pdf2docx import Converter


def excel():
    c = pdftables_api.Client('jqdek0qhp7dw')

    file_name = input("what is the file?:")
    user = input("what is your username?:")
    file_path = (r"C:\Users\\" + user + r"\Documents\conversion\\")
    file = (file_path + file_name + ".pdf")
    output = input("what do you want output to be?:")
    output_path = (r"C:\Users\\" + user + r"\Documents\conversion\\")
    output_file = (output_path + output + ".xlsx")
    c.xlsx(file, output_file)
    return


def word():
    file = input("what is the file?:")
    path = input("what is your username?:")
    output = input("what do you want output to be?:")
    pdf_file = r"C:\Users\\" + path + r"\Documents\conversion\\" + file + ".pdf"
    docx_file = r"C:\Users\\" + path + r"\Documents\conversion\\" + output + ".docx"

    # convert pdf to docx
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    return


def main():
    print("Hello and welcome to Justin Ellis's PDF convertor. This PDF convertor requires a "
          "conversion folder in your documents folder. Please ensure the file you want to convert is "
          "in that folder also.")
    x = input("What type of file do you want to convert to?:")
    if x == "word" or x == "Word":
        return word()
    elif x == "excel" or x == "Excel":
        return excel()
    else:
        print("You did not specify file")


if __name__ == "__main__":
    main()