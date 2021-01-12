# -*- coding: utf-8 -*-

import re

class urlctrl:

    # スキーム削除パターン
    delPtn = re.compile(r'^https?:\/\/')
    # ドメイン抽出パターン
    protoPtn = re.compile(r'^https?:\/\/([\w][^\/]*)')
    # パス抽出パターン
    pathPtn = re.compile(r'/([^\r\n].*)')
    # ファイル名抽出パターン
    filenamePtn = re.compile(r'/([\w=#.?]+)\r\n')
    
    # ドメイン抽出関数
    def pickDomain(self, url):

        # 引数取得
        self.URL = url

        # URLの先頭からドメイン部分までを取得し配列へ格納
        matched = self.protoPtn.findall(self.URL)
        parsedPredomain = str(matched[0])
        
        # URLのスキーム部分を削除
        parsedDomain = self.delPtn.sub('', parsedPredomain)

        return parsedDomain

    # パス抽出関数
    def pickPath(self, url):

        # スキーム削除パターン
        delPtn = r'^https?://'

        # パス抽出パターン
        pathPtn = r'/([^\r\n].*)'

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

    # ファイル名抽出関数
    def pickFilename(self, url):

        # スキーム削除パターン
        delPtn = r'^https?:\/\/'

        # ファイル名抽出パターン
        filenamePtn = r'/([\w=#.?]+)\r\n'

        # 引数取得
        self.URL = url

        # ファイル名（クエリストリング含む）を取得し配列へ格納
        if(re.search(filenamePtn, self.URL)):

            delSchema = re.sub(delPtn, "", self.URL)
            matched = re.findall(filenamePtn, delSchema)
            result = matched[0]

        else:

            result = '[*]Don\'t Filename match.'

        return result


