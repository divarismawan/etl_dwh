import Connection

db_dimension = Connection.connect('db_dimensional_perpus')
cursor = db_dimension.cursor()

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

def show_by_month(self):
    month = self.sp_month.GetStringSelection()
    month = select_month(month)
    year  = self.sp_year.GetStringSelection()
    sql = "SELECT dim_buku.`nama_buku`, COUNT(fakta_trans.`id_buku`) FROM fakta_trans " \
          "JOIN dim_buku ON dim_buku.`id_buku` = fakta_trans.`id_buku` " \
          "WHERE YEAR(tanggal_pinjam) = {0}  AND MONTH(tanggal_pinjam)= {1} " \
          "GROUP BY MONTH(tanggal_pinjam),fakta_trans.`id_buku`".format(year,month)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for i in range(0, len(rows)):
        for j in range(0, len(rows[i])):
            self.grid_showResult.SetCellValue(i, j, str(rows[i][j]))

def show_by_year(self):
    year = self.m_choice4.GetStringSelection()
    sql = "SELECT COUNT(DISTINCT fakta_trans.`id_buku`), COUNT(fakta_trans.`id_buku`), MONTH(tanggal_pinjam)" \
          "FROM fakta_trans WHERE YEAR(tanggal_pinjam) = {0} GROUP BY MONTH(tanggal_pinjam)".format(year)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for i in range(0, len(rows)):
        for j in range(0, len(rows[i])):
            self.grid_showResult1.SetCellValue(i, j, str(rows[i][j]))

def show_fact(self):
    sql = "SELECT dim_member.`nama_member`, dim_buku.`nama_buku`, dim_penulis.`nama_penulis`, " \
          "dim_penerbit.`nama_perusahaan`,  dim_perpus.`nama_perpus`, dim_pegawai.`nama_pegawai`, " \
          "tanggal_pinjam, tanggal_kembali FROM fakta_trans  JOIN dim_buku ON dim_buku.`id_buku` = fakta_trans.`id_buku` " \
          "JOIN dim_member ON dim_member.`id_member` = fakta_trans.`id_member` " \
          "JOIN dim_perpus ON dim_perpus.`id_perpus` = fakta_trans.`id_perpus` " \
          "JOIN dim_penerbit ON dim_penerbit.`id_penerbit` = fakta_trans.`id_penerbit` " \
          "JOIN dim_penulis ON dim_penulis.`id_penulis` = fakta_trans.`id_penulis` " \
          "JOIN dim_pegawai ON dim_pegawai.`id_pegawai` = fakta_trans.`id_pegawai` ORDER BY tanggal_pinjam DESC"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for i in range(0, len(rows)):
        for j in range(0, len(rows[i])):
            self.m_grid7.SetCellValue(i, j, str(rows[i][j]))


