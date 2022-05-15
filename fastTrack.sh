#!/bin/bash
echo "Música, maestro!"
FILE=$1
# Compile
cd lang
python3 jsbach.py input.jsb Hanoi

# Create masterpiece
cd ../music

n=0
while ! mkdir $FILE$n
do
    n=$((n+1))
done

cd $FILE$n
mv ../../lang/$FILE.ly .
lilypond $FILE.ly
timidity -Ow -o $FILE.wav $FILE.midi
ffmpeg -y -i $FILE.wav -codec:a libmp3lame -qscale:a 2 $FILE.mp3
# One of Linux play commands
ffplay -autoexit -showmode 1 $FILE.mp3