# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Photosorter", pos = wx.DefaultPosition, size = wx.Size( 474,275 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( -1,-1 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Source Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_SourceDir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer2.Add( self.m_SourceDir, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Target Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_TargetDir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer3.Add( self.m_TargetDir, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		self.m_chkMoveFiles = wx.CheckBox( self, wx.ID_ANY, u"Move files", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_chkMoveFiles, 0, wx.ALL, 5 )
		
		self.m_chkDeleteDuplicates = wx.CheckBox( self, wx.ID_ANY, u"Delete duplicates", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_chkDeleteDuplicates, 0, wx.ALL, 5 )
		
		self.m_chkDeleteEmptyDir = wx.CheckBox( self, wx.ID_ANY, u"Delete empty source folder(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_chkDeleteEmptyDir, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( sbSizer1, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_BtnSort = wx.Button( self, wx.ID_ANY, u"Sort", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_BtnSort.SetDefault() 
		bSizer4.Add( self.m_BtnSort, 0, wx.ALL, 5 )
		
		self.m_btnQuit = wx.Button( self, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_btnQuit, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_BtnSort.Bind( wx.EVT_BUTTON, self.CmdSort )
		self.m_btnQuit.Bind( wx.EVT_BUTTON, self.CmdQuit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def CmdSort( self, event ):
		event.Skip()
	
	def CmdQuit( self, event ):
		event.Skip()
	

