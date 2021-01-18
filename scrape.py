# -*- coding: utf-8 -*-

import requests
import re
import sys
import urlctrl
import network

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

    pin = network.networkClass()


    # urlctrlクラス読み込み
    uct = urlctrl.urlctrl()

    # domain match
    domResult = uct.pickDomain(url)

    # path match
    pathResult = uct.pickPath(url)

    # filename match
    filenameResult = uct.pickFilename(url)

    # querystring match
    #-- querystringResult = uct.pickQuerystring(url)

    # portnumber match
    #-- portnumberResult = uct.pickPortnumber(url)


    print("Domain   : %s" % domResult)
    print("Path     : %s" % pathResult)
    print("Filename : %s" % filenameResult)
    #-- print("Port     : %s" % portnumberResult)
    #-- print("Query    : %s" % querystringResult)

    pinres = pin.doPing(domResult)
    print("- - - - - - - - - - ")
    print(pinres)

if __name__ == "__main__":
    main()