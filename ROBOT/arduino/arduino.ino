const int Echo1Pin = 2;
const int Trig1Pin = 3;
const int Echo2Pin = 4;
const int Trig2Pin = 5;
const int Echo3Pin = 6;
const int Trig3Pin = 7;

float distance;
void setup()
{   // 初始化串口通信及连接SR04的引脚
        Serial.begin(9600);
        pinMode(Trig1Pin, OUTPUT);
    // 要检测引脚上输入的脉冲宽度，需要先设置为输入状态
        pinMode(Echo1Pin, INPUT);
        pinMode(Trig2Pin, OUTPUT);
    // 要检测引脚上输入的脉冲宽度，需要先设置为输入状态
        pinMode(Echo2Pin, INPUT);
        pinMode(Trig3Pin, OUTPUT);
    // 要检测引脚上输入的脉冲宽度，需要先设置为输入状态
        pinMode(Echo3Pin, INPUT);
        //Serial.println("Ultrasonic sensor:");
}
float detectdistance(int num){
     if(num==1){
       // 产生一个10us的高脉冲去触发TrigPin
        digitalWrite(Trig1Pin, LOW);
        delayMicroseconds(2);
        digitalWrite(Trig1Pin, HIGH);
        delayMicroseconds(10);
        digitalWrite(Trig1Pin, LOW);
    // 检测脉冲宽度，并计算出距离
        distance = pulseIn(Echo1Pin, HIGH) / 58.00;
     }
     if(num==2){
       // 产生一个10us的高脉冲去触发TrigPin
        digitalWrite(Trig2Pin, LOW);
        delayMicroseconds(2);
        digitalWrite(Trig2Pin, HIGH);
        delayMicroseconds(10);
        digitalWrite(Trig2Pin, LOW);
    // 检测脉冲宽度，并计算出距离
        distance = pulseIn(Echo2Pin, HIGH) / 58.00;
     }
     if(num==3){
       // 产生一个10us的高脉冲去触发TrigPin
        digitalWrite(Trig3Pin, LOW);
        delayMicroseconds(2);
        digitalWrite(Trig3Pin, HIGH);
        delayMicroseconds(10);
        digitalWrite(Trig3Pin, LOW);
    // 检测脉冲宽度，并计算出距离
        distance = pulseIn(Echo3Pin, HIGH) / 58.00;
     }
     return distance; 
}
void loop()
{
        int val = Serial.read();
        if(val >0){
           distance=detectdistance(val-48); //assical 1 is 49, so we muste munuls 48
           Serial.print(distance);
           //
           //Serial.print("cm");
           Serial.println();
        }
        //delay(1000);
}
