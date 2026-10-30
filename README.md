# Sistema de préstamos BNPHU

Proyecto base en Python con SQLite para gestionar los préstamos de la Biblioteca Nacional
Pedro Henríquez Ureña (BNPHU): usuarios, materiales, ejemplares (copias físicas), préstamos
y devoluciones.

**Autor:** Johan Almanzar de Jesús
**Curso:** 5toC — Politécnico El Ave María
**Docente:** Robinson Sánchez

## Estructura

```
proyecto_base/
├── main.py                  # Conexión + prueba del CRUD, préstamos y reportes
├── requirements.txt         # Dependencias (ninguna externa)
├── .gitignore               # Archivos que Git ignora
├── README.md                # Este archivo
├── sql/
│   ├── esquema.sql          # Tablas, índices y vistas
│   └── datos.sql            # Datos de ejemplo
├── src/
│   ├── config.py            # Rutas y configuración
│   ├── database.py          # Conexión a SQLite
│   ├── reportes.py          # Consultas de solo lectura
│   └── models/              # Una clase por tabla
│       ├── base.py          # CRUD común a todas las clases
│       ├── categoria.py
│       ├── usuario.py
│       ├── empleado.py
│       ├── autor.py
│       ├── material.py
│       ├── ejemplar.py
│       └── prestamo.py
└── tests/
    └── test_modelos.py      # Pruebas automáticas
```

## Requisitos

- Python 3.10 o superior (SQLite ya viene incluido en Python)

## Cómo ejecutarlo

```
python main.py
```

Crea la base de datos `bnphu.db`, carga los datos de ejemplo y prueba la conexión, las
operaciones crear/consultar/actualizar/eliminar, un préstamo con su devolución y los reportes.

## Cómo correr las pruebas

```
python -m unittest discover -s tests -t .
```
