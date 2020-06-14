# 使用 Alfred 快速添加 Anki 笔记

## 特性

* 使用剪切板添加笔记
* 自定义 anki-connect 地址
* 自定义默认牌组

## 安装

这个 workflow 依赖度于 [anki-connect](https://github.com/FooSoft/anki-connect)，所以你需要先安装这个工具。
请遵循其 Github 项目的指导，同时你需要注意，Anki 需要在使用这个 workflow 的过程中保持打开。

之后可以通过这个项目的 release 页面下载 anki.workflow 并双击安装。
如果你需要使用剪切板相关的特性，请为您的 Python 解释器安装以下包

```shell
pip install Pillow
pip install pyperclip
```

## 如何使用

Alfred 是一个非常棒的工具，Anki 对于记忆东西也非常有帮助。
有时候，你只是想建立一个快速的备忘卡片。这个是一个简单的操作，不需要任何复杂的设置。
所以这个 workflow 只支持了 `Basic` 这种类型的 Anki 笔记，你可以配合 aText 这类的工具对这个 workflow 进行使用。

```shell
# 向默认笔记本（使用前需要通过 anset 指令先设置）添加笔记
an front>>back

# 向自定义的牌组添加笔记
an front>>back@@deck

# 通过 {cb} 或 「cb」 来通过剪切板的内容添加笔记
an front>>「cb」@@deck
# or
an front>>{cb}
```

强制同步本地和云端的数据

```shell
an sync
```

设置默认牌组和 anki-connect 服务器的地址

```shell
# Set the default deck
anset Default Deck deck_name

# Set the anki-connect server address
anset AnkiConnect URL http://localhost:8765
```

## 问题解决

Q: 我已经安装了 Pillow 和 pyperclip 包，为啥剪切板还是不能用？
A: 请检查您安装两个包的 Python 解释器，我使用的是 `/usr/bin/python`，你可以在 workflow 中重新设置

Q: Alfred 的调试面板告诉我 `UnboundLocalError: local variable 'response' referenced before assignment`
A: 请检查你的 Anki 应用是否处于唤醒状态，请根据 anki-connect [Github](https://github.com/FooSoft/anki-connect) 中 "Notes for Mac OS X Users" 这个部分检查一下相关设置