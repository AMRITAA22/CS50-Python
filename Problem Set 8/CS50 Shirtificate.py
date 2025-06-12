from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        # Set title font
        self.set_font("Helvetica", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

def main():
    name = input("Name: ")

    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    # Add the image
    pdf.image("shirtificate.png", x=10, y=50, w=190)

    # Overlay text on the shirt
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=55, y=140, txt=f"{name} took CS50")

    # Output the PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
