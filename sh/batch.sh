#!/bin/bash

tmp_file="/tmp/params"

# todo 总结xargs命令
echo ${tmp_file} | xargs ./calc_batch_params.sh  

#计算结果一行一个的命令
# echo ${tmp_file} | xargs  ./extract_electric.sh

#如果需要将计算结果放到一行，可以使用下面的命令
echo ${tmp_file} | xargs  ./extract_electric.sh | xargs | sed 's/ /, /g'

# 删除临时文件 
rm -f ${tmp_file}
