#!/bin/bash
python3 -m pydoc -w func_def

if [ -f 'func_def.html' ]; then
   echo "documentation created successfully"
   echo "----------------------------------"
   echo "file contents"
   cat func_def.html
else
   echo "failed"
fi
