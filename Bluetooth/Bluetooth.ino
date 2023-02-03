void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);

}

int val = 3;
void loop() {
  Serial.print(12331);
  Serial.print("   ");
  Serial.println("sdf");
  if(Serial.available()){
    val = Serial.read();
    if(val == '1'){
      digitalWrite(13,1);
      Serial.print(12331);
      Serial.println("sdf");
    }
    if(val == '0'){
      digitalWrite(13,0);
    }
  }
}