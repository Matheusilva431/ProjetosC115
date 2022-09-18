CREATE DATABASE IF NOT EXISTS projetodocker;
USE projetodocker;

CREATE TABLE IF NOT EXISTS produtos(
    id INT(11) AUTO_INCREMENT,
    nome VARCHAR(255),
    preco DECIMAL(10, 2),
    descricao VARCHAR(255),
    PRIMARY KEY (id)
);

INSERT INTO produtos VALUE (0, 'MacBook Air 13', 7499, 'M1 256GB de SSD');
INSERT INTO produtos VALUE (0, 'Mouse Redragon Cobra', 115, 'RGB 7 Botoes');