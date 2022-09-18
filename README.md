# Projetos C115
Este repositório contém os projeto desenvolvidos para a matéria C115.

Autores: 
- Isadora Bello Pereira Rodrigues
- Matheus Chagas da Silva

Projetos:
1. Cliente Servidor
2. Docker-project
![WhatsApp Image 2022-09-18 at 19 35 38](https://user-images.githubusercontent.com/85804680/190931580-fcba1d01-23bb-4747-a5b2-0e479c3d6207.jpeg)

![WhatsApp Image 2022-09-18 at 19 35 38 (1)](https://user-images.githubusercontent.com/85804680/190931597-920441bc-491f-4a38-8d49-432230e646c3.jpeg)


## 1) Cliente Servidor
### Como utilizar
Execute o botServer.py e logo em seguida execute o botCliente.py

Após isso digite o seu número do celular e escolha as opções informadas pelo programa
```
2 - Para fatura
3 - Para o saldo
4 - Para cancelamento
5 - Para encerrar a chamada
```
Para finalizar a seção basta selecionar a opção '5'.

## 2) Docker-Project
Referencia:
https://www.youtube.com/watch?v=Kzcz-EVKBEQ
## Como rodar
Abrar o terminal até a paste Docker-Project

### Instalando dependências
Acesse a pasta `./api` pelo terminal e execute:
```
npm install
```

Com isso é instalado as dependências Node.

### Construindo as imagens

Ainda no terminal devemos criar cada imagem (MySQL, Node API e PHP):

```
docker build -t mysql-image -f api/db/Dockerfile .
```
```
docker build -t node-image -f api/Dockerfile .
```
```
docker build -t php-image -f website/Dockerfile .
```

### Rodando os containers

Após criar as imagens devemos executar cada container por vez:

```
docker run -d -v $(pwd)/api/db/data:/var/lib/mysql --rm --name mysql-container mysql-image
```
```
docker run -d -v $(pwd)/api:/home/node/app -p 9001:9001 --link mysql-container --rm --name node-container node-image
```
```
docker run -d -v "$(pwd)/website":/var/www/html -p 8888:80 --link node-container --rm --name php-container php-image
```

### Agora faça o restore do banco:
```
docker exec -i mysql-container mysql -uroot -projetodocker < api/db/script.sql
```

### Como ver:
Abrir o navegador e digitar: `localhost:8888`

