# autozshell
全新的shell,使用python编写，支持主题和插件，开发特别简单

# 安装
终端内输入
1.
国内(版本较新)```git clone http://git.zjnsans.top/Autoz/AutozShell.git /usr/local/bin```
国外(版本较低)```git clone https://github.com/0zjn0123/AutozShell.git /usr/local/bin```
2.
```cd AutozShell```
```python main.py```

# 主题
## 使用方法
在ash内输入```ash theme <主题名称>```
目前可以用的有default,sus，当然你也可以自己开发

## 开发
1.在theme目录里新建一个目录，名字是主题名称
2.复制default主题里的theme.py文件到新建的目录里面
3.修改head变量

## 从网上下载主题并使用
```git clone <主题仓库> ./theme```

# 插件
## 使用方法
### 安装插件
在ash内输入```ash plugin <插件名称>```
### 查看已加载插件
```ash plugin list```
### 卸载插件
```ash unplugin <插件名>```

目前可用的插件有lsfix,pythonim
## 开发
可以参照lsfix和pythonim这两个插件开发，目前只能通过插件开发命令
command_list列表是注册的命令
必须要有run方法必须有command参数

# 有大佬可以帮我编译打包一下吗？我这个自己打包会报错


# 
