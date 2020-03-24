import urequests as requests
zip_code='96148'
country='us'
api_key='67435cfb0af4e35add908b65325f31ad'

url='http://api.openweathermap.org/data/2.5/weather?zip='+zip_code+','+country+'&appid='+api_key

def weather_pull():
    response = requests.get(url)
    #print(response.text)
    data=response.json()
    conditions=data['weather'][0]['description']
    temp_k=data['main']['temp']
    temp_c=round((temp_k-273.15),1)
    temp_f=round((temp_c*(9/5)+32),1)
    print(temp_c,temp_f)

