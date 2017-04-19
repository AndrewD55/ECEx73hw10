# Andrew Schulz
import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname='www.youtube.com')

try:
    ssl_sock.connect(('www.youtube.com', 443))
    ssl_sock.settimeout(1.0)
    ssl_sock.sendall("GET / HTTP/1.1\r\nHostname: www.youtube.com\r\n\r\n")
    while 1:
        try:
            data = ssl_sock.recv(2048).strip()
            print data
        except:
            break
except:
    print "Socket connection error!"
finally:
    ssl_sock.close()
