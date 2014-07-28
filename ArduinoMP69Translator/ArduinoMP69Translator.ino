

void setup(){
  pinMode(3,INPUT);
  delay(1500);
}

const int bits_to_read=105;
const int timerBits=56;
volatile int dataBits[bits_to_read+timerBits];
int k=0;

///First bit of the stream to start reading from 
int start_bits=1;

int bit1=0;
int bit2=0;
int bit3=0;
int bit4=0;
int shift=32;

void loop() {
  
  ////Wait for a first high pulse after long quiet period, then start capturing bits
  if(pulseIn(3,HIGH,15000)==0){
    attachInterrupt(1,capture,RISING);
    attachInterrupt(0,captureTimers,RISING);

  }
  


  if(k>=(bits_to_read+timerBits)){
    detachInterrupt(0);
    detachInterrupt(1);

    Serial.begin(19200);

    int j=0;
    for(int i=start_bits;i<bits_to_read+timerBits;i++){ 
      j++;
       Serial.print(dataBits[i]);
       ///Delimit bits in groups of 4 (bytes)
       if(j%4==0){
        Serial.print("|"); 
       }
         
    }
    Serial.print("\n");

    resetValues();

    delay(15);

  }

}



////Checks to see if current bit is high or low (interrupt)
void capture() {
  detachInterrupt(1);
  if(k<bits_to_read){
    //delayMicroseconds(2);
    dataBits[k]=bitRead(PIND,3);
    k++;
  }
  attachInterrupt(1,capture,RISING);
}


void captureTimers() {
  detachInterrupt(0);
  if(k<bits_to_read+timerBits && k>=bits_to_read){
    delayMicroseconds(4);
    dataBits[k]=bitRead(PIND,2);
    k++;
  }
  attachInterrupt(0,captureTimers,RISING);
}


/*
///Takes 4-bit binary number and returns integer decimal equivalent
int BCDconvert(){
  bit1=dataBits[shift+3]*pow(2,0);
  bit2=dataBits[shift+2]*pow(2,1);
  bit3=dataBits[shift+1]*pow(2,2);
  bit4=dataBits[shift]*pow(2,3);
  int total=bit1+bit2+bit3+bit4;
  if(total==15){
    return 0;
  }
  else{
    return total; 
  }

}


*/
void resetValues(){
  bit1=0;
  bit2=0;
  bit3=0;
  bit4=0;
  k=0;
  shift=32;
}




