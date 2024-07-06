"""
lsfix by autoz
v0.1
"""
command_list = ['la','ll']
def run(command):
    if command == 'la':
        la()
    elif command == 'll':
        ll()


def la():
    import os
    os.system('ls -la')

def ll():
    import os
    os.system('ls -l')