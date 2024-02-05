create database llenadegracia;

use llenadegracia;

create table Administradores (
	ID_admin bigint primary key not null,
    Nombre varchar(30) not null,
    Apellido varchar(30) not null,
	Correo varchar(100) not null,
    Celular bigint not null,
    Clave varchar(150) not null
);

create table Usuarios (
	ID_usuario bigint primary key not null,
    Nombre varchar(50) not null,
    Apellido varchar(50) not null,
    Correo varchar(100) not null,
    Celular bigint not null,
    Profesion varchar(30) null
);

create table Eventos (
	ID_evento int primary key auto_increment,
    Titulo varchar(50) not null,
    Descripcion varchar(500) not null,
    Fecha date not null,
    Imagen blob null,
    Costo int null,
    ID_admin bigint,
    constraint Eventos foreign key(ID_admin) references Administradores (ID_admin)
);

create table Inscripciones (
	ID_inscripcion int primary key auto_increment,
    ID_evento int,
    ID_usuario bigint,
    fecha_inscripcion date,
    constraint fk_Eventos_Inscripciones foreign key(ID_evento) references Eventos (ID_evento),
    constraint fk_Usuarios_Inscripciones foreign key(ID_usuario) references Usuarios (ID_usuario)
);



-- INSERTANDO ADMIN :V --
insert into administradores (ID_admin, Nombre, Apellido, Correo, Celular, Clave)
values
	(1005176108, "Omar Andrés", "Rodríguez Corzo", "orandres028@gmail.com", 3015133330, 0011);



-- AÑADIENDO VALORES A LA TABLA EVENTOS --
select * from eventos;

insert into eventos (Titulo, Descripcion, Fecha, Imagen, Costo, ID_admin)
values
  ('Concierto de Beneficencia', 'Un evento musical para recaudar fondos', '2023-12-01', NULL, 20, 1005176108),
  ('Exposición de Arte Contemporáneo', 'Descubre las últimas tendencias artísticas', '2023-11-15', NULL, 10, 1005176108),
  ('Conferencia de Desarrollo Personal', 'Charlas inspiradoras y motivadoras', '2023-11-30', NULL, 15, 1005176108);



-- INSERTADOS DATOS DE USUARIOS --
insert into usuarios (ID_usuario, Nombre, Apellido, Correo, Celular, Profesion)
values
	(1001185687, "Javier", "Quiñonez", "javier@gmail.com", 3102665879, "Aprendiz"),
    (2002185687, "María", "Gómez", "maria@gmail.com", 3113365880, "Estudiante"),
    (3003185687, "Carlos", "Pérez", "carlos@gmail.com", 3012709181, "Ingeniero"),
    (4004185687, "Laura", "Hernández", "laura@gmail.com", 3129919090, "Médico"),
    (5005185687, "Pedro", "Martínez", "pedro@gmail.com", 3106213561, "Programador");

    

-- IINSERTANDO DATOS DE INCRIPCIONES --
INSERT INTO Inscripciones (ID_evento, ID_usuario, Fecha_inscripcion)
VALUES
	(1, 1001185687, "2023-11-18"),
    (2, 2002185687, "2023-10-04"),
    (3, 3003185687, "2022-12-24"),
    (1, 4004185687, "2021-07-28"),
    (2, 5005185687, "2019-04-08");