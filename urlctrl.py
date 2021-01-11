# -*- coding: utf-8 -*-

import re

class urlctrl:
    
    # ドメイン抽出
    def pickDomain(self, url):

        # URLスキーム検出 & スキーム削除パターン
        protoPtn = r'^https?:\/\/([\w][^\/]*)'
        delPtn = r'^https?:\/\/'

        # 引数取得
        self.URL = url

        # URLの先頭からドメイン部分までを取得し配列へ格納
        matched = re.findall(protoPtn, self.URL)
        parsedPredomain = str(matched[0])
        
        # URLのスキーム部分を削除
        parsedDomain = re.sub(delPtn, '', parsedPredomain)

        return parsedDomain