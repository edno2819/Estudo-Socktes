import socket

HOST = '127.0.0.1'
PORT = 1235

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    '''
        addr - especifica o endereço de quem tenou se conectar comigo como,
                IP da maquina, porta usada
        conn - objeto usado para se comunicar com a maquina no addr
    '''
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('CLiente', addr)
        while True:
            data = conn.recv(1024)  # numero máximo de bytes a ser recebido
            if not data:
                break
            conn.sendall(data)

