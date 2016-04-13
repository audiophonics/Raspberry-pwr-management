#!/bin/bash
#Thanks to Hondagx35
#http://www.runeaudio.com/forum/audiophonics-i-sabre-v3-dac-es9023-tcxo-t3377.html#p13106
#http://www.runeaudio.com/forum/audiophonics-i-sabre-v3-dac-es9023-tcxo-t3377-20.html#p13195

PATH=/bin:/usr/bin:/usr/bin/gpio

echo "Audiophonics Shutdown script starting..."
echo "Asserting pins : "
echo "ShutDown : GPIO17=in, Low"
echo "BootOK : GPIO22=out, High"

gpio -g mode 17 in
gpio -g write 17 0
gpio -g mode 22 out
gpio -g write 22 1

while [ 1 ]; do
  if [ "$(/usr/bin/gpio -g read 17)" = "1" ]; then
        echo "ShutDown order received, RaspBerry pi will now enter in standby mode..."
        /var/www/command/rune_shutdown poweroff
        systemctl poweroff
        break
  fi
/bin/sleep 0.25
done

exit 0
