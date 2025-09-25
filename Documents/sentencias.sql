CREATE TABLE IF NOT EXISTS carrera (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

INSERT INTO carrera (descripcion) VALUES
('Ingenieria en Sistemas de Informacion'),
('Licenciatura en Sistemas de Informacion'),
('Tecnicatura en Programacion'),
('Tecnicatura en Analisis de Sistemas'),
('Tecnicatura en Redes y Telecomunicaciones');
('Zootecnia'),
('Veterinaria'),
('Medicina'),
('Psicologia'),
('Derecho');