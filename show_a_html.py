# show_a_html.py
import socket
def service_client(new_socket):
    """为这个客户端返回数据"""
    # 1. 接收浏览器发送过来的请求 ，即http请求  
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(1024)
    print(request)
    # 2. 返回http格式的数据，给浏览器
    # 2.1 准备发送给浏览器的数据---header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"  # 浏览器解析换行 用\r\n
    # 2.2 准备发送给浏览器的数据---body
    response += "hahahhah"
    new_socket.send(response.encode("utf-8"))
    new_socket.close()  # 关闭套接字 !
def main():
    """用来完成整体的控制"""
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1. 创建套接字
    tcp_server_socket.bind(("", 7890))  # 2. 绑定
    tcp_server_socket.listen(128)  # 3. 变为监听套接字
    while True:
        new_socket, client_addr = tcp_server_socket.accept()  # 4. 等待新客户端的链接
        service_client(new_socket)  # 5. 为这个客户端服务
    tcp_server_socket.close()  # 关闭监听套接字 !
if __name__ == "__main__":
    main()
