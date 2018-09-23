# -*- coding: utf-8 -*-

"""
builderSuite
Build code for different release targets
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?py;builder_suite

This Source Code Form is subject to the terms of the Mozilla Public License,
v. 2.0. If a copy of the MPL was not distributed with this file, You can
obtain one at http://mozilla.org/MPL/2.0/.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;mpl2
----------------------------------------------------------------------------
#echo(builderSuiteVersion)#
#echo(__FILEPATH__)#
"""

from distutils.command.sdist import sdist as _sdist
from os import path
import os

from dNG.distutils.py_builder import PyBuilder
from .build_mixin import BuildMixin

class Sdist(_sdist, BuildMixin):
    """
python.org: Create a source distribution (tarball, zip file, etc.)

:author:    direct Netware Group
:copyright: direct Netware Group - All rights reserved
:package:   builderSuite
:since:     v1.0.0
:license:   https://www.direct-netware.de/redirect?licenses;mpl2
            Mozilla Public License, v. 2.0
    """

    def copy_file(self, infile, outfile, **kwargs):
        """
python.org: Copy a file respecting verbose, dry-run and force flags.

:return: (tuple) Tuple (dest_name, copied)
:since:  v1.0.0
        """

        src_path = "src" + path.sep

        if (infile[:4] == src_path): infile = path.join(Sdist._build_target_path, infile)

        return _sdist.copy_file(self, infile, outfile, **kwargs)
    #

    def make_release_tree(self, base_dir, files):
        """
python.org: Create the directory tree that will become the source
distribution archive.
        """

        target_path_length = len(Sdist._build_target_path)
        target_src_path = path.join(Sdist._build_target_path, "src") + path.sep

        target_relative_src_path = path.join(".", target_src_path)

        target_src_path_length = len(target_src_path)
        target_relative_src_path_length = len(target_relative_src_path)

        files_filtered = [ ]

        for _file in files:
            if (_file[:target_src_path_length] == target_src_path): _file = _file[target_path_length + 1:]
            elif (_file[:target_relative_src_path_length] == target_relative_src_path):
                _file = _file[target_path_length + 3:]
            #

            files_filtered.append(_file)
        #

        _sdist.make_release_tree(self, base_dir, files_filtered)
    #
#
