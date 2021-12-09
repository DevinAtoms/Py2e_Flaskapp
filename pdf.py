from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_line_width(1)
        self.cell(0, 24, 'Spell Title', border='B', align='L')
        self.cell(0, 24, 'Cantrip 1', border='B', align='R', ln=1)
    pass  # nothing happens when it is executed.


pdf = PDF(orientation='L', unit='pt', format=(216, 360))
pdf.add_page()
pdf.set_font('Arial', '', 8)
pdf.set_margins(26, 26, 26)
pdf.cell(0, 4, ln=2)
trait_w = pdf.get_string_width('Trait#')
pdf.set_draw_color(216, 196, 131)
pdf.set_fill_color(82, 46, 44)
pdf.set_text_color(255, 255, 255)
pdf.set_line_width(1)
pdf.cell(trait_w+8, 12, 'Trait1', border=1, ln=0, align='C', fill=True)
pdf.cell(trait_w+8, 12, 'Trait2', border=1, ln=0, align='C', fill=True)
pdf.cell(trait_w+8, 12, 'Trait3', border=1, ln=0, align='C', fill=True)
pdf.cell(trait_w+8, 12, 'Trait4', border=1, ln=1, align='C', fill=True)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Arial', 'B', 8)
tradition_w = pdf.get_string_width('Traditions:')
pdf.cell(tradition_w+2, 16, 'Traditions:', ln=0, align='L')
pdf.set_font('Arial', 'IU', 8)
traditions_w = pdf.get_string_width('Tradition#')
pdf.cell(traditions_w+8, 16, 'Tradition1,', ln=0, align='L')
pdf.cell(traditions_w+8, 16, 'Tradition2,', ln=0, align='L')
pdf.cell(traditions_w+8, 16, 'Tradition3,', ln=0, align='L')
pdf.cell(traditions_w+8, 16, 'Tradition4', ln=0, align='L')
pdf.output('spell.pdf', 'F')
