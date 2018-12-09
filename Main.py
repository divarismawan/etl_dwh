import wx

import ETL
import GUI
import Query

class GuiShow(GUI.GUI_DWH):

    def __init__(self):
        GUI.GUI_DWH.__init__(self,parent=None)
        self.m_buttonSmt.Bind(wx.EVT_BUTTON,self.show_etl)
        self.m_button_peminjaman.Bind(wx.EVT_BUTTON,self.show_by_month)
        self.m_button_tahunan.Bind(wx.EVT_BUTTON,self.show_by_year)
        self.m_button_fact.Bind(wx.EVT_BUTTON,self.show_fact)
        self.m_button_perpus.Bind(wx.EVT_BUTTON,self.show_by_perpus)


    def show_etl(self,event):
        ETL.show_etl(self)

    def show_by_month(self,event):
        self.m_dataViewList_peminjaman.DeleteAllItems()
        Query.show_by_month(self)

    def show_by_year(self, event):
        self.m_dataViewList_tahun.DeleteAllItems()
        Query.show_by_year(self)

    def show_fact(self,event):
        self.m_dataView_fact.DeleteAllItems()
        Query.show_fact(self)

    def show_by_perpus(self, event):
        self.m_dataViewList_perpus.DeleteAllItems()
        Query.show_data_perpus(self)


class OpenGui(wx.App):

    def OnInit(self):
        myframe = GuiShow()
        myframe.Show(True)
        return True


def main():

    app = OpenGui()
    app.MainLoop()

if __name__ == "__main__":
    main()
