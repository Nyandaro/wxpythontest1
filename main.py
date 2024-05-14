
import wx
from MyClassMyFrame1 import MyClassMyFrame1

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyClassMyFrame1(None)
    frame.Show(True)
    app.MainLoop()