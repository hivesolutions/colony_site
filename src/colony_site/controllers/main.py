#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Website
# Copyright (c) 2008-2014 Hive Solutions Lda.
#
# This file is part of Hive Colony Website.
#
# Hive Colony Website is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Colony Website is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Colony Website. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2014 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony

import base

mvc_utils = colony.__import__("mvc_utils")
controllers = colony.__import__("controllers")

class MainController(base.BaseController):

    def index(self, request):
        self._template(
            request = request,
            partial_page = "general/index.html.tpl",
            title = "Colony Framework"
        )

    def landing(self, request):
        self._template(
            request = request,
            partial_page = "general/landing.html.tpl",
            title = "Colony Framework"
        )
