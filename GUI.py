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

panel_pinjam = 1000
sp_month = 1001
grid_showResult = 1002


###########################################################################
## Class GUI_DWH
###########################################################################

class GUI_DWH(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(999, 538), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_pinjam = wx.Notebook(self, panel_pinjam, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panelETL = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel5 = wx.Panel(self.m_panelETL, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10.Add(self.m_panel5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_grid3 = wx.grid.Grid(self.m_panelETL, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(3, 7)
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
        self.m_grid3.SetColLabelValue(5, u"Perpus")
        self.m_grid3.SetColLabelValue(6, u"Transaksi")
        self.m_grid3.SetColLabelValue(7, wx.EmptyString)
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

        self.m_buttonSmt = wx.Button(self.m_panelETL, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_buttonSmt, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer10.Add(bSizer12, 0, wx.ALIGN_RIGHT, 5)

        bSizer9.Add(bSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panelETL.SetSizer(bSizer9)
        self.m_panelETL.Layout()
        bSizer9.Fit(self.m_panelETL)
        self.panel_pinjam.AddPage(self.m_panelETL, u"ETL", False)
        self.m_panel1 = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        sp_monthChoices = [u"Januari", u"Februari", u"Maret", u"April", u"Mei", u"Juni", u"Juli", u"Agustus",
                           u"September", u"Oktober", u"November", u"Desember"]
        self.sp_month = wx.Choice(self.m_panel1, sp_month, wx.DefaultPosition, wx.DefaultSize, sp_monthChoices, 0)
        self.sp_month.SetSelection(0)
        bSizer5.Add(self.sp_month, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sp_yearChoices = [u"2017", u"2018"]
        self.sp_year = wx.Choice(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, sp_yearChoices, 0)
        self.sp_year.SetSelection(1)
        bSizer5.Add(self.sp_year, 0, wx.ALL, 5)

        bSizer13.Add(bSizer5, 0, 0, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.grid_showResult = wx.grid.Grid(self.m_panel1, grid_showResult, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_showResult.CreateGrid(10, 2)
        self.grid_showResult.EnableEditing(True)
        self.grid_showResult.EnableGridLines(True)
        self.grid_showResult.EnableDragGridSize(False)
        self.grid_showResult.SetMargins(0, 0)

        # Columns
        self.grid_showResult.SetColSize(0, 300)
        self.grid_showResult.SetColSize(1, 100)
        self.grid_showResult.EnableDragColMove(True)
        self.grid_showResult.EnableDragColSize(True)
        self.grid_showResult.SetColLabelSize(30)
        self.grid_showResult.SetColLabelValue(0, u"Buku")
        self.grid_showResult.SetColLabelValue(1, u"Jumlah")
        self.grid_showResult.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_showResult.AutoSizeRows()
        self.grid_showResult.EnableDragRowSize(True)
        self.grid_showResult.SetRowLabelSize(90)
        self.grid_showResult.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_showResult.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer4.Add(self.grid_showResult, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer61 = wx.BoxSizer(wx.HORIZONTAL)

        self.button_pinjam = wx.Button(self.m_panel1, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer61.Add(self.button_pinjam, 0, wx.ALL, 5)

        bSizer4.Add(bSizer61, 0, wx.ALIGN_RIGHT, 5)

        bSizer13.Add(bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer3.Add(bSizer13, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel1.SetSizer(bSizer3)
        self.m_panel1.Layout()
        bSizer3.Fit(self.m_panel1)
        self.panel_pinjam.AddPage(self.m_panel1, u"Peminjaman ", False)
        self.m_panel7 = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        bSizer42 = wx.BoxSizer(wx.VERTICAL)

        m_choice4Choices = [u"2017", u"2018"]
        self.m_choice4 = wx.Choice(self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0)
        self.m_choice4.SetSelection(0)
        bSizer42.Add(self.m_choice4, 0, wx.ALL, 5)

        self.grid_showResult1 = wx.grid.Grid(self.m_panel7, grid_showResult, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_showResult1.CreateGrid(12, 3)
        self.grid_showResult1.EnableEditing(True)
        self.grid_showResult1.EnableGridLines(True)
        self.grid_showResult1.EnableDragGridSize(False)
        self.grid_showResult1.SetMargins(0, 0)

        # Columns
        self.grid_showResult1.SetColSize(0, 150)
        self.grid_showResult1.SetColSize(1, 100)
        self.grid_showResult1.EnableDragColMove(True)
        self.grid_showResult1.EnableDragColSize(True)
        self.grid_showResult1.SetColLabelSize(30)
        self.grid_showResult1.SetColLabelValue(0, u"Buku")
        self.grid_showResult1.SetColLabelValue(1, u"Jumlah")
        self.grid_showResult1.SetColLabelValue(2, u"Bulan")
        self.grid_showResult1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_showResult1.AutoSizeRows()
        self.grid_showResult1.EnableDragRowSize(True)
        self.grid_showResult1.SetRowLabelSize(90)
        self.grid_showResult1.SetRowLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_showResult1.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        bSizer42.Add(self.grid_showResult1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer611 = wx.BoxSizer(wx.HORIZONTAL)

        self.button_pinjam1 = wx.Button(self.m_panel7, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer611.Add(self.button_pinjam1, 0, wx.ALL, 5)

        bSizer42.Add(bSizer611, 0, wx.ALIGN_RIGHT, 5)

        bSizer15.Add(bSizer42, 1, wx.EXPAND, 5)

        bSizer14.Add(bSizer15, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel7.SetSizer(bSizer14)
        self.m_panel7.Layout()
        bSizer14.Fit(self.m_panel7)
        self.panel_pinjam.AddPage(self.m_panel7, u"Per Tahun", True)
        self.m_panel8 = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer24 = wx.BoxSizer(wx.VERTICAL)

        bSizer25 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel9 = wx.Panel(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer25.Add(self.m_panel9, 1, wx.EXPAND | wx.ALL, 5)

        self.m_grid7 = wx.grid.Grid(self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid7.CreateGrid(20, 8)
        self.m_grid7.EnableEditing(True)
        self.m_grid7.EnableGridLines(True)
        self.m_grid7.EnableDragGridSize(False)
        self.m_grid7.SetMargins(0, 0)

        # Columns
        self.m_grid7.SetColSize(0, 100)
        self.m_grid7.SetColSize(1, 100)
        self.m_grid7.SetColSize(2, 100)
        self.m_grid7.SetColSize(3, 100)
        self.m_grid7.SetColSize(4, 100)
        self.m_grid7.SetColSize(5, 100)
        self.m_grid7.SetColSize(6, 100)
        self.m_grid7.SetColSize(7, 100)
        self.m_grid7.EnableDragColMove(False)
        self.m_grid7.EnableDragColSize(True)
        self.m_grid7.SetColLabelSize(30)
        self.m_grid7.SetColLabelValue(0, u"Member")
        self.m_grid7.SetColLabelValue(1, u"Buku")
        self.m_grid7.SetColLabelValue(2, u"Penulis")
        self.m_grid7.SetColLabelValue(3, u"Penerbit")
        self.m_grid7.SetColLabelValue(4, u"Perpus")
        self.m_grid7.SetColLabelValue(5, u"Pegawai")
        self.m_grid7.SetColLabelValue(6, u"Tgl_pinjam")
        self.m_grid7.SetColLabelValue(7, u"Tgl Kembali")
        self.m_grid7.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid7.EnableDragRowSize(True)
        self.m_grid7.SetRowLabelSize(80)
        self.m_grid7.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid7.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer25.Add(self.m_grid7, 0, wx.ALL, 5)

        bSizer26 = wx.BoxSizer(wx.HORIZONTAL)

        self.button_fact = wx.Button(self.m_panel8, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer26.Add(self.button_fact, 0, wx.ALL, 5)

        bSizer25.Add(bSizer26, 1, wx.ALIGN_RIGHT, 5)

        bSizer24.Add(bSizer25, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel8.SetSizer(bSizer24)
        self.m_panel8.Layout()
        bSizer24.Fit(self.m_panel8)
        self.panel_pinjam.AddPage(self.m_panel8, u"Fact Data", False)

        bSizer1.Add(self.panel_pinjam, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


