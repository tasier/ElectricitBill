# !/bin/bash

# 进入python脚本所在目录
cd ../

# 将电费文件提取出来，并以一行一个文件显示
ls degrees | sed 's/ /\n/g' > /tmp/all_degree_files

num_of_files=$(cat /tmp/all_degree_files | wc -l)
# echo ${num_of_files}

# 需要统计几个月的电费情况
month_num=`expr ${num_of_files} - 1`

# 上个月电费度数文件名集合
head -n ${month_num} /tmp/all_degree_files > /tmp/pre_month
# cat /tmp/pre_month

#这个月电费度数文件名集合
tail -n ${month_num} /tmp/all_degree_files > /tmp/current_month
# cat /tmp/current_month

#这个月电费总额文件名集合
tail -n ${month_num} /tmp/all_degree_files | sed 's/\./fee./g' > /tmp/current_fee
# cat /tmp/current_fee

#获取存储临时参数的文件名称
tmp_params_filename=$1

#1.三个文件合并为一个文件（paste命令）
#2.组装参数
paste /tmp/pre_month /tmp/current_month /tmp/current_fee | awk '{printf "degrees/%s degrees/%s bills/%s\n",$1,$2,$3 }'  > ${tmp_params_filename} 

#删除临时文件
rm -f /tmp/all_degree_files
rm -f /tmp/pre_month
rm -f /tmp/current_month
rm -f /tmp/current_fee
