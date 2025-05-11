## READMEは現在作成中  

重要なことは、N1MMlogger+でExportされるADIFファイルをpyファイル、exeファイルと同じフォルダに保存して、ツールを起動することです。
  
# N1MM2JARL_contestlogツール

---

## index

- [N1MM2JARL\_contestlogツール](#n1mm2jarl_contestlogツール)
  - [index](#index)
  - [Overview](#overview)
  - [Description](#description)
  - [Features](#features)
  - [Demo](#demo)
  - [Requirement](#requirement)
  - [Usage](#usage)
  - [Install](#install)
  - [Note](#note)
  - [Contribution](#contribution)
  - [Licence](#licence)
  - [Author](#author)

## Overview

N1MM2JARL_contestlogツールは、N1MM Logger+が生成するADIFファイルをJARLコンテストログver.2.1のコンテストログを作成するツールです。  
また、このツールは、提出用コンテストログ作成機能のほか、TurboHamlog用のCSVファイルを作成する機能などを有します。  
  
!["図1"](/image/1.jpg)

!["図2"](/image/2.jpg)

!["図3"](/image/3.jpg)

## Description

N1MM2JARL_contestlogツールは、N1MM Logger+が生成するADIFファイルをJARLコンテストログver.2.1のコンテストログを作成するツールです。  
従来、N1MM Loger+で国内コンテストに参加する方は、コンテスト終了後に、コンテストログを提出するため、CtestwinなどのコンテストロガーにN1MM Logger+が生成するADIFファイルを読み込ませ、提出ログを作成したていたものと思います。このツールは、pyファイルやexeファイルと同じフォルダに、N1MM Looger+のADIFファイル callsign.adiを保存し、アプリを操作すれば、簡単にJARLコンテストログ形式の提出ログを作成します。  
このツールは、日本でよく使われていTurboHamlogにログ情報を読み込ませるためのCSVファイルも作成します。  
このツールは、以下のものを作成する機能を有します。  
callsign.txt  : 提出用コンテストログファイル  
callsign.csv  : Turbo Hamlog用のCSVファイル  
callsign_score.txt : コンテストの集計結果、バンド別のQSO状況、バンド別のマルチ獲得状況  
  
>※：callsing.*のコールサインは、サマリーシート作成作成時に入力したコールサインです。  

**重要： N1MM logger+で生成したADIFファイル名のコールサインとサマリーシートのコールサインが異なるとエラーとなります。**  
**重要：コールサインが移動局の場合、ソフトウェアの機能確認を行っていません。**
  
## Features

このツールの機能は、以下のとおりです。

1. JARLコンテストログv.2.1の提出ログを作成する。  
2. コンテストログからQSO状況のスコア資料を作成する。
3. ターボハムログ用のCSVファイルを作成する。  

## Demo

このツールは、

1. N1MMlogger+でExportされるADIFファイルをpyファイル、exeファイルと同じフォルダに保存して、
2. サマリーシートを作成し、
3. 提出ログを作成するためのパラメータを設定し、
4. ログ作成を押すことで、 

コンテストログを作成します。

## Requirement

1. python 3.13がインストールされているマシーンであること  
2. 実行ファイルn1mm2jarl_TkEasyGUI.exeを利用する場合には、実行ファイルがWindows11 x64環境でpyinstallで実行ファイルを作成しているために、Windows X64環境が必要となります。
3. pythonコンパイラでこのツールを利用する場合には、以下の機能拡張をインストールする必要があります。
   1. TkEasyGUI
   2. BeautifulSoup
   3. sys
   4. pathlib
   5. chardet
   6. datetime
   7. os
   8. pickle

## Usage

このツールの使い方は、初めて利用することを前提に示します。  
(1)ツールの起動  
n1mm2jarl_TkEasyGUIを起動します。  

(2)サマリーシート作成  

   1. サマリーシート作成  
   「サマリーシート作成」ボタンを押す。  
   ボタンを押すと【「サマリーシート作成」【JARL v.2.1用】画面が表示さます。  
   この画面上部の「ファイルの新規作成」ボタンを押します。この動作で、ツールを保存するフォルダ内に"summarysheet.txt"を作成されます。 
      >※：２度目以降のサマリーシート作成は、「ファイル読込」ボタンを押すことで、"summarysheet.txt"に保存されていた情報が【「サマリーシート作成」【JARL v.2.1用】画面が表示さます。

   2. サマリーシートの記入  
   【「サマリーシート作成」【JARL v.2.1用】画面の各項目を記入する。  
   3. サマリーシートの保存  
   この画面上部の「ファイルの保存」ボタンを押すことで、サマリーシートの情報が、"summarysheet.txt"に保存されます。  
   4. サマリーシート作成終了  
   「終了」ボタンを押してください　　


(3)　QSO‗DBライブラリ作成  
   このボタンは、N1MM2JARL_contestツールがTurboHamlogのQSL発行可否処理において、過去のQSO状況とコンテストでのQSO状況を比較し、QSLを発行するか否かを判断するために、過去のQSO状況をデータベース化するものです。  
   このN1MM2JARL_contesツールは、QSL発行の可否を、同一局、同一バンド、同一モードで初QSOの場合にQSLを発行すると判断します。このQSO‗DBライブラリ作成は、「ADIFファイル」からcallsign band modeを抽出し、「callsign-band-mode」のデータベースを作成します。ADIFファイルはハムログでも、N1MM logger+のexportしたものでも可能です。  
   ***【重要】この機能を利用しない場合においても、必ず、「空ファイル」を作成してください。***

   1. a
   2. b
   3. c
   4. d
   5. e  

(4) ログ作成パラメータの設定  
***【重要】パラメータを設定したら、必ず「パラメータ設定」ボタンをおしてください。***  

   1. コールサインと局種係数はサマリーシートとから自動的に転記されます。
   2. 「UTC時刻をJSTに変換する」チェックボックスは、ADIFファイルの時刻がUTCの場合に、JSTに変換する場合にチェックするものです。
   3. 「QSLの発行」チェックボックスは、ここをチェックすると、QSL発行条件（バンド、モードで初QSO）の場合に、callsign.csvファイルに”J”を設します。このチェックボックスをチェックしない場合には、一律、”N”を設定します。
   4. 「'1.2Gバンド以上のパワーコード変換 M -> L'」チェックボックスは、N1MMではバンドごとにパワーコードを設定できないために、多分、自局のマルチをMに設定していると思われるので、1.2Gバンド以上のQSOで自局のマルチをMからLへ変換するものです。
   5. 「'ALL Asia DX Contest?'チェックボックスは、オールアジアコンテスト用の提出ログ処理をするためのものです。

(5) コンテストログ生成
   この「"コンテストログ生成"」ボタンは、このボタンを押すことで、提出ログ作成する処理を実行します。

## Install

このツールのインストール方法は、2つの方法があります。  
一つ目は、実行ファイルn1mm2jarl_TkEasyGUI.exeを任意のフォルダにコピーし、実行することができます。  
二つ目は、xxx.pyファイルを任意のフォルダにコピーし、python 3.13がインストールされていれば、pythonのインタプリタで実行することができます。  

## Note

注意点をまとめる

## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

Seiichi Tanaka JI1FLB