float voltage1, voltage2;
void setup() {
  pinMode(5, OUTPUT);
}

void loop() {
  if (digitalRead(5) == HIGH){
      _delay_us(100);
      if(digitalRead(5) == HIGH){
        Serial.begin(9600); //fastest frequency
        Serial.println("START SAMPLING");
        while(1){
            voltage1 = (5.0 * analogRead(A0))/1024.0;
            voltage2 = (5.0 * analogRead(A1))/1024.0;
            Serial.print("CH1 ");
            Serial.print(voltage1);
            Serial.print(" CH2 ");
            Serial.print(voltage2);
            Serial.print("\n");
            _delay_us(40);
            if(digitalRead(5) == LOW){
                _delay_us(100);
                if(digitalRead(5) == LOW){
                    Serial.println("\nSTOP SAMPLING");
                    break;
                }
            }                
        }
    }
}
}
