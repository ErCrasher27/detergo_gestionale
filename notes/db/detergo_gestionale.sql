CREATE DATABASE detergo_gestionale;

USE detergo_gestionale;

CREATE TABLE cliente(
    id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(64) NOT NULL,
    cognome VARCHAR(64) NOT NULL,
    telefono VARCHAR(16) NULL,
    indirizzo VARCHAR(128) NULL,
    note VARCHAR(256) NULL,
    PRIMARY KEY (id)
);

CREATE TABLE ordine(
    id INT AUTO_INCREMENT NOT NULL,
    data_attuale DATETIME NOT NULL,
    data_ritiro DATETIME NOT NULL,
    totale FLOAT NOT NULL,
    credito FLOAT NOT NULL,
    domicilio ENUM("si", "no") NOT NULL,
    note VARCHAR(256) NULL, 
    stato ENUM("non_iniziato", "parziale", "completato") NOT NULL,
    id_cliente INT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);

CREATE TABLE categoria(
    id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(64) NOT NULL,
    icona BLOB NULL,
    PRIMARY KEY (id)
);

CREATE TABLE articolo(
    id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(64) NOT NULL,
    prezzo_acqua FLOAT NULL,
    prezzo_secco FLOAT NULL,
    prezzo_sartoria FLOAT NULL,
    id_categoria INT,
    PRIMARY KEY(id),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);

CREATE TABLE capo_portato(
    id_ordine INT NOT NULL,
    id_articolo INT NOT NULL,
    stato ENUM ("non iniziato", "pronto", "restituito") NOT NULL,
    prezzo_modificato FLOAT NULL,
    foto BLOB NULL,
    PRIMARY KEY(id_ordine, id_articolo),
    FOREIGN KEY (id_ordine) REFERENCES ordine(id),
    FOREIGN KEY (id_articolo) REFERENCES articolo(id)
);

CREATE TABLE colore(
    id INT AUTO_INCREMENT,
    nome VARCHAR(64) NOT NULL,
    icon BLOB NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE difetto(
    id INT AUTO_INCREMENT,
    nome VARCHAR(64) NOT NULL,
    icon BLOB NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE colore_capo_portato(
    id_colore INT NOT NULL,
    id_ordine INT NOT NULL,
    id_articolo INT NOT NULL,
    PRIMARY KEY(id_colore, id_ordine, id_articolo),
    FOREIGN KEY (id_colore) REFERENCES colore(id),
    FOREIGN KEY (id_ordine, id_articolo) REFERENCES capo_portato(id_ordine, id_articolo)
);

CREATE TABLE difetto_capo_portato(
    id_difetto INT NOT NULL,
    id_ordine INT NOT NULL,
    id_articolo INT NOT NULL,
    PRIMARY KEY(id_difetto, id_ordine, id_articolo),
    FOREIGN KEY (id_difetto) REFERENCES difetto(id),
    FOREIGN KEY (id_ordine, id_articolo) REFERENCES capo_portato(id_ordine, id_articolo)
);


