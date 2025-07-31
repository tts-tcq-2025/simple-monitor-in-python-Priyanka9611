

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testPartlyCloudy():
    def pcStub():
        return {
            'temperatureInC': 27,
            'precipitation': 20,
            'humidity': 20,
            'windSpeedKMPH': 15
        }
    weather = report(pcStub)
    print(weather)
    assert weather == "Partly Cloudy"
    
    def pcStub():
        return {
            'temperatureInC': 30,
            'precipitation': 59,
            'humidity': 20,
            'windSpeedKMPH': 15
        }
    weather = report(pcStub)
    print(weather)
    assert weather == "Partly Cloudy"


def testSunnyDay():
    def sunnyStub():
        return {
            'temperatureInC': 25,
            'precipitation': 30,
            'humidity': 20,
            'windSpeedKMPH': 60
        }
    weather = report(sunnyStub)
    print(weather)
    assert weather == "Sunny Day"
    
    def sunnyStub():
        return {
            'temperatureInC': 15,
            'precipitation': 10,
            'humidity': 20,
            'windSpeedKMPH': 15
        }
    weather = report(sunnyStub)
    print(weather)
    assert weather == "Sunny Day"
    
    def sunnyStub():
        return {
            'temperatureInC': 60,
            'precipitation': 10,
            'humidity': 20,
            'windSpeedKMPH': 15
        }
    weather = report(sunnyStub)
    print(weather)
    assert weather == "Sunny Day"


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    weather = report(sensorStub)

    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert(len(weather) > 0);
    
    def humidityStub():
        return {
            'temperatureInC': 50,
            'precipitation': 70,
            'humidity': 26,
            'windSpeedKMPH': 10
            }
    weather = report(humidityStub)
    assert('rain' in weather);


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    testSunnyDay()
    testPartlyCloudy()
    print("All is well (maybe!)");
