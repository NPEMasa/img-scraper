# -*- coding: utf-8 -*-

import re
import sys
import pings

sys.dont_write_bytecode = True

class networkClass:

    # ping用関数
    def doPing(self, url):

        self.URL = url

        p = pings.Ping()
        result = p.ping(self.URL)

        if result.is_reached():
            res = result.print_messages()

        else:
            res = "No route to host"

        return res