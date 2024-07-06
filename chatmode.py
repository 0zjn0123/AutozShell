import os,sys
import configparser
from pluginbase import PluginBase


runcanshu = 0



config = configparser.ConfigParser()
config.read(os.path.expanduser('~') + '/.ashrc')
themefile = config.get('ash', 'ash_theme')
plugin_list = config.get('ash', 'plugin')
if "," in plugin_list:
    plugin_list = plugin_list.split(",")

# 插件

plugin_base = PluginBase(package='main.plugins')
plugin_source = plugin_base.make_plugin_source(searchpath=['./plugin'])

def plugin_load():
    config.read(os.path.expanduser('~') + '/.ashrc')
    themefile = config.get('ash', 'ash_theme')
    plugin_list = config.get('ash', 'plugin')
    if "," in plugin_list:
        plugin_list = plugin_list.split(",")

    if type(plugin_list) == str:
        if plugin_list in plugin_source.list_plugins():
            pass
        else:
            if not plugin_list:

                if plugin_list != "":
                    plugin_source.load_plugin(plugin_list)

    else:
        for i in plugin_list:
            if i in plugin_source.list_plugins():
                pass
            else:
                if not i == "":
                    plugin_source.load_plugin(i)

plugin_load()






themeconfig = configparser.ConfigParser()
# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 从绝对路径中提取目录
current_file_dir = os.path.dirname(current_file_path)
themeconfig.read(current_file_dir+ "/" + "theme" + "/" + themefile + "/" + themefile + ".ini")
#print(current_file_dir+ "/" + "theme" + "/" + themefile + "/" + themefile + ".ini")
#print(themeconfig["theme"])






while True:

    # 重新加载plugin

    plugin_load()
    runcanshu = 0
    config.read(os.path.expanduser('~') + '/.ashrc')
    themefile = config.get('ash', 'ash_theme')
    os.system("python3 " + current_file_dir + "/" + "theme/"+ themefile + "/" + "theme.py")
    with open(current_file_dir + "/" + "themetext", "r") as f:
        themetext = f.read()

    # 获取当前用户和地址
    user = os.getlogin()
    address = os.getcwd()
    # 把inputtext这个变量里的{user}换成user变量
    inputtext = themetext.replace("{user}", user)
    # 把inputtext这个变量里的{address}换成address变量
    inputtext = inputtext.replace("{address}", address)

    text1 = str(input(inputtext))
    if text1 == "exit":
        runcanshu = 1
        sys.exit()
    try:
        if text1[0] == 'c' and text1[1] == 'd':
            # 如果cd后面的路径不存在，则提示错误
            if len(text1) > 2 and not os.path.exists(text1[3:]):
                print("路径不存在")
            else:
                os.chdir(text1[3:])

                runcanshu = 1

    except:
        pass
    try:
        if text1[0] == 'a' and text1[1] == 's' and text1[2] == 'h':
            runcanshu = 1
            os.system("python3 " + current_file_dir + "/" + "main.py " + text1[4:])
    except:
        pass
    # 判断输入的内容是否在插件的command_list中，如果在，则执行对应的函数
    for i in plugin_list:
        # print(plugin_source.list_plugins())
        if type(plugin_list) == list:
            if text1 in plugin_source.load_plugin(i).command_list:
                # print(plugin_source.load_plugin(i).command_list)
                plugin_source.load_plugin(i).run(text1)

                runcanshu = 1
                break
        else:
            if text1 in plugin_source.load_plugin(plugin_list).command_list:
                # print(plugin_source.load_plugin(plugin_list).command_list)
                plugin_source.load_plugin(plugin_list).run(text1)

                runcanshu = 1
                break

    try:
        if text1[0] == 'p' and text1[1] == 'c' and text1[2] == 'm' and text1[3] == 'd':
            exec(text1[5:])
            runcanshu = 1
    except IndexError:
        pass
    except (NameError, SyntaxError) as nerror:
        print(repr(nerror))

    if runcanshu == 1:
        continue


    if runcanshu == 0:
        os.system(text1)



