# Fairplay MP-69D Decoder Scripts

The code in this repository is used to translate the raw electronic signal data from the [FairPlay MP-69D](https://nesc-timekeeping.fandom.com/wiki/Fair-Play_MP-69) into meaningful serial data that can be used in other applications. For example, an Arduino Uno receives the raw electronic signals from the Fairplay controller, turns those raw signals into serial data which it then sends out over USB to a computer running the `serialDecoder.py` Python script, which then integrates the live scoreboard data into some other software application i.e. video streaming/live graphics. 

This code was originally intended to be used in conjunction with a Raspberry Pi to generate live graphic overlays for sports game video streams. You can see a demo video of a hardware prototype running this code [here](https://www.youtube.com/watch?v=JgkRyoUVtak).

## Code Overview

-  `ArduinoMP69Translator.ino`: This is an Arduino sketch that takes as input the two data lines from the Fair-Play MP69D and outputs the raw bit stream coming from the MP-69D over USB serial. The Fairplay MP-69D has two outputs, a SCOREBOARD output and a TIMERS output. Both of these are 1/4" jacks on the back of the device. The setup uses a AM26LS33 Quad Differential Receiver Chip from Texas Instruments. The SCOREBOARD and TIMERS signals go into two separate inputs on the AM26LS33 chip and the output from the TIMERS signal is brought into pin 2 on the Arduino Uno and the SCOREBOARD output is brought into pin 3. The sketch outputs a string of zeroes and ones that is grouped into fours, delimited by vertical bars. Here is an example string: 
    ```
    |0000|0000|0000|0000|1101|0101|0001|
    ``` 

- `serialDecoder.py`: This Python script takes as input the serial string from the Arduino translator sketch and parses it into a data structure that maps sport statistic codes to their corresponding values. You can set the serial port by changing the argument to the Serial() object at the top of the file and you can edit the sport setting by changing the argument to the `buildScoreModel()` function. 
