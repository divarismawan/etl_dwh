import xlsxwriter
import Show_data


# Transaction
def excel_member(data):
    excel_file = xlsxwriter.Workbook('member.xlsx')
    sheet = excel_file.add_worksheet('sheet_member')

    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Barcode")
    sheet.write(0, 2, "Book Title")
    sheet.write(0, 3, "Library")
    sheet.write(0, 4, "Day")
    sheet.write(0, 5, "Month")
    sheet.write(0, 6, "Year")

    # Data
    row = 1
    col = 0
    for barcode, book, perpus, tanggal, Month, tahun in (data):
        Month = Show_data.select_month_int(Month)
        sheet.write(row, col, row)
        sheet.write(row, col + 1, barcode)
        sheet.write(row, col + 2, book)
        sheet.write(row, col + 3, perpus)
        sheet.write(row, col + 4, tanggal)
        sheet.write(row, col + 5, Month)
        sheet.write(row, col + 6, tahun)
        row += 1

    excel_file.close()

def excel_month(data):
    excel_file = xlsxwriter.Workbook('month.xlsx')
    sheet = excel_file.add_worksheet('sheet_month')
    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Barcode")
    sheet.write(0, 2, "Book Title")
    sheet.write(0, 3, "Total")

    # Body
    row = 1
    col = 0

    for val_a, val_b, val_c in (data):
        sheet.write(row, col, row)
        sheet.write(row, col + 1, val_a)
        sheet.write(row, col + 2, val_b)
        sheet.write(row, col + 3, val_c)
        row += 1
    excel_file.close()

def excel_year(data):
    excel_file = xlsxwriter.Workbook('year.xlsx')
    sheet = excel_file.add_worksheet('sheet_year')
    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Title Book")
    sheet.write(0, 2, "Total")
    sheet.write(0, 3, "Month")

    # Body
    row = 1
    col = 0
    for val_a, val_b, val_c in (data):
        val_c = Show_data.select_month_int(val_c)
        sheet.write(row, col, row)
        sheet.write(row, col + 1, val_a)
        sheet.write(row, col + 2, val_b)
        sheet.write(row, col + 3, val_c)
        row += 1
    excel_file.close()

# Book
def excel_by_title(data):
    excel_file = xlsxwriter.Workbook('book_title.xlsx')
    sheet = excel_file.add_worksheet('sheet1')

    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Barcode")
    sheet.write(0, 2, "Book Title")
    sheet.write(0, 3, "Total")
    sheet.write(0, 4, "Library")
    sheet.write(0, 5, "Month")

    # Body
    row = 1
    col = 0
    for val_a, val_b, val_c, val_d, val_e in (data):
        val_c = Show_data.select_month_int(val_c)
        sheet.write(row, col, row) #number row
        sheet.write(row, col + 1, val_a)
        sheet.write(row, col + 2, val_b)
        sheet.write(row, col + 3, val_c)
        sheet.write(row, col + 4, val_d)
        sheet.write(row, col + 5, val_e = Show_data.select_month_int(val_e))
        row += 1
    excel_file.close()

def excel_book_month(data):
    excel_file = xlsxwriter.Workbook('book_month.xlsx')
    sheet = excel_file.add_worksheet('sheet1')
    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Book Title")
    sheet.write(0, 2, "Barcode")
    sheet.write(0, 3, "Library")
    sheet.write(0, 4, "Date")
    sheet.write(0, 5, "Month")
    sheet.write(0, 6, "Year")
    sheet.write(0, 7, "Member")

    # Body
    row = 1
    col = 0

    for val_a, val_b, val_c, val_d,val_e, val_f, val_g in (data):
        val_e = Show_data.select_month_int(val_e)
        sheet.write(row, col, row)
        sheet.write(row, col + 1, val_a)
        sheet.write(row, col + 2, val_b)
        sheet.write(row, col + 3, val_c)
        sheet.write(row, col + 4, val_d)
        sheet.write(row, col + 5, val_e)
        sheet.write(row, col + 6, val_f)
        sheet.write(row, col + 7, val_g)
        row += 1
    excel_file.close()

def excel_book_year(data):
    excel_file = xlsxwriter.Workbook('all_book.xlsx')
    sheet = excel_file.add_worksheet('sheet1')

    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Book Title")
    sheet.write(0, 2, "Library")
    sheet.write(0, 3, "Total")
    sheet.write(0, 4, "Month")

    # Body
    row = 1
    col = 0
    for val_a, val_b, val_c, val_d in (data):
        val_c = Show_data.select_month_int(val_c)
        sheet.write(row, col, row) #number row
        sheet.write(row, col + 1, val_a)
        sheet.write(row, col + 2, val_b)
        sheet.write(row, col + 3, val_c)
        sheet.write(row, col + 4, val_d)
        row += 1
    excel_file.close()

def excel_perpus(data):
    excel_file = xlsxwriter.Workbook('perpus.xlsx')
    sheet = excel_file.add_worksheet('sheet1')

    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Book Title")
    sheet.write(0, 2, "Total")
    sheet.write(0, 3, "Month")

    # Body
    row = 1
    col = 0
    for val_a, val_b, val_c in (data):
        val_c = Show_data.select_month_int(val_c)
        sheet.write(row, col, row) #number row
        sheet.write(row, col + 1, val_a)
        sheet.write(row, col + 2, val_b)
        sheet.write(row, col + 3, val_c = Show_data.select_month_int(val_c))
        row += 1
    excel_file.close()

def excel_fact(data):
    excel_file = xlsxwriter.Workbook('fact.xlsx')
    sheet = excel_file.add_worksheet('sheet1')

    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Member")
    sheet.write(0, 2, "Book Title")
    sheet.write(0, 3, "Author")
    sheet.write(0, 4, "Publisher")
    sheet.write(0, 5, "Bookshilf")
    sheet.write(0, 6, "Library")
    sheet.write(0, 7, "Employee")
    sheet.write(0, 8, "Date of load")
    sheet.write(0, 9, "Date of return")

    # Body
    row = 1
    col = 0
    for val_a, val_b, val_c, val_d, val_e, val_f, val_g, val_h, val_i in (data):
        sheet.write(row, col, row) #number row
        sheet.write(row, col + 1, val_a)
        sheet.write(row, col + 2, val_b)
        sheet.write(row, col + 3, val_c)
        sheet.write(row, col + 4, val_d)
        sheet.write(row, col + 5, str(val_e,encoding='ascii'))
        sheet.write(row, col + 6, val_f)
        sheet.write(row, col + 7, val_g)
        sheet.write(row, col + 8, str(val_h))
        sheet.write(row, col + 9, str(val_i))
        row += 1
    excel_file.close()