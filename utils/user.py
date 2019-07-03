#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pybotgram
# Copyright (C) 2019  Mirko Brombin <mriko.pm>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

'''
Get username from user or first_name and last_name if missing
'''
def get_name(u):
    if u.username is not None:
        return u.username
    else:
        first,last = ""
        if u.first_name is not None:
            first = u.first_name
        if u.last_name is not None:
            last = u.last_name
        return first + " " + last
