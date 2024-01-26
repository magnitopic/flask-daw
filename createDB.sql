CREATE DATABASE IF NOT EXISTS 'db_flask';

USE db_flask;

# nombre, artista, genero, precio, discografica, fecha
CREATE TABLE IF NOT EXISTS 'discos' (
	'id' INT AUTO_INCREMENT PRIMARY KEY,
	'nombre' VARCHAR(255),
	'artista' VARCHAR(255),
	'genero' VARCHAR(255),
	'precio' INT,
	'discografica' VARCHAR(255),
	'fecha' DATE
);

CREATE TABLE pedidos (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(255),
	email VARCHAR(255),
	direccion VARCHAR(255),
	tarjeta VARCHAR(255),
	telefono VARCHAR(255),
	caducidad VARCHAR(255),
	cvv INT,
	ip VARCHAR(255),
	user_agent VARCHAR(1200)
);
CREATE TABLE productopedido (
	id INT AUTO_INCREMENT PRIMARY KEY,
	id_producto INT,
	id_pedido INT,
	cantidad_producto INT,
	FOREIGN KEY (id_producto) REFERENCES discos(id),
	FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
);