import wx

import ETL
import GUI
import Query

class GuiShow(GUI.GUI_DWH):

    def __init__(self):
        GUI.GUI_DWH.__init__(self,parent=None)
        self.m_buttonSmt.Bind(wx.EVT_BUTTON,self.show_etl)
        self.button_pinjam.Bind(wx.EVT_BUTTON,self.show_by_month)
        self.button_pinjam1.Bind(wx.EVT_BUTTON,self.show_by_year)
        self.button_fact.Bind(wx.EVT_BUTTON,self.show_fact)

    def show_etl(self,event):
        ETL.show_etl(self)

    def show_by_month(self,event):
        self.grid_showResult.ClearGrid()
        Query.show_by_month(self)

    def show_by_year(self, event):
        self.grid_showResult1.ClearGrid()
        Query.show_by_year(self)

    def show_fact(self,event):
        self.m_grid7.ClearGrid()
        Query.show_fact(self)


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
