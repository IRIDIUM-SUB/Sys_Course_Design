# File System Dev Log

## 系统设计

非常简单的文件系统,仅表现文件头,不涉及读写

目录结构以`json`序列化实现.

直接往 `simdisk`里面塞.

提供CMD和命令解析.

```bash
mkfs #格式化磁盘
ls [None]
pwd [None]
cd [foldername]
rm [filename]
su #Switch between root and user
mkdir [foldername]
touch [filename]
cat [filename]#Return success or fail
exit#此时再写入文件
```

`simdisk`标定为20M

使用`dict`

## 数据规范

```json
{
    "folder":{
        "type":"Directory",
        "ctime":"timestamp",
        "mtime":"timestamp",
        "owner":None,
        "size":obj,
        "subfile1":{},
        "subfile2":{}
    },
    "file":{
        "type":"File",
        "ctime":"timestamp",
        "mtime":"timestamp",
        "owner":"user/root",
        "size":"fake data"
    }
}
```

## 技术细节

- 支持过量的括号分隔符
- logger
- `console()`->`class commandresolve()`->`class fileprocessing()`
- 命名不可以取保留字
- 多余的参数会被忽略
- 没有做``cd ..`...

