#include <WiFi.h>

#define SECRET_SSID "Wokwi-GUEST" // replace with your WiFi network
name
#define SECRET_PASS "123456gnugnu" // replace with your WiFi password

char ssid[] = SECRET_SSID; // your network SSID (name)
char pass[] = SECRET_PASS; // your network password

WiFiClient client;

void setup()
   {
   Serial.begin(115200); //Initialize serial
   while (!Serial) {
   }
   WiFi.mode(WIFI_STA);
}
void loop()
{
	if(WiFi.status() != WL_CONNECTED)
	{
		Serial.print("Attempting to connect to SSID: ");
		Serial.println(SECRET_SSID);
		while(WiFi.status() != WL_CONNECTED)
		{
			WiFi.begin(ssid, pass); // Connect to WPA/WPA2 network. Change
			this line if using open or WEP network
			Serial.print(".");
			delay(5000);
		}
		Serial.println("\nConnected.");
		
		
		//need send data to server code, but no hardware to test
	}
}