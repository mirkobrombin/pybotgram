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

from configs import users

'''
Binds a function to private chats only
'''
def only_private(fn):
	def wrapper(*args,**kwargs):
		message = args[0].message
		if message.chat.type == 'private':
			return fn(*args,**kwargs)
		else:
			return False
	return wrapper

'''
Binds a function to groups only
'''
def only_groups(fn):
	def wrapper(*args,**kwargs):
		message = args[0].message
		if message.chat.type != 'private':
			return fn(*args,**kwargs)
		else:
			return False
	return wrapper