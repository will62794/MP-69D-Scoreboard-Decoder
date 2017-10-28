# Fairplay MP-69D Decoder Scripts

The code files in this repository work together to translate the raw electronic signal data from the MP-69D into meaningful serial data that can be used in other applications. For example, the Arduino Uno receives the raw electronic signals from the Fairplay controller, turns those raw signals into serial data which it then sends out over USB to a computer running the "serialDecoder.py" Python script, which then integrates the live scoreboard data into some other software application i.e. video streaming/live graphics. This hardware was originally going to be used in conjunction with a Raspberry Pi to generate live graphic overlays for sports game video streams.


#### ArduinoMP69Translator.ino
This is an Arduino sketch that takes as input the two data lines from the Fair-Play MP69D and outputs the raw bit stream coming from the MP-69D over USB serial. The Fairplay MP-69D has two outputs, a SCOREBOARD output and a TIMERS output. Both of these are 1/4" jacks on the back of the device. The setup uses a AM26LS33 Quad Differential Receiver Chip from Texas Instruments. The SCOREBOARD and TIMERS signals go into two separate inputs on the AM26LS33 chip and the output from the TIMERS signal is brought into pin 2 on the Arduino Uno and the SCOREBOARD output is brought into pin 3. The sketch outputs a string of zeroes and ones that is grouped into fours, delimited by vertical bars. An example string(without the quotes): "|0000|0000|0000|0000|1101|0101|0001|”. 

#### serialDecoder.py
This Python script takes as input the serial string from the Arduino translator sketch and parses it into a data structure that maps sport statistic codes to their corresponding values. You can set the serial port by changing the argument to the Serial() object at the top of the file and you can edit the sport setting by changing the argument to the buildScoreModel() function. 
