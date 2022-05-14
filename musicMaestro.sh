#!/bin/bash
echo "Música, maestro!"
FILE=$1
cd music
lilypond $FILE.ly
timidity -Ow -o $FILE.wav $FILE.midi
ffmpeg -y -i $FILE.wav -codec:a libmp3lame -qscale:a 2 $FILE.mp3
# One of Linux play commands
ffplay -autoexit -showmode 1 $FILE.mp3