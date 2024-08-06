# nicovideo2discord
ニコニコ動画にある動画を閲覧したら、自動的にDiscord Rich Presenceで共有します。
Ubuntu 24.04のChromiumで動作確認をしています。

# 使い方
ブラウザから直接Discordにいろいろするのは難しいので、Python3でHTTPサーバーを建ててそこらへんを代わりにいろいろしてもらう、という構造になっています。

## Requirements
* PC
* ブラウザ
* Python3
* {Git,Python3,シェル}の基礎知識

## 初期設定
1. `git clone`  
    ブランチv1をcloneして、cdしてください。
2. `python3 -m pip install poetry`  
    （インストールされていない場合）poetryをインストールします。
3. `poetry install`  
    poetryで依存ライブラリをインストールします。
4. ブラウザに拡張機能をインストール  
    （Chromium系の場合）`chrome://extensions`を開き、右上の「デベロッパー モード」をONにし、左上の「パッケージ化されていな拡張機能を読み込む」を押し、このリポジトリの`browser_addon`ディレクトリを選択

## 使用
1. Discordを開く
2. `poetry run python3 server.py`  
    リポジトリにcdしてから、サーバーを起動します。
3. (初回のみ) サーバーを起動した際にプロンプトが出てくるので、`1269728794944475166`と入力してEnterしてください。
4. 動画を観る

### License
[MIT License](LICENSE.md)
### Contributer
* [okaits#7534](https://www.okaits7534.net/)
