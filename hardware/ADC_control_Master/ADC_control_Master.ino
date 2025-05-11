#include <SPI.h>
#include <string.h>

#define DRAWER_B_IR 7
#define DRAWER_A_IR 6
#define IR 5
#define SLAVE_A 37
#define SLAVE_B 30

String command = "";
int drawer;
int currentState;
void setup() {
  Serial.begin(19200);
  SPI.begin();               // Begin SPI as Master
  pinMode(SLAVE_A, OUTPUT);  // Set SS pin as output
  pinMode(SLAVE_B, OUTPUT);
  digitalWrite(SLAVE_A, HIGH);
  digitalWrite(SLAVE_B, HIGH);

  // PIR SENSORS INIT
  pinMode(DRAWER_A_IR, INPUT);
  pinMode(DRAWER_B_IR, INPUT);
  pinMode(IR, INPUT);
}

void loop() {

  //PIR Variables
  int DA_STATUS = digitalRead(DRAWER_A_IR);
  int DB_STATUS = digitalRead(DRAWER_B_IR);



  if (Serial.available()) {
    Serial.print("Drawer A status: ");
    Serial.println(DA_STATUS);
    Serial.print("Drawer B status: ");
    Serial.println(DB_STATUS);
    byte action = 0x00;
    command = Serial.readStringUntil('\n');
    command.trim();
    char selectedDrawer = command[command.length() - 1];
    command = command.substring(0, command.length() - 1);
    int slot = String(command[command.length() - 1]).toInt();
    action |= slot;
    command = command.substring(0, command.length() - 1);

    if (selectedDrawer == 'A') {
      drawer = SLAVE_A;
      currentState = DA_STATUS;
    } else if (selectedDrawer == 'B') {
      drawer = SLAVE_B;
      currentState = DB_STATUS;
    }

    if (command == "open" & currentState == 0) {
      action |= 0xA0;
      digitalWrite(drawer, LOW);             // Select the Slave
      byte response = SPI.transfer(action);  // Send byte to Slave
      digitalWrite(drawer, HIGH);            // Deselect the Slave

      Serial.print("command: " + command + " slot: " + slot + " drawer: " + String(selectedDrawer) + "\n");

      // 1 second delay
    } else if (command == "close") {
      digitalWrite(drawer, LOW);
      switch (currentState == 0) {
      }
      // Select the Slave
      byte response = SPI.transfer(action);  // Send byte to Slave
      digitalWrite(drawer, HIGH);            // Deselect the Slave

      Serial.print("command: " + command + " slot: " + slot + " drawer: " + String(selectedDrawer) + "\n");
      // 1 second delay
    }
  }
}


// #include <SPI.h>

// void setup() {
//   Serial.begin(9600);
//   SPI.begin();            // Begin SPI as Master
//   pinMode(22, OUTPUT);    // Set SS pin as output
// }

// void loop() {
//   digitalWrite(22, LOW);         // Select the Slave
//   byte response = SPI.transfer('B');  // Send byte to Slave
//   digitalWrite(22, HIGH);        // Deselect the Slave

//   Serial.print("Sent: H, Received: ");
//   Serial.println(response);

//   delay(1000); // 1 second delay
// }
