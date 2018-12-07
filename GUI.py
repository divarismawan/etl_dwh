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
et_year = 1002
grid_showResult = 1003


###########################################################################
## Class GUI_DWH
###########################################################################

class GUI_DWH(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(772, 392), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_pinjam = wx.Notebook(self, panel_pinjam, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel1 = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel6 = wx.Panel(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        monthChoices = [u"Januari", u"Februari", u"Maret", u"April", u"Mei", u"Juni", u"Juli", u"Agustus", u"September",
                        u"Oktober", u"November", u"Desember"]
        self.month = wx.Choice(self.m_panel1, sp_month, wx.DefaultPosition, wx.DefaultSize, monthChoices, 0)
        self.month.SetSelection(0)
        bSizer5.Add(self.month, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.year = wx.TextCtrl(self.m_panel1, et_year, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.year.SetMaxLength(4)
        bSizer5.Add(self.year, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer3.Add(bSizer5, 0, 0, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.grid_showResult = wx.grid.Grid(self.m_panel1, grid_showResult, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_showResult.CreateGrid(5, 3)
        self.grid_showResult.EnableEditing(True)
        self.grid_showResult.EnableGridLines(True)
        self.grid_showResult.EnableDragGridSize(False)
        self.grid_showResult.SetMargins(0, 0)

        # Columns
        self.grid_showResult.SetColSize(0, 150)
        self.grid_showResult.SetColSize(1, 300)
        self.grid_showResult.SetColSize(2, 70)
        self.grid_showResult.EnableDragColMove(True)
        self.grid_showResult.EnableDragColSize(True)
        self.grid_showResult.SetColLabelSize(30)
        self.grid_showResult.SetColLabelValue(0, u"Perpustakaan")
        self.grid_showResult.SetColLabelValue(1, u"Buku")
        self.grid_showResult.SetColLabelValue(2, u"Jumlah")
        self.grid_showResult.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_showResult.AutoSizeRows()
        self.grid_showResult.EnableDragRowSize(True)
        self.grid_showResult.SetRowLabelSize(80)
        self.grid_showResult.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_showResult.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer4.Add(self.grid_showResult, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer3.Add(bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel1.SetSizer(bSizer3)
        self.m_panel1.Layout()
        bSizer3.Fit(self.m_panel1)
        self.panel_pinjam.AddPage(self.m_panel1, u"Peminjaman", False)
        self.m_panel2 = wx.Panel(self.panel_pinjam, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid2 = wx.grid.Grid(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(12, 5)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        # Columns
        self.m_grid2.SetColSize(0, 117)
        self.m_grid2.SetColSize(1, 132)
        self.m_grid2.SetColSize(2, 123)
        self.m_grid2.SetColSize(3, 115)
        self.m_grid2.SetColSize(4, 103)
        self.m_grid2.EnableDragColMove(True)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelValue(0, u"Buku")
        self.m_grid2.SetColLabelValue(1, u"Penulis")
        self.m_grid2.SetColLabelValue(2, u"Penerbit")
        self.m_grid2.SetColLabelValue(3, u"Perpus")
        self.m_grid2.SetColLabelValue(4, u"Transaksi")
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer6.Add(self.m_grid2, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel2.SetSizer(bSizer6)
        self.m_panel2.Layout()
        bSizer6.Fit(self.m_panel2)
        self.panel_pinjam.AddPage(self.m_panel2, u"ETL", True)

        bSizer1.Add(self.panel_pinjam, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class OpenGui(wx.App):

    def OnInit(self):
        myframe = GUI_DWH(None)
        myframe.Show(True)
        return True



def main():

    app = OpenGui()
    app.MainLoop()
    # dummy_word ="   "
    #clean_word = TrainingData.clean_words(dummy_word)
    #print(clean_word)


if __name__ == "__main__":
    main()