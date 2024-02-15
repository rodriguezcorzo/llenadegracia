create database llenadegracia;

use llenadegracia;

create table Personas(
	id_persona bigint primary key,
    nombre text(30) not null,
    apellido text(30) not null,
    correo text(100) not null,
    celular bigint not null,
    direccion text(100) not null,
    profesion text null
);

create table Usuarios(
	id_usuario bigint primary key,
    clave text(150) not null,
    id_persona bigint,
    constraint Usuarios foreign key (id_persona) references Personas (id_persona)
);

create table Eventos(
	id_evento int primary key auto_increment,
    titulo text(30) not null,
    descripcion text(500) not null,
    fecha datetime,
    imagen longblob,
    id_usuario bigint,
    constraint Eventos foreign key (id_usuario) references Usuarios (id_usuario)
);

create table Inscripciones(
	id_inscripcion int primary key auto_increment,
    fecha datetime,
    id_evento int,
    id_usuario bigint,
    constraint Inscripciones_eventos foreign key (id_evento) references Eventos (id_evento),
    constraint Inscripciones_usuarios foreign key (id_usuario) references Usuarios (id_usuario)
);

create table Donaciones(
	id_donacion int primary key auto_increment,
    descripcion text(500) not null,
    fecha datetime,
    id_persona bigint,
    constraint Donaciones foreign key (id_persona) references Personas (id_persona)
);