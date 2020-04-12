import socket


def main():
    # 1. 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 获取服务器的ip port
    dest_ip = input("请输入下载服务器的ip:")
    dest_port = int(input("请输入下载服务器的port:"))

    # 3. 链接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 4. 获取下载的文件名字
    download_file_name = input("请输入要下载的文件名字：")

    # 5. 将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode("gbk"))

    # 6. 接收文件中的数据
    recv_data = tcp_socket.recv(1024)  # 1024--->1K  1024*1024--->1k*1024=1M 1024*1024*124--->1G
    # 这是简单实现，大文件有问题
    if recv_data:  # 如果接收到数据
        # 7. 保存接收到的数据到一个文件中 由于收到数据为字节型，因此直接 wb 就可以
        with open("[接收]" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 8. 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
