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
def function_condition(val_rel, val_dim, countRel, countDim, tbl_name):
    print("Data in table %s"%tbl_name)
    if(val_dim != None):
        if(countRel > countDim):
            # val_newRel = val_rel
            result = countRel - countDim
            print("Jumlah data baru = %d"%result)
            print("Tambah data mulai dari = %d"%val_dim)
            print("")
            return val_dim+1
        else:
            val_newDim = val_rel+1
            print("Nilai sama")
            print("")
            return val_newDim
    else:
        val_newDim = 1
        print("Tambah data sebanyak : {0}".format(countRel))
        print("")
        return val_newDim



# ----------------- SQL Query Get Value Max----------------- #
# Buku

rel_idBuku     = fun_lastId("id_buku","tb_buku",db_perpus)
countRel_buku  = fun_count("id_buku","tb_buku",db_perpus)

dim_idBuku     = fun_lastId("id_buku","dim_buku",db_dimension)
countDim_buku  = fun_count("id_buku","dim_buku",db_dimension)

# Member
rel_idMember     = fun_lastId("id_member","tb_member",db_perpus)
countRel_Member  = fun_count("id_member","tb_member",db_perpus)

dim_idMember     = fun_lastId("id_member","dim_member",db_dimension)
countDim_Member  = fun_count("id_member","dim_member",db_dimension)

# Pegawai
rel_idPegawai     = fun_lastId("id_pegawai","tb_pegawai",db_perpus)
countRel_Pegawai  = fun_count("id_pegawai","tb_pegawai",db_perpus)

dim_idPegawai     = fun_lastId("id_pegawai","dim_pegawai",db_dimension)
countDim_Pegawai  = fun_count("id_pegawai","dim_pegawai",db_dimension)

# penerbit
rel_idPenerbit     = fun_lastId("id_penerbit","tb_penerbit",db_perpus)
countRel_Penerbit  = fun_count("id_penerbit","tb_penerbit",db_perpus)

dim_idPenerbit    = fun_lastId("id_penerbit","dim_penerbit",db_dimension)
countDim_Penerbit = fun_count("id_penerbit","dim_penerbit",db_dimension)

#penulis
rel_idPenulis     = fun_lastId("id_penulis","tb_penulis",db_perpus)
countRel_Penulis  = fun_count("id_penulis","tb_penulis",db_perpus)

dim_idPenulis    = fun_lastId("id_penulis","dim_penulis",db_dimension)
countDim_Penulis = fun_count("id_penulis","dim_penulis",db_dimension)

#perpus
rel_idPerpus     = fun_lastId("id_perpus","tb_perpus",db_perpus)
countRel_Perpus  = fun_count("id_perpus","tb_perpus",db_perpus)

dim_idPerpus    = fun_lastId("id_perpus","dim_perpus",db_dimension)
countDim_Perpus = fun_count("id_perpus","dim_perpus",db_dimension)

#trans
rel_idDetail    = fun_lastId("id_detail","tb_detail_trans",db_perpus)
countRel_Trans  = fun_count("id_detail","tb_detail_trans",db_perpus)

dim_idTrans    = fun_lastId("id_fakta_trans","fakta_trans",db_dimension)
countDim_Trans = fun_count("id_fakta_trans","fakta_trans",db_dimension)


# ----------------- Check Condition -----------------#
val_buku     = function_condition(rel_idBuku, dim_idBuku, countRel_buku,countDim_buku, 'Buku')
val_member   = function_condition(rel_idMember, dim_idMember, countRel_Member,countDim_Member, "Member")
val_pegawai  = function_condition(rel_idPegawai, dim_idPegawai, countRel_Pegawai,countDim_Pegawai, "Pegawai")
val_penerbit = function_condition(rel_idPenerbit,dim_idPenerbit,countRel_Penerbit, countDim_Penerbit,"Penerbit")
val_penulis  = function_condition(rel_idPenulis,dim_idPenulis,countRel_Penulis,countDim_Penulis,"Penulis")
val_perpus   = function_condition(rel_idPerpus,dim_idPerpus,countRel_Perpus,countDim_Perpus,"Perpus")
val_trans    = function_condition(rel_idDetail,dim_idTrans,countRel_Trans,countDim_Trans,"Transaksi")

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

print("Loading...")
for x in select_trans:
    val_a, val_b, val_c, val_d, val_e, val_f, val_g, val_h, val_i = x
    query_insert = "INSERT INTO fakta_trans SET id_trans = {0}, id_pegawai = '{1}', id_member = '{2}', tanggal_pinjam = '{3}', tanggal_kembali = '{4}', id_perpus = '{5}', id_buku = '{6}', id_penerbit = '{7}', id_penulis = '{8}'".format(val_a, val_b, val_c, val_d, val_e, val_f, val_g, val_h, val_i)
    function_instert(db_dimension,query_insert)
print("Sukses")

# disconnect from server
db_perpus.close()
db_dimension.close()