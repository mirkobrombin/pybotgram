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
Define a function that requires bot admin permissions.
'''
def is_bot_admin():
	def decorator(fn):
		def wrapper(*args,**kwargs):
			user = args[0].message.from_user
			if user.id in users.bot_admin:
				return fn(*args,**kwargs)
			else:
				return False
		return wrapper
	return decorator

'''
Define a function that requires group admin permissions.
'''
def is_admin():
	def decorator(fn):
		def wrapper(*args,**kwargs):
			bot = args[1].bot
			user = args[0].message.from_user
			chat_id = args[0].message.chat_id
			if bot.get_chat_member(chat_id, user.id).status in ["creator", "administrator"]:
				return fn(*args,**kwargs)
			else:
				return False
		return wrapper
	return decorator