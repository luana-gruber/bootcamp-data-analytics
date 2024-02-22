import sqlite3

conexao = sqlite3.connect('desafio_sql')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id
# (inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no
# exercício anterior.

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Maria da Silva", 18, "Análise e Desenvolvimento de Sistemas"),'
               '(2, "João Santos", 20, "Sistemas de Informação"), (3, "Clara Pereira", 19, "Ciência da Computação"),'
               '(4, "Helena Games", 18, "Engenharia"), (5, "Marcelo Almeida", 22, "Engenharia");')

# a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos;')

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20;')

# c) Selecionar os alunos do curso de "Engenharia" em ordem
# alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome ASC;')

# d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT count(*) FROM alunos')

# a) Atualize a idade de um aluno específico na tabela.
dados = cursor.execute('UPDATE alunos SET idade=23 WHERE idade=18')

# b) Remova um aluno pelo seu ID.
dados = cursor.execute('DELETE FROM alunos WHERE id=5')

# Crie uma tabela chamada "clientes" com os campos: id (chave
# primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
# registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Maria da Silva", 18, 120.00),'
               '(2, "João Santos", 35, 740.00), (3, "Clara Pereira", 59, 350.00),'
               '(4, "Helena Games", 18, 800.00), (5, "Marcelo Almeida", 42, 680.00);')

# a) Selecione o nome e a idade dos clientes com idade superior a
# 30 anos.
dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30;')

# b) Calcule o saldo médio dos clientes.
dados = cursor.execute('SELECT AVG(saldo) FROM clientes as Média;')

# c) Encontre o cliente com o saldo máximo.
dados = cursor.execute('SELECT MAX(saldo) FROM clientes;')

# d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('SELECT count(*) FROM clientes where saldo>1000;')

# a) Atualize o saldo de um cliente específico.
dados = cursor.execute('UPDATE clientes SET saldo=1200 WHERE id=2')

# b) Remova um cliente pelo seu ID
dados = cursor.execute('DELETE FROM clientes WHERE id=3')

# Crie uma segunda tabela chamada "compras" com os campos: id
# (chave primária), cliente_id (chave estrangeira referenciando o id
# da tabela "clientes"), produto (texto) e valor (real). Insira algumas
# compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o
# valor de cada compra.

cursor.execute('CREATE TABLE compras(id INT, cliente_id INT, produto VARCHAR(100), valor FLOAT, PRIMARY KEY(id), FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(6, 1, "Televisão", 3920.00),'
               '(7, 2, "Panela", 140.00), (8, 4, "Secador", 350.00),'
               '(9, 5, "Mouse", 80.00);')

dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras WHERE clientes.id=compras.cliente_id')

for i in dados:
    print(i)

conexao.commit()
conexao.close 