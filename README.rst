==============
乗りログアプリ
==============

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
   $ python3 -m venv venv
   $ source venv/bin/activate
   (venv) $ pip install .
   (venv) $ norilog -n 127.0.0.1:8000
    * Running on http://127.0.0.1:8000/


開発手順
=========

開発用インストール
------------------

1. チェックアウトする
2. 以下の手順でインストールする::

     (venv) $ pip install -e .
