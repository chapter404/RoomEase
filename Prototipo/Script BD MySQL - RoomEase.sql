CREATE DATABASE RoomEase;
USE RoomEase;

CREATE TABLE Cliente (
    idCliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    rut INT NOT NULL,
    dv CHAR(1) NOT NULL,
    telefono INT,
    correo VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    UNIQUE (rut, dv)
);

CREATE TABLE Administrador (
    idAdministrador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Reserva (
    idReserva INT AUTO_INCREMENT PRIMARY KEY,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    estado ENUM('pendiente', 'confirmada', 'cancelada') NOT NULL,
    clienteId INT NOT NULL,
    FOREIGN KEY (clienteId) REFERENCES Cliente(idCliente) ON DELETE CASCADE
);

CREATE TABLE Habitacion (
    idHabitacion INT AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(10) NOT NULL UNIQUE,
    tipo VARCHAR(100) NOT NULL,
    precio INT NOT NULL,
    estado ENUM('disponible', 'ocupada', 'mantenimiento') NOT NULL,
    descripcion TEXT
);

CREATE TABLE FotoHabitacion (
    idFoto INT AUTO_INCREMENT PRIMARY KEY,
    habitacionId INT NOT NULL,
    urlFoto VARCHAR(255) NOT NULL,
    descripcionFoto VARCHAR(255),
    orden INT,
    FOREIGN KEY (habitacionId) REFERENCES Habitacion(idHabitacion) ON DELETE CASCADE
);

CREATE TABLE Pago (
    idPago INT AUTO_INCREMENT PRIMARY KEY,
    fechaPago DATE NOT NULL,
    monto INT NOT NULL,
    estado ENUM('pendiente', 'completado', 'fallido') NOT NULL,
    reservaId INT NOT NULL,
    FOREIGN KEY (reservaId) REFERENCES Reserva(idReserva) ON DELETE CASCADE
);

CREATE TABLE Reserva_Habitacion (
    reservaId INT NOT NULL,
    habitacionId INT NOT NULL,
    PRIMARY KEY (reservaId, habitacionId),
    FOREIGN KEY (reservaId) REFERENCES Reserva(idReserva) ON DELETE CASCADE,
    FOREIGN KEY (habitacionId) REFERENCES Habitacion(idHabitacion) ON DELETE CASCADE
);