#!/bin/bash

FILE=/usr/local/lib/antlr-4.10.1-complete.jar

if [ -f "$FILE" ]; then
    echo "ANTLR4 jar file already exists."
else
    cd /usr/local/lib
    curl -O https://www.antlr.org/download/antlr-4.10.1-complete.jar
fi

export CLASSPATH=".:/usr/local/lib/antlr-4.10.1-complete.jar:$CLASSPATH"

alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.10.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.10.1-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'

echo "Environment set up correctly."
