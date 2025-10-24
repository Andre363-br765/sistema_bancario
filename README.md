# 🏦 Sistema Bancário em Python (Versão OO)

Esta é a versão **atualizada e orientada a objetos** do sistema bancário desenvolvido nas aulas de Python.  
O projeto evoluiu de funções simples para classes e abstrações, tornando o código mais **modular**, **reutilizável** e próximo de um sistema real.

---

## ✨ Evolução do Projeto

| Versão             | Paradigma             | Características principais |
|-------------------|----------------------|---------------------------|
| Desafio 1          | Funções              | Menu simples, saldo único, sem histórico detalhado |
| Desafio 2 (Atual)  | Orientação a Objetos  | Classes Cliente, Conta e Transação, histórico completo, múltiplas contas, regras de saque, modularização OO |

---

## 🚀 Funcionalidades

- 💰 **Depósito e Saque:** transações registradas automaticamente no histórico da conta.  
- 📄 **Extrato detalhado:** mostra todas as movimentações (depósitos e saques) com data e hora.  
- 👤 **Clientes e Contas:** cada cliente pode ter múltiplas contas.  
- ⚠️ **Regras de saque:** limite diário de saques e limite por operação.  
- 📝 **Histórico de transações:** cada conta mantém seu próprio registro.  
- 🧩 **Código modular OO:** classes, heranças e abstrações bem organizadas.  

---

## 🗂 Estrutura do Projeto

```text
sistema_bancario/
│
├── main.py                       # Entrada do sistema, menu principal
│
├── utils/
│   ├── __init__.py
│   └── helpers.py                # Funções auxiliares (input seguro)
│
├── contas/
│   ├── __init__.py
│   └── contas.py                 # Classes Cliente, Conta, ContaCorrente e transações
│
├── operacoes/
│   ├── __init__.py
│   └── operacoes.py              # Funções de depósito, saque e extrato
│
├── dados/
│   ├── __init__.py
│   └── armazenamento.py          # Placeholder para persistência de dados
│
└── menu/
    ├── __init__.py
    └── menu.py                   # Função para exibir e capturar opção do usuário
```

---

## 🧩 Tecnologias Utilizadas

- **Linguagem:** Python 3  
- **Paradigma:** Programação Orientada a Objetos (POO)  
- **Ferramentas:** VS Code ou qualquer IDE de sua preferência  
- **Bibliotecas:** Nenhuma biblioteca externa necessária  

---

## 💡 Objetivo Educacional

Este projeto visa:  

- 💻 Aplicar POO em um sistema realista;  
- 📦 Organizar código em módulos e pacotes;  
- 🔄 Criar classes, heranças e abstração (Transações, Contas, Histórico);  
- ⚖️ Implementar regras de negócio (limite de saques, extrato detalhado);  
- 📝 Praticar boas práticas de legibilidade e manutenção.  

---

## 🧠 Próximos Passos

- 💾 Adicionar persistência de dados (JSON, CSV ou banco de dados);  
- 🔑 Permitir múltiplas contas por cliente com seleção no menu;  
- 🛡 Implementar autenticação de clientes (login por CPF);  
- 🎨 Criar interface gráfica ou menu mais interativo.  

---

Se quiser, posso criar também uma versão **visual** do README com GIF mostrando o sistema funcionando, estilo tutorial interativo, que deixa o projeto **muito mais atrativo no GitHub**.