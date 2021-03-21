==============
乗りログアプリ
==============

TestPyPI Server:
https://test.pypi.org/project/raimon49.norilog/

目的
=====

Webブラウザーでコメントを投稿するWebアプリケーションの練習。

ツールのバージョン
====================

:Python:     3.6.4
:pip:        19.x


インストールと起動方法
=======================

リポジトリーからコードを取得し、その下にvenv環境を用意します::

   $ git clone https://github.com/raimon49/pypro3-ch02-ch03
   $ cd norilog
   $ python3 -m venv venv/pypro3
   $ source venv/pypro3/bin/activate
   (pypro3) $ pip install .
   (pypro3) $ norilog -n 127.0.0.1 -p 8000
    * Running on http://127.0.0.1:8000/


開発手順
=========

開発用インストール
------------------

1. チェックアウトする
2. 以下の手順でインストールする::

     (pypro3) $ pip install -e .


依存ライブラリ変更時
---------------------

1. ``setup.py`` の ``install_requires`` を更新する
2. 以下の手順で環境を更新する::

     (pypro3) $ deactivate
     $ python3 -m venv --clear venv
     $ source venv/bin/activate
     (pypro3) $ pip install -e ./norilog
     (pypro3) $ pip freeze > requirements.txt

3. ``setup.py`` と ``requirements.txt`` をリポジトリーにコミットする

