import socket
import threading
"""
案例：多任务版udp聊天器
编写一个有2个线程的程序
线程1用来接收数据然后显示
线程2用来检测键盘数据然后通过udp发送数据

效果：可以实现同时收发消息
"""


def send_data(udp_socket, dest_ip, dest_port):
    """发送数据"""
    while True:
        # dest_ip = input("请输入接收方ip：")
        # dest_port = int(input("请输入接收方port："))
        dest_msg = input("请输入发送内容：")
        udp_socket.sendto(dest_msg.encode("gbk"), (dest_ip, dest_port))


def recv_data(udp_socket):
    """接收数据并显示"""
    while True:
        receive_data = udp_socket.recvfrom(1024)
        print("%s: %s" % (str(receive_data[1]), receive_data[0].decode("gbk")))


def main():
    """完成udp聊天器的整体控制"""
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定本地信息
    udp_socket.bind(("127.0.0.1", 10789))
    # 3. 获取对方的ip
    dest_ip = input("请输入接收方ip：")
    dest_port = int(input("请输入接收方port："))
    # 4. 创建2个线程，去执行相应的功能
    t_send = threading.Thread(target=send_data, args=(udp_socket, dest_ip, dest_port))
    t_recv = threading.Thread(target=recv_data, args=(udp_socket,))
    
    t_send.start()
    t_recv.start()

    # udp_socket.close()  # 这不能关  主线程会执行这个

if __name__ == "__main__":
    main()