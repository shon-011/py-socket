# HTTPクライアントつくってみた

## 導入
新卒研修のWEB基礎を担当することになったので、webの基礎技術の本をいくつか読んでいました。
そのなかで、現在利用しているWEBフレームワークとのつながりが感じられませんでした。

このままではいかん！と言うことでフレームワークのありがたみを感じるため自分で実装してみることにしました。
私自身WEBフレームワークがすでに確立されている時代からプログラミングを始めています。
こうした基礎技術はタイミングがないとなかなか学習する機会がないのでは？と思ったのも今回実装する理由です。

## HTTPクライアント
フレームワークすべてを実装することは今回控えておきます。
初めの一歩ということで、HTTPクライアントを作りリクエストを捌いていくということをやっていきます。

TCP/IPをプログラムから利用するためsocketを利用します。
>インターネットはTCP/IPと呼ぶ通信プロトコルを利用しますが、そのTCP/IPを プログラムから利用するには、プログラムの世界とTCP/IPの世界を結ぶ特別な 出入り口が必要となります。その出入り口となるのがソケット (Socket)であり、TCP/IPのプログラミング上の大きな特徴となっています。 このため、TCP/IP通信をソケット通信と呼ぶこともあります。
引用元：http://research.nii.ac.jp/~ichiro/syspro98/socket.html

>INET (すなわち IPv4) ソケットのことしか語らないつもりだが、利用率でいうとソケットの 99% 以上はこれだ。さらに中でも STREAM (すなわち TCP) ソケットに話題を絞ろうと思う - 自分が何をしているのか分かっているのでない限り (分かってるならこの HOWTO なんて要らないだろ!)、STREAM ソケットが一番分かりやすく、一番性能が出るのだ。
引用元：https://docs.python.org/ja/3/howto/sockets.html

socketといえばTCP/IPらしいです

Pythonには標準モジュールとしてsocketが含まれていて簡単に始めることができます。


### Step1:リクエストを受け取ってレスポンスを返す
``` python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.01",1235)) 
s.listen()

while True:
    clientsocket, address = s.accept()
    clientsocket.send(bytes("Welcome to the server!", 'utf-8'))
    clientsocket.close()
```
＊AF_INET = ipv4,
＊SOCK_STREAM = tcp/ip 

こんな感じでリクエストを受け付けます。

### Step2:HTTP/GET
HTTPメッセージを実装しGETを行います

`/test`にアクセスすると、Helloとレスポンスが戻り、それ以外だと404を返す処理を追加しました。


### Step3: 関数化して整理
リクエストとレスポンス処理を関数化して整理しました。


## 最後に...
今回これをやってみるまで、恥ずかしながらsocketのことを知りませんでした。
基礎的な技術を知らずして作ることはできると思いますが、知っておいて損はないかと思います。
少しずつwebの基礎技術を理解できたらと思います。
インターネット作った人すごい。


### 索引
Real World HTTP: https://www.oreilly.co.jp/books/9784873119038/
https://dev.classmethod.jp/articles/python3socketserver/
https://logmi.jp/tech/articles/314757
https://qiita.com/megadreams14/items/32a3eed4661e55419e1c
