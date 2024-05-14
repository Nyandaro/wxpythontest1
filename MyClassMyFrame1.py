"""Subclass of MyFrame1, which is generated by wxFormBuilder."""

import wx
import test1
import a1
import a2


# Implementing MyFrame1
class MyClassMyFrame1(test1.MyFrame1):
    def __init__(self, parent):
        test1.MyFrame1.__init__(self, parent)

        # イベント処理時、どのメソッドを呼び出すかを登録する
        self.m_button1.Bind(wx.EVT_BUTTON, self.OnButtonPress)

    # イベント処理を記載
    def OnButtonPress(self, event):
        zzz = a2.streamcheck()
        self.m_textCtrl1.SetLabel(zzz)
