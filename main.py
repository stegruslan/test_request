import requests


API_KEY = "b1fc7ce7de5b76ac73f7381ea4ded36a"

URL = "https://api.openweathermap.org/data/2.5/weather"


def get_city():
    return input("Введите название города!\n"
                 ": ")


def request(city, appid=API_KEY, lang="ru", url=URL):
    params = {
        "q": city,
        "appid": appid,
        "lang": lang
    }
    response = requests.get(url, params)
    if response.status_code == 200:
        return response.json()


def main():
    print("Привет!")
    while True:
        city = get_city()
        response = request(city)
        if response:
            break
        print("Не смог найти такой город, повторите попыту!")
    data = get_data(response)
    msg = massage(data, city)
    print(msg)


def get_data(response):
    data = dict()
    data['description'] = response['weather'][0]['description']
    data['temp'] = response['main']['temp'] - 273.15
    data['feels'] = response['main']['feels_like'] - 273.15
    data['wind'] = response['wind']['speed']
    data['pressure'] = response['main']['pressure']
    return data


def massage(data, city):
    return (f"Погода в {city.capitalize()}:\n"
            f"{data['description'].capitalize()}\n"
            f"Температура: {data['temp']} t, "
            f"ощущается как {data['feels']} t\n"
            f"Скорость ветра: {data['wind']} м/с\n"
            f"Давление: {data['pressure']} мм р.с")




main()


# округлить температуру ( math ( возможно установить pip)