# Djangoサンプル

## セットアップ

以下のURLを参考に、Djangoのインストールする。

[クイックインストールガイド](https://docs.djangoproject.com/ja/3.0/intro/install/#verifying)

※pipenvをインストールする前のコマンド

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

## パッケージ管理
pipenvでパッケージを管理する.
インストール処理はDockerfileに記述する.

pipenvをインストールする.

```shell
$ pip install pipenv==2020.6.2
```

プロジェクトの直下に仮想環境を作るため、以下の環境変数も設定する.

```shell
ENV PIPENV_VENV_IN_PROJECT=1
```


## 開発環境
Remote-Containersを使用する.

使用したイメージ: mcr.microsoft.com/vscode/devcontainers/python:3.8

## デバッグ

### 開発サーバの起動

```shell
$ python manage.py runserver
```

初回のみ、以下のコマンドを実行して、Pipfileを作成する。

```
pipenv install --python 3.8
```

デバッグ時にはコンテナ上で仮想環境を作成し、実際に動作させるときには、```--system```オプションをつける.



## gitignoreの追加
djangoとpythonとVisual Studio Code

https://www.toptal.com/developers/gitignore/api/visualstudiocode,python,django

## 参考URL

- [【開発効率UP】アプリ開発でおすすめのディレクトリ構造の工夫の仕方](https://code-ship-blog.wemotion.co.jp/technology/【開発効率up】アプリ開発でおすすめのディレクト)
- [2020 年の Python パッケージ管理ベストプラクティス](https://qiita.com/sk217/items/43c994640f4843a18dbe)
- [Pythonのパッケージ周りのベストプラクティスを理解する](https://www.m3tech.blog/entry/python-packaging)
- [きたない requirements.txt から Pipenv への移行](https://www.kabuku.co.jp/developers/python-pipenv-graph)
- [pipenvとGitとDockerを使ったPython開発フロー](https://qiita.com/Aruneko/items/796d7eeb61e1f36ae4a0)
- [あえてdockerにpipenv環境を作る](https://qiita.com/nassy20/items/3724aeda49238f965fb1)