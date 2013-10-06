import wx
import photosorterMainFrame

if __name__ == '__main__':
  app = wx.PySimpleApp()
  frame = photosorterMainFrame.PhotosorterMainFrame(parent=None)
  frame.Show()
  app.MainLoop()

