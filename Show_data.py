import Connection
import Excels

import SQL

db_dimension = Connection.connect('db_dimensional_perpus')
cursor = db_dimension.cursor()


# ---------------------- Show GUI ---------------------- #
def select_month(month):
    if month   == "Januari":
        return 1
    elif month == "Februari":
        return 2
    elif month == "Maret":
        return 3
    elif month == "April":
        return 4
    elif month == "Mei":
        return 5
    elif month == "Juni":
        return 6
    elif month == "Juli":
        return 7
    elif month == "Agustus":
        return 8
    elif month == "September":
        return 9
    elif month == "Oktober":
        return 10
    elif month == "November":
        return 11
    elif month == "Desember":
        return 12

def select_library(library):
    if library == "Tianjin Binhai Library":
        return 1
    elif library == "Seattle Public Library":
        return 2
    elif library == "Library of Birmingham":
        return 3

def select_month_int(month):
    if month == 1:
        return "Januari"
    elif month == 2:
        return "Februari"
    elif month == 3:
        return "Maret"
    elif month == 4:
        return "April"
    elif month == 5:
        return "Mei"
    elif month == 6:
        return "Juni"
    elif month == 7:
        return "Juli"
    elif month == 8:
        return "Agustus"
    elif month == 9:
        return "September"
    elif month == 10:
        return "Oktober"
    elif month == 11:
        return "November"
    elif month == 12:
        return "Desember"

def show_member(self):
    member = self.m_text_member.GetValue()
    sql = SQL.sql_member(member)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for x, item in enumerate(rows, start=1):
        y = list(item)
        y.insert(0, x)
        y[5] = str(select_month_int(y[5]))
        self.m_dataViewList_member.AppendItem(y)

def show_by_month(self):
    month = self.m_choice_month.GetStringSelection()
    month = select_month(month)
    year  = self.m_choice_year.GetStringSelection()
    sql   = SQL.sql_month(month,year)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for x, item in enumerate(rows, start=1):
        y = list(item)
        y.insert(0,x)
        self.m_dataViewList_peminjaman.AppendItem(y)

def show_by_year(self):
    year = self.m_choice_tahunan.GetStringSelection()
    sql  = SQL.sql_year(year)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for x, item in enumerate(rows, start=1):
        y = list(item)
        y.insert(0,x)
        y[3] = str(select_month_int(y[3]))
        self.m_dataViewList_tahun.AppendItem(y)

def show_data_perpus(self):
    library = self.m_choice_library.GetStringSelection()
    library = select_library(library)
    year = self.m_choice_tahun.GetStringSelection()
    sql  = SQL.sql_perpus(year,library)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for x, item in enumerate(rows, start=1):
        y = list(item)
        y.insert(0,x)
        self.m_dataViewList_perpus.AppendItem(y)

def show_fact(self):
    sql  = SQL.sql_fact()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for x, item in enumerate(rows, start=1):
        y = list(item)
        y.insert(0,x)
        y[8] = str(y[8])
        y[9] = str(y[9])
        self.m_dataView_fact.AppendItem(y)

# ---------------------- Save GUI ---------------------- #
def save_member(self):
    member = self.m_text_member.GetValue()
    sql = SQL.sql_member(member)
    cursor.execute(sql)
    rows = cursor.fetchall()
    Excels.excel_member(rows)

def save_month(self):
    month = self.m_choice_month.GetStringSelection()
    month = select_month(month)
    year  = self.m_choice_year.GetStringSelection()
    sql   = SQL.sql_month(month, year)
    cursor.execute(sql)
    rows  = cursor.fetchall()
    Excels.excel_month(rows)

def save_year(self):
    year = self.m_choice_tahunan.GetStringSelection()
    sql = SQL.sql_year(year)
    cursor.execute(sql)
    rows = cursor.fetchall()
    Excels.excel_year(rows)

def save_fact():
    sql = SQL.sql_fact()
    cursor.execute(sql)
    rows = cursor.fetchall()
    Excels.excel_fact(rows)