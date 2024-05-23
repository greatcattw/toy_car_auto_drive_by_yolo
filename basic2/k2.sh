#!/bin/bash
sudo chmod a+rw /dev/ttyUSB0
delay1=0.5
echo -ne "Z" > /dev/ttyUSB0
cmd="0"
while [ ! "$cmd" == "q"  ];
do
  read -p "cmd:" cmd
  echo ${cmd}

  if [ "$cmd" == "1" ]; then
    echo -ne "H" > /dev/ttyUSB0  && sleep $delay1 && echo -ne "Z" > /dev/ttyUSB0
  fi

  if [ "$cmd" == "2" ]; then
    echo -ne "A" > /dev/ttyUSB0 && sleep $delay1 && echo -ne "Z" > /dev/ttyUSB0
  fi
  
  if [ "$cmd" == "g" ]; then
    echo -ne "A" > /dev/ttyUSB0 
  fi

  if [ "$cmd" == "5" ]; then
    echo -ne "Z" > /dev/ttyUSB0 
  fi


  if [ "$cmd" == "3" ]; then
    echo -ne "B" > /dev/ttyUSB0 && sleep $delay1 && echo -ne "Z" > /dev/ttyUSB0
  fi

  if [ "$cmd" == "8" ]; then
    echo -ne "E" > /dev/ttyUSB0 && sleep $delay1 && echo -ne "Z" > /dev/ttyUSB0
  fi
  if [ "$cmd" == "b" ]; then
    echo -ne "E" > /dev/ttyUSB0 && sleep $delay1 && echo -ne "Z" > /dev/ttyUSB0
  fi



  if [ "$cmd" == "4" ]; then
    echo -ne "G" > /dev/ttyUSB0 && sleep $delay1 && echo -ne "Z" > /dev/ttyUSB0
  fi
  if [ "$cmd" == "l" ]; then
    echo -ne "G" > /dev/ttyUSB0 && sleep $delay1 && echo -ne "Z" > /dev/ttyUSB0
  fi

  if [ "$cmd" == "6" ]; then
    echo -ne "C" > /dev/ttyUSB0 && sleep $delay1 && echo -ne "Z" > /dev/ttyUSB0
  fi
  if [ "$cmd" == "r" ]; then
    echo -ne "C" > /dev/ttyUSB0 && sleep $delay1 && echo -ne "Z" > /dev/ttyUSB0
  fi



  if [ "$cmd" == "y" ]; then
    echo -ne "Y" > /dev/ttyUSB0
  fi


  ##sleep 1
  ##echo -ne "Z" > /dev/ttyUSB0
done
