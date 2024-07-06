theme_name = "default"
theme_version = "1.0.0"
head = "{user}@{address}$ "

import os
# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 从绝对路径中提取目录
current_file_dir = os.path.dirname(current_file_path)
# 拼接成配置文件路径
current_file_dir = current_file_dir.split("/")
current_file_dir = "/".join(current_file_dir[:-1])
with open(current_file_dir + "text", "w") as f:
    f.write(head)