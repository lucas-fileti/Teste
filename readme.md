# Controle Financeiro com Login

Projeto simples em Python para cadastro/login de usuarios e controle basico de entradas, saidas, saldo e registro de movimentacoes.

## Funcionalidades

- Criar conta de usuario
- Salvar usuarios no arquivo `usuarios.json`
- Fazer login com usuario e senha cadastrados
- Registrar entradas de dinheiro
- Registrar saidas/gastos
- Consultar saldo atual
- Ver o registro das movimentacoes feitas durante a execucao

## Tecnologias

- Python 3
- JSON como banco de dados local para usuarios

## Como executar

1. Clone o repositorio:

```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do projeto:

```bash
cd Teste
```

3. Execute o programa:

```bash
python app.py
```

No Windows, se `python` nao funcionar, tente:

```bash
py app.py
```

## Como usar

Ao iniciar o programa, escolha uma das opcoes:

```text
1 - Login
2 - Criar Conta
```

Depois de fazer login, o menu principal sera exibido:

```text
1 - Entradas
2 - Saidas
3 - Saldo
4 - Registro
5 - Sair
```

## Estrutura do projeto

```text
.
|-- app.py
|-- usuarios.json
`-- readme.md
```

- `app.py`: arquivo principal do programa.
- `usuarios.json`: banco de dados local onde os usuarios cadastrados ficam salvos.
- `readme.md`: documentacao do projeto.

## Observacoes

O arquivo `usuarios.json` e usado para persistir os cadastros. Ou seja, quando um novo usuario e criado, ele fica salvo para os proximos usos do programa.

As movimentacoes financeiras ficam salvas apenas enquanto o programa esta aberto. Ao fechar e abrir novamente, o saldo e o registro voltam ao estado inicial.
