<?php
require_once "./phpQuery-onefile.php";
header("Content-type: text/html; charset=utf-8");
$html = array(
    file_get_contents("https://transit.yahoo.co.jp/traininfo/area/2/"),
    file_get_contents("https://transit.yahoo.co.jp/traininfo/area/3/"),
    file_get_contents("https://transit.yahoo.co.jp/traininfo/area/4/"),
    file_get_contents("https://transit.yahoo.co.jp/traininfo/area/5/"),
    file_get_contents("https://transit.yahoo.co.jp/traininfo/area/6/"),
    file_get_contents("https://transit.yahoo.co.jp/traininfo/area/8/"),
    file_get_contents("https://transit.yahoo.co.jp/traininfo/area/9/"),
    file_get_contents("https://transit.yahoo.co.jp/traininfo/area/7/"),
);
$aria = array("Hokaido", "Tohoku", "Kanto", "Chubu", "Kinki", "Chugoku", "Shikoku", "Kyushu");
$date = date("Y-m-d,H:i:s(TP)\n");
$result = array();
file_put_contents ("./log.txt" ,$date,FILE_APPEND);
for ($i = 0; $i <= 7; $i++) {
    $doc = phpQuery::newDocument($html[$i]);
    $trouble_line = str_replace("\n",",",$doc["#mdStatusTroubleLine div table tr td a"]->text());
    $result[$aria[$i]] = $trouble_line;
    #echo "*",$line[$i],"* \n", $trouble_line,"";
}
echo json_encode($result);
?>