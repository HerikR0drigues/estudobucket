import boto3
import paramiko
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações de conexão do SFTP
hostname = '16.170.208.57'
port = 22
username = 'ec2-user'
private_key_path = 'pardechavesteste.pem'

# Configurações de credenciais AWS
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
bucket_name = 'estudoherikr0drigues'
s3_file_key = 'arquivo.txt'
local_file_path = 'arquivo_temp.txt'

# Configuração do boto3 com credenciais explícitas
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# Download do arquivo do S3
s3.download_file(bucket_name, s3_file_key, local_file_path)
print("Arquivo baixado do S3 para o caminho local.")

# Criar um objeto SSHClient
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Carregar a chave privada
private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

# Conectar ao servidor SFTP
client.connect(hostname, port=port, username=username, pkey=private_key)
sftp = client.open_sftp()

# Enviar o arquivo baixado para o servidor SFTP
remote_file = '/home/ec2-user/estudo/arquivo.txt'
sftp.put(local_file_path, remote_file)
print("Arquivo enviado para o servidor SFTP.")

# Fechar a conexão SFTP
sftp.close()

# Abrir e ler o arquivo usando SSH para confirmar que a transferência foi bem-sucedida
stdin, stdout, stderr = client.exec_command(f'cat {remote_file}')
file_content = stdout.read().decode()  # Decodifica os bytes para string

# Imprimir o conteúdo do arquivo
print("Conteúdo do arquivo no servidor:")
print(file_content)

# Fechar a conexão SSH
client.close()
