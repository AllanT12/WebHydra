def write(err, message):
    f = open("log.txt", "a")
    f.write(str(err) + message)
    f.close()
