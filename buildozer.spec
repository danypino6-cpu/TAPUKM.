[app]
# (str) Titulo de tu aplicacion
title = ControlFlota

# (str) Nombre del paquete (sin espacios ni caracteres raros)
package.name = tapuku

# (str) Dominio del paquete (estilo reverse domain)
package.domain = org.geston

# (str) Directorio donde esta el main.py
source.dir = .

# (list) Extensiones de archivos a incluir
source.include_exts = py,png,jpg,kv,atlas,db,csv

# (str) Version de la aplicacion (OBLIGATORIO para evitar Error 100)
version = 1.0

# (list) Requerimientos de la aplicacion
# IMPORTANTE: sqlite3 y csv no se ponen aqui porque vienen con python3
requirements = python3,kivy==2.3.0,kivymd==1.1.1

# (str) Orientacion (landscape, portrait o all)
orientation = portrait

# (bool) Indica si la aplicacion debe ser a pantalla completa
fullscreen = 1

# ==================================
# CONFIGURACION DE ANDROID (CRITICO)
# ==================================

# (int) API de Android que se usara (33 es el estandar actual)
android.api = 33

# (int) API minima soportada (24 asegura compatibilidad con KivyMD)
android.minapi = 24

# (str) Version del NDK de Android (25b es la mas estable para esta config)
android.ndk = 25b

# (int) API del NDK (debe coincidir con minapi o ser similar)
android.ndk_api = 24

# (list) Arquitecturas a compilar (arm64-v8a es para celulares modernos)
android.archs = arm64-v8a

# (bool) Aceptar licencias automaticamente
android.accept_sdk_license = True

# (str) Formato de salida (apk o aab)
android.release_artifact = apk

[buildozer]
# (int) Nivel de log (2 muestra todo el detalle para ver errores)
log_level = 2

# (int) Pausar en caso de error
warn_on_root = 1
