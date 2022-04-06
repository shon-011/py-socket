# socket

# HTTPサーバーを作ってみる

# 導入

### 最近の話

- 新卒研修のためWEBの基礎的な本を読む
- Django学習

基礎技術をどのようのにしてフレームワークはりようしているのか、ワカラナイ...😢

---

- フレームワークのありがたみを感じる
- タイミングがないとなかなか学習する機会がないのでは？

→ **作ってみる!**

# ネットワークの基礎

フレームワークすべてを実装することは今回控えておきます。

まずはアプリケーション間の通信に触れるためHTTPサーバーらしきものを作りリクエストを捌いていくということをやっていきます。

# socket ソケット通信

ネットワークの基礎技術

> インターネットはTCP/IPと呼ぶ通信プロトコルを利用しますが、そのTCP/IPを プログラムから利用するには、プログラムの世界とTCP/IPの世界を結ぶ特別な 出入り口が必要となります。その**出入り口となるのがソケット (Socket)**であり、TCP/IPのプログラミング上の大きな特徴となっています。 このため、TCP/IP通信をソケット通信と呼ぶこともあります。
引用元：http://research.nii.ac.jp/~ichiro/syspro98/socket.html
> 

→ これは概念的なもので、実際にはプログラムが利用する標準入出力やファイル入出力をOSが識別するための**識別子**らしい

## Socketのフロー

![d9bbd3786f65025dbaf748de7c0cd34d-1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ed9dc55c-d79f-4e2e-8471-1b123821cbd1/d9bbd3786f65025dbaf748de7c0cd34d-1.png)

## 通信のバリエーション

通信にはいくつもの方式があり、方式を決めるための主なパラメーターは

- アドレスファミリー
- ソケットタイプ

## アドレスファミリー

ソケットにバインドするアドレスの種類

- AF_UNIC ローカル通信
- AF_INET  IPv4
- AF_INET6 IPv6

他にもいろいろある

[https://man7.org/linux/man-pages/man2/socket.2.html](https://man7.org/linux/man-pages/man2/socket.2.html)

## ソケットタイプ

- SOCK_STREAM  双方向コネクション TCP
- SOCK_DGRAM  コネクションレス　UDP

こちらも色々あるみたい。

## Python socketモジュール

Pythonには標準モジュールとしてsocketが含まれていて簡単に始めることができます。

## socketといえばTCP/IPらしいです

> INET (すなわち IPv4) ソケットのことしか語らないつもりだが、利用率でいうとソケットの 99% 以上はこれだ。さらに中でも STREAM (すなわち TCP) ソケットに話題を絞ろうと思う - 自分が何をしているのか分かっているのでない限り (分かってるならこの HOWTO なんて要らないだろ!)、STREAM ソケットが一番分かりやすく、一番性能が出るのだ。
引用元：https://docs.python.org/ja/3/howto/sockets.html
> 

# やってみる

## Step1:リクエストを受け取ってレスポンスを返す

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.01",1235))
s.listen()

while True:
    clientsocket, address = s.accept()
    clientsocket.send(bytes("Welcome to the server!", 'utf-8'))
    clientsocket.close()

```

## Step2:HTTP/GET

HTTPメッセージを実装しGETを行います

`/test`にアクセスすると、Helloとレスポンスが戻り、それ以外だと404を返す処理を追加しました。

## Step3: 関数化して整理

リクエストとレスポンス処理を関数化して整理しました。

## Step4: curl

HTTPは単なるテキストデータの交換にすぎない！

# 最後に...

今回これをやってみるまで、恥ずかしながらsocketのことを知りませんでした。
基礎的な技術を知らずして作ることはできると思いますが、知っておいて損はないかと思います。
少しずつwebの基礎技術を理解できたらと思います。

## 索引

- Real World HTTP: [https://www.oreilly.co.jp/books/9784873119038/](https://www.oreilly.co.jp/books/9784873119038/)
- [https://dev.classmethod.jp/articles/python3socketserver/](https://dev.classmethod.jp/articles/python3socketserver/)
- [https://logmi.jp/tech/articles/314757](https://logmi.jp/tech/articles/314757)
- [https://qiita.com/megadreams14/items/32a3eed4661e55419e1c](https://qiita.com/megadreams14/items/32a3eed4661e55419e1c)