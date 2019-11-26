print("program no 2")
def weather():
    forecast = "It will be a sunny day today"
    print("a)",forecast.count("day"))
    return
weather()


def indexweather():
    forecast = "It will be a sunny day today"
    print("b)",forecast.index("sunny"))
    return
indexweather()

def changeweather():
    forecast = "It will be a sunny day"
    print("c)",forecast.replace("sunny","cloud"))
    return
changeweather()