CREATE DATABASE IF NOT EXISTS Kravit;

USE Kravit;

CREATE TABLE IF NOT EXISTS Cuentas(
    dni_cuenta int(10) auto_increment not null,
    Plataforma varchar(40) NOT NULL,
    Contraseña varchar(100) NOT NULL,

    CONSTRAINT pk_Cuenta PRIMARY KEY (dni_cuenta)
);