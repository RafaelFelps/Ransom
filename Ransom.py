import os
from cryptography.fernet import Fernet

# Define a chave de criptografia aleatória
key = Fernet.generate_key()

# Cria o objeto Fernet com a chave definida
fernet = Fernet(key)

# Define a pasta que será criptografada
folder_path = 'C:/important_folder'

# Percorre os arquivos da pasta e criptografa cada um
for subdir, dirs, files in os.walk(folder_path):
    for file in files:
        # Abre o arquivo original e lê seu conteúdo
        with open(os.path.join(subdir, file), 'rb') as f:
            data = f.read()

        # Criptografa o conteúdo do arquivo
        encrypted_data = fernet.encrypt(data)

        # Escreve o conteúdo criptografado em um novo arquivo com o mesmo nome
        with open(os.path.join(subdir, file), 'wb') as f:
            f.write(encrypted_data)

# Salva a chave de criptografia em um arquivo
with open('key.key', 'wb') as f:
    f.write(key)
