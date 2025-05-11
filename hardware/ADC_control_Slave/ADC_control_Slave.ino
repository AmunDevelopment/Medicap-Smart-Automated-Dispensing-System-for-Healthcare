#include <Servo.h>
#include <string.h>
#include <SPI.h>


#define lock 2
int lock_status = 0;

#define Motor_pwm 5
#define Motor_dir 4
#define speed 120
#define close 1
#define open 0


#define servo_pin 3
Servo drw_servo;

#define ledStrip 6

#define limit_switch 7

#define OPEN 0x0A
#define CLOSE 0x0B
#define CLOSE_LEDS 0x0C

int ledSwitch = 0;

int leds[] = { A0, A1, A2, A3, A4, A5 };
volatile byte receivedData;
volatile boolean newData = false;

byte status = CLOSE;
byte command = 0x00;
byte slot_number = 0x00;

void setup() {
  pinMode(lock, OUTPUT);
  pinMode(Motor_dir, OUTPUT);
  pinMode(Motor_pwm, OUTPUT);
  pinMode(ledStrip, OUTPUT);
  pinMode(limit_switch, INPUT);

  for (int i = 0; i < 6; i++) {
    pinMode(leds[i], OUTPUT);
  }

  drw_servo.attach(servo_pin);
  drw_servo.write(40);

  Serial.begin(9600);
  pinMode(MISO, OUTPUT);  // Have to set MISO as output
  SPCR |= _BV(SPE);       // Enable SPI in Slave mode
  SPI.attachInterrupt();  // Enable interrupt on SPI transfer
}

ISR(SPI_STC_vect) {
  receivedData = SPDR;  // Read data from SPI Data Register
  slot_number = receivedData & 0x0F;
  command = (receivedData >> 4) & 0x0F;
  newData = true;
  if (command == OPEN)
    ledSwitch = 1;
  else
    ledSwitch = 0;
}

void loop() {
  heartbeatEffect();
  if (newData) {

    if (command == OPEN) {
      heartbeatEffect();
      digitalWrite(lock, HIGH);
      drw_servo.write(100);
      delay(100);
      analogWrite(Motor_pwm, speed);
      digitalWrite(Motor_dir, open);
      digitalWrite(leds[slot_number], HIGH);
      delay(1000);
      while (digitalRead(limit_switch) == 0) {
        analogWrite(Motor_pwm, speed);
        digitalWrite(Motor_dir, open);
        if (digitalRead(limit_switch) == 1)
          break;
      }
      drw_servo.write(40);
      analogWrite(Motor_pwm, 0);
      digitalWrite(Motor_dir, 0);
      digitalWrite(lock, LOW);
      command = 0x00;
    }


    if (command == CLOSE) {
      digitalWrite(lock, LOW);
      drw_servo.write(100);
      delay(100);
      analogWrite(Motor_pwm, speed - 35);
      digitalWrite(Motor_dir, close);
      digitalWrite(leds[slot_number], LOW);
      delay(1000);
      while (digitalRead(limit_switch) == 0) {
        analogWrite(Motor_pwm, speed - 35);
        digitalWrite(Motor_dir, close);
        if (digitalRead(limit_switch) == 1)
          break;
      }
      drw_servo.write(40);
      analogWrite(ledStrip, 100);
      analogWrite(Motor_pwm, 0);
      digitalWrite(Motor_dir, 0);

      command = 0x00;
      //analogWrite(leds[slot_number], LOW);
    }
    newData = false;

    if (command == CLOSE_LEDS) {
      for (int i = 0; i < 6; i++) {
        digitalWrite(leds[i], LOW);
      }
      ledSwitch = 0;
    }
  }
}



void heartbeatEffect() {
  if (!ledSwitch) {
    digitalWrite(ledStrip, HIGH);
  } else {
    for (int i = 0; i < 2; i++) {  // Simulate the "double beat"
      for (int brightness = 0; brightness <= 255; brightness += 5) {
        analogWrite(ledStrip, brightness);
        delay(8);
      }
      for (int brightness = 255; brightness >= 0; brightness -= 5) {
        analogWrite(ledStrip, brightness);
        delay(8);
      }
      delay(150);  // Short pause between beats
    }
    delay(1000);  // Longer pause between heartbeat cycles
  }
}
