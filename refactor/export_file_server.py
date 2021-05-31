import socket

HOST = '127.0.0.1'
PORT = 11122

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()


    with conn:
        print("Connected by ", addr)
        while True:
            data = conn.recv(1024).decode(encoding="UTF-8")
            if not data:
                break
            if any(character == "[" or character == "{" for character in data):
                with open("final_students.json", 'w') as final:
                    final.write(data)
                    final.close()
                    break
            elif any(character != "[" for character in data):
                with open("final_students.csv", 'a') as final:
                    final.write(data)
                    final.close()
                    break
            else:
                print('invalid format')




