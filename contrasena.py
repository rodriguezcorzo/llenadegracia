import hashlib
from werkzeug.security import generate_password_hash

# Contraseña original
original = '12345'

# Generar el hash utilizando SHA-256 y truncarlo a 150 caracteres
contraseña_encriptada = hashlib.sha256(original.encode()).hexdigest()[:150]

print(f'Contraseña original: {original}')
print(f'Contraseña encriptada: {contraseña_encriptada}')
print(f'Longitud de la contraseña encriptada: {len(contraseña_encriptada)}')
