# -*- coding: utf-8 -*-


def login(username, password):
    try:
        user_file = open('/etc/users.txt')
        user_buf = user_file.read()
        users = [line.split('|') for line in user_buf.split('\n')]
        if [username, password] in users:
            return True
        else:
            return False
    except Exception as e:
        print("can't authentication you")
        return False


def logout():
    print("这一行不会被测试用例覆盖")
    print("这一行也不会被测试用例覆盖")


