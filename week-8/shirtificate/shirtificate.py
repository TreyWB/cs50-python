from fpdf import FPDF

class PDF:
    def image(self):
        self.image("shirtificate.png", 10, 8, 33)

def main():
    name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Hello World!")
pdf.output("tuto1.pdf")

if __name__ == "__main__":
    main()