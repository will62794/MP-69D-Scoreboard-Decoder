import serial
import time

ser = serial.Serial('/dev/tty.usbmodem1411', 19200, timeout=3)

sport_tables={}

#Maps each sport statistic code to its corresponding byte in the data stream
sport_tables["basketball"]={'VF1': 8, 'VF2': 9,'HF1':10,'HF2':11,'POSS':15,'PRD':17,'VS1':18,'VS2':19,'HS1':20,'HS2':21,'CLKSEC1':22,'CLKSEC2':23,'CLKMIN1':24,'CLKMIN2':25,'SHOT1':32,'SHOT2':33}

sport_tables["football"]={'HTO':4,'VTO':5,'BALLON1': 6,'BALLON2': 7,'POSS':10,'DOWN':14,'QTR':15,'VS1':16,'VS2':17,'HS1':18,'HS2':19,'CLKSEC1':20,'CLKSEC2':21,'CLKMIN1':22,'CLKMIN2':23,'TIMER1':26,'TIMER2':27}

sport_tables["hockey"]={'PRD':17,'VS1':18,'VS2':19,'HS1':20,'HS2':21,'CLKSEC1':22,'CLKSEC2':23,'CLKMIN1':24,'CLKMIN2':25,'TIMER1':26,'TIMER2':27}

sport_tables["wrestling"]={'MATCHWEIGHT2':5,'MATCHWEIGHT1':7,'PRD':17,'CLKSEC1':22,'CLKSEC2':23,'CLKMIN1':24, 'CLKMIN2':25,'VS1':18,'VS2':19,'HS1':20,'HS2':21}

sport_tables["soccer"]={'PRD':15,'VS1':16,'VS2':17,'HS1':18,'HS2':19,'CLKSEC1':20,'CLKSEC2':21,'CLKMIN1':22,'CLKMIN2':23}

sport_tables["volleyball"]={'GAME':5,'PRD':17,'VS1':18,'VS2':19,'HS1':20,'HS2':21,'CLKSEC1':22,'CLKSEC2':23,'CLKMIN1':24,'CLKMIN2':25,'TIMER1':26,'TIMER2':27}





#converts the groups of bits into list of decimal values
def bitsToBytes(bitString):
	bytes=bitString.split("|")[:-1]
	try:
		bytes=[int(b,2) for b in bytes]
	except:
		pass
	return bytes

#takes the list of decimal values and creates a dictionary mapping each stat code to its decimal value
def buildScoreModel(sport,rawBytes):
	bytes=rawBytes
	STATS={}
	for stat_code in sport_tables[sport].keys():
		b=sport_tables[sport][stat_code]
		STATS[stat_code]=bytes[b]
	return STATS


while True:
	dataBits=ser.readline()
	bytes=bitsToBytes(dataBits)
	print bytes
	try:
		STATS=buildScoreModel("basketball",bytes)
		#print STATS
	except:
		pass
	time.sleep(.05)










