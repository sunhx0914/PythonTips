# -*- coding:utf8 -*-
"""
在一个电脑中编写1个程序，有2个功能
1.获取键盘数据，并将其发送给对方
2.接收数据并显示
并且功能数据进行选择以上的2个功能调用
"""
import socket


def send_data(udp_socket):
    """获取键盘数据，并将其发送给对方"""
    addr_ip = input("\n请输入对方的ip地址:")
    addr_port = int(input("请输入对方的port:"))
    send_msg = input("请输入要发送的数据:")
    udp_socket.sendto(send_msg.encode("gbk"), (addr_ip, addr_port))  
    # window gbk   linux utf-8


def recv_data(udp_socket):
    """接收数据并显示"""
    recv_tuple = udp_socket.recvfrom(1024)
    recv_msg = recv_tuple[0].decode("gbk")  # window gbk   linux utf-8
    recv_addr = recv_tuple[1]
    print("%s: %s" % (recv_addr, recv_msg))
    # print("%s: %s" % (str(recv_addr), recv_msg))  # str 可以不加吗


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ("", 10456)
    udp_socket.bind(local_addr)

    while True:
        print("=" * 30)
        print("1:发送消息")
        print("2:接收消息")
        print("0:结束")
        print("="*30)
        op = input("请输入要操作的功能序号:")

        if op == "1":
            send_data(udp_socket)
        elif op == "2":
            recv_data(udp_socket)
        elif op == "0":
            break
        else:
            print("输入有误，请重新输入...")

if __name__ == "__main__":
    main()
