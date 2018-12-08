from numpy.distutils.fcompiler import none

import Connection

db_perpus    = Connection.connect('db_perpus')
db_dimension = Connection.connect('db_dimensional_perpus')

# ----------------- Functions ----------------- #
# for get all data in table
def function_select(db,query):
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# for get one data in table
def fun_lastId(id_table, tb_name,db):
    cursor = db.cursor()
    cursor.execute("SELECT MAX({0}) FROM {1}".format(id_table,tb_name))
    result = cursor.fetchone()[0]
    return result

def fun_count(id_table, tb_name,db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT({0}) FROM {1}".format(id_table,tb_name))
    result = cursor.fetchone()[0]
    return result

# for insert data to table
def function_instert(db_dimensi,query):
    cursor = db_dimensi.cursor()
    cursor.execute(query)
    db_dimensi.commit()

# for check different data in both database
def fun_all(id_rel, tb_rel, id_dim, tb_dim, table_name):
    print("Data in table %s" % table_name)
    # Relational db
    getId_rel = fun_lastId(id_rel,tb_rel,db_perpus)
    countRel  = fun_count(id_rel,tb_rel,db_perpus)

    #Dimensional db
    getId_dim = fun_lastId(id_dim, tb_dim, db_dimension)
    countDim = fun_count(id_dim, tb_dim, db_dimension)

    result = countRel - countDim
    if (getId_dim != None):
        print("Jumlah data baru = %d" % result)
        if (countRel > countDim):
            getId_dim +=1
            print("Tambah data mulai dari = %d" % getId_dim)
            print("")
            return getId_dim
        else:
            print("Value data sama")
            print("")
            return getId_rel+1
    else:
        val_newDim = 1
        print("Tambah data sebanyak : {0}".format(result))
        print("")
        return val_newDim


# ----------------- SQL Query Get Value Max----------------- #
val_buku       = fun_all("id_buku","tb_buku","id_buku","dim_buku","Buku")
val_member     = fun_all("id_member","tb_member","id_member","dim_member","Member")
val_pegawai    = fun_all("id_pegawai","tb_pegawai","id_pegawai","dim_pegawai","Pegawai")
val_penerbit   = fun_all("id_penerbit","tb_penerbit","id_penerbit","dim_penerbit","Penerbit")
val_penulis    = fun_all("id_penulis","tb_penulis","id_penulis","dim_penulis","Penulis")
val_perpus     = fun_all("id_perpus","tb_perpus","id_perpus","dim_perpus","Perpus")
val_trans      = fun_all("id_detail","tb_detail_trans","id_fakta_trans","fakta_trans","Transaksi")

# ----------------- SQL Query SELECT----------------- #
sql_buku        = "SELECT id_buku,title_buku, ISBN FROM tb_buku WHERE id_buku >= {0}".format(val_buku)
sql_member      = "SELECT id_member,nama FROM tb_member WHERE id_member >={0}".format(val_member)
sql_pegawai     = "SELECT id_pegawai,nama_pegawai FROM tb_pegawai WHERE id_pegawai >={0}".format(val_pegawai)
sql_penerbit    = "SELECT id_penerbit, nama_perusahaan FROM tb_penerbit WHERE id_penerbit >={0}".format(val_penerbit)
sql_penulis     = "SELECT id_penulis,nama_penulis FROM tb_penulis WHERE id_penulis >={0}".format(val_penulis)
sql_perpus      = "SELECT id_perpus,nama_perpus, alamat_perpus FROM tb_perpus WHERE id_perpus >={0}".format(val_perpus)
sql_trans       = "SELECT tb_detail_trans.`id_trans`, tb_transaksi.`id_pegawai`, id_member, " \
                  "tb_transaksi.`tgl_pinjam`, tb_transaksi.`tgl_kembali`, tb_pegawai.`id_perpus`, " \
                  "tb_detail_trans.`id_buku`, tb_buku.`id_penerbit`, tb_buku.`id_penulis` " \
                  "FROM tb_transaksi JOIN tb_detail_trans JOIN tb_pegawai " \
                  "JOIN tb_buku WHERE tb_detail_trans.`id_trans` = tb_transaksi.`id_trans` " \
                  "AND tb_transaksi.`id_pegawai` = tb_pegawai.`id_pegawai` " \
                  "AND tb_buku.`id_buku` = tb_detail_trans.`id_buku` " \
                  "AND tb_detail_trans.`id_detail` >={0}".format(val_trans)


#----------------- Use function SELECT -----------------#
select_buku     = function_select(db_perpus, sql_buku)
select_member   = function_select(db_perpus, sql_member)
select_pegawai  = function_select(db_perpus, sql_pegawai)
select_penerbit = function_select(db_perpus, sql_penerbit)
select_penulis  = function_select(db_perpus, sql_penulis)
select_perpus   = function_select(db_perpus, sql_perpus)
select_trans    = function_select(db_perpus, sql_trans)

# ----------------- INSERT data to Data Warehouse -----------------#
print("Loading...")
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

for x in select_trans:
    val_a, val_b, val_c, val_d, val_e, val_f, val_g, val_h, val_i = x
    query_insert = "INSERT INTO fakta_trans SET id_trans = {0}, id_pegawai = '{1}', id_member = '{2}', tanggal_pinjam = '{3}', tanggal_kembali = '{4}', id_perpus = '{5}', id_buku = '{6}', id_penerbit = '{7}', id_penulis = '{8}'".format(val_a, val_b, val_c, val_d, val_e, val_f, val_g, val_h, val_i)
    function_instert(db_dimension,query_insert)
print("Sukses")

# disconnect from server
db_perpus.close()
db_dimension.close()