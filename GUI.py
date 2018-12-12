# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.dataview

panel_pinjam = 1000


###########################################################################
## Class GUI_DWH
###########################################################################

class GUI_DWH(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(843, 426), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_pinjam = wx.Notebook(self, panel_pinjam, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_ETL = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel5 = wx.Panel(self.m_panel_ETL, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10.Add(self.m_panel5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_grid3 = wx.grid.Grid(self.m_panel_ETL, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(3, 8)
        self.m_grid3.EnableEditing(True)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)

        # Columns
        self.m_grid3.SetColSize(0, 90)
        self.m_grid3.SetColSize(1, 90)
        self.m_grid3.SetColSize(2, 90)
        self.m_grid3.SetColSize(3, 90)
        self.m_grid3.SetColSize(4, 90)
        self.m_grid3.SetColSize(5, 90)
        self.m_grid3.SetColSize(6, 90)
        self.m_grid3.EnableDragColMove(False)
        self.m_grid3.EnableDragColSize(True)
        self.m_grid3.SetColLabelSize(40)
        self.m_grid3.SetColLabelValue(0, u"Buku")
        self.m_grid3.SetColLabelValue(1, u"Penulis")
        self.m_grid3.SetColLabelValue(2, u"Penerbit")
        self.m_grid3.SetColLabelValue(3, u"Member")
        self.m_grid3.SetColLabelValue(4, u"Pegawai")
        self.m_grid3.SetColLabelValue(5, u"Rak Buku")
        self.m_grid3.SetColLabelValue(6, u"Perpus")
        self.m_grid3.SetColLabelValue(7, u"Transaksi")
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid3.SetRowSize(0, 30)
        self.m_grid3.SetRowSize(1, 30)
        self.m_grid3.SetRowSize(2, 30)
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(90)
        self.m_grid3.SetRowLabelValue(0, u"Data awal")
        self.m_grid3.SetRowLabelValue(1, u"Penambahan")
        self.m_grid3.SetRowLabelValue(2, u"Total")
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        bSizer10.Add(self.m_grid3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_buttonSmt = wx.Button(self.m_panel_ETL, wx.ID_ANY, u"Extract and Load", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        bSizer12.Add(self.m_buttonSmt, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer10.Add(bSizer12, 0, wx.ALIGN_RIGHT, 5)

        bSizer9.Add(bSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel_ETL.SetSizer(bSizer9)
        self.m_panel_ETL.Layout()
        bSizer9.Fit(self.m_panel_ETL)
        self.panel_pinjam.AddPage(self.m_panel_ETL, u"ETL", False)
        self.m_panel_peminjaman = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TAB_TRAVERSAL)
        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook4 = wx.Notebook(self.m_panel_peminjaman, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel_member = wx.Panel(self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL)
        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        bSizer32 = wx.BoxSizer(wx.VERTICAL)

        bSizer33 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText8 = wx.StaticText(self.m_panel_member, wx.ID_ANY, u"Nama Member", wx.DefaultPosition,
                                           wx.Size(100, -1), 0)
        self.m_staticText8.Wrap(-1)
        bSizer33.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_text_member = wx.TextCtrl(self.m_panel_member, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer33.Add(self.m_text_member, 0, wx.ALL, 5)

        self.m_button_member = wx.Button(self.m_panel_member, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer33.Add(self.m_button_member, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_button_save_member = wx.Button(self.m_panel_member, wx.ID_ANY, u"Save ", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        bSizer33.Add(self.m_button_save_member, 0, wx.ALL, 5)

        bSizer32.Add(bSizer33, 0, 0, 5)

        self.m_dataViewList_member = wx.dataview.DataViewListCtrl(self.m_panel_member, wx.ID_ANY, wx.DefaultPosition,
                                                                  wx.DefaultSize, 0)
        self.m_dataViewListColumn26 = self.m_dataViewList_member.AppendTextColumn(u"No")
        self.m_dataViewListColumn35 = self.m_dataViewList_member.AppendTextColumn(u"Kode Buku")
        self.m_dataViewListColumn27 = self.m_dataViewList_member.AppendTextColumn(u"Buku")
        self.m_dataViewListColumn28 = self.m_dataViewList_member.AppendTextColumn(u"Perpustakaan")
        self.m_dataViewListColumn29 = self.m_dataViewList_member.AppendTextColumn(u"Tanggal")
        self.m_dataViewListColumn30 = self.m_dataViewList_member.AppendTextColumn(u"Bulam")
        self.m_dataViewListColumn31 = self.m_dataViewList_member.AppendTextColumn(u"Tahun")
        bSizer32.Add(self.m_dataViewList_member, 1, wx.ALL | wx.EXPAND, 5)

        bSizer31.Add(bSizer32, 1, wx.EXPAND, 5)

        self.m_panel_member.SetSizer(bSizer31)
        self.m_panel_member.Layout()
        bSizer31.Fit(self.m_panel_member)
        self.m_notebook4.AddPage(self.m_panel_member, u"Member", True)
        self.m_panel_peminjaman1 = wx.Panel(self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TAB_TRAVERSAL)
        bSizer21 = wx.BoxSizer(wx.VERTICAL)

        bSizer22 = wx.BoxSizer(wx.VERTICAL)

        bSizer241 = wx.BoxSizer(wx.HORIZONTAL)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText3 = wx.StaticText(self.m_panel_peminjaman1, wx.ID_ANY, u"Bulan", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gSizer1.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_monthChoices = [u"Januari", u"Februari", u"Maret", u"April", u"Mei", u"Juni", u"Juli", u"Agustus",
                                 u"September", u"Oktober", u"November", u"Desember"]
        self.m_choice_month = wx.Choice(self.m_panel_peminjaman1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        m_choice_monthChoices, 0)
        self.m_choice_month.SetSelection(0)
        gSizer1.Add(self.m_choice_month, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel_peminjaman1, wx.ID_ANY, u"Tahun", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        gSizer1.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_yearChoices = [u"2017", u"2018"]
        self.m_choice_year = wx.Choice(self.m_panel_peminjaman1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       m_choice_yearChoices, 0)
        self.m_choice_year.SetSelection(1)
        gSizer1.Add(self.m_choice_year, 0, wx.ALL, 5)

        bSizer241.Add(gSizer1, 1, wx.EXPAND, 5)

        bSizer271 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_peminjaman = wx.Button(self.m_panel_peminjaman1, wx.ID_ANY, u"Show", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        bSizer271.Add(self.m_button_peminjaman, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button_save_month = wx.Button(self.m_panel_peminjaman1, wx.ID_ANY, u"Save", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        bSizer271.Add(self.m_button_save_month, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer241.Add(bSizer271, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        bSizer22.Add(bSizer241, 0, 0, 5)

        self.m_dataViewList_peminjaman = wx.dataview.DataViewListCtrl(self.m_panel_peminjaman1, wx.ID_ANY,
                                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_dataViewListColumn6 = self.m_dataViewList_peminjaman.AppendTextColumn(u"No")
        self.m_dataViewListColumn36 = self.m_dataViewList_peminjaman.AppendTextColumn(u"Kode Buku")
        self.m_dataViewListColumn7 = self.m_dataViewList_peminjaman.AppendTextColumn(u"Buku")
        self.m_dataViewListColumn8 = self.m_dataViewList_peminjaman.AppendTextColumn(u"Jumlah")
        bSizer22.Add(self.m_dataViewList_peminjaman, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer21.Add(bSizer22, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel_peminjaman1.SetSizer(bSizer21)
        self.m_panel_peminjaman1.Layout()
        bSizer21.Fit(self.m_panel_peminjaman1)
        self.m_notebook4.AddPage(self.m_panel_peminjaman1, u"Bulanan", False)
        self.m_panel_tahun = wx.Panel(self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer28 = wx.BoxSizer(wx.VERTICAL)

        bSizer29 = wx.BoxSizer(wx.VERTICAL)

        bSizer30 = wx.BoxSizer(wx.VERTICAL)

        bSizer191 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self.m_panel_tahun, wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size(80, -1),
                                           0)
        self.m_staticText5.Wrap(-1)
        bSizer191.Add(self.m_staticText5, 0, wx.ALL, 5)

        m_choice_tahunanChoices = [u"2017", u"2018"]
        self.m_choice_tahunan = wx.Choice(self.m_panel_tahun, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          m_choice_tahunanChoices, 0)
        self.m_choice_tahunan.SetSelection(0)
        bSizer191.Add(self.m_choice_tahunan, 0, wx.ALL, 5)

        self.m_button_tahunan = wx.Button(self.m_panel_tahun, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer191.Add(self.m_button_tahunan, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_button_save_year = wx.Button(self.m_panel_tahun, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        bSizer191.Add(self.m_button_save_year, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer30.Add(bSizer191, 0, 0, 5)

        bSizer29.Add(bSizer30, 0, 0, 5)

        self.m_dataViewList_tahun = wx.dataview.DataViewListCtrl(self.m_panel_tahun, wx.ID_ANY, wx.DefaultPosition,
                                                                 wx.DefaultSize, 0)
        self.m_dataViewListColumn22 = self.m_dataViewList_tahun.AppendTextColumn(u"No")
        self.m_dataViewListColumn23 = self.m_dataViewList_tahun.AppendTextColumn(u"Buku")
        self.m_dataViewListColumn24 = self.m_dataViewList_tahun.AppendTextColumn(u"Jumlah")
        self.m_dataViewListColumn25 = self.m_dataViewList_tahun.AppendTextColumn(u"Bulan")
        bSizer29.Add(self.m_dataViewList_tahun, 1, wx.ALL | wx.EXPAND, 5)

        bSizer28.Add(bSizer29, 1, wx.EXPAND, 5)

        self.m_panel_tahun.SetSizer(bSizer28)
        self.m_panel_tahun.Layout()
        bSizer28.Fit(self.m_panel_tahun)
        self.m_notebook4.AddPage(self.m_panel_tahun, u"Tahunan", False)

        bSizer23.Add(self.m_notebook4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel_peminjaman.SetSizer(bSizer23)
        self.m_panel_peminjaman.Layout()
        bSizer23.Fit(self.m_panel_peminjaman)
        self.panel_pinjam.AddPage(self.m_panel_peminjaman, u"Periode Peminjaman", False)
        self.m_panel11 = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer25 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook5 = wx.Notebook(self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel12 = wx.Panel(self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer26 = wx.BoxSizer(wx.VERTICAL)

        bSizer281 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText81 = wx.StaticText(self.m_panel12, wx.ID_ANY, u"Book Title", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)
        bSizer281.Add(self.m_staticText81, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer281.Add(self.m_textCtrl2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_bookTitleChoices = [u"2017", u"2018"]
        self.m_choice_bookTitle = wx.Choice(self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            m_choice_bookTitleChoices, 0)
        self.m_choice_bookTitle.SetSelection(0)
        bSizer281.Add(self.m_choice_bookTitle, 0, wx.ALL, 5)

        self.m_button_bookTitle = wx.Button(self.m_panel12, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer281.Add(self.m_button_bookTitle, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button_save_book = wx.Button(self.m_panel12, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer281.Add(self.m_button_save_book, 0, wx.ALL, 5)

        bSizer26.Add(bSizer281, 0, 0, 5)

        self.m_dataViewListCtrl6 = wx.dataview.DataViewListCtrl(self.m_panel12, wx.ID_ANY, wx.DefaultPosition,
                                                                wx.DefaultSize, 0 | wx.NO_BORDER)
        self.m_dataViewListColumn261 = self.m_dataViewListCtrl6.AppendTextColumn(u"No")
        self.m_dataViewListColumn37 = self.m_dataViewListCtrl6.AppendTextColumn(u"Kode Buku")
        self.m_dataViewListColumn291 = self.m_dataViewListCtrl6.AppendTextColumn(u"Jumlah Peminjaman")
        self.m_dataViewListColumn271 = self.m_dataViewListCtrl6.AppendTextColumn(u"Perpustakaan")
        self.m_dataViewListColumn281 = self.m_dataViewListCtrl6.AppendTextColumn(u"Bulan")
        bSizer26.Add(self.m_dataViewListCtrl6, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel12.SetSizer(bSizer26)
        self.m_panel12.Layout()
        bSizer26.Fit(self.m_panel12)
        self.m_notebook5.AddPage(self.m_panel12, u"Book Name", True)
        self.m_panel13 = wx.Panel(self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer291 = wx.BoxSizer(wx.VERTICAL)

        bSizer301 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText9 = wx.StaticText(self.m_panel13, wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer301.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_allBookChoices = [u"2017", u"2018"]
        self.m_choice_allBook = wx.Choice(self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          m_choice_allBookChoices, 0)
        self.m_choice_allBook.SetSelection(0)
        bSizer301.Add(self.m_choice_allBook, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button_allBook = wx.Button(self.m_panel13, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer301.Add(self.m_button_allBook, 0, wx.ALL, 5)

        self.m_button_save_allBook = wx.Button(self.m_panel13, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize,
                                               0)
        bSizer301.Add(self.m_button_save_allBook, 0, wx.ALL, 5)

        bSizer291.Add(bSizer301, 0, 0, 5)

        self.m_dataView_allBook = wx.dataview.DataViewListCtrl(self.m_panel13, wx.ID_ANY, wx.DefaultPosition,
                                                               wx.DefaultSize, 0)
        self.m_dataViewListColumn301 = self.m_dataView_allBook.AppendTextColumn(u"No")
        self.m_dataViewListColumn311 = self.m_dataView_allBook.AppendTextColumn(u"Book Title")
        self.m_dataViewListColumn32 = self.m_dataView_allBook.AppendTextColumn(u"Perpustakaan")
        self.m_dataViewListColumn33 = self.m_dataView_allBook.AppendTextColumn(u"Jumlah")
        self.m_dataViewListColumn34 = self.m_dataView_allBook.AppendTextColumn(u"Bulan")
        bSizer291.Add(self.m_dataView_allBook, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel13.SetSizer(bSizer291)
        self.m_panel13.Layout()
        bSizer291.Fit(self.m_panel13)
        self.m_notebook5.AddPage(self.m_panel13, u"All Book", False)
        self.m_panel_perpus = wx.Panel(self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL)
        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self.m_panel_perpus, wx.ID_ANY, u"Nama Perpustakaan", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer18.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_libraryChoices = [u"Tianjin Binhai Library", u"Seattle Public Library", u"Library of Birmingham"]
        self.m_choice_library = wx.Choice(self.m_panel_perpus, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          m_choice_libraryChoices, 0)
        self.m_choice_library.SetSelection(0)
        bSizer18.Add(self.m_choice_library, 0, wx.ALL, 5)

        self.m_staticText1 = wx.StaticText(self.m_panel_perpus, wx.ID_ANY, u"Tahun", wx.DefaultPosition,
                                           wx.Size(50, -1), 0)
        self.m_staticText1.Wrap(-1)
        bSizer18.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice_tahunChoices = [u"2017", u"2018"]
        self.m_choice_tahun = wx.Choice(self.m_panel_perpus, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        m_choice_tahunChoices, 0)
        self.m_choice_tahun.SetSelection(0)
        bSizer18.Add(self.m_choice_tahun, 0, wx.ALL, 5)

        self.m_button_perpus = wx.Button(self.m_panel_perpus, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.m_button_perpus, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

        self.m_button_save_perpus = wx.Button(self.m_panel_perpus, wx.ID_ANY, u"Save", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        bSizer18.Add(self.m_button_save_perpus, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer20.Add(bSizer18, 0, wx.EXPAND, 5)

        bSizer17.Add(bSizer20, 0, 0, 5)

        bSizer19 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataViewList_perpus = wx.dataview.DataViewListCtrl(self.m_panel_perpus, wx.ID_ANY, wx.DefaultPosition,
                                                                  wx.DefaultSize, 0)
        self.m_dataViewListColumn1 = self.m_dataViewList_perpus.AppendTextColumn(u"No")
        self.m_dataViewListColumn2 = self.m_dataViewList_perpus.AppendTextColumn(u"Buku")
        self.m_dataViewListColumn3 = self.m_dataViewList_perpus.AppendTextColumn(u"Jumlah Peminjaman")
        self.m_dataViewListColumn39 = self.m_dataViewList_perpus.AppendTextColumn(u"Bulan")
        bSizer19.Add(self.m_dataViewList_perpus, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)

        bSizer17.Add(bSizer19, 1, wx.EXPAND, 5)

        self.m_panel_perpus.SetSizer(bSizer17)
        self.m_panel_perpus.Layout()
        bSizer17.Fit(self.m_panel_perpus)
        self.m_notebook5.AddPage(self.m_panel_perpus, u"Perpustakaan", False)

        bSizer25.Add(self.m_notebook5, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel11.SetSizer(bSizer25)
        self.m_panel11.Layout()
        bSizer25.Fit(self.m_panel11)
        self.panel_pinjam.AddPage(self.m_panel11, u"Book", False)
        self.m_panel_fact = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer261 = wx.BoxSizer(wx.VERTICAL)

        bSizer27 = wx.BoxSizer(wx.VERTICAL)

        self.m_dataView_fact = wx.dataview.DataViewListCtrl(self.m_panel_fact, wx.ID_ANY, wx.DefaultPosition,
                                                            wx.DefaultSize, 0)
        self.m_dataViewListColumn12 = self.m_dataView_fact.AppendTextColumn(u"No")
        self.m_dataViewListColumn13 = self.m_dataView_fact.AppendTextColumn(u"Member")
        self.m_dataViewListColumn14 = self.m_dataView_fact.AppendTextColumn(u"Buku")
        self.m_dataViewListColumn15 = self.m_dataView_fact.AppendTextColumn(u"Penulis")
        self.m_dataViewListColumn16 = self.m_dataView_fact.AppendTextColumn(u"Penerbit")
        self.m_dataViewListColumn391 = self.m_dataView_fact.AppendTextColumn(u"Rak  Buku")
        self.m_dataViewListColumn17 = self.m_dataView_fact.AppendTextColumn(u"Perpustakann")
        self.m_dataViewListColumn18 = self.m_dataView_fact.AppendTextColumn(u"Pegawai")
        self.m_dataViewListColumn19 = self.m_dataView_fact.AppendTextColumn(u"Tanggal Pinjam")
        self.m_dataViewListColumn20 = self.m_dataView_fact.AppendTextColumn(u"Tanggal Kembali")
        bSizer27.Add(self.m_dataView_fact, 1, wx.ALL | wx.EXPAND, 5)

        bSizer282 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_save_fact = wx.Button(self.m_panel_fact, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        bSizer282.Add(self.m_button_save_fact, 0, wx.ALL, 5)

        self.m_button_fact = wx.Button(self.m_panel_fact, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer282.Add(self.m_button_fact, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer27.Add(bSizer282, 0, wx.ALIGN_RIGHT, 5)

        bSizer261.Add(bSizer27, 1, wx.EXPAND, 5)

        self.m_panel_fact.SetSizer(bSizer261)
        self.m_panel_fact.Layout()
        bSizer261.Fit(self.m_panel_fact)
        self.panel_pinjam.AddPage(self.m_panel_fact, u"Fact Data", True)

        bSizer1.Add(self.panel_pinjam, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


