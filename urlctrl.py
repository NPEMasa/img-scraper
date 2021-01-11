# -*- coding: utf-8 -*-

import re

class urlctrl:
    
    # ドメイン抽出関数
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

    # パス抽出関数
    def pickPath(self, url):

        # スキーム削除パターン
        delPtn = r'^https?:\/\/'

        # パス抽出パターン
        pathPtn = r'\/([^\r\n].*)'

        # 引数取得
        self.URL = url

        # ディレクトリパス配下を取得し配列へ格納
        if(re.search(pathPtn, self.URL)):

            delSchema = re.sub(delPtn, "", self.URL)
            matched = re.findall(pathPtn, delSchema)
            result = matched[0]

        else:

            result = '[*]Don\'t path match.'

        return result
