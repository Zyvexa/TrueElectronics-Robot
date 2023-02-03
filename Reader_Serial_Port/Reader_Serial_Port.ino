// Пример отправки и приёма структуры через Serial
// ПРИЁМНИК
// Ардуины соединены так:
// приёмник D10 -> отправитель D11
// #include < SoftwareSerial.h>
// SoftwareSerial mySerial(10, 11); // RX, TX
// структура для приёма
//
// создаём саму структуру

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  // mySerial.begin(4000);
}

void loop() {

  SerialRead();
}


// 82 84 71 


long t = 0;
int flag = 0;
int count = 0;
int arr[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

void SerialRead() {

  if (Serial.available() > 0) {
    t = Serial.read();
    flag = 1;
  }
  if (flag == 1) {
    if (t >= 32) {
      arr[count] = t;
      count++;
    } else {
      if (arr[0] != 0) {
        for (int i = 0; i < 10; i++) {
          Serial.print(arr[i]);
          Serial.print(" ");
          arr[i] = 0;
        }
        Serial.println("");

        count = 0;
      }
    }
    flag = 0;
  }
}
