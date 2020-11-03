

# 문제
# <?php
# include "../../config.php";
# if($_GET['view_source']) view_source();
# if(!$_COOKIE['user']){
#   $val_id="guest";
#   $val_pw="123qwe";
#   for($i=0;$i<20;$i++){
#     $val_id=base64_encode($val_id);
#     $val_pw=base64_encode($val_pw);
#   }
#   $val_id=str_replace("1","!",$val_id);
#   $val_id=str_replace("2","@",$val_id);
#   $val_id=str_replace("3","$",$val_id);
#   $val_id=str_replace("4","^",$val_id);
#   $val_id=str_replace("5","&",$val_id);
#   $val_id=str_replace("6","*",$val_id);
#   $val_id=str_replace("7","(",$val_id);
#   $val_id=str_replace("8",")",$val_id);

#   $val_pw=str_replace("1","!",$val_pw);
#   $val_pw=str_replace("2","@",$val_pw);
#   $val_pw=str_replace("3","$",$val_pw);
#   $val_pw=str_replace("4","^",$val_pw);
#   $val_pw=str_replace("5","&",$val_pw);
#   $val_pw=str_replace("6","*",$val_pw);
#   $val_pw=str_replace("7","(",$val_pw);
#   $val_pw=str_replace("8",")",$val_pw);

#   Setcookie("user",$val_id,time()+86400,"/challenge/web-06/");
#   Setcookie("password",$val_pw,time()+86400,"/challenge/web-06/");
#   echo("<meta http-equiv=refresh content=0>");
#   exit;
# }
# ?>
# <html>
# <head>
# <title>Challenge 6</title>
# <style type="text/css">
# body { background:black; color:white; font-size:10pt; }
# </style>
# </head>
# <body>
# <?php
# $decode_id=$_COOKIE['user'];
# $decode_pw=$_COOKIE['password'];

# $decode_id=str_replace("!","1",$decode_id);
# $decode_id=str_replace("@","2",$decode_id);
# $decode_id=str_replace("$","3",$decode_id);
# $decode_id=str_replace("^","4",$decode_id);
# $decode_id=str_replace("&","5",$decode_id);
# $decode_id=str_replace("*","6",$decode_id);
# $decode_id=str_replace("(","7",$decode_id);
# $decode_id=str_replace(")","8",$decode_id);

# $decode_pw=str_replace("!","1",$decode_pw);
# $decode_pw=str_replace("@","2",$decode_pw);
# $decode_pw=str_replace("$","3",$decode_pw);
# $decode_pw=str_replace("^","4",$decode_pw);
# $decode_pw=str_replace("&","5",$decode_pw);
# $decode_pw=str_replace("*","6",$decode_pw);
# $decode_pw=str_replace("(","7",$decode_pw);
# $decode_pw=str_replace(")","8",$decode_pw);

# for($i=0;$i<20;$i++){
#   $decode_id=base64_decode($decode_id);
#   $decode_pw=base64_decode($decode_pw);
# }

# echo("<hr><a href=./?view_source=1 style=color:yellow;>view-source</a><br><br>");
# echo("ID : $decode_id<br>PW : $decode_pw<hr>");

# if($decode_id=="admin" && $decode_pw=="nimda"){
#   solve(6);
# }
# ?>
# </body>
# </html>


# 해설

# 14 ~ 30 번 줄과 68 ~ 77 번 줄을보면

# admin을 20번 인코딩, 디코딩 한 후
# user 쿠키 값으로 설정한 후

# nimda를 20번 인코딩, 디코딩 한 후
# password 쿠키 값으로 설정한 후 새로고침 하면 
# 문제가 풀린다


# 풀이
import base64

str1 = 'admin' # nimda 로 변경후 한번 더 실행

i = 0

while i < 20:
  i+=1
  str1 = str1.encode('utf-8')
  str1 = base64.b64encode(str1)
  str1 = str1.decode('utf-8')

str1 = str1.replace("1","!")
str1 = str1.replace("2","@")
str1 = str1.replace("3","$")
str1 = str1.replace("4","^")
str1 = str1.replace("5","&")
str1 = str1.replace("6","*")
str1 = str1.replace("7","(")
str1 = str1.replace("8",")")


print(str1)