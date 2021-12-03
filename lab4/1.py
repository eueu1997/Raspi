import Adafruit_DHT
import os
import cherrypy
import time
import json
#from MyMQTT import *

sensor = Adafruit_DHT.DHT11
pin = 23
class temp():
    exposed = True
    @cherrypy.tools.json_out()
    def GET(self,*path,**query):
        humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
	print("temperatura \n")
	return {
            "bn": "http://localhost/sensor1/",
            "e": [
                    {
                        "n": "temperature",
                        "u": "Cel",
                        "t": time.time(),
                        "v": temperature
		            }
			    ]
		}

class hum():
    exposed = True
    @cherrypy.tools.json_out()
    def GET(self,*path,**query):
        humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
        print("humidity \n")
	return {
            "bn": "http://localhost/sensor1/",
            "e": [
                    {
                        "n": "humidity",
                        "u": "Cel",
                        "t": time.time(),
                        "v": humidity
                    }
                ]   
            }

class alls():
    exposed = True

    def GET(self,*path,**query):
        pass

#class subscribe():
 #   def __init__(self, clientID, topic,broker,port):
#		self.client=MyMQTT(clientID,broker,port,self)
#		self.topic=topic
#		self.status=None
        

if __name__ == "__main__":
    conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True,
			}
		}
    cherrypy.tree.mount(temp(),'/sensor1/temperature',conf)
    cherrypy.tree.mount(hum(),'/sensor1/humidity',conf)
    cherrypy.tree.mount(alls(),'/allSensor',conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
