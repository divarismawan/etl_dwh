import xlsxwriter
import xlrd
import Show_data

excel_file = xlsxwriter.Workbook('Data_perpustakaan.xlsx')


def excel_member(data):
    sheet = excel_file.add_worksheet('sheet_member')

    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Barcode")
    sheet.write(0, 2, "Book Title")
    sheet.write(0, 3, "Perpustakaan")
    sheet.write(0, 4, "Tanggal")
    sheet.write(0, 5, "Bulan")
    sheet.write(0, 6, "Tahun")

    # Data
    row = 1
    col = 0
    for barcode, book, perpus, tanggal, bulan, tahun in (data):
        bulan = Show_data.select_month_int(bulan)
        sheet.write(row, col, row)
        sheet.write(row, col + 1, barcode)
        sheet.write(row, col + 2, book)
        sheet.write(row, col + 3, perpus)
        sheet.write(row, col + 4, tanggal)
        sheet.write(row, col + 5, bulan)
        sheet.write(row, col + 6, tahun)
        row += 1
    excel_file.close()

def excel_month(data):
    sheet = excel_file.add_worksheet('sheet_month')
    # Header
    sheet.write(0,0,"No")
    sheet.write(0,1,"Kode Buku")
    sheet.write(0,2,"Book Title")
    sheet.write(0,3,"Summary")

    #Body
    row = 1
    col = 0
    for val_a, val_b, val_c in (data):
        sheet.write(row, col, row)
        sheet.write(row, col + 1, val_a)
        sheet.write(row, col + 2, val_b)
        sheet.write(row, col + 3, val_c)
        row +=1
    excel_file.close()

def excel_year(data):
    sheet = excel_file.add_worksheet('sheet_year')
    # Header
    sheet.write(0, 0, "No")
    sheet.write(0, 1, "Buku")
    sheet.write(0, 2, "Summary")
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