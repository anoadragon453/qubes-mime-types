#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2017 Andrew Morgan <andrew@amorgan.xyz>
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#

import unittest
import imp
import xattr
import sys
import io

qvm_file_trust = imp.load_source('qvm-file-trust', '../qvm-file-trust')

#class TC_00_trust(unittest.TestCase):
#    def test_000_retri(self):
#        self.assertEqual(fun(3), 4)

class TC_10_misc(unittest.TestCase):
    def test_000_quiet(self):
        """Make sure we're not printing when we shouldn't be."""
        qvm_file_trust.OUTPUT_QUIET = True
        captured_obj = io.StringIO()
        sys.stdout = captured_obj
        qvm_file_trust.qprint('Test string!')
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_obj.getvalue(), '')

        qvm_file_trust.OUTPUT_QUIET = False
        captured_obj = io.StringIO()
        sys.stdout = captured_obj
        qvm_file_trust.qprint('Test string!')
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_obj.getvalue(), 'Test string!\n')

    def test_010_error(self):
        """Ensure errors are reported properly."""
        qvm_file_trust.OUTPUT_QUIET = False
        captured_obj = io.StringIO()
        sys.stdout = captured_obj
        qvm_file_trust.error('Test string!')
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_obj.getvalue(), 'Error: Test string!\n')

        qvm_file_trust.OUTPUT_QUIET = True
        captured_obj = io.StringIO()
        sys.stdout = captured_obj
        qvm_file_trust.error('Test string!')
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_obj.getvalue(), '')


def list_tests():
    return (
            TC_10_misc
    )

if __name__ == '__main__':
    unittest.main()
