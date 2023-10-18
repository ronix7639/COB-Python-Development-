import requests
apikey = 'b1b42a67f3c35d96f5ba11ff47f795d8' #Apikey of openweathermap website

userlocation = input("Enter city to check the weather :") #Asks user to give their desired location to check the weather

weatherdata = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userlocation}&units=imperial&APPID={apikey}")

if weatherdata.status_code ==200:
    weather = weatherdata.json()['weather'][0]['main']
    temperature = round(weatherdata.json()['main']['temp']) #Gives weather in Fahrenheit
    temp = round((temperature-32)*5/9) #Logic to convert from Fahrenheit to Celcius
    userchoice = input("Enter your choice check weather in Fahrenheit or Celcius(F/C): ")
    if userchoice=='F':
        print(f"The weather in {userlocation} is: {weather}")
        print(f"The temparature in {userlocation} is : {temperature}°F")
    elif userchoice=='C':
        print(f"The weather in {userlocation} is: {weather}")
        print(f"The temparature in {userlocation} is : {temp}°C")
    else:
        print("Enter valid input")
else:
    print("Couldn't fetch data , recheck your input")