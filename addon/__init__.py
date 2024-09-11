# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from . import preferences, properties, operators, ui


def register():
    preferences.register()
    properties.register()
    operators.register()
    ui.register()


def unregister():
    preferences.unregister()
    properties.unregister()
    operators.unregister()
    ui.unregister()




# if __DEBUG__:
#     import importlib
#     importlib.reload(preferences)
#     importlib.reload(ui)