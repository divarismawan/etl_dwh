# Transaksi berdasarkan waktu
def sql_member(val):
    sql = "SELECT  dim_buku.`barcode_buku`,dim_buku.`title_buku`, dim_perpus.`nama_perpus`, " \
                 "DAY(tanggal_pinjam) AS tanggal, MONTH(tanggal_pinjam) AS bulan, YEAR(tanggal_pinjam) AS tahun " \
                 "FROM fakta_trans " \
                 "JOIN dim_buku ON dim_buku.`id_detail_buku` = fakta_trans.`id_detail_buku` " \
                 "JOIN dim_member ON dim_member.`id_member` = fakta_trans.`id_member` " \
                 "JOIN dim_perpus ON dim_perpus.`id_perpus` = fakta_trans.`id_perpus` " \
                 "WHERE dim_member.`nama_member` = '{0}' " \
                 "ORDER BY tanggal_pinjam".format(val)
    return sql

def sql_month(month,year):
      sql="SELECT dim_buku.`barcode_buku`, dim_buku.`title_buku`, COUNT(fakta_trans.`id_detail_buku`) FROM fakta_trans " \
          "JOIN dim_buku ON dim_buku.`id_detail_buku` = fakta_trans.`id_detail_buku` " \
          "WHERE YEAR(tanggal_pinjam) = {0}  AND MONTH(tanggal_pinjam)= {1} " \
          "GROUP BY MONTH(tanggal_pinjam),fakta_trans.`id_detail_buku`".format(year, month)
      return sql

def sql_year(year):
    sql = "SELECT dim_buku.`title_buku`, COUNT(fakta_trans.`id_detail_buku`) AS jumlah_terpinjam, " \
          "MONTH(tanggal_pinjam) AS bulan " \
          "FROM fakta_trans " \
          "JOIN dim_buku ON dim_buku.`id_detail_buku` = fakta_trans.`id_detail_buku` " \
          "WHERE YEAR(tanggal_pinjam) = {0} GROUP BY MONTH(tanggal_pinjam),fakta_trans.`id_detail_buku`".format(year)
    return sql

# Peminjaman berdasarkan jenis buku
def sql_book_title(title, year):
    sql = "SELECT dim_buku.`title_buku`, dim_buku.`barcode_buku`, COUNT(dim_buku.`barcode_buku`), " \
          "dim_perpus.`nama_perpus`, MONTH(fakta_trans.`tanggal_pinjam`) " \
          "FROM fakta_trans " \
          "JOIN dim_buku ON dim_buku.`id_detail_buku` = fakta_trans.`id_detail_buku` " \
          "JOIN dim_perpus ON dim_perpus.`id_perpus` = fakta_trans.`id_perpus` " \
          "WHERE YEAR(fakta_trans.`tanggal_pinjam`) = {0} AND dim_buku.`title_buku` = '{1}' " \
          "GROUP BY dim_buku.`barcode_buku` " \
          "ORDER BY MONTH(fakta_trans.`tanggal_pinjam`)".format(year,title)
    return sql

def sql_book_month(month, year):
    sql = "SELECT dim_buku.`title_buku`, dim_buku.`barcode_buku`, dim_perpus.`nama_perpus`, " \
          "DAY(fakta_trans.`tanggal_pinjam`) AS tanggal, " \
          "MONTH(fakta_trans.`tanggal_pinjam`) AS bulan, " \
          "YEAR(fakta_trans.`tanggal_pinjam`) AS tahun, dim_member.`nama_member` " \
          "FROM fakta_trans " \
          "JOIN dim_buku ON dim_buku.`id_detail_buku` = fakta_trans.`id_detail_buku` " \
          "JOIN dim_perpus ON dim_perpus.`id_perpus` = fakta_trans.`id_perpus` " \
          "JOIN dim_member ON dim_member.`id_member` = fakta_trans.`id_member` " \
          "WHERE MONTH(fakta_trans.`tanggal_pinjam`) = {0} AND YEAR(fakta_trans.`tanggal_pinjam`) = {1} " \
          "ORDER BY fakta_trans.`tanggal_pinjam`".format(month,year)
    return sql

def sql_book_year(year):
    sql = "SELECT dim_buku.`title_buku`, dim_perpus.`nama_perpus`, COUNT(dim_buku.`id_buku`) AS jumlah, " \
          "MONTH(dim_buku.`time_update`) AS bulan  " \
          "FROM dim_buku " \
          "JOIN dim_perpus ON dim_perpus.`id_perpus` = dim_buku.`id_perpus`  " \
          "WHERE YEAR(dim_buku.`time_update`) = {0}  " \
          "GROUP BY dim_buku.`id_buku`, YEAR(dim_buku.`time_update`)".format(year)
    return sql

def sql_perpus(year,library):
    sql = "SELECT dim_buku.`title_buku`, COUNT(fakta_trans.`id_detail_buku`) AS jumlah_terpinjam, MONTH(tanggal_pinjam)  " \
          "FROM fakta_trans " \
          "JOIN dim_buku ON dim_buku.`id_detail_buku` = fakta_trans.`id_detail_buku` " \
          "JOIN dim_perpus ON dim_perpus.`id_perpus` = fakta_trans.`id_perpus`" \
          "WHERE YEAR(tanggal_pinjam) = {0} AND fakta_trans.`id_perpus` = {1} " \
          "GROUP BY MONTH(tanggal_pinjam),fakta_trans.`id_detail_buku`, fakta_trans.`id_perpus`".format(year, library)
    return sql

def sql_fact():
    sql = "SELECT dim_member.`nama_member`, dim_buku.`title_buku`, dim_penulis.`nama_penulis`, " \
          "dim_penerbit.`nama_perusahaan` AS penerbit, dim_rak.`nama_rak`, dim_perpus.`nama_perpus`, " \
          "dim_pegawai.`nama_pegawai`, tanggal_pinjam, tanggal_kembali " \
          "FROM fakta_trans  " \
          "JOIN dim_buku ON dim_buku.`id_detail_buku` = fakta_trans.`id_detail_buku` " \
          "JOIN dim_member ON dim_member.`id_member` = fakta_trans.`id_member` " \
          "JOIN dim_rak ON dim_rak.`id_rak` = fakta_trans.`id_rak` " \
          "JOIN dim_perpus ON dim_perpus.`id_perpus` = fakta_trans.`id_perpus` " \
          "JOIN dim_penerbit ON dim_penerbit.`id_penerbit` = fakta_trans.`id_penerbit` " \
          "JOIN dim_penulis ON dim_penulis.`id_penulis` = fakta_trans.`id_penulis` " \
          "JOIN dim_pegawai ON dim_pegawai.`id_pegawai` = fakta_trans.`id_pegawai` " \
          "ORDER BY tanggal_pinjam DESC"
    return  sql