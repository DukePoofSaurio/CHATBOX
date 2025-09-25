CREATE TABLE IF NOT EXISTS carrera (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

INSERT INTO carrera (descripcion) VALUES
('Zootecnia'),
('Veterinaria'),
('Medicina'),
('Psicologia'),
('Derecho');