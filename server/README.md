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
```pipenv```でパッケージを管理する.
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

使用したイメージ: ```mcr.microsoft.com/vscode/devcontainers/python:3.8```

Remote-Containersの使用有無に関係せずに、同じ開発環境の設定を使用できるように、**devcontainer.json**には設定を記載せずに、settings.jsonを記述する.

## デバッグ

### 開発サーバの起動

```shell
$ python manage.py runserver
```

初回のみ、以下のコマンドを実行して、**Pipfile**を作成する。

```shell
$ pipenv install --python 3.8
```

開発時にはコンテナ上で仮想環境を作成し、CIを回すときは、実際に動作させるときには、```--system```オプションをつける.

## Linterの導入

```flake8```と```black```をインストールする.
設定を```.flake8```ファイルに記述する.

以下のコマンドを実行して、インストールする.

```shell
$ pipenv install -d flake8
$ pipenv install -d --pre black # ★--preがないとインストールでエラーが起きる.
```

blackの設定(除外対象など)は```pyproject.toml```に記述する.


```black```でフォーマットしたコードに**E231**の指摘がでるため、除外する.

GitHub Issues #1289 https://github.com/psf/black/issues/1289

## ドキュメント

ドキュメントのスタイルチェックを行う```pydocstyle```と```flake8-docstrings```を使用する.

```shell
$ pipenv install -d pydocstyle
$ pipenv install -d flake8-docstrings
```

テストケース名を記述したとき(関数のドキュメント)に、空行がないと**D202**のエラーがでたため、除外した.


## テストの導入

標準ライブラリ```unittest```を使用する.
テストレポートをJUnit形式で出力させるには、```unittest-xml-reporting```を使用する.

```shell
$ pipenv install -d unittest-xml-reporting
```

**unittest_runner.py**にテストの設定(テスト結果の出力先など)を記述する.

カバレッジの計測は```coverage```を導入する.

```shell
$ pipenv install -d coverage
```

```coverage```の設定は、**.coveragerc**に記述する.

**omit**パラメータにカバレッジ計測対象外のフォルダを指定する.
除外の設定をしないと、**.venv**内のソースコードに対してもカバレッジの計測が行われる.



## コマンドの登録

Pipfileに```[scripts]```を記述することで、コマンドを実行することができる.


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
- [Pipenvでnpm-scriptsみたいにPipfileへコマンドを書く](https://qiita.com/toto1310/items/a8ab8391bc8169721b4f)
- [Configuring Flake8](https://flake8.pycqa.org/en/latest/user/configuration.html)
- [開発を効率的に進めるためのツール設定](https://logmi.jp/tech/articles/322611)
- [black](https://github.com/psf/black)
- [もうPythonの細かい書き方で議論しない。blackで自動フォーマットしよう](https://blog.hirokiky.org/entry/2019/06/03/202745)
- [flake8 error E231 after a successful black run #1289](https://github.com/psf/black/issues/1289)
- [unittest-xml-reporting (aka xmlrunner)](https://github.com/xmlrunner/unittest-xml-reporting)
- [カウボーイには嫌がられるPythonの話](https://qiita.com/mima_ita/items/cabcf014aa08e27c8de7)
- [Configuration reference](https://coverage.readthedocs.io/en/coverage-5.2.1/config.html)
- [Pythonのコード改善のためのツール5つを試してみた](https://minus9d.hatenablog.com/entry/2018/10/22/235604)