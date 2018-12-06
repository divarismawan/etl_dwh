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
def function_select_max(db,q):
    cursor = db.cursor()
    cursor.execute(q)
    result = cursor.fetchone()
    return result

# for insert data to table
def function_instert(db_dimensi,query):
    cursor = db_dimensi.cursor()
    cursor.execute(query)
    db_dimensi.commit()

# for check different data in both database
def function_condition(val_rel, val_dim, tbl_name):
    print("Data in table %s"%tbl_name)
    if(val_dim[0] != None):
        if(val_rel > val_dim):
            val_newRel = val_rel[0]
            val_newDim = val_dim[0] +1
            result = val_newRel - val_newDim +1
            print("Jumlah data baru = %d"%result)
            print("Tambah data mulai dari = %d"%val_newDim)
            print("")
            return val_newDim
        else:
            val_newDim = val_rel[0]+1
            print("Nilai sama")
            print("")
            return val_newDim
    else:
        val_newDim = 1
        print("Tambah data sebanyak : {0}".format(val_rel[0]))
        print("")
        return val_newDim



# ----------------- SQL Query Get Value Max----------------- #
# Buku
getRel_buku = "SELECT MAX(id_buku) from tb_buku"
rel_idBuku  = function_select_max(db_perpus,getRel_buku)

getDim_buku = "SELECT MAX(id_buku) from dim_buku"
dim_idBuku  = function_select_max(db_dimension,getDim_buku)

# Member
getRel_member = "SELECT MAX(id_member) from tb_member"
rel_idMember  = function_select_max(db_perpus,getRel_member)

getDim_member = "SELECT MAX(id_member) from dim_member"
dim_idMember  = function_select_max(db_dimension,getDim_member)

# Pegawai
getRel_pegawai = "SELECT MAX(id_pegawai) from tb_pegawai "
rel_idPegawai  = function_select_max(db_perpus,getRel_pegawai)

getDim_pegawai = "SELECT MAX(id_pegawai) from dim_pegawai"
dim_idPegawai  = function_select_max(db_dimension,getDim_pegawai)

# penerbit
getRel_penerbit = "SELECT MAX(id_penerbit) from tb_penerbit"
rel_idPenerbit  = function_select_max(db_perpus,getRel_penerbit)

getDim_penerbit = "SELECT MAX(id_penerbit) from dim_penerbit"
dim_idPenerbit  = function_select_max(db_dimension,getDim_penerbit)

#penulis
getRel_penulis = "SELECT MAX(id_penulis) from tb_penulis"
rel_idPenulis  = function_select_max(db_perpus,getRel_penulis)

getDim_penulis = "SELECT MAX(id_penulis) from dim_penulis"
dim_idPenulis  = function_select_max(db_dimension,getDim_penulis)

#perpus
getRel_perpus = "SELECT MAX(id_perpus) from tb_perpus"
rel_idPerpus  = function_select_max(db_perpus,getRel_perpus)

getDim_perpus = "SELECT MAX(id_perpus) from dim_perpus"
dim_idPerpus  = function_select_max(db_dimension,getDim_perpus)

#trans
getRel_detail = "SELECT MAX(id_detail) from tb_detail_trans"
rel_idDetail  = function_select_max(db_perpus,getRel_detail)

getDim_trans  = "SELECT MAX(id_fakta_trans) from fakta_trans"
dim_idTrans   = function_select_max(db_dimension,getDim_trans)


# ----------------- Check Condition -----------------#
val_buku     = function_condition(rel_idBuku, dim_idBuku, 'Buku')
val_member   = function_condition(rel_idMember, dim_idMember, "Member")
val_pegawai  = function_condition(rel_idPegawai, dim_idPegawai, "Pegawai")
val_penerbit = function_condition(rel_idPenerbit,dim_idPenerbit,"Penerbit")
val_penulis  = function_condition(rel_idPenulis,dim_idPenulis,"Penulis")
val_perpus   = function_condition(rel_idPerpus,dim_idPerpus,"Perpus")
val_trans    = function_condition(rel_idDetail,dim_idTrans,"Transaksi")

# ----------------- SQL Query SELECT----------------- #
sql_buku        = "SELECT id_buku,title_buku, ISBN FROM tb_buku WHERE id_buku >= {0}".format(val_buku)
sql_member      = "SELECT id_member,nama FROM tb_member WHERE id_member >={0}".format(val_member)
sql_pegawai     = "SELECT id_pegawai,nama_pegawai FROM tb_pegawai WHERE id_pegawai >={0}".format(val_pegawai)
sql_penerbit    = "SELECT id_penerbit, nama_perusahaan FROM tb_penerbit WHERE id_penerbit >={0}".format(val_penerbit)
sql_penulis     = "SELECT id_penulis,nama_penulis FROM tb_penulis WHERE id_penulis >={0}".format(val_penulis)
sql_perpus      = "SELECT id_perpus,nama_perpus, alamat_perpus FROM tb_perpus WHERE id_perpus >={0}".format(val_perpus)
sql_trans       = "SELECT id_trans FROM tb_detail_trans WHERE id_detail >={0}".format(val_trans)


#----------------- Use function SELECT -----------------#
select_buku     = function_select(db_perpus, sql_buku)
select_member   = function_select(db_perpus, sql_member)
select_pegawai  = function_select(db_perpus, sql_pegawai)
select_penerbit = function_select(db_perpus, sql_penerbit)
select_penulis  = function_select(db_perpus, sql_penulis)
select_perpus   = function_select(db_perpus,sql_perpus)
select_trans    = function_select(db_perpus,sql_trans)

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

for x in select_trans:
    print("Loading...")
    val_a = x[0]
    query_insert = "INSERT INTO fakta_trans SET id_trans = {0}".format(val_a)
    print("Load")
    function_instert(db_dimension,query_insert)
    print("Sukses")

# disconnect from server
db_perpus.close()
db_dimension.close()