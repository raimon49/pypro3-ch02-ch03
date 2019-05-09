# -*- coding: utf-8 -*-
import json
from datetime import datetime
import argparse

from flask import Flask, render_template, redirect, request, Markup, escape

application = Flask(__name__)

DATA_FILE = 'norilog.json'
NETWORK = '127.0.0.1'
PORT = 8000

def parse_args():
    parser = argparse.ArgumentParser(
        description='A norikae log web application.')
    parser.add_argument('-v', '--version',
                        action='version',
                        version='norilog 1.1.0')
    parser.add_argument('-n', '--network',
                        default=NETWORK)
    parser.add_argument('-p', '--port',
                        type=int,
                        default=PORT)

    return parser.parse_args()


def save_data(start, finish, memo, created_at):
    """記録データを保存します
    :param start: 乗った駅
    :type start: str
    :param finish: 降りた駅
    :type finish: str
    :param memo: 乗り降りのメモ
    :type memo: str
    :param created_at: 乗り降りの日付
    :type created_at: datetime.datetime
    :return: None
    """
    try:
        # json モジュールでデータベースファイルを開きます
        database = json.load(open(DATA_FILE, mode="r", encoding="utf-8"))
    except FileNotFoundError:
        database = []

    database.insert(0, {
        "start": start,
        "finish": finish,
        "memo": memo,
        "created_at": created_at.strftime("%Y-%m-%d %H:%M")
    })

    json.dump(database, open(DATA_FILE, mode="w", encoding="utf-8"), indent=4, ensure_ascii=False)


def load_data():
    """記録データを返します"""
    try:
        # json モジュールでデータベースファイルを開きます
        database = json.load(open(DATA_FILE, mode="r", encoding="utf-8"))
    except FileNotFoundError:
        database = []
    return database


@application.route('/')
def index():
    """トップページ
    テンプレートを使用してページを表示します
    """
    # 記録データを読み込みます
    rides = load_data()
    return render_template('index.html', rides=rides)


@application.route('/save', methods=['POST'])
def save():
    """記録用 URL"""
    # 記録されたデータを取得します
    start = request.form.get('start') # 出発
    finish = request.form.get('finish') # 到着
    memo = request.form.get('memo') # メモ
    created_at = datetime.now() # 記録日時（現在時間）データを保存します
    save_data(start, finish, memo, created_at)
    # 保存後はトップページにリダイレクトします
    return redirect('/')


@application.template_filter('nl2br')
def nl2br_filter(e):
    """改行文字をbr要素に置き換えるテンプレートフィルター"""
    return escape(e).replace('\n', Markup('<br>'))


def main():
    args = parse_args()
    application.run(args.network,
                    args.port,
                    debug=True)


if __name__ == '__main__':
    main()
