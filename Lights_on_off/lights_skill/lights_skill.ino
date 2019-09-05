int inputByte;
int ledPin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
}

void loop() {
  if(Serial.available()>0){
    inputByte = Serial.read();
    if(inputByte == 'H'){
      digitalWrite(ledPin,HIGH);
    }
    if(inputByte == 'L'){
      digitalWrite(ledPin,LOW);
    }
  }

}
