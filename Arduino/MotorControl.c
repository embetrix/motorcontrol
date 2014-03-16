#include <AFMotor.h>
#include <Servo.h> 

//Create x2 dc motor instances #1 and #2 at 64KHz pwm
AF_DCMotor motor1(1, MOTOR12_64KHZ); 
AF_DCMotor motor2(2, MOTOR12_64KHZ); 

//Create servo motor instance
Servo servo;

int startbyte;
int Buffer[3];
int i;
int pos = 0;

void setup() {  
    Serial.begin(9600);
    myservo.attach(9);
    Serial.println("Arduino Motor Control...");
}

void loop() {
    if (Serial.available()>3) {
        
    /* parse the first byte */ 
    startbyte = Serial.read(); 
        
    /* if the startbyte is ('z' = 122) then process with MoveDCMotorMotor */
    if (startbyte == 122) {  
          
        /* get the next tree bytes*/  
        for (i=0;i<3;i++) {  
            Buffer[i] = Serial.read();
        }  
        MoveDCMotorMotor(Buffer[0], Buffer[1], Buffer[2]);   
    }
        
    /* if the startbyte is ('y' = 121) then process with MoveServoMotor */
    if (startbyte == 121) {  
          
        /* get the next tree bytes */ 
        for (i=0;i<3;i++) {  
            Buffer[i] = Serial.read();
        }          
        MoveServoMotor(Buffer[0]); 
         
    }
  }
}


void MoveDCMotorMotor(int direction, int speed1, int speed2){
    motor1.setSpeed(speed1);
    motor2.setSpeed(speed2);  

    motor1.run(direction);
    motor2.run(direction);
}


void MoveServoMotor(int pos){                          
    servo.write(pos);            
}
