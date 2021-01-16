# -*- coding: utf-8 -*-

import re
import sys

sys.dont_write_bytecode = True

class urlctrl:

    # スキーム削除パターン
    delPtn = re.compile(r'^https?:\/\/')
    # ドメイン抽出パターン
    protoPtn = re.compile(r'^https?:\/\/([\w][^\/]*)')
    # パス抽出パターン
    pathPtn = re.compile(r'(.*\/[\w\/]+\/)')
    # クエリストリング抽出パターン
    queryPtn = re.compile(r'\?([\w].*)')
    # ポート番号抽出パターン
    portPtn = re.compile(r':([\w]+)')

    # ファイル名抽出パターン
    # filenamePtn = re.compile(r'([\w.#=?&]+)[\r\n]')
    
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

        # 引数取得
        self.URL = url

        # ディレクトリパス配下を取得し配列へ格納
        if(self.pathPtn.search(self.URL)):

            delSchema = self.delPtn.sub('', self.URL)
            matched = self.pathPtn.findall(delSchema)
            result = matched[0]

        else:

            result = '[*]Don\'t path match.'

        return result

    # ファイル名抽出関数
    def pickFilename(self, url):

        # 引数取得
        self.URL = url

        # ファイル名（クエリストリング含む）を取得し配列へ格納
        delSchema = self.delPtn.sub("", self.URL)
        delPath = self.pathPtn.sub("", delSchema)
        result = delPath

        return result


    # クエリストリング抽出関数
    def pickQuerystring(self, url):

        # 出力変数 初期化
        result = ''

        # 引数取得
        self.URL = url

        # クエリストリングのみを取得し配列へ格納
        pickSchema = self.queryPtn.findall(self.URL)
        result =  pickSchema[0]

        return result


    # ポート番号抽出関数
    def pickPortnumber(self, url):

        # 出力変数 初期化
        result = ''

        # 引数取得
        self.URL = url

        # ポート番号を抽出し配列へ格納
        pickSchema = self.portPtn.findall(self.URL)
        result = pickSchema[0]

        return result
        
