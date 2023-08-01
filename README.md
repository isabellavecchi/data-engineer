# data-engineer
ETL: Busca dados em um Excel do Google Docs e insere no MongoDB e depois no PostgreSQL. Utilizando Python, pandas e docker.

On Ubuntu 20

"""
python3 -m venv venv
./venv/Scripts/Activate.ps1
"""

Estou adicionando RabbitMQ a esta aplicação.
Aqui está uma onde já existe esta parte implementada:
https://github.com/isabellavecchi/Arquitetura-de-Software-Aplicada/tree/master/trab1-rabbitMQ

Para este projeto é necessário instalar algumas bibliotecas do python,
como estou utilizando um ambiente virtual, ele lista todas as dependências
do meu projeto em um arquivo de saída com o seguinte comando:
"""
pip freeze > requirements.txt
"""
para que você possa instalá-las em seu ambiente, basta digitar o seguinte comando no prompt:
"""
pip3 install --no-cache-dir -r requirements.txt
"""
Banco de Dados PostgreSQL e MongoDB estão em containers separados da aplicação.

O fluxo principal do código se encontra no arquivo
"""
main.py
"""

No diretório "connectors" se encontram os arquivos responsáveis por fazer a conexão com os respectivos bancos
Neles também se encontram métodos gerais de CRUD dos dados.

No diretório "repositories" se encontram os arquivos que enviam/buscam dados para/de as collections/tabelas

No diretório "services" se encontra a camada da aplicação que transforma os dados de e para os modelos declarados
dentro de "models"

No diretório "models" se encontram os modelos de classes em POO, que são utilizados nos tráfegos de dados e também
pra padronizar os objetos a serem inseridos nas collections do Mongo.
Há também um arquivo específico para a criação de tabelas no PostgreSQL, através do SQLAlchemy - ferramenta que
facilita a atualização de modelos conforme o necessário para um projeto corrente.

No diretório "readers" há uma classe que importa Dados de um Google Docs Excel e realiza as transformações necessárias
para a inserção nos bancos.


Não cheguei a concluir a parte do PostgreSQL, pois fiquei estudando Pandas, e faltava reconstruir os objetos para
inseri-los no postgres. E as queries no Mongo estavam mais desafiadoras. Como já tenho um bom portifólio nessa
parte, acabei dando mais atenção as outras.

Segue aqui um link para um repositório onde fiz uma Agenda e um Sistema de Aeroportos em PostgreSQL:
https://github.com/isabellavecchi/Arquitetura-de-Software-Aplicada

E aqui, segue outro do meu primeiro projetinho de SQL puro
https://github.com/isabellavecchi/SQL_Projeto

E um pouco do meu trabalho que poderia ser mostrado sem causar prejuízos a locais onde trabalhei:
https://github.com/isabellavecchi/SQL
