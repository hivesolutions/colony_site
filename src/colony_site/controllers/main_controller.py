#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Website
# Copyright (c) 2008-2012 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony.libs.import_util

AVAILABLE_LOCALES = (
    "en_us",
)
""" The available locales """

# runs the external imports
web_mvc_utils = colony.libs.import_util.__import__("web_mvc_utils")

class MainController:
    """
    The colony site main controller.
    """

    colony_site_main_plugin = None
    """ The colony site main plugin """

    colony_site_main = None
    """ The colony site main """

    def __init__(self, colony_site_main_plugin, colony_site_main):
        """
        Constructor of the class.

        @type colony_site_main_plugin: ColonySiteMainPlugin
        @param colony_site_main_plugin: The colony site main plugin.
        @type colony_site_main: ColonySiteMain
        @param colony_site_main: The colony site main.

        """

        self.colony_site_main_plugin = colony_site_main_plugin
        self.colony_site_main = colony_site_main

    def handle_colony_index(self, rest_request, parameters = {}):
        """
        Handles the given colony index rest request.

        @type rest_request: RestRequest
        @param rest_request: The colony index rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/index.html.tpl",
            locale = locale
        )
        template_file.assign("title", "Colony Framework")
        self.process_set_contents(rest_request, template_file)

    def handle_colony_landing(self, rest_request, parameters = {}):
        """
        Handles the given colony landing rest request.

        @type rest_request: RestRequest
        @param rest_request: The colony landing rest request to be handled.
        @type parameters: Dictionary
        @param parameters: The handler parameters.
        """

        # retrieves the current locale
        locale = self.get_locale(rest_request, AVAILABLE_LOCALES)

        # processes the contents of the template file assigning the
        # appropriate values to it
        template_file = self.retrieve_template_file(
            "general.html.tpl",
            partial_page = "general/landing.html.tpl",
            locale = locale
        )
        template_file.assign("title", "Colony Framework")
        self.process_set_contents(rest_request, template_file)
