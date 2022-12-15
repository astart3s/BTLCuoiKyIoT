from time import sleep
import ObjDetectAndCount
import requests

countObject = [0, 0, 0]
IDObject = ["bottle", "chair", "tvmonitor"]

def main():
    while True:
        ObjDetectAndCount.mainFuct(countObject)
        for i in range(3):
            if countObject[i] > 0:
                requests.get(url="https://api.thingspeak.com/update?api_key=E5I93OJ6DDRFG1MK&field"
                                 + str(i + 2) + "=" + str(countObject[i]))
                print(IDObject[i], end=": ")
                print(str(countObject[i]))
                print("Uploaded data to Thingspeak")

        # upload data for each 20 second + 5 second recognizing
        sleep(20)

if __name__ == "__main__":
    main()
