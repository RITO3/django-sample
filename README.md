# Djangoサンプル

## セットアップ

以下のURLを参考に、Djangoのインストールする。

[クイックインストールガイド](https://docs.djangoproject.com/ja/3.0/intro/install/#verifying)


```shell
$ python -m pip install Django
```

Djangoプロジェクトを作成する。
アプリケーション名は```app```にした。

```shell
$ cd server
$ django-admin startproject config .
$ python manage.py startapp app
```

templateフォルダの作成

## フォルダ構成

```shell
.
└── server
    ├── app
    │   ├── migrations
    │   └── template
    └── config
```

## 開発環境
Remote-Containersを使用する.

使用したイメージ: mcr.microsoft.com/vscode/devcontainers/python:3.8

## デバッグ

### 開発サーバの起動

```shell
$ python manage.py runserver
```

## gitignoreの追加
djangoとpythonとVisual Studio Code

https://www.toptal.com/developers/gitignore/api/visualstudiocode,python,django

## 参考URL

- [【開発効率UP】アプリ開発でおすすめのディレクトリ構造の工夫の仕方](https://code-ship-blog.wemotion.co.jp/technology/【開発効率up】アプリ開発でおすすめのディレクト)