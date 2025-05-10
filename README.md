# READMEは現在作成中


N1MM2JARL_contestlogツール
====

# Overview

N1MM2JARL_contestlogツールは、N1MM Logger+が生成するADIFファイルをJARLコンテストログver.2.1のコンテストログを作成するツールです。  
また、このツールは、コンテストログ作成機能のほか、TurboHamlog用のCSVファイルを作成する機能などを有します。


## Description

N1MM2JARL_contestlogツールは、N1MM Logger+が生成するADIFファイルをJARLコンテストログver.2.1のコンテストログを作成するツールです。  
従来、N1MM Loger+で国内コンテストに参加する方は、コンテスト終了後に、コンテストログを提出するため、CtestwinなどのコンテストロガーにN1MM Logger+が生成するADIFファイルを読み込ませ、提出ログを作成したていたものと思います。
このN1MM2JARL_contestlogツールは、N1MM Looger+のADIFファイル callsign.adiを簡単にJARLコンテストログ形式の提出ログを作成します。  
このツールは、日本でよく使われていTurboHamlogにログ情報を読み込ませるためのCSVファイルも作成します。  
このツールは、以下のものを作成する機能を有します。  
  callsign.txt  : 提出用コンテストログファイル　　
  callsign.csv  : Turbo Hamlog用のCSVファイル
  callsign_score.txt : コンテストの集計結果、バンド別のQSO状況、バンド別のマルチ獲得状況　　

<ins>※：callsing.*のコールサインは、サマリーシート作成作成時に入力したコールサインです。　　
重要： N1MM logger+で生成したADIFファイル名のコールサインとこのコールサインが異なるとエラーとなります</ins>  
  


## Demo

このツールの使い方は、初めて利用することを前提に示します。  
(1)ツールの起動  
n1mm2jarl_TkEasyGUIを起動します。  

(2)サマリーシート作成  
・サマリーシート作成   

<ins>※：２度目以降のサマリーシート作成は、「ファイル読込」ボタンを押すことで、"summarysheet.txt"に保存されていた情報が【「サマリーシート作成」【JARL v.2.1用】画面が表示さます。 </ins>  

「サマリーシート作成」ボタンを押す。  
ボタンを押すと【「サマリーシート作成」【JARL v.2.1用】画面が表示さます。  
この画面上部の「ファイルの新規作成」ボタンを押します。この動作で、ツールを保存するフォルダ内に"summarysheet.txt"を作成されます。  
・サマリーシートの記入  
【「サマリーシート作成」【JARL v.2.1用】画面の各項目を記入する。  
・サマリーシートの保存  
この画面上部の「ファイルの保存」ボタンを押すことで、サマリーシートの情報が、"summarysheet.txt"に保存されます。  
・サマリーシート作成終了　　
「終了」ボタンを押してください　　

(3)　QSO‗DBライブラリ作成  
このボタンは、TurboHamlogのQSL発行処理において、過去のQSO状況とコンテストでのQSO状況を比較するために、過去のQSO状況をデータベース化するものです。  
このツールは、コールサイン.csvファイル作成時に、過去のQSO状況として、  
  同一局、同一バンド、同一モードでQSOした局  
の場合には、QSLフィールとの情報をNとします。　　
a)  
b)  
c)
d)  

(4) ログ作成パラメータの設定
a) コールサインと局種係数はサマリーシートとから自動的に転記されます。  
b) UTC  


## Requirement

１．python 3.13がインストールされているマシーンであること  
２．実行ファイルn1mm2jarl_TkEasyGUI.exeを利用する場合には、実行ファイルがWindows11 x64環境でpyinstallで実行ファイルを作成しているために、
## Usage


## Install

このツールのインストール方法は、2つの方法があります。  
一つ目は、実行ファイルn1mm2jarl_TkEasyGUI.exeを任意のフォルダにコピーし、実行することができます。  
二つ目は、xxx.pyファイルを任意のフォルダにコピーし、python 3.13がインストールされていれば、pythonのインタプリタで実行することができます。  


## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

Seiichi Tanaka JI1FLB


