import requests as request

if __name__=="__main__":
	r = request.get('http://localhost:8080/sensor1/temperature')
	print(r.json())
	r = request.get('http://localhost:8080/sensor1/humidity')
	print(r.json())
