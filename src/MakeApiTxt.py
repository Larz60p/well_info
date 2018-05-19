import wx
import wx.aui as aui
import wx.lib.agw.aui as aui
import WellPaths


class MakeApiTxt(wx.Frame):
    """
    Author: Larz60+

    Initialize - inherits from wx.Frame. Instantiates all widgets and variables for application

    """
    def __init__(self):
        self.main_width = 1200
        self.main_height = 675
        app = wx.App()
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title='API comand Manager', pos=wx.DefaultPosition,
                          size=(self.main_width, self.main_height), style=wx.DEFAULT_FRAME_STYLE, name='MakeAPI')
        app.SetTopWindow(self)
        self._mgr = aui.AuiManager(self)

        menuBar = wx.MenuBar()
        file_menu = wx.Menu()
        file_menu.Append(101, 'Open', 'Open a file')
        file_menu.Append(102, 'Save', 'Save to file')
        file_menu.Append(103, 'Save As', 'Save file as')
        file_menu.Append(104, 'Delete', 'Delete file')
        file_menu.Append(105, 'Rename', 'Rename file')
        menuBar.Append(file_menu, "&File")

        tool_menu = wx.Menu()
        tool_menu.Append(201, 'Sort', 'sort entries in API window')
        menuBar.Append(tool_menu, '&Tools')

        self.SetMenuBar(menuBar)

        left_panel_width = self.main_width * .3  # This is 30% of main width
        left_panel_height = self.main_height  # This is 75% of main height
        left_panel_sz = left_panel_width, left_panel_height  # combined for widget size

        right_panel_width = self.main_width - left_panel_width  # which is 70% of main width
        right_panel_height = left_panel_height  # Keep same height as left panel
        right_panel_sz = right_panel_width, right_panel_height

        self.left_panel = wx.Panel(self, id=wx.ID_ANY, size=left_panel_sz)
        self.right_panel = wx.Panel(self, id=wx.ID_ANY, size=right_panel_sz)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        self.api_editor = wx.TextCtrl(self.left_panel,
                                      id=wx.ID_ANY,
                                      size=(left_panel_width, left_panel_height),
                                      style=wx.TE_MULTILINE)

        vsizer.Add(self.api_editor, 0, 0, 0)

        # hsizer = wx.BoxSizer(wx.HORIZONTAL)

        self._mgr.AddPane(self.left_panel, aui.AuiPaneInfo().Left().Caption("Api Fetch List"))
        self._mgr.AddPane(self.right_panel, aui.AuiPaneInfo().Center().Caption("File Manager"))

        self._mgr.Update()
        self.Show()

        app.MainLoop()

    def api_display_load(self):
        pass

if __name__ == '__main__':
    tm = MakeApiTxt()
