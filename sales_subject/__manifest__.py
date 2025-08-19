# -*- coding: utf-8 -*-
################################################################################
#
#    Quotation Subject Viewer
#tes
#    Copyright (C) 2025 Alireza (AR)
#    Author: Alireza (alir.riazi@gmail.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
{
 'name': "Quotation Subject Viewer",
    'version': '16.0.0.1',
    'summary': "Adds a visible subject/title field to the quotation list view for quick scanning",
    'description': """
        Quotation Subject Viewer enhances Odoo's quotation list view by adding a visible subject/title field.
        Users can quickly identify the purpose of each quotation without opening it.
        This module is lightweight, easy to install, and fully integrated with Odoo's sales workflow.
""",
    'category': 'Sales',
    'author': "Alireza (AR)",
    'maintainer': "Alireza",
    'support': "alir.riazi@gmail.com",
    'license': 'LGPL-3',
    'depends': ['sale'],
    'data' : [
        'views/sales_order_view.xml',
    ],
    #'images': [
    #    'static/description/screenshot1.png',
    #    'static/description/screenshot2.png',
    #],
    'images': ['static/description/banner.png'],
    'assets': {
    'web.assets_backend': [
        'static/description/index.html',
       ],
     },
    'installable': True,
    'application': False,
    'auto_install': False,

}


