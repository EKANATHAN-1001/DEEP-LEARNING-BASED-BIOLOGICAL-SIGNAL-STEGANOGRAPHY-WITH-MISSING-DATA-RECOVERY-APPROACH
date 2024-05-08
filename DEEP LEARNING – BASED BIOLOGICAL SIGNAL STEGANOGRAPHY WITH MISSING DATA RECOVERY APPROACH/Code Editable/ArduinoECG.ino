const int ECG_PIN = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int ecgValue = analogRead(ECG_PIN);
  Serial.println(ecgValue);
  delay(10); 
}
