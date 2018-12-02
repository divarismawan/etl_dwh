import pymysql
import Connection

db_perpus    = Connection.connect('db_perpus')
db_dimension = Connection.connect('db_dimensional_perpus')

# ----------------- Functions ----------------- #
def function_select(db,query):
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def function_instert(db_dimensi,query):
    cursor = db_dimensi.cursor()
    cursor.execute(query)
    db_dimensi.commit()

# ----------------- SQL Query ----------------- #
sql_selectBuku    = "SELECT id_buku,title_buku, ISBN FROM tb_buku"
sql_selectMember  = "SELECT id_member,nama FROM tb_member"
sql_selectPegawai = "SELECT id_pegawai,nama_pegawai FROM tb_pegawai"
sql_penerbit      = "SELECT id_penerbit, nama_perusahaan FROM tb_penerbit"
sql_penulis       = "SELECT id_penulis,nama_penulis FROM tb_penulis"
sql_perpus        = "SELECT id_perpus,nama_perpus, alamat_perpus FROM tb_perpus"

#----------------- Use function SELECT -----------------#
select_buku     = function_select(db_perpus,sql_selectBuku)
select_member   = function_select(db_perpus, sql_selectMember)
select_pegawai  = function_select(db_perpus, sql_selectPegawai)
select_penerbit = function_select(db_perpus, sql_penerbit)
select_penulis  = function_select(db_perpus, sql_penulis)
select_perpus   = function_select(db_perpus,sql_perpus)

# ----------------- Use function INSERT -----------------#
for x in select_buku:
    val_a,val_b,val_c  = x
    query_insert = ("INSERT INTO dim_buku SET id_buku = {0}, nama_buku = '{1}', ISBN = '{2}'".format(val_a, val_b, val_c))
    function_instert(db_dimension, query_insert)

for x in select_member:
    val_a, val_b = x
    query_insert =("INSERT INTO dim_member SET id_member ={0},nama_member='{1}'".format(val_a,val_b))
    function_instert(db_dimension,query_insert)

for x in select_pegawai:
    val_a, val_b = x
    query_insert =("INSERT INTO dim_pegawai SET id_pegawai={0},nama_pegawai='{1}'".format(val_a,val_b))
    function_instert(db_dimension,query_insert)

for x in select_penerbit:
    val_a, val_b = x
    query_insert =("INSERT INTO dim_penerbit SET id_penerbit = {0}, nama_perusahaan = '{1}'".format(val_a,val_b))
    function_instert(db_dimension,query_insert)

for x in select_penulis:
    val_a, val_b = x
    query_insert = ("INSERT INTO dim_penulis SET id_penulis = {0}, nama_penulis='{1}'".format(val_a,val_b))
    function_instert(db_dimension,query_insert)

for x in select_perpus:
    val_a, val_b, val_c = x
    query_insert = ("INSERT INTO dim_perpus SET id_perpus = {0}, nama_perpus = '{1}', alamat_perpus = '{2}'".format(val_a, val_b, val_c))
    function_instert(db_dimension, query_insert)

month = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
for x in month:
        query_insert = ("INSERT INTO dim_waktu SET bulan = '{0}'".format(x))
        function_instert(db_dimension,query_insert)

# disconnect from server
db_perpus.close()