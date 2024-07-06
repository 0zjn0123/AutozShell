import os,sys

if len(sys.argv) > 1:
    try:
        if not sys.argv[1] == "-c":
            # 判断当前目录有没有main.py
            
            os.system("pip install pluginbase")
            if os.path.exists("main.py"):

                os.system("python3 main.py")
            else:
                if os.path.exists("autozshell.zip"):
                    os.system("unzip autozshell.zip")
                    os.system("python3 main.py")
    except:
        pass

    if sys.argv[1] == "-c":
        os.system("zip autozshell.zip *")
