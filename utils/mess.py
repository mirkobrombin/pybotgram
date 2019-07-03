
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
Check if message is equal to text
'''
def equal(message, text):
    if message.lower() == text.lower():
        return True
    else:
        return False

'''
Check if message starts with text
'''
def start(message, text):
    if str(message.lower()).startswith(text.lower()):
        return True
    else:
        return False

'''
Check if message contains text
'''
def contains(message, text):
    if text.lower() in message.lower():
        return True
    else:
        return False

'''
Get text after command
'''
def get_cmd_text(cmd, update):
    return update.message.text[(len(cmd)+1):]

'''
Delete message
'''
def delete(bot, update):
    bot.delete_message(update.message.chat_id, update.message.message_id)
