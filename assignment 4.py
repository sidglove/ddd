o	# Program Name: Assignment4.py 
o	# Course: IT3883/Section 
o	# Student Name: Michael Glover
o	# Assignment Number: Lab 4
o	# Due Date: 03/24/2025
o	# Purpose: Transmits a string over a socket to program b while program b will listen for a string from a 

import socket

host = 'localhost'  
port = 12345 

def program_a():
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
       
        user_input = input("Send to program b: ")
        
        s.sendall(user_input.encode('utf-8'))
        
        data = s.recv(1024)
        
        print("Program B response:", data.decode('utf-8'))

    if __name__ == "__main__":
             program_a()

import socket

host = 'localhost' 
port = 12345 

def program_b():
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Listening  {host}:{port}")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected {addr}")
    
            data = conn.recv(1024)

          
            uppercase_data = data.decode('utf-8').upper()

          
            conn.sendall(uppercase_data.encode('utf-8'))

        if __name__ == "__main__":
            program_b()