from fpdf import FPDF

def main():
    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("helvetica", "B", 30)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C")

    pdf.image("shirtificate.png", x=35, y=70, w=140)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 20)
    pdf.text(60, 145, name)

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
