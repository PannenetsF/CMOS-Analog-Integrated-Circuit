# ElegantBook 优美的 LaTeX 书籍模板

本项目直接来源于由 [Dongsheng Deng](https://ddswhu.me/) 和 [Liam Huang](https://liam.page/) 创立的 ElegantBook 项目，做出了一定的修改以适应个人的习惯并应用于日常笔记等的整理。

## 具体改动

- 取消了正文中的小图标，如“练习”等环境侧面的🖊
- 开启了目录的超链接
- 引入了单章文件，方便独立编译


## 使用方式

个人使用习惯是将除去导言的部分拆分成章节，在正文中使用`\input{}`引入。

复制章节
```sh
cp elegantbook-chap.tex chap/chap05.seq-logic.tex
```

在正文引入
```tex
\input{chap\chap05.seq-logic.tex}
```
