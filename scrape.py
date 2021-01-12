# -*- coding: utf-8 -*-

import requests
import re
import sys
import urlctrl

sys.dont_write_bytecode = True
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

    # domain match
    domResult = uct.pickDomain(url)

    # path match
    pathResult = uct.pickPath(url)

    # filename match
    filenameResult = uct.pickFilename(url)

    print("Domain   : %s" % domResult)
    print("Path     : %s" % pathResult)
    print("Filename : %s" % filenameResult)

if __name__ == "__main__":
    main()