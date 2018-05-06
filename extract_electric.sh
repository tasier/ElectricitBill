# !/bin/bash

python_params=$1

while read -r line
do
  #提取电费
  #python Electric.py $line |  awk '/1号屋/ && /\./ {print $12} '
  #提取度数
  python Electric.py $line | awk '/1号屋/ && !/\./ {print $5}'
done < ${python_params}
