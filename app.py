'''
ref:

https://pynative.com/parse-json-response-using-python-requests-library/
https://requests.readthedocs.io/en/master/user/quickstart/#passing-parameters-in-urls



'''

import requests
from requests.exceptions import HTTPError
from influxdb import InfluxDBClient


client = InfluxDBClient()

url = "https://api.openweathermap.org/data/2.5/onecall"
payload = {
    "lat": 51.539188,
    "lon": -0.142500,
    # "exclude": {"minute", "hourly", "daily"},
    "appid": "071e2ca913b7853e0af44db7564ec477",
    "units": "metric"}

  out = {}
   for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten(subdict).items()
                out.update(
                    {key + '_' + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out


try:  # use try method to promt errors
    # request data from the server
    response = requests.get(url, params=payload)
    response.raise_for_status()
    json_responce = response.json()
    daily = json_responce['daily']
    current_day = daily[0]
    # print(current_day)

    for day in daily:
        day_flatten = flatten(day)
        bjson_body = [
            {
                "measurement": "prediction",
                "tags": {
                    "day": "current" if daily.index(day) == 0 else "current" + "+" + str(daily.index(day))
                },
                "fields": day_flatten
            }
        ]
        client.write_points(bjson_body, database='test6')

    print(response.status_code)

    # jsonobj = response.json()
    # #print (jsonobj)
    # t_city = jsonobj['name']
    # t_country = jsonobj['sys']['country']
    # t_type = jsonobj["weather"][0]
    # t_type = t_type['main']
    # t_temp = jsonobj['main']['temp']
    # t_temp = round(t_temp)
    # t_humidity = jsonobj['main']['humidity']
    # t_wind = jsonobj['wind']['speed']
    # t_wind = round(t_wind)

    # bjson_body = [
    #     {
    #         "measurement": "weather",
    #         "tags": {
    #             "city": t_city,
    #             "country": t_country
    #         },
    #         "fields": {
    #             "type": t_type,
    #             "temp": t_temp,
    #             "humidity": t_humidity,
    #             "wind": t_wind
    #         }
    #     }
    # ]


# iterate Json responce

# print("Print each key-value pair from JSON response")
# for key, value in json_responce.items():
#     print(key, ":", value)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')

except Exception as err:
    print(f'Other error occurred: {err}')


# Send to InfluxDB


'''
Ref:
https://influxdb-python.readthedocs.io/en/latest/examples.html#tutorials-basic
https://www.influxdata.com/blog/getting-started-python-influxdb/

https://www.open-plant.com/knowledge-base/how-to-install-influxdb-docker-for-windows-10/


'''
# client = InfluxDBClient()
# client.write_points(bjson_body, database='test5')
# print(bjson_body)

# def daily_to_influxdb(d):


# yB6yP6pH5mX4yL0uW3pF0rR4rE3rB8iR6nE5bC5xD7dK1xA6iK MetofficeAPI #hide 

# added new line

# added new line2

