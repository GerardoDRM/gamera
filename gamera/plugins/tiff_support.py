#
#
# Copyright (C) 2001-2002 Ichiro Fujinaga, Michael Droettboom,
# and Karl MacMillan
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#

from gamera.plugin import *
import glob

class tiff_info(PluginFunction):
    self_type = None
    args = Args([String("image_file_name")])
    return_type = ImageInfo("tiff_info")
    
tiff_info = tiff_info()

class load_tiff(PluginFunction):
    self_type = None
    args = Args([String("image_file_name"), Int("compression")])
    return_type = ImageType([ONEBIT, GREYSCALE, GREY16, RGB, FLOAT])
    def __call__(self, filename, compression = 0):
        return _tiff_support.load_tiff(filename, compression)
load_tiff = load_tiff()

class TiffSupportModule(PluginModule):
    category = "File"
    cpp_headers = ["tiff_support.hpp"]
    cpp_include_dirs = ["include/libtiff"]
    library_dirs = ["include/libtiff"]
    functions = [tiff_info]
    author = "Michael Droettboom and Karl MacMillan"
    url = "http://gamera.dkc.jhu.edu/"
    extra_libraries = ["tiff", "jpeg", "z"]

module = TiffSupportModule()
