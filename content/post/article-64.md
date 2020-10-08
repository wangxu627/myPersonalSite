
---
title: 一个基于asyncio的文件传输工具
date: 2019-11-08 14:46:42.084617
Description: ""
Tags: []
Categories: []
DisableComments: false
---
  

import sys

import asyncio

import os

import struct

  

PORT = 11199

USAGE = '''

Usage:

    python file-transfer.py server 

    python file-transfer.py client server-ip file

'''

def write_data(f, data):

    return f.write(data)

  

def read_data(f, size):

    return f.read(size)

  

async def handle_read_data(reader, writer):

    print("client connected")

    loop = asyncio.get_event_loop()

    data = await reader.read(4)

    fn_len = struct.unpack(">i", data)[0]

    data = await reader.read(fn_len)

    file_path = data.decode()

    fn = os.path.basename(file_path)

    if(os.path.exists(fn)):

        os.remove(fn)

    with open(fn, "wb") as f:

        while True:  

            data = await reader.read()  

            if(not data):

                break

            

            await loop.run_in_executor(None, write_data, f, data)

        print('Close the client socket')  

        reader.close()  

  

async def create_server(address, port, loop):

    server = await asyncio.start_server(handle_read_data, address, port, loop=loop)

    return server

  

def run_server():  

    loop = asyncio.get_event_loop()

    server = loop.run_until_complete(create_server("0.0.0.0", PORT, loop)) 

    host = server.sockets[0].getsockname()  

    print('Serving on {}. Hit CTRL-C to stop.'.format(host))  

    try:

        loop.run_forever()  

    except KeyboardInterrupt:  

        pass

    print('Server shutting down.')

    server.close()

    loop.run_until_complete(server.wait_closed())  

    loop.close()  

  

async def create_connect(address, port, filename, loop):

    print("filename : ", filename)

    reader, writer = await asyncio.open_connection(address, port, loop=loop) 

    buf = struct.pack(">i",  len(filename.encode()))

    writer.write(buf)

    await writer.drain()

    writer.write(filename.encode())

    await writer.drain()

    with open(filename, "rb") as f:

        while(1):

            data = await loop.run_in_executor(None, read_data, f, 4 * 1024 * 1024)

            writer.write(data)

            await writer.drain()

            if(not data):

                break

        writer.close()  

        

def run_client(address='127.0.0.1', filename = None):  

    loop = asyncio.get_event_loop()

    loop.run_until_complete(create_connect(address, PORT, filename, loop))    

    print('Client shutting down.')

    loop.close()  

  

if __name__ == '__main__':

    if(len(sys.argv) < 2):

        print(USAGE)

        exit(0)

    if(sys.argv[1] == "server"):

        run_server()

    else:

        print(sys.argv[3])

        run_client(sys.argv[2], sys.argv[3])


