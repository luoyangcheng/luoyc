#!/bin/bash
#输出
echo "Hello World !"

#字符串
myname="luoyc"
echo $myname

your_name='runoob'
str="Hello, I know you are \"$your_name\"! \n"
echo -e $str

#计算加减乘除
a=10
b=20
echo $(($a+$b))

#判断文件是否存在
#-f:判断文件是否存在存在
#-d:判断目录是否存在
#-r:判断是否有读的权限
#-w:判断是否有写的权限
#-x:判断是否有执行权限
filename=/home/zhangsan
test -f $filename && echo 'exist' || 'not exist'

#判断逻辑
[ "$a" == "$b" ]&&echo 'yes' || echo 'no'
[ '12' == '10' ]&&echo 'yes' || echo 'no'

#if判断
filename=/home/asdf
if[ test -f $filename ];then
  echo 'aa'
elif
  echo 'bb'
else
  echo 'cc'
fi

#case in 方式例子
echo '输入一个值：'
read number
case $number in
1)
  echo '1';;
2)
  echo '2';;
*)
  echo '错误';;
esac

#for循环
for((i=1;i<=10;i++));do
  echo $i
done;

#函数定义
function print(){
  echo 'luoyc'
}
#函数调用
print



exit 0 #退出