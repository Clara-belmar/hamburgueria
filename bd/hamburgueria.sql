create database if not exists bdHamburgueria;
use bdHamburgueria;
create table if not exists cliente(
    id_cliente int primary key auto_increment, 
    nome varchar(50) not null, 
    sobrenome varchar(30) not null,
    telefone varchar(14) not null,
    email varchar(60) not null,
    cpf varchar(14)
); 65ms
create table if not exists fornecedor(
    id_forecedor int primary key auto_increment, 
    nome varchar(50) not null,
    telefone varchar(14) not null,
    email varchar(60) not null,
    registro varchar(14)
); 57ms 