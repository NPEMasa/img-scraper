# -*- coding: utf-8 -*-

import requests
import re
import sys

class webcapture():
    url = sys.argv[1]
    def parseUrl(self):
        if re.match(r'^http\:\/\/|^https\:\/\/',self.url):
            print('This is URL format.')
        else:
            print('This is not URL format.')

def main():
    cap = webcapture()
    cap.parseUrl()

if __name__ == "__main__":
    main()