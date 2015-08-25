import paho.mqtt.client as mqtt
import os,json,time, random
from threading import Thread

# we are going to maintain this dictionary
todos = []

# This class is wrapper for mqtt client, copied from
# paho examples
class MyMQTTClass:
    def __init__(self, clientid=None):
        self._mqttc = mqtt.Client(clientid)
        self._mqttc.on_message = self.mqtt_on_message
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_disconnect = self.mqtt_on_disconnect
        self._mqttc.on_publish = self.mqtt_on_publish
        self._mqttc.on_subscribe = self.mqtt_on_subscribe

    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print("mqtt connect with rc: "+str(rc))

    def mqtt_on_disconnect(self, mqttc, obj, rc):
        print("mqtt disconnect with rc: "+str(rc))

    def mqtt_on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def mqtt_on_publish(self, mqttc, obj, mid):
        print("published message id: "+str(mid)+", obj: "+str(obj))

    def mqtt_on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def mqtt_on_log(self, mqttc, obj, level, string):
        print(string)

    def publish(self, topic, obj):
        jsonStr = json.dumps(obj)
        print jsonStr
        self._mqttc.publish(topic, jsonStr, qos=1)

    def run(self):
        #self._mqttc.connect("localhost")
        self._mqttc.connect("192.168.1.13")

        rc = 0
        while rc == 0:
            rc = self._mqttc.loop_forever()
        return rc

def postpone(function):
  def decorator(*args, **kwargs):
    t = Thread(target = function, args=args, kwargs=kwargs)
    t.daemon = True
    t.start()
  return decorator

client = None

@postpone
def init_mqtt():
    # mqttc = MyMQTTClass("client-id")
    # but note that the client id must be unique on the broker. Leaving the client
    # id parameter empty will generate a random id for you.
    global client
    client = MyMQTTClass()
    rc = client.run()
    print "completed:", rc

# init mqtt client in a separate thread
init_mqtt()
ops=['get', 'create']
listops=[{}, {"task":"call me back?"}]
entityops=['get','update','delete']
entityparams=[{},{"task":"right now?"}, {}]
while True:
    print "..."
    id =  random.randint(0,1)
    rpc = {"jsonrpc":"2.0", "method": ops[id], "params": listops[id]}
    time.sleep( 5 )
    client.publish("/data/todos", rpc)
    # if its create, we'll do another operation
    if id==1:
        id=random.randint(0,2)
        rpc = {"jsonrpc":"2.0", "method": entityops[id], "params": entityparams[id]}
        time.sleep(3)
        client.publish("/data/todos/id", rpc)
