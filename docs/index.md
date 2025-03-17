# PyAppScript Docs
## 概要
PyAppScriptを描くのは、どれだけの時間がかかるでしょうか。flaskのように、ルーティングがあるわけではありません。また、テンプレートエンジンはjinjaの最低限な範囲です。
このシンプルなフレームワークは、大規模なアプリの作成には適していませんが、簡単なアプリや簡単にpythonに入門したり、自作のwebフレームワークを開発する程度に使えるでしょう。

## 簡単にコードを書いてみよう
### download
pas.pyをダウンロードしましょう。このレポジトリの中に、pas.pyが必ずあるはずです。
このpas.pyはpyappscriptの本体です。このことから、pyappscriptは非常に軽いことがわかります。
### 作成する
pas.pyをプロジェクトフォルダに配置しましょう。
すると、プログラミングの開始です! 以下のコードがHelloWorldを表示するコードです。
```python
import pas

@pas.get
def main(e):
    return "Hello,World!"
pas.run(8000)
```
asgiを利用する場合、functionにasyncをつけ、uvicornで起動しましょう。
下手にルーティングを心配する必要はありません。

このframeworkにはルーティングが存在しない(といってよい)のです。
