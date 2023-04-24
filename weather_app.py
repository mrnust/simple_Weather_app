import requests
import json
import win32com.client as wincl

flag=True
while flag:
    print('************** Welcome to Weather app *****************')
    try:
        city=input("Enter the name of city. ")
        url=f"https://api.weatherapi.com/v1/current.json?key="Your API_KEY" ={city}%27"

        r=requests.get(url);
        wdic=json.loads(r.text) 
        result=f'''Tempearture in {city} {wdic["location"]["region"]} :
            *** {wdic["current"]["temp_c"]} Celsius ***
            ***** wind: {wdic["current"]["wind_kph"]} kmph *****
            ****** Humidity: {wdic["current"]["humidity"]}% ******'''
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(result)
        print(result)
        flag=input('''\n Do you want to continue
            If yes type true
            else type false\n''').lower()=='true'
        print("********************************************************")
        if(not(flag)):
            speak.Speak(" Bye bye")
            print("******** Bye bye ********")
            break
    except Exception as e:
        print("error occured",e)
