# show_need_html.py
# 存在问题：有时候 request 返回空值，会报错！
import socket
import re
import os
def service_client(new_socket):
    """为这个客户端返回数据"""
    # 1. 接收浏览器发送过来的请求 ，即http请求  
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(1024).decode("utf-8")
    print(">>>"*50)
    print(request)
    request_lines = request.splitlines()  # 先切割
    print("")
    print(">"*20)
    print(request_lines)
    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0]) # 不是/都行  空格停
    if ret:
        file_name = ret.group(1)
        print("*"*50, file_name)
        if file_name == "/":  # 这需要上面的变量
            file_name = "/index.html"
        file_name = file_name[1:]  # 和linux 不同，路径不一致 这用替换更好
    # 2. 返回http格式的数据，给浏览器
    file_path = os.path.join(".\html", file_name)
    print("file_path >>> ", file_path)
    try:
        f = open(file_path, "rb")  # 打开文件有危险
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据---header
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "\r\n"
        # 2.2 准备发送给浏览器的数据---boy
        response_body = html_content
        response = response_header.encode("utf-8") + response_body
        # 将response发送给浏览器
        new_socket.send(response)
        # 将response body发送给浏览器
        # new_socket.send(html_content)
    # 关闭套接字
    new_socket.close()
def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1. 创建套接字
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放
    # 这样就保证了，下次运行程序时 可以立即绑定7890端口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2. 绑定
    tcp_server_socket.bind(("127.0.0.1", 7899))
    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()
        # 5. 为这个客户端服务
        service_client(new_socket)
    # 关闭监听套接字
    tcp_server_socket.close()
if __name__ == "__main__":
    main()