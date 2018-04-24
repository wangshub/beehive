from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('shenzhen')
condition = location.condition
forecasts = location.forecast
for forecast in forecasts:
    print('-------------')
    print()
    print(forecast.text)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)
    print(forecast.day)
    print(forecast.code)
