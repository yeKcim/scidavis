#!/usr/bin/python

############################################################################
#                                                                          #
# File                 : python-sipcmd.py                                  #
# Project              : SciDAVis                                          #
# Description          : Auto-detect SIP/PyQt location; dump commandline   #
# Copyright            : (C) 2007-2010 Knut Franke (knut.franke*gmx.de)    #
#                        (replace * with @ in the email address)           #
#                                                                          #
############################################################################
#                                                                          #
#  This program is free software; you can redistribute it and/or modify    #
#  it under the terms of the GNU General Public License as published by    #
#  the Free Software Foundation; either version 2 of the License, or       #
#  (at your option) any later version.                                     #
#                                                                          #
#  This program is distributed in the hope that it will be useful,         #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#  GNU General Public License for more details.                            #
#                                                                          #
#   You should have received a copy of the GNU General Public License      #
#   along with this program; if not, write to the Free Software            #
#   Foundation, Inc., 51 Franklin Street, Fifth Floor,                     #
#   Boston, MA  02110-1301  USA                                            #
#                                                                          #
############################################################################

import sipconfig
config = sipconfig.Configuration()
from PyQt4.QtCore import QT_VERSION_STR


import re
flags = ["-I ../scidavis"]

try:
        from PyQt4.pyqtconfig import Configuration
        sipFlags=Configuration().pyqt_sip_flags
except:
        sipFlags="-x VendorID -t WS_X11 -x PyQt_NoPrintRangeBug -x Py_v3 -g -t Qt_"+re.sub('\.','_',QT_VERSION_STR)
        

if config.sip_version >= 0x040a00:
	# make use of docstring generation feature in SIP >= 4.10
	flags.append("-o")
print " ".join([config.sip_bin, "-I", config.default_sip_dir+"/PyQt4",sipFlags] + flags)
