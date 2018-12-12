import wx

import ETL
import GUI
import Show_data

class GuiShow(GUI.GUI_DWH):

    def __init__(self):
        GUI.GUI_DWH.__init__(self,parent=None)

        # Show data
        self.m_buttonSmt.Bind(wx.EVT_BUTTON,self.show_etl)
        self.m_button_peminjaman.Bind(wx.EVT_BUTTON,self.show_by_month)
        self.m_button_tahunan.Bind(wx.EVT_BUTTON,self.show_by_year)
        self.m_button_fact.Bind(wx.EVT_BUTTON,self.show_fact)
        self.m_button_perpus.Bind(wx.EVT_BUTTON,self.show_by_perpus)
        self.m_button_member.Bind(wx.EVT_BUTTON,self.show_by_member)

        #Save data
        self.m_button_save_member.Bind((wx.EVT_BUTTON),self.save_member)
        self.m_button_save_month.Bind((wx.EVT_BUTTON),self.save_month)
        self.m_button_save_year.Bind((wx.EVT_BUTTON),self.save_year)
        self.m_button_save_fact.Bind(wx.EVT_BUTTON,self.save_fact)

    # --------Show data-------- #
    def show_etl(self,event):
        ETL.show_etl(self)
        wx.MessageBox('Database sudah Paling Baru', 'Sukses', wx.OK)

    def show_by_month(self,event):
        self.m_dataViewList_peminjaman.DeleteAllItems()
        Show_data.show_by_month(self)

    def show_by_year(self, event):
        self.m_dataViewList_tahun.DeleteAllItems()
        Show_data.show_by_year(self)

    def show_by_perpus(self, event):
        self.m_dataViewList_perpus.DeleteAllItems()
        Show_data.show_data_perpus(self)

    def show_by_member(self,event):
        self.m_dataViewList_member.DeleteAllItems()
        Show_data.show_member(self)

    def show_fact(self,event):
        self.m_dataView_fact.DeleteAllItems()
        Show_data.show_fact(self)

    # --------Save data-------- #
    def save_member(self, event):
        Show_data.save_member(self)
        wx.MessageBox('Data member tersimpan', 'Sukses', wx.OK)

    def save_month(self,event):
        Show_data.save_month(self)
        wx.MessageBox('Data perbulan tersimpan', 'Sukses', wx.OK)

    def save_year(self,event):
        Show_data.save_year(self)
        wx.MessageBox('Data pertahun tersimpan', 'Sukses', wx.OK)

    def save_fact(self, event):
        Show_data.save_fact()
        wx.MessageBox('Data pertahun tersimpan', 'Sukses', wx.OK)
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
