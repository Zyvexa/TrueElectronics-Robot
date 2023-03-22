// Libraries
#include <ESP8266WiFi.h>

#define SPACE   " "
#define ME      "robot_1"

#define PORT    80
#define SSId    "babay"
#define PASS    "89197275518"

#define HOST    "31.10.97.79"

#define T_BASE  250

/*

  SSId    "default";
  PASS    "g1s2o3m4";

  SSId    "Galaxy";
  PASS    "11111111";

  SSId    "robotics";
  PASS    "17122018";

  SSId    "babay";
  PASS    "89197275518";
*/

int start_;

byte battery = 100;
byte i;

int sensor1 = 1020;
int sensor2 = 10;
int sensor3 = 800;
int sensor4 = 1010;

bool mode = false; // режим false - шлём данные. ture - запрашиваем

WiFiClient client;

void setup() {
  Serial.begin(115200);
  WiFi.begin(SSId, PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {

    delay(T_BASE);
  conn();


  if (mode) {

    Serial.println("> " + Receive());

  }

  else if (!mode) {
    send_all();
  }

  mode = !mode;

}

void conn() //reconnection to server
{
  if (client.connect(HOST, PORT)) {}
  else {
    Serial.println("Connection to server failed");
  }
}

String Receive() // receiving data
{
  client.print(String("[receive] ") + ME);
  String response = client.readStringUntil('\n');
  return response;

}

void send_all() // отправка пакета данных с датчиков
{
  i++;
  if (i >= 2) {
    battery --;
    i = 0;
  }

  sensor1 = random(0, 1024);
  sensor2 = random(0, 1024);
  sensor3 = random(0, 1024);
  sensor4 = random(0, 1024);

  client.print(String("[data] ") + ME + SPACE + battery + SPACE + sensor1 + SPACE + sensor2 + SPACE + sensor3 + SPACE + sensor4);

}
