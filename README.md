# Projeto de Transferência de Arquivos via SFTP com Python

Este projeto demonstra como criar um bucket S3 na AWS, configurar uma instância EC2 e usar Python com a biblioteca Paramiko para transferir e ler arquivos via SFTP.
Basicamente ele copia um arquivo de um Bucket para um servidor via SFTP utilizando Python.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Criando um Bucket S3](#criando-um-bucket-s3)
- [Configurando a Instância EC2](#configurando-a-instância-ec2)
- [Execução do Script](#execução-do-script)
- [Exemplo de saida](#exemplo-saida)
- [Considerações Finais](#consideracoes-finais)

## Pré-requisitos

Antes de começar, você precisará de:

- Uma conta na [AWS](https://aws.amazon.com/).
- O [AWS CLI](https://aws.amazon.com/cli/) instalado e configurado.
- Python 3 instalado em sua máquina.
- As bibliotecas `paramiko` e `boto3` instalada. Você pode instalar usando pip:

```bash
pip install paramiko boto3
```

## Criando um Bucket S3

- Faça login no console da AWS.
- Navegue até o serviço S3.
- Clique em Create bucket.
- Dê um nome ao seu bucket e selecione a região desejada.
- Clique em Create.
- Realize as configurações necessárias para transferências de arquivos.

## Configurando a Instância EC2

- Navegue até o serviço EC2 no console da AWS.
- Clique em Launch Instance.
- Selecione uma AMI (Amazon Machine Image) desejada (ex: Amazon Linux).
- Escolha um tipo de instância (ex: t2.micro para uso gratuito).
- Configure detalhes da instância conforme necessário.
- Adicione armazenamento se necessário.
- Configure o Security Group para permitir conexões SSH (porta 22).
- Revise e inicie a instância, criando uma nova chave de par (ou usando uma existente) para acesso SSH.
- Realize as configurações necessárias para transferências de arquivos.

## Execução do Script

- Certifique-se de que o arquivo arquivo.txt esteja no mesmo diretório que o seu script ou forneça o caminho completo para ele.
- Certifique-se de que as bibliotecas `paramiko` e `boto3` estão instaladas.
- Execute o script no terminal:

```bash
python robot.py
```

## Exemplo de saida

```bash
Arquivo baixado do S3 para o caminho local.
Arquivo enviado para o servidor SFTP.
Conteúdo do arquivo no servidor:
Conteudo do arquivo

Estou cansado de jogar DUST2 e perder! Por favor, vamos começar a ganhar senão vou enlouquecer!

Ass: Herik 'paranoic' Rodrigues
```

## Considerações Finais

- As credenciais são específicas para meu usuário, porém o codigo é reutilizável
- Foi ignorado um arquivo .env com credenciais
