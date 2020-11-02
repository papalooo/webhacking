
#문제 
# <?php
#   include "../../config.php";
#   if($_GET['view-source'] == 1){ view_source(); }
#   if(!$_COOKIE['user_lv']){
#     SetCookie("user_lv","1",time()+86400*30,"/challenge/web-01/");
#     echo("<meta http-equiv=refresh content=0>");
#   }
# ?>
# <html>
# <head>
# <title>Challenge 1</title>
# </head>
# <body bgcolor=black>
# <center>
# <br><br><br><br><br>
# <font color=white>
# ---------------------<br>
# <?php
#   if(!is_numeric($_COOKIE['user_lv'])) $_COOKIE['user_lv']=1;
#   if($_COOKIE['user_lv']>=6) $_COOKIE['user_lv']=1;
#   if($_COOKIE['user_lv']>5) solve(1);
#   echo "<br>level : {$_COOKIE['user_lv']}";
# ?>
# <br>
# <a href=./?view-source=1>view-source</a>
# </body>
# </html>


# 21 ~ 24 번 줄을 보면
# 쿠키 값을 5 이상으로 수정했을 때
# 문제가 풀리는 것을 알 수 있다.

# 풀이 : user_lv 쿠키값을 5 보다 크게 변경