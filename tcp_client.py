import socket


def main():
    # 创建 tcp 套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    server_ip = input("请输入服务器 ip ：")
    server_port = int(input(("请输入服务器 port：")))
    tcp_client_socket.connect((server_ip, server_port))
    # 发送消息
    send_msg = input("请输入发送的消息：")
    tcp_client_socket.send(send_msg.encode("gbk"))
    # 接收消息，最大接收1024个字节
    recv_data = tcp_client_socket.recv(1024)
    print("收到消息：%s" % recv_data.decode("gbk"))
    # 关闭套接字
    tcp_client_socket.close()

if __name__ == "__main__":
    main()