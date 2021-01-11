# -*- coding: utf-8 -*-

import requests
import re
import sys
import urlctrl

url = sys.argv[1]

class webcapture():
    def parseUrl(self):
        if re.match(r'^https?\:\/\/',url):
            print('This is URL format.')
        else:
            print('This is not URL format.')

def main():
    cap = webcapture()
    cap.parseUrl()

    # urlctrlクラス読み込み
    uct = urlctrl.urlctrl()
    result = uct.pickDomain(url)
    print("Domain : %s" % result)

if __name__ == "__main__":
    main()