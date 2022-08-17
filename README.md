# Python3

Repositorio para salvar exemplos de estudo e dicas sobre a ferramenta e suas bibliotecas.

## Ambiente virtual

Para configurar um ambiente virtual use os comandos:

```sh
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate

```

## Testes

Alguns testes estão implementados, para rodá-los use o comando:

```sh
pytest ./arquivo.py
```

## file_io

Alguns exemplos de como converter dados de formatos comuns para arrays python.

- CSV
- JSON
- XML

### Testes:

```sh
pytest file_io/csv_import.py
pytest file_io/json_import.py
pytest file_io/xml_import.py
```