import kakaoi

client = Client()

def main(message):
    if message.request.utterance == "ping":
        return SimpleText("Pong!")
    elif message.request.utterance == "pong":
        return SimpleText("Ping!")

    return SimpleText("Ping!")

client.run(main, host='0.0.0.0')

print(main(" "))
