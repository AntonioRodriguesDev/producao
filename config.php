<?php
$dbHost = '10.0.2.111';
$dbUsername = 'metalbi';
$dbPassword = 'metalbi';
$dbName = 'metalsinos';

$conexao = new mysqli($dbHost,$dbUsername,$dbPassword,$dbName);

if($conexao->connect_errno)
{
    echo "erro";
}
else
{
    echo "conexão feita com sucesso"
}
?>

