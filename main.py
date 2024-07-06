import configparser
import sys,os
import fun
version = "1.5.0"

config = configparser.ConfigParser()
if not os.path.exists(os.path.expanduser('~') + '/.ashrc'):
    with open(os.path.expanduser('~') + '/.ashrc', 'w') as f:
        pass
config.read(os.path.expanduser('~') + '/.ashrc')
if not config.has_option('ash', 'ash_theme'):
    # 添加新的节（section）
    config.add_section('ash')
    config.set('ash', 'ash_theme', 'default')
    with open(os.path.expanduser('~') + '/.ashrc', 'w') as f:
        config.write(f)

if not config.has_option('ash', 'plugin'):
    config.set('ash', 'plugin', '')
    with open(os.path.expanduser('~') + '/.ashrc', 'w') as f:
        config.write(f)

def hhelp():
    print(f"""
    AutozShell v{version}
    ash 
    -v version
    """)



if __name__ == '__main__':


        if len(sys.argv) > 1:
            if sys.argv[1] == '-h':
                hhelp()

            elif sys.argv[1] == '-v':
                print(f"AutozShell v{version}")


            elif sys.argv[1] == 'theme':
                # if len(sys.argv) > 2:
                # 判断theme目录里有没有这个主题文件
                # print(os.listdir("./theme/" + sys.argv[2]))
                if sys.argv[2] in os.listdir("./theme"):
                    print(f"Set theme to {sys.argv[2]}")
                    os.system("python3 ./theme/" + sys.argv[2] + "/theme.py")
                    config.set('ash', 'ash_theme', sys.argv[2])
                    with open(os.path.expanduser('~') + '/.ashrc', 'w') as f:
                        config.write(f)

            elif sys.argv[1] == 'plugin':
                if len(sys.argv) > 2:
                    # 判断plugin目录里有没有这个插件文件
                    if sys.argv[2] in os.listdir("./plugin"):

                        print(f"Set plugin to {sys.argv[2]}")
                        if config.get('ash', 'plugin') == '':
                            config.set('ash', 'plugin', sys.argv[2])
                        else:
                            config.set('ash', 'plugin', config['ash']['plugin'] + "," + sys.argv[2])

                        with open(os.path.expanduser('~') + '/.ashrc', 'w') as f:
                            config.write(f)
                        print("插件已添加，请重新启动ash以生效")


                    if sys.argv[2] == 'list':
                        print(f"Plugin list: {config['ash']['plugin']}")

            # 取消插件
            elif sys.argv[1] == 'unplugin':
                if len(sys.argv) > 2:

                    # 判断plugin目录里有没有这个插件文件
                    if sys.argv[2] in os.listdir("./plugin"):

                        print(f"Unset plugin to {sys.argv[2]}")

                        pluginlist = config['ash']['plugin'].split(',')

                        pluginlist.remove(sys.argv[2])

                        config.set('ash', 'plugin', ','.join(pluginlist))

                        with open(os.path.expanduser('~') + '/.ashrc', 'w') as f:
                            config.write(f)

                        print("插件已取消，请重新启动ash以生效")





            elif not sys.argv[1] in fun.fun_list:
                # 判断是不是sh文件
                if sys.argv[1].endswith('.sh'):

                    os.system(f"bash {sys.argv[1]}")
                else:
                    print(f"Command not found: {sys.argv[1]}")



        else:
            print(f"""AutozShell {version}
Help:ash -h""")
            import chatmode