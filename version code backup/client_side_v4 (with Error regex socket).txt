from PyQt5.QtWidgets import QApplication, QMessageBox,QLabel
from PyQt5.uic import loadUi
import sys
import rpyc
from socket import socket
import json
import re

def register():
    username_checker = register_ui.username_field.text()
    email_checker = register_ui.email_field.text()

    pattern_user = '^[\w0-9]{4,}'
    pattern_email = '([a-zA-Z0-9][\w-.]{2,}@\w{2,}\.[a-zA-Z0-9-.]+$)'
    match_user = re.match(pattern_user, username_checker)
    match_email = re.match(pattern_email, email_checker)
    try:
        if match_user is None:
            label_username = QLabel
            error= "Username Invalid"
            register_ui.label_username.settext(error)
            register_ui.label_username.setStyleSheet('color:red')

    except:
        label_username = QLabel
        error = str('use another username')
        register_ui.label_username.settext(error)
        register_ui.label_username.setStyleSheet('color:red')


    try:
        if match_email is None:
            label_email = QLabel
            error='Email Invalid'
            register_ui.label_email.settext('Email Invalid')
    except:
        label_email = QLabel
        error = 'use Correct Email'
        register_ui.label_email.settext('use Correct Email')


    pass1 = register_ui.password1_field.text()
    pass2 = register_ui.password2_field.text()
    if pass1 == pass2 and match_user and match_email:
        username = username_checker
        email = email_checker
        result = services.register(username, email, pass1)
        if result:
            message = QMessageBox()
            message.setText('Registered successfully')
            message.setIcon(QMessageBox.Information)
            message.exec()
            register_ui.username_field.clear()
            register_ui.email_field.clear()
            register_ui.password1_field.clear()
            register_ui.password2_field.clear()
            register_ui.close()

        else:
            message = QMessageBox()
            message.setText('Error in registration, please try later')
            message.setIcon(QMessageBox.Warning)
            message.exec()
    else:
        message = QMessageBox()
        message.setText('passwords do not match')
        message.setIcon(QMessageBox.Warning)
        message.exec()


def login():
    username = login_ui.username_field.text()
    password = login_ui.password_field.text()
    result = services.login(username, password)
    if result:
        chat()
        login_ui.close()

    if result is None:
        message = QMessageBox()
        message.setText('user or pass is incorrect')
        message.setIcon(QMessageBox.Warning)
        message.exec()

    if result is False:
        verifycheck_ui.show()
        login_ui.password_field.clear()



def verify():
    username = login_ui.username_field.text()
    verify_code = verifycheck_ui.verify_check.text()
    result_check = services.verify(username , verify_code)
    if result_check:
        message = QMessageBox()
        message.setText('Verify Successfully Please Login Again')
        message.setIcon(QMessageBox.Information)
        message.exec()
        verifycheck_ui.close()
    else:
        message = QMessageBox()
        message.setText('verify code is not valid')
        message.setIcon(QMessageBox.Warning)
        message.exec()
        verifycheck_ui.verify_check.clear()


def chat():
    chat_ui.show()
    chat_ui.userlist_view.clear()
    lists = services.list_users()
    if lists:
        for row in lists:
            chat_ui.userlist_view.addItem(row[0])

    chat_ui.actionsign_out.triggered.connect(lambda: login_ui.show())
    chat_ui.actionsign_out.triggered.connect(lambda: chat_ui.close())

def message():

    message_sender = chat_ui.message_field.text()
    username_sender = login_ui.username_field.text()
    data = json.dumps({"username": username_sender, "message": message_sender})
    client_socket.send(data.encode())

    lists = services.message()
    if lists:
        data = client_socket.recv(4096)
        data = json.loads(data.decode())
        username_sender = data.get("username")
        message_sender = data.get("message")
        list = "%s : %s".format(username_sender,message_sender)
        chat_ui.chat_view.addItem(list)
    if lists is False:
        error = "Error"
        chat_ui.chat_view.clear()
        chat_ui.chat_view.addItem(error)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_ui = loadUi('views/login.ui')
    register_ui = loadUi('views/register.ui')
    chat_ui = loadUi('views/chat-room.ui')
    verifycheck_ui = loadUi('views/verifycheck.ui')
    login_ui.register_btn.clicked.connect(lambda: register_ui.show())
    login_ui.login_btn.clicked.connect(login)
    register_ui.pushButton.clicked.connect(register)
    verifycheck_ui.verifycheck_btn.clicked.connect(verify)
    chat_ui.send_btn.clicked.connect(message)
    login_ui.show()
    client_socket = socket()
    client_socket.bind(('localhost', 1234))
    services = rpyc.connect('localhost', port=1234).root
    app.exec()