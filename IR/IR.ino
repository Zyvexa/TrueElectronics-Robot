#include <iarduino_IR_RX.h>                      // Подключаем библиотеку для работы с ИК-приёмником
#define IR_PORT A3
iarduino_IR_RX IR(IR_PORT);                            // Объявляем объект IR, с указанием вывода к которому подключён ИК-приёмник


void setup(){
  Serial.begin(9600);                            // Инициируем передачу данных в монитор последовательного порта, на скорости 9600 бит/сек

  IR.begin();                                    // Инициируем работу с ИК-приёмником
}
void loop(){
  if(IR.check()){
    unsigned long data_IR = IR.data;
    // Serial.println(IR.data, HEX);                // Выводим код нажатой кнопки
    Serial.println(data_IR);                // Выводим количество бит в коде
  }
}
unsigned long IR_READER(){
  if(IR.check()){
    // unsigned long data_IR = IR.data;
    // Serial.println(IR.data, HEX);                // Выводим код нажатой кнопки
    // Serial.println(data_IR);                // Выводим количество бит в коде
    return IR.data;
  }
}

#define IR_1 16753245
#define IR_2 16736925
#define IR_3 16769565
#define IR_4 16720605
#define IR_5 16712445
#define IR_6 16761405
#define IR_7 16769055
#define IR_8 16754775
#define IR_9 16748655
#define IR_0 16750695 

#define IR_STAR 16738455
#define IR_LATTICE 16756815

#define IR_UP 16718055
#define IR_DOWN 16730805
#define IR_LEFT 16716015
#define IR_RIGHT 16734885

#define IR_OK 16726215

