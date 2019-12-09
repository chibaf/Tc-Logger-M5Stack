import serial, sys
import re

strPort = sys.argv[2]   # serial port
ser=serial.Serial(strPort, 115200)
print("connected to: " + ser.portstr)

file=sys.argv[1]  # file name
regex = re.compile('\d+')  # for extracting number from strings
f=open(file,"w+")
while True:
  try:
    line = ser.readline()
    match = regex.findall(line)  # extracting number from strings
    # "match[4]+"."+match[5]" is the first Tc value, ..., "match[22]+"."+match[23]" is the tenth Tc value.
    f1=match[4]+"."+match[5]+", "+match[6]+"."+match[7]+", "+match[8]+"."+match[9]+", "+match[10]+"."+match[11]+", "+match[12]+"."+match[13]+", "+match[14]+"."+match[15]+", "+match[16]+"."+match[17]+", "+match[18]+"."+match[19]+", "+match[20]+"."+match[21]+", "+match[22]+"."+match[23]
    if(match[3]=="0"):
    # match[1] is minutes, match[2] is seconds, match[3] is sub seconds.
      print(match[1]+" "+match[2]+" "+match[3]+": "+f1)
    f.write(f1+"\n")
  except KeyboardInterrupt:
    print 'exiting'
    break
ser.flush()
ser.close()
f.close()
