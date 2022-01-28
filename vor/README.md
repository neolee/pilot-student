## 进入编程世界的第一课

这里是存放学习反馈（*Voice of Readers*）的地方，你的感想、心得或者抱怨都可以写好放在这个目录下。



### 关于类定义后面有没有括号的问题

之前一直没有注意到这个问题，今天再看的时候才发现 `class` 后面的类名称是可以没有括号的，继承的时候就有了。然后自己给不需要继承其他类的类名称后面加了括号，发现没有什么影响。



关于机器人作业，写了一个记录读书记录的小机器人。

包括，问读了什么书，然后写到文件里，用到 `with open` 文件操作，还用到了 `f-string` ，第二个是之前自己不太会用的。

```python
import locale
import time

class BookRecordBot(Bot):
    def __init__(self, runtype='once'):
        self.runtype = runtype
        self.q = "你最近有读什么书吗？告诉我书名吧。"
        
    def _think(self, s):
        locale.setlocale(locale.LC_CTYPE, 'chinese')
        today = time.strftime('%Y年%m月%d日')
        if "没" in s:
            return("什么？你想变成傻子吗？还不去读书。")
        else:
            with open('./book-read-record.txt', 'a') as f:
                f.write(f"{today}\t{s}\n")
            return (f"我帮你做了一条记录，{today} 你读完了《{s}》。\n恭喜你，多读好书！")
```

