import rpyc
import pymysql
import random
from socket import socket
import json

class Services(rpyc.Service):

    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', password='', database='chat')
        self.cursor = self.connection.cursor()

    def exposed_register(self, username, email, password):
        sql = 'insert into users values(%s, %s, %s,%s)'
        sql1 = 'insert into verify values(%s,%s)'
        verifycode_maker = random.randint(1000, 9999)
        enabled = 0
        self.connection.begin()
        try:
            self.cursor.execute(sql, (username, email, password,enabled))
            self.cursor.execute(sql1, (username,verifycode_maker))
        except:
            self.connection.rollback()
            return False
        else:
            self.connection.commit()
            return True

    def exposed_login(self, username, password):
        sql = 'SELECT * from users where username=%s and password=%s'
        try:
            self.cursor.execute(sql, (username, password))
            check = self.cursor.fetchall()
        except:
            return None
        else:
            for row in check:
                if row[3] == '1':
                    return True
                else:
                    return False


    def exposed_verify(self,username,verify_code):
        sql1 = 'SELECT * from verify where username=%s '
        try:
            self.cursor.execute(sql1, username)
            check = self.cursor.fetchall()
            for row in check:
                if row[1] == verify_code:
                    sql = 'UPDATE users SET enabled = %s WHERE username = %s'
                    values = (1,username)
                    self.connection.begin()
                    try:
                        self.cursor.execute(sql, values)
                    except:
                        self.connection.rollback()
                        return False
                    else:
                        self.connection.commit()
                        return True

        except:
            return False
        else:
            return self.cursor.fetchone() is not None


    def exposed_list_users(self):
        sql = 'SELECT username FROM users WHERE enabled=%s ORDER BY username ASC '
        try:
            self.cursor.execute(sql,1)
        except:
            return False
        else:
            list = self.cursor.fetchall()
            return list

    def exposed_message(self):
        try:
            data = client_socket.recv(4096)
            data = json.loads(data.decode())
            username_sender = data.get("username")
            message_sender = data.get("message")
            list = "%s : %s".format(username_sender, message_sender)
            client_socket.send(data.encode())
        except:
            return False

        else:
            return True


if __name__ == '__main__':
    server_socket = socket()
    server_socket.bind(('localhost', 1234))
    server_socket.listen(20)
    print('listening...') #FOR TEST CONNECTION
    client_socket, address = server_socket.accept()
    print('someone connected', address) #FOR TEST CONNECTION
    server = rpyc.ThreadedServer(Services, port=1234)
    server.start()