# Django サンプル

## セットアップ

以下の URL を参考に、Django のインストールする。

[クイックインストールガイド](https://docs.djangoproject.com/ja/3.0/intro/install/#verifying)

※pipenv をインストールする前のコマンド

```shell
$ python -m pip install Django
```

Django プロジェクトを作成する。
アプリケーション名は`app`にした。

```shell
$ cd server
$ django-admin startproject config .
$ python manage.py startapp app
```

template フォルダの作成

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

`pipenv`でパッケージを管理する.
インストール処理は Dockerfile に記述する.

pipenv をインストールする.

```shell
$ pip install pipenv==2020.6.2
```

プロジェクトの直下に仮想環境を作るため、以下の環境変数も設定する.

```shell
ENV PIPENV_VENV_IN_PROJECT=1
```

## 開発環境

Remote-Containers を使用する.

使用したイメージ: `mcr.microsoft.com/vscode/devcontainers/python:3.8`

Remote-Containers の使用有無に関係せずに、同じ開発環境の設定を使用できるように、**devcontainer.json**には設定を記載せずに、settings.json を記述する.

### PostgreSQL コンテナを使用する場合

複数のコンテナ(Web アプリ用と DB コンテナ用)を使用するため、コンテナの定義を**docker-compose.yml**に記述する.

**devcontainer.json**は、直接 Dockerfile を読み込まずに、**docker-compose.yml**を読み込むように設定を変更する.

**Dockerfile**を読み込む処理を無効化.

```json
    "build": {
        "dockerfile": "Dockerfile",
        "context": "..",
        "args": {
     	    "VARIANT": "3.8"
     	}
    }
```

ポートフォワーディングも**docker-compose.yml**に記述しているので、以下のコードを削除する.

```json
    "forwardPorts": [
	    8000
    ],
```

**docker-compose.yml**を読み込む.

```json
    "service": "app", // 接続するコンテナのラベル
    "dockerComposeFile": "docker-compose.yml", // 読み込むdocker-compose.ymlファイルのパス
```

## デバッグ

### 開発サーバの起動

```shell
$ python manage.py runserver
```

初回のみ、以下のコマンドを実行して、**Pipfile**を作成する。

```shell
$ pipenv install --python 3.8
```

開発時にはコンテナ上で仮想環境を作成し、CI を回すときは、実際に動作させるときには、`--system`オプションをつける.

## Linter の導入

`flake8`と`black`をインストールする.
設定を`.flake8`ファイルに記述する.

以下のコマンドを実行して、インストールする.

```shell
$ pipenv install -d flake8
$ pipenv install -d --pre black # ★--preがないとインストールでエラーが起きる.
```

black の設定(除外対象など)は`pyproject.toml`に記述する.

`black`でフォーマットしたコードに**E231**の指摘がでるため、除外する.

GitHub Issues #1289 https://github.com/psf/black/issues/1289

## ドキュメント

ドキュメントのスタイルチェックを行う`pydocstyle`と`flake8-docstrings`を使用する.

```shell
$ pipenv install -d pydocstyle
$ pipenv install -d flake8-docstrings
```

テストケース名を記述したとき(関数のドキュメント)に、空行がないと**D202**のエラーがでたため、除外した.

## テストの導入

標準ライブラリ`unittest`を使用する.
テストレポートを JUnit 形式で出力させるには、`unittest-xml-reporting`を使用する.

```shell
$ pipenv install -d unittest-xml-reporting
```

**unittest_runner.py**にテストの設定(テスト結果の出力先など)を記述する.

カバレッジの計測は`coverage`を導入する.

```shell
$ pipenv install -d coverage
```

`coverage`の設定は、**.coveragerc**に記述する.

**omit**パラメータにカバレッジ計測対象外のフォルダを指定する.
除外の設定をしないと、**.venv**内のソースコードに対してもカバレッジの計測が行われる.

## コマンドの登録

Pipfile に`[scripts]`を記述することで、コマンドを実行することができる.

## DB 処理

DB のテーブル定義は以下のドキュメントを参考に作成する.

[モデル](https://docs.djangoproject.com/ja/3.1/topics/db/models/)

### PostgreSQL 用の設定

デフォルトでは、**SQLite3**を使用することになっているため、PostgreSQL を使用するように変更する.

以下のドキュメントをもとに、セットアップする.

[PostgreSQL notes](https://docs.djangoproject.com/ja/3.1/ref/databases/#postgresql-notes)

`psycopg2`を使用する.

## gitignore の追加

django と python と Visual Studio Code

https://www.toptal.com/developers/gitignore/api/visualstudiocode,python,django

## 参考 URL

- [【開発効率 UP】アプリ開発でおすすめのディレクトリ構造の工夫の仕方](https://code-ship-blog.wemotion.co.jp/technology/【開発効率up】アプリ開発でおすすめのディレクト)
- [2020 年の Python パッケージ管理ベストプラクティス](https://qiita.com/sk217/items/43c994640f4843a18dbe)
- [Python のパッケージ周りのベストプラクティスを理解する](https://www.m3tech.blog/entry/python-packaging)
- [きたない requirements.txt から Pipenv への移行](https://www.kabuku.co.jp/developers/python-pipenv-graph)
- [pipenv と Git と Docker を使った Python 開発フロー](https://qiita.com/Aruneko/items/796d7eeb61e1f36ae4a0)
- [あえて docker に pipenv 環境を作る](https://qiita.com/nassy20/items/3724aeda49238f965fb1)
- [Pipenv で npm-scripts みたいに Pipfile へコマンドを書く](https://qiita.com/toto1310/items/a8ab8391bc8169721b4f)
- [Configuring Flake8](https://flake8.pycqa.org/en/latest/user/configuration.html)
- [開発を効率的に進めるためのツール設定](https://logmi.jp/tech/articles/322611)
- [black](https://github.com/psf/black)
- [もう Python の細かい書き方で議論しない。black で自動フォーマットしよう](https://blog.hirokiky.org/entry/2019/06/03/202745)
- [flake8 error E231 after a successful black run #1289](https://github.com/psf/black/issues/1289)
- [unittest-xml-reporting (aka xmlrunner)](https://github.com/xmlrunner/unittest-xml-reporting)
- [カウボーイには嫌がられる Python の話](https://qiita.com/mima_ita/items/cabcf014aa08e27c8de7)
- [Configuration reference](https://coverage.readthedocs.io/en/coverage-5.2.1/config.html)
- [Python のコード改善のためのツール 5 つを試してみた](https://minus9d.hatenablog.com/entry/2018/10/22/235604)
