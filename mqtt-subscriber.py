import paho.mqtt.client as mqtt
broker_address="iot.eclipse.org"

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("test",)

def on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()
client = mqtt.Client()
client.connect("iot.eclipse.org",1883,60)
#client.subscribe("topic/test",)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
