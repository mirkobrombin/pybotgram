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

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import admin, user, configs, dialogs, utils

def main():
    updater = Updater(configs.telegram.bot_token, use_context=True)
    dp = updater.dispatcher

    # Admin
    dp.add_handler(CommandHandler("say", admin.say.init))

    # User
    dp.add_handler(CommandHandler("start", user.start.init))
    
    # Initialize Handlers
    dp.add_handler(MessageHandler(None, dialogs.handler.init))
    dp.add_error_handler(utils.logging.error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
