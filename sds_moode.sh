#!/bin/bash
#Volumio version

PATH=/usr/bin:/usr/local/bin

echo "Audiophonics Shutdown script starting..."
echo "Asserting pins : "
echo "ShutDown : GPIO17=in, Low"
echo "BootOK   : GPIO22=out, High"
echo "SoftSD   : GPIO04=out, Low"

gpio -g mode 04 out
gpio -g write 04 0
gpio -g mode 17 in
gpio -g write 17 0
gpio -g mode 22 out
gpio -g write 22 1

while [ 1 ]; do
  if [ "$(gpio -g read 17)" = "1" ]; then
        echo "ShutDown order received, RaspBerry pi will now enter in standby mode..."
        sudo shutdown -h -P now
        break
  fi
  /bin/sleep 0.25
done

exit 0
