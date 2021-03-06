from numpy.distutils.fcompiler import none
import wx

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
            return getId_dim
        else:
            print("Value data sama")
            print("")
            return getId_rel
    else:
        val_newDim = 0
        print("Tambah data sebanyak : {0}".format(result))
        print("")
        return val_newDim

def show_etl(self):
    # ----------------- SQL Query Get Value Max----------------- #
    val_buku     = fun_all("id_detail_buku", "tb_detail_buku", "id_detail_buku", "dim_buku", "Buku")
    val_member   = fun_all("id_member", "tb_member", "id_member", "dim_member", "Member")
    val_pegawai  = fun_all("id_pegawai", "tb_pegawai", "id_pegawai", "dim_pegawai", "Pegawai")
    val_penerbit = fun_all("id_penerbit", "tb_penerbit", "id_penerbit", "dim_penerbit", "Penerbit")
    val_penulis  = fun_all("id_penulis", "tb_penulis", "id_penulis", "dim_penulis", "Penulis")
    val_rak      = fun_all("id_rak", "tb_rak_buku", "id_rak","dim_rak","Rak Buku")
    val_perpus   = fun_all("id_perpus", "tb_perpus", "id_perpus", "dim_perpus", "Perpus")
    val_trans    = fun_all("id_detail", "tb_detail_trans", "id_detail_trans", "fakta_trans", "Transaksi")

    # ----------------- SQL Query SELECT----------------- #
    sql_member   = "SELECT id_member,nama FROM tb_member WHERE id_member >{0}".format(val_member)

    sql_pegawai  = "SELECT id_pegawai,nama_pegawai FROM tb_pegawai WHERE id_pegawai >{0}".format(val_pegawai)

    sql_penerbit = "SELECT id_penerbit, nama_perusahaan FROM tb_penerbit WHERE id_penerbit >{0}".format(val_penerbit)

    sql_penulis  = "SELECT id_penulis,nama_penulis FROM tb_penulis WHERE id_penulis >{0}".format(val_penulis)

    sql_perpus   = "SELECT id_perpus,nama_perpus, alamat_perpus FROM tb_perpus WHERE id_perpus >{0}".format(val_perpus)

    sql_rak      = "SELECT id_rak, nama_rak FROM tb_rak_buku WHERE id_rak >{0}".format(val_rak)

    sql_buku     = "SELECT tb_detail_buku.`id_detail_buku`, tb_detail_buku.`id_buku`, tb_rak_buku.`id_rak`, " \
                   "tb_rak_buku.`id_perpus`, tb_buku.`title_buku`, tb_detail_buku.`barcode_buku`, tb_buku.`time_update` " \
                   "FROM tb_detail_buku " \
                   "JOIN tb_buku ON tb_buku.`id_buku` = tb_detail_buku.`id_buku` " \
                   "JOIN tb_rak_buku ON tb_detail_buku.`id_rak_buku` = tb_rak_buku.`id_rak` " \
                   "WHERE tb_detail_buku.`id_detail_buku` > {0} " \
                   "ORDER BY tb_detail_buku.`id_detail_buku`".format(val_buku)

    sql_trans    = "SELECT tb_detail_trans.`id_detail`,tb_detail_trans.`id_trans`,tb_detail_buku.`id_detail_buku`," \
                   "tb_detail_buku.`id_rak_buku`,tb_rak_buku.`id_perpus`,tb_buku.`id_penerbit`,tb_buku.`id_penulis`," \
                   "tb_transaksi.`id_member`,tb_transaksi.`id_pegawai`,tb_transaksi.`tgl_pinjam`,tb_transaksi.`tgl_kembali`" \
                   "FROM tb_detail_trans " \
                   "JOIN tb_transaksi ON tb_detail_trans.`id_trans` = tb_transaksi.`id_trans` " \
                   "JOIN tb_detail_buku ON tb_detail_buku.`id_detail_buku` = tb_detail_trans.`id_detail_buku`" \
                   "JOIN tb_rak_buku ON tb_rak_buku.`id_rak` = tb_detail_buku.`id_rak_buku`" \
                   "JOIN tb_buku ON tb_detail_buku.`id_buku` = tb_buku.`id_buku`" \
                   "AND tb_detail_trans.`id_detail` > {0} ORDER BY tb_detail_trans.`id_detail` ".format(val_trans)

    # ----------------- Count -----------------#
    # Buku
    countRel_buku = fun_count("id_detail_buku", "tb_detail_buku", db_perpus)
    countDim_buku = fun_count("id_detail_buku", "dim_buku", db_dimension)

    add_buku = countRel_buku - countDim_buku

    data_buku = [countDim_buku,add_buku,countDim_buku+add_buku]

    for x in range(0,len(data_buku)):
        self.m_grid3.SetCellValue(x,0,str(data_buku[x]))

    # penulis
    countRel_Penulis = fun_count("id_penulis", "tb_penulis", db_perpus)
    countDim_Penulis = fun_count("id_penulis", "dim_penulis", db_dimension)

    add_penulis  = countRel_Penulis - countDim_Penulis
    data_penulis = [countDim_Penulis, add_penulis, countDim_Penulis + add_penulis]

    for x in range(0, len(data_penulis)):
        self.m_grid3.SetCellValue(x, 1, str(data_penulis[x]))


    # penerbit
    countRel_Penerbit = fun_count("id_penerbit", "tb_penerbit", db_perpus)
    countDim_Penerbit = fun_count("id_penerbit", "dim_penerbit", db_dimension)

    add_penerbit  = countRel_Penerbit - countDim_Penerbit
    data_penerbit = [countDim_Penerbit, add_penerbit, countDim_Penerbit + add_penerbit]

    for x in range(0, len(data_penerbit)):
        self.m_grid3.SetCellValue(x, 2, str(data_penerbit[x]))

    # Member
    countRel_Member = fun_count("id_member", "tb_member", db_perpus)
    countDim_Member = fun_count("id_member", "dim_member", db_dimension)

    add_member  = countRel_Member - countDim_Member
    data_member = [countDim_Member, add_member, countDim_Member + add_member]

    for x in range(0, len(data_member)):
        self.m_grid3.SetCellValue(x, 3, str(data_member[x]))

    # Pegawai
    countRel_Pegawai = fun_count("id_pegawai", "tb_pegawai", db_perpus)
    countDim_Pegawai = fun_count("id_pegawai", "dim_pegawai", db_dimension)

    add_pegawai  = countRel_Pegawai - countDim_Pegawai
    data_pegawai = [countDim_Pegawai, add_pegawai, countDim_Pegawai + add_pegawai]

    for x in range(0, len(data_pegawai)):
        self.m_grid3.SetCellValue(x, 4, str(data_pegawai[x]))

    # Rak Buku

    countRel_rak  = fun_count("id_rak","tb_rak_buku",db_perpus)
    countDim_rak  = fun_count("id_rak","dim_rak",db_dimension)

    add_rak       = countRel_rak - countDim_rak
    data_rak      = [countDim_rak, add_rak, countDim_rak + add_rak]

    for x in range(0,len(data_rak)):
        self.m_grid3.SetCellValue(x,5,str(data_rak[x]))

    # perpus
    countRel_Perpus = fun_count("id_perpus", "tb_perpus", db_perpus)
    countDim_Perpus = fun_count("id_perpus", "dim_perpus", db_dimension)

    add_perpus = countRel_Perpus - countDim_Perpus
    data_perpus = [countDim_Perpus, add_perpus, countDim_Perpus + add_perpus]

    for x in range(0, len(data_perpus)):
        self.m_grid3.SetCellValue(x, 6, str(data_perpus[x]))

    # trans
    countRel_Trans = fun_count("id_detail", "tb_detail_trans", db_perpus)
    countDim_Trans = fun_count("id_fakta_trans", "fakta_trans", db_dimension)

    add_trans = countRel_Trans - countDim_Trans
    data_trans = [countDim_Trans, add_trans, countDim_Trans + add_trans]

    for x in range(0, len(data_trans)):
        self.m_grid3.SetCellValue(x, 7, str(data_trans[x]))


    # ----------------- Use function SELECT -----------------#
    select_member   = function_select(db_perpus, sql_member)
    select_pegawai  = function_select(db_perpus, sql_pegawai)
    select_penerbit = function_select(db_perpus, sql_penerbit)
    select_penulis  = function_select(db_perpus, sql_penulis)
    select_rak      = function_select(db_perpus, sql_rak)
    select_perpus   = function_select(db_perpus, sql_perpus)
    select_buku     = function_select(db_perpus, sql_buku)
    select_trans    = function_select(db_perpus, sql_trans)

    # ----------------- INSERT data to Data Warehouse -----------------#
    print("Loading...")
    for x in select_member:
        val_a, val_b = x
        query_insert = ("INSERT INTO dim_member SET id_member ={0},nama_member='{1}'".format(val_a, val_b))
        function_instert(db_dimension, query_insert)

    for x in select_pegawai:
        val_a, val_b = x
        query_insert = ("INSERT INTO dim_pegawai SET id_pegawai={0},nama_pegawai='{1}'".format(val_a, val_b))
        function_instert(db_dimension, query_insert)

    for x in select_penerbit:
        val_a, val_b = x
        query_insert = (
            "INSERT INTO dim_penerbit SET id_penerbit = {0}, nama_perusahaan = '{1}'".format(val_a, val_b))
        function_instert(db_dimension, query_insert)

    for x in select_penulis:
        val_a, val_b = x
        query_insert = ("INSERT INTO dim_penulis SET id_penulis = {0}, nama_penulis='{1}'".format(val_a, val_b))
        function_instert(db_dimension, query_insert)

    for x in select_rak:
        val_a, val_b = x
        query_insert = ("INSERT INTO dim_rak SET id_rak ={0}, nama_rak = '{1}'".format(val_a,val_b))
        function_instert(db_dimension,query_insert)

    for x in select_perpus:
        val_a, val_b, val_c = x
        query_insert = (
            "INSERT INTO dim_perpus SET id_perpus = {0}, "
            "nama_perpus = '{1}', "
            "alamat_perpus = '{2}'".format(val_a,val_b,val_c))
        function_instert(db_dimension, query_insert)

    for x in select_buku:
        val_a, val_b, val_c, val_d, val_e, val_f, val_g = x
        query_insert = ("INSERT INTO dim_buku SET id_detail_buku = {0}, id_buku = {1}, id_rak = {2}, "
                        "id_perpus = {3}, title_buku = '{4}', "
                        "barcode_buku = '{5}', time_update = '{6}'".format(val_a, val_b, val_c, val_d, val_e, val_f, val_g))
        function_instert(db_dimension, query_insert)

    for x in select_trans:
        val_a, val_b, val_c, val_d, val_e, val_f, val_g, val_h, val_i, val_j, val_k = x
        query_insert = "INSERT INTO fakta_trans SET id_detail_trans = {0}, id_trans = {1}, id_detail_buku = {2}, id_rak = {3}," \
                       "id_perpus = {4}, id_penerbit = {5}, id_penulis = {6}, id_member ={7}, id_pegawai = {8}," \
                       "tanggal_pinjam = '{9}', tanggal_kembali = '{10}'".format(val_a,val_b,val_c,val_d,val_e,val_f,val_g,val_h,val_i,val_j,val_k)
        function_instert(db_dimension, query_insert)
    print("Sukses")

    # reload from server
    db_perpus.rollback()
    db_dimension.rollback()

def fun_trancate_database():
        cursor = db_dimension.cursor()
        sql = "CALL clear()"
        cursor.execute(sql)
        pass
        wx.MessageBox("Data berhasil Dihapus", "Message", wx.OK | wx.ICON_INFORMATION)



