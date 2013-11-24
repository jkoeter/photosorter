"""Subclass of MainFrame, which is generated by wxFormBuilder."""

import re
import os
import wx
import time
import hashlib
import photosorter
import datetime
import time
import shutil
import calendar

import hachoir_core.config as hachoir_config
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_metadata import extractMetadata


def CreateChecksum(a_File, blocksize=65536) :
    hasher = hashlib.md5()
    _fileHandle = open(a_File, 'rb')
    buf = _fileHandle.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = _fileHandle.read(blocksize)
    return hasher.digest()

def get_creation_date(_path):
    # Initialise result
    _creation_date = None

    # Using the hachoir metadata library retrieve file metadata
    hachoir_config.quiet = True
    try:
        parser = createParser(unicode(_path), _path)
        if parser:
            metadata = extractMetadata(parser)
            if metadata:
                _creation_date = metadata.get("creation_date")
    except Exception:
        pass

    # Validate and use ctime if not available
    if not _creation_date:
        _ctime = os.path.getctime(_path)
        _creation_date = datetime.datetime.fromtimestamp(_ctime)

    # Return result
    return _creation_date

# Implementing MainFrame
class PhotosorterMainFrame( photosorter.MainFrame ):
	def __init__( self, parent ):
		photosorter.MainFrame.__init__( self, parent )
		self.parent = parent
	
	# Handlers for MainFrame events.
	def CmdSort( self, event ):
		# Show a progress dialog because this can take long...
		dlg = wx.ProgressDialog("Progressing...", "Looking for photo files", style = wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME)
		dlg.Show()

		# scan for all files
		_files = []
 
		for root, dirs, files in os.walk(self.m_SourceDir.GetPath()) :
			dlg.Pulse()
			for name in files:
				if re.match(".+\.jpg", name, flags=re.IGNORECASE) :
					_files.append(os.path.join(root, name))
		dlg.Destroy()
		
		# create a hash of all files
		dlg = wx.ProgressDialog("Progressing...", "Creating hashes for photo files", maximum = len(_files), style = wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
		dlg.Show()

		_fileHash = {}
		_fileCount = 0
		for _file in _files :
			dlg.Update(value = _fileCount, newmsg = _file)
			_chksum = CreateChecksum(_file)
			if _chksum in _fileHash :
				_fileHash[_chksum].append(_file)
			else :
				_fileHash[_chksum] = [_file]
			_fileCount = _fileCount + 1
		
		dlg.Destroy()
	
		# Copying / moving files
		dlg = wx.ProgressDialog("Progressing...", "Copying / moving files", maximum = len(_fileHash), style = wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
		dlg.Show()

		_fileCount = 0
		_duplicates = 0
		for _key in _fileHash :
			# make sure the files with the same filehash are true duplicates
			_datesProcessed = [] 
			for _fileToProcess in _fileHash[_key] :
				_newDate = get_creation_date(_fileToProcess)
				if _newDate not in _datesProcessed :
					_datesProcessed.append(_newDate)
					_year = str(_newDate.year)
					_yearDir = os.path.join(self.m_TargetDir.GetPath(), _year)
					if not os.path.isdir(_yearDir) :
						os.mkdir(_yearDir)
					_newName = "%s-%02d-%02d%02d%02d.jpg"%(calendar.month_abbr[_newDate.month], _newDate.day, _newDate.hour, _newDate.minute, _newDate.second)
					dlg.Update(value = _fileCount, newmsg = _newName)
					if self.m_chkMoveFiles :
						shutil.move(_fileToProcess, os.path.join(_yearDir, _newName))
					else :
						shutil.copy2(_fileToProcess, os.path.join(_yearDir, _newName))
					_fileCount = _fileCount + 1
				else :
					if self.m_chkDeleteDuplicates :
						os.remove(_fileToProcess)
					_duplicates = _duplicates + 1
		
		dlg.Destroy()
		
		wx.MessageBox("Files: %d\nDuplicates: %d" % (len(_files), _duplicates), 'Info', wx.OK | wx.ICON_INFORMATION)
	
	def CmdQuit( self, event ):
		# close the main window to terminate the application
		self.Close()
	
	
