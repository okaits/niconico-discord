# nicovideo2discord
ニコニコ動画にある動画を閲覧したら、自動的にDiscord Rich Presenceで共有します。  
Ubuntu 24.04のChromiumで動作確認をしています。

# 使い方
ブラウザから直接Discordにいろいろするのは難しいので、Python3でHTTPサーバーを建ててそこらへんを代わりにいろいろしてもらう、という構造になっています。

## Requirements
* PC
* ブラウザ

## 初期設定
1. ソースコードをダウンロード  
   [最新リリース](https://github.com/okaits/nicovideo2discord/releases/latest)から、ソースコードをダウンロードしてください。
2. ブラウザに拡張機能をインストール  
    （Chromium系の場合）`chrome://extensions`を開き、右上の「デベロッパー モード」をONにし、左上の「パッケージ化されていない拡張機能を読み込む」を押し、先ほどダウンロードしたソースコードの`browser_addon`ディレクトリを選択してください。
3. サーバーのダウンロード
   [最新リリース](https://github.com/okaits/nicovideo2discord/releases/latest)から、Windowsなら`windows_amd64_executable_server.exe`を、Linuxなら`linux_amd64_executable_server.elf`をダウンロードしてください。

## 使用
### Windows
1. Discordを開く
2. 初期設定時にダウンロードした`windows_amd64_executable_server.exe`をダブルクリック（実行）してください。
3. 初回のみ「WindowsによってPCが保護されました」というダイアログが表示されるので、詳細情報をクリックすることで右下に現れる実行ボタンを押して実行してください。
4. 動画を観る
### Linux
1. Discordを開く
2. 初期設定時にダウンロードした`linux_amd64_executable_server.elf`に、付与されていない場合は実行権限を付与し、実行する
3. 動画を観る
### 開発者向け
1. Discordを開く
2. `python3 -m poetry run python3 server.py`  
    リポジトリにcdしてから、サーバーを起動します。
3. 動画を観る

### License
[MIT License](LICENSE.md)
### Contributer
* [okaits#7534](https://www.okaits7534.net/)
