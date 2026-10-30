"""Conexión a la base de datos SQLite.

SQLite viene incluido en Python (módulo sqlite3): no hay que instalar nada.
"""

import sqlite3

from src.config import RUTA_BD, RUTA_DATOS, RUTA_ESQUEMA


def conectar(ruta=None):
   
    conexion = sqlite3.connect(str(ruta or RUTA_BD))
    conexion.row_factory = sqlite3.Row        
    conexion.execute("PRAGMA foreign_keys = ON")  
    return conexion


def _ejecutar_archivo(conexion, ruta):

    with open(ruta, encoding="utf-8") as archivo:
        conexion.executescript(archivo.read())
    conexion.commit()


def crear_tablas(conexion):

    _ejecutar_archivo(conexion, RUTA_ESQUEMA)


def cargar_datos(conexion):

    _ejecutar_archivo(conexion, RUTA_DATOS)


def inicializar(conexion):

    crear_tablas(conexion)
    cargar_datos(conexion)