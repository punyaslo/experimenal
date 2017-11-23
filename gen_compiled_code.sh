#!/bin/bash
python3 -m py_compile sample.py

if [ -d "__pycache__" ]; then
   echo "__pycache__ dir created"
   cd "__pycache__"
   echo "compiled bytecode file is: `ls`"
else
   echo "failed"
fi
