# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2015 Therp BV <http://therp.nl>.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Register for free events",
    "version": "8.0.1.0.0",
    "author": "Therp BV,"
              "Serv. Tecnol. Avanzados - Pedro M. Baeza,"
              "Antiun Ingeniería S.L.,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Website",
    "summary": "Avoid shopping chart when registering for free events",
    "depends": [
        'website',
        'website_event',
    ],
    "data": [
        'view/templates.xml',
    ],
    "test": [
    ],
    "auto_install": False,
    'installable': False,
    "application": False,
    "external_dependencies": {
        'python': [],
    },
}
