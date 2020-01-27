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
References:
<https://core.telegram.org/bots/api>
<https://python-telegram-bot.readthedocs.io/en/stable/>
'''
from utils import user
from utils.decorators import chat

@chat.only_private
def init(update, context):
    update.message.reply_text(
        "Hi {username}, you can see the source here: https://github.com/mirkobrombin/pybotgram".format
        (
            username = user.get_name(update.message.from_user)
        )
    )
