#!/bin/bash
i=1
echo -n "please enter number 1]:"
read num
echo "\$num = " $num
max=$num
min=$num
i=`expr $i + 1`	

while [ $i -le 10 ]
do
echo -n "please enter number $i]:" 
read num1
if [ $num1 -gt $max ]
then
	max=$num1
fi
if [ $num1 -lt $min ]
then
	min=$num1
fi

i=`expr $i + 1`
done
echo $max
echo $min




