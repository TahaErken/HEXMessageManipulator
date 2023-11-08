import socket
import threading
import time
from flask import Flask, request, render_template
import MessageUpdater

app = Flask(__name__)

UDPSEND_IP = '127.0.0.1'
UDPSEND_PORT = 5005         #loopback için 5006 yapıldı normalı 5005
MESSAGE_INTERVAL = 1  # seconds

UDPLISTEN_IP = '127.0.0.1'
UDPLISTEN_PORT = 5006

# Variables to control the sending thread
send_thread_running = True
listen_thread_running = True



def send_udp_message():
    global send_thread_running

    while send_thread_running:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = MessageUpdater.update_message(0,0)
        sock.sendto(message.encode(), (UDPSEND_IP, UDPSEND_PORT))
        sock.close()
        time.sleep(MESSAGE_INTERVAL)


if __name__ == '__main__':
    send_thread_running = True
    send_thread = threading.Thread(target=send_udp_message)
    send_thread.start()
    app.run()
    send_thread.join()
