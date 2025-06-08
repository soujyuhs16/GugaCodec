# GugaCodec
> 咕咕嘎嘎！

## 简介
1. 首先，这是为了出CTF题目，让CTFer能够解码用的，稍微bing搜一下就能搜到了
2. 这个项目fork自CPSparrow/PenguinCodec！可以让你在把人类的语言翻译成企鹅语，用咕咕嘎嘎语言交流！

## 使用方法
1. 仅终端运行

    如果你不想使用 streamlit , 可以直接运行 `python3 gugugaga.py` 测试。按照这里面的示例，你也可以编写自己的测试代码！
2. Streamlit WebUI

    如果你喜欢在浏览器里使用，可以运行 `streamlit run .\webui.py` 启动 Streamlit WebUI。

    安装说明：

    streamlit: 使用命令`pip install streamlit`来安装。官方文档说支持 python 3.9~3.13,建议创建虚拟环境之后再安装。

## 终端内运行示例
```bash
(.venv) python gugugaga.py
原始字符串：我喜欢你。
编码后：嘎嘎嘎咕咕嘎嘎咕~嘎咕咕咕嘎咕咕咕~嘎咕咕嘎咕咕咕嘎~嘎嘎嘎咕咕嘎咕嘎~嘎咕咕嘎咕嘎嘎咕~嘎咕咕嘎嘎嘎咕咕~嘎嘎嘎咕咕嘎嘎咕~嘎咕嘎咕嘎嘎咕咕~嘎咕嘎咕咕咕嘎咕~嘎嘎嘎咕咕嘎咕咕~嘎咕嘎嘎嘎嘎咕嘎~嘎咕嘎咕咕咕咕咕
解码后：'我喜欢你。'
```
