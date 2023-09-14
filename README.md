# Open Interpreter Devcontainer
Open InterpreterのDevcontainerでの実行環境です。

## Setup
### Clone or Download
適当な場所にCloneするかZipでダウンロード＆解答してください。

### .envファイルへAPIキー等を記入
`.env` ファイルを開き、必要な情報を記入します。


## Dev Containersで開く
### VScodeにDev Containersをインストール
VScodeを立ち上げ、拡張機能から  `Dev Containers` をインストールします。
※Dockerをインストールしていない場合には、事前にインストールしてください。

### フォルダを開く＆コンテナ立ち上げ
CloneしたこのリポジトリをVScodeで開きます。
右下のポップアップの「コンテナーで再度開く」をクリックするか、画面左下のDev Containersのアイコンをクリックして「コンテナーで再度開く」をクリックします。
VScodeの左下の表示が変わり、コンテナが立ち上がったことが確認できます。

## ライブラリのインストール
### 利用したいAPIのディレクトリに移動
GPT-4, GPT-3.5, AzureのAPIごとにディレクトリを分けています。
ターミナルを起動し、利用したいAPIのディレクトリに移動してください。

### ライブラリのインストール
ターミナルで移動したら、 `poetry install` コマンドを実行し、ライブラリをインストールします。

## Open Interpreterの起動
上記のディレクトリ内で、 `poetry run python open_interpreter.py` コマンドを実行します。
ターミナルでOpen Interpreterが起動し、対話モードが開始されます。
※上記コマンドで自動的に仮想環境が立ち上がります。

## Open Interpreterの終了
Open Interpreterを終了するには、 `CTRL + C` で終了できます。
※仮想環境は自動で終了します。

## Dev Containersの終了
VScodeの左下のDev Containersのアイコンをクリックし、 `リモート接続を終了する` を選択すると、コンテナが終了します。

## 備考
- 利用するAPIごとに環境を分けていますが、 `open_interpreter.py` の内容が異なるだけで、インストールしているパッケージは同様です。
- 別の仮想環境を用意したい場合には、 別フォルダを用意し（好きな名前でOK）、`.venv` 以外のファイルをコピペ（利用するAPIのもの）し、上記の `ライブラリのインストール` を実行すればOKです。