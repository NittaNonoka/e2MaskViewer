# e2MaskViewer

Arduinoから読み取ったセンサのデータを可視化するviewer


# DEMO

画像は一例ですが、センサデータをマスクの位置と対応するように、ヒートマップなどで可視化するとわかりやすいかと思います

![viewerイメージ](https://user-images.githubusercontent.com/40416853/94401996-64aa1880-01a6-11eb-88df-a83a020a282a.jpg)


# Features
どうして表情が変化したかの説明の役割

センサのいる要らないの判断ができる


# Requirement

必要な環境

* Python3系
* Arduino IDE

# Installation

### Pythonのライブラリインストール方法

```bash
pip install [ライブラリ]
```

### ArduinoIDEのインストール

以下よりダウンロードしてインストールする

https://www.arduino.cc/en/Main/Software

# Usage

実行方法

自分のPCにクローンして、実行する

Arduinoを繋ぐCOMポートの名称は適宜変えること(viewer.py)
```bash
git clone https://github.com/NittaNonoka/e2MaskViewer.git
python viewer.py
```

# Note
masterブランチにはPushしないこと！
