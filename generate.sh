#!/bin/bash
name=$1
liczba=100
if [ $name ]; then echo "generuje $liczba hasel w pliku $name ."; else echo "generuje $liczba hasel w pliku password ."; name=password.dat; fi
echo "" > $name
for i in {1..1000}
do
   str=$(cat /dev/urandom | tr -dc '_[:alnum:]' | head -c${1:-$(( ( RANDOM % 10 )  + 5 ))})
   echo  "$str" >> $name

done
