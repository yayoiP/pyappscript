# pyappscript
pyappscriptはオープンソースで開発を助けます。[本体](pas.py)

pyappscriptは簡単にアプリケーションを作成可能で、jinjaを搭載しています。:)

## アプリケーションの作成
```python
import pas

@pas.get
def getpage(e):
    if e.path == "":  #mainpage
        return "helloWorld"
    return "pyappscript :D"

pas.run(8000)
```
<a href="http://localhost:8000">このように</a>なります。

Pyappscriptの特性として、ルーティングは自分で行う点があります。
flaskのような便利なフレームワークに存在するようなroute関数が存在しないのです。
これは一見デメリットのように感じますが、一つ一つが結びつくのではなく、集合となって結びつくと考えられるのです。

たとえば、flaskで行われる以下のようなものが必要ないのです。
```python
@route("/user/<userid>")
```
これは明らかな柔軟性をもたらします。

またこれらはシンプルであるため、自分でhttpの仕組みを考えることができるのです。

## methodの解説
@pas.getのようにhttpの処理を行うデコレータが4つ存在します。
それは以下の通りです。

- get
- post
- put
- delete

これらが存在することにより、すべてのことが可能になります。
これらのデコレータは「リクエストオブジェクト」を返り値として渡します・

リクエストオブジェクトは、method,path,ip address,ua,host,cookie,header,パラメータ(data)
post(formで返されるもの),item(セッション)を返します。

セッションは自動で作成されます。
