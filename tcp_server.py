import socket


def main():
    # 创建 tcp 套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地信息
    server_addr = ("127.0.0.1", 10456)
    tcp_server_socket.bind(server_addr)
    # 让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)
    # 循环目的：调用多次accept,从而为多个客户端服务
    while True:
        print("等待一个新的客户端的到来...")
        # 等待客户端的链接 accept
        client_socket, client_addr = tcp_server_socket.accept()  # 返回元组，拆包
        # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
        # client_socket用来为这个客户端服务
        # tcp_server_socket就可以省下来专门等待其他新客户端的链接
        # 第一个接收 新的套接字，第二个接收 链接客户端的地址
        # 新的套接字 负责客户端通信，tcp套接字 负责监听 等待新客户端链接
        print("一个新的客户端已经到来%s" % str(client_addr))
        # 循环目的: 为同一个客户端 服务多次
        while True:
            # 接收客户端发送过来的请求
            recv_data = client_socket.recv(1024)  # 只返回数据
            print("收到客户端消息：%s" % recv_data.decode("gbk"))
            # 如果recv解堵塞，那么有2种方式：
            # 1. 客户端发送过来数据
            # 2. 客户端调用close导致了 这里 recv解堵塞

            # 客户端不能发送空的内容 因此，若recv_data 为空，则一定是 客户端调用close
            if recv_data:
                # 回送一部分数据给客户端
                # send_data = input("请输入回复客户端的消息：")
                send_data = "hihihi ----- ok -----"
                client_socket.send(send_data.encode("gbk"))
            else:
                break
        # 关闭套接字
        # 关闭accept返回的套接字 意味着 不会在为这个客户端服务
        client_socket.close()
    # 如果将监听套接字 关闭了，那么会导致 不能再次等待新客户端的到来，即xxxx.accept就会失败
    tcp_server_socket.close()


if __name__ == "__main__":
    main()