from googletrans import Translator
from singleton import Singleton
import csv
from datetime import datetime

SRC_URL = "./language_code.csv"

class Tran(Singleton):
    """翻訳クラス"""

    def __init__(self):
        self.trans = Translator()

    def translate_text(self, text, dest='en', src='auto'):
        """引数指定の文章を引数指定の言語に翻訳する"""
        return self.trans.translate(text, dest=dest, src=src).text

    def get_language_master(self):
        """言語マスタをcsvから読みこみ、リストで返却する"""
        with open(SRC_URL, "r", encoding="utf-8_sig") as f:
            reader = csv.reader(f)
            return [{"code": row[0], "name": row[1], "name_en": row[2]} for index, row in enumerate(reader) if index != 0]
