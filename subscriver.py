import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "senai/dev"
def on_message(client, userdata, msg):
  print("Mensagem recebida no tópico '{msg.topic}': {msg.payload.decode()}")
        
client = mqtt.client()
client.on_message = on_message
client.connect(broker, port)

client.subscribe(topic)
print(f"Inscrito no tópico '{topic}', aguardando mensagens...")
      
client.loop_forever()
