#include "ESP8266WiFi.h"

void prinScanResult()
{
  //  Serial.printf("%d network(s) found\n", networksFound);
  for (int i = 0; i < 3; i++)
  {
    Serial.print(WiFi.SSID(i).c_str());
    Serial.print(": ");
    Serial.println(WiFi.RSSI(i));
    //    Serial.printf("%d: %s, Ch:%d (%ddBm) %s\n", i + 1, WiFi.SSID(i).c_str(), WiFi.channel(i), WiFi.RSSI(i), WiFi.encryptionType(i) == ENC_TYPE_NONE ? "open" : "");
  }
}


void setup()
{
  Serial.begin(115200);
  Serial.println();

  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  //  WiFi.scanNetworksAsync(prinScanResult);
}


void loop() {
  int nets = WiFi.scanNetworks();
  for (int i = 0; i < nets; i++)
  {
    Serial.print(WiFi.SSID(i).c_str());
    Serial.print(": ");
    Serial.println(WiFi.RSSI(i));
    Serial.println("---------------");
  }
//  Serial.println(WiFi.scanNetworks());

}
