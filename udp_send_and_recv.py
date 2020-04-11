import socket

def main():
    # 1. 创建一个 udp 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定本地信息 如果一个网络程序不绑定，则系统会随机分配
    local_addr = ("", 10789)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    udp_socket.bind(local_addr)
    # 3. 发送信息
    send_msg = input("请输入发送的消息：")
    send_addr = ("192.168.0.105", 104560)
    udp_socket.sendto(send_msg.encode("utf-8"), send_addr)
    # 4. 接收信息
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    recv_msg = recv_data[0].decode("gbk")
    recv_addr = recv_data[1]
    print("%s: %s" % (str(recv_addr), recv_msg))
    # 5. 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()