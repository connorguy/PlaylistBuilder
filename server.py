import socket
import math
import json

users = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((socket.gethostname(), 6969))

while True:
    sock.listen(1)
    conn, addr = sock.accept()


    typeOfConnection = conn.recv(1) #If you are sending information
    if ord(typeOfConnection) == 1:
        print "Receiving song and locationd data"
        sizeData = conn.recv(4)
        total = 0
        for v in sizeData:
            total += ord(v)

        inputString = conn.recv(total)

        stringValues = inputString.split(" ")

        data = [stringValues[1], stringValues[2]]
        songName = ""
        for i in range(3, len(stringValues)):
            songName += stringValues[i] + " "
        songName[:-1]
        data.append(songName)

        users[stringValues[0]] = data

    elif ord(typeOfConnection) == 2: # If you are requesting information
        print "Receiving requestion packet"
        earthRadius =  6371
        sizeData = conn.recv(4)
        total = 0
        for v in sizeData:
            total += ord(v)

        inputString = conn.recv(total)
        stringValues = inputString.split(" ")

        lat1 = float(stringValues[0])
        long1 = float(stringValues[1])
        lat1 = math.radians(lat1)
        long1 = math.radians(long1)

        for user in users:
            lat2 = math.radians(float(users[user][0]))
            long2 = math.radians(float(users[user][1]))

            dlat = lat2 - lat1
            dlong = long2 - long1

            a = math.sin(dlat/2) * math.sin(dlat/2) + math.sin(dlong/2)*math.sin(dlong/2)*math.cos(lat1)*math.cos(lat2)

            c = 2 *math.atan(math.sqrt(a)/ math.sqrt(1-a))

            distance = earthRadius * c
            print distance


    elif ord(typeOfConnection) == 3: #If you are sending information using JSON file
        print "Getting JSON info"
        sizeData = conn.recv(4)
        total = 0
        for v in sizeData:
            total += ord(v)

        inputString = conn.recv(total)
        info = json.loads(inputString)

        users[info["Location"]] = info["SongUris"]

        print users







    






