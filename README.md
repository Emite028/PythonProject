
# 🍔 Burger Master — Terminal de Vendas

Aplicação desktop desenvolvida em Python para simular o gerenciamento de pedidos de uma hamburgueria, com cardápio interativo, carrinho de compras e cálculo automático do valor total.

O **Burger Master** foi desenvolvido com foco em simplicidade, organização visual e praticidade no atendimento, reunindo em uma única interface as principais etapas da montagem e confirmação de um pedido.

## 📋 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação e execução](#-instalação-e-execução)
- [Como utilizar](#-como-utilizar)
- [Cardápio disponível](#-cardápio-disponível)
- [Limitações atuais](#-limitações-atuais)
- [Possíveis melhorias](#-possíveis-melhorias)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

## 📖 Sobre o projeto

O Burger Master é um sistema de vendas com interface gráfica desenvolvido para representar o fluxo básico de atendimento de uma hamburgueria.

A aplicação permite visualizar os produtos disponíveis, adicionar itens ao carrinho, acompanhar o valor acumulado do pedido, selecionar uma forma de pagamento e confirmar a operação por meio de mensagens na interface.

O projeto também demonstra conceitos importantes de desenvolvimento com Python, como programação orientada a objetos, criação de interfaces gráficas, manipulação de listas e dicionários, tratamento de eventos e atualização dinâmica de componentes visuais.

## ✨ Funcionalidades

- **Cardápio interativo:** exibe os produtos organizados por categorias, com nomes e preços.
- **Adição de produtos:** permite incluir itens no carrinho por meio de botões de ação.
- **Carrinho de compras:** apresenta os produtos selecionados e seus respectivos valores.
- **Cálculo automático:** atualiza o total do pedido sempre que o carrinho é modificado.
- **Seleção de pagamento:** disponibiliza Pix, dinheiro, cartão de débito e cartão de crédito.
- **Confirmação de pedido:** valida se existem itens no carrinho e apresenta um resumo da operação.
- **Limpeza do carrinho:** permite remover todos os itens após uma confirmação do usuário.
- **Interface personalizada:** utiliza tema escuro, cores de destaque e componentes visuais organizados.
- **Preparação para o próximo atendimento:** limpa o carrinho após a confirmação do pedido.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Linguagem principal e implementação das regras da aplicação |
| CustomTkinter | Construção da interface gráfica e dos componentes visuais |
| Tkinter | Exibição de caixas de diálogo e mensagens ao usuário |

O projeto utiliza o CustomTkinter para criar uma interface desktop com aparência moderna, mantendo a lógica de funcionamento em um único arquivo Python.

## 📁 Estrutura do projeto

```text
PythonProject/
├── .idea/
├── .gitattributes
└── interface.py
```

### Arquivo principal

**`interface.py`**

Contém a implementação da aplicação, incluindo:

- Configuração do tema e da janela principal.
- Cadastro dos produtos e preços do cardápio.
- Renderização das categorias e dos produtos.
- Gerenciamento do carrinho de compras.
- Atualização do valor total.
- Seleção da forma de pagamento.
- Confirmação e limpeza dos pedidos.

Os dados do cardápio e do pedido são mantidos em estruturas de dados na memória durante a execução.

## 💻 Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

- Python 3 instalado.
- Pip disponível para instalar dependências.
- Um ambiente gráfico compatível com a execução de aplicações Tkinter.

A biblioteca `customtkinter` precisa ser instalada. O módulo `tkinter` é utilizado pela aplicação para exibir mensagens e, dependendo da distribuição do Python, pode exigir instalação separada.

## 🚀 Instalação e execução

### 1. Clone o repositório

```bash
git clone https://github.com/Emite028/PythonProject.git
```

### 2. Acesse a pasta do projeto

```bash
cd PythonProject
```

### 3. Crie um ambiente virtual (recomendado)

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux ou macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instale a dependência

```bash
python -m pip install customtkinter
```

### 5. Execute a aplicação

**Windows:**

```bash
python interface.py
```

**Linux ou macOS:**

```bash
python3 interface.py
```

Após a inicialização, a janela do Burger Master será aberta com o cardápio e o painel do carrinho.

## 🛒 Como utilizar

1. **Explore o cardápio:** navegue pelas categorias disponíveis e consulte os preços.
2. **Adicione produtos:** clique no botão de adição correspondente ao item desejado.
3. **Confira o carrinho:** verifique os itens selecionados e o valor total atualizado.
4. **Escolha o pagamento:** selecione uma das opções disponíveis no painel lateral.
5. **Confirme o pedido:** clique em `CONFIRMAR PEDIDO` para visualizar a confirmação.
6. **Prepare o próximo atendimento:** após a confirmação, o carrinho é esvaziado automaticamente.

Caso queira cancelar a seleção antes de finalizar, utilize a opção `Limpar Carrinho` e confirme a operação.

> **Observação:** selecionar uma forma de pagamento não significa que uma transação financeira será realizada. O sistema apenas registra a opção escolhida durante a execução e apresenta uma mensagem de confirmação.

## 🍟 Cardápio disponível

Os produtos são definidos diretamente no código e estão organizados nas seguintes categorias:

| Categoria | Produtos |
|---|---|
| Mais vendidos | Smash Burger, Bacon Deluxe e Monster Burger |
| Basicamente Burgers | Cheddar Melt, Veggie Power e Duplo Egg |
| Acompanhamentos | Batata Palito, Batata Rústica e Onion Rings |
| Bebidas | Coca-Cola 350ml, Suco Natural e Cerveja Artesanal |

Os preços são definidos em reais (R$) e podem ser alterados diretamente no dicionário `menu_itens`, localizado no arquivo `interface.py`.

## ⚠️ Limitações atuais

O projeto implementa um fluxo básico de vendas para fins demonstrativos. Na versão atual:

- Os pedidos e o cardápio são mantidos em memória; os dados não são persistidos em banco de dados ou arquivos.
- O encerramento da aplicação elimina os dados do carrinho que ainda estiverem na memória.
- As formas de pagamento são apenas opções de seleção; não há integração com serviços financeiros ou processamento real de pagamentos.
- Não há emissão de notas fiscais, recibos fiscais ou comprovantes financeiros.
- Não há cadastro de clientes, autenticação de usuários ou controle de estoque.
- Não há histórico de vendas ou relatórios gerenciais.
- Não há testes automatizados identificados na estrutura atual do repositório.

Essas limitações delimitam o escopo atual da aplicação e indicam oportunidades para futuras evoluções.

## 🔮 Possíveis melhorias

- **Persistência de dados:** integrar SQLite ou outro banco de dados para armazenar produtos, pedidos e vendas.
- **Gestão de produtos:** permitir cadastrar, editar e remover itens diretamente pela interface.
- **Controle de estoque:** registrar entradas, saídas e disponibilidade dos produtos.
- **Histórico de pedidos:** consultar vendas anteriores, horários, valores e formas de pagamento selecionadas.
- **Relatórios gerenciais:** calcular faturamento, produtos mais vendidos e indicadores de desempenho.
- **Experiência de compra:** permitir alterar quantidades e remover itens individualmente do carrinho.
- **Validação e testes:** implementar testes automatizados para o cálculo de totais e o fluxo de confirmação.
- **Organização do código:** separar interface, regras de negócio e persistência em módulos independentes.
- **Distribuição da aplicação:** criar um executável para facilitar a instalação em computadores sem um ambiente Python configurado.

## 🤝 Contribuição

Contribuições são bem-vindas para aprimorar a interface, corrigir problemas e adicionar funcionalidades.

1. Faça um fork do repositório.
2. Crie uma branch para sua alteração:

   ```bash
   git checkout -b feature/nova-funcionalidade
   ```

3. Implemente e teste suas modificações.
4. Faça um commit descritivo:

   ```bash
   git commit -m "feat: adiciona nova funcionalidade"
   ```

5. Envie a branch para seu fork e abra um Pull Request.

Para mudanças maiores, recomenda-se abrir uma issue antes de iniciar o desenvolvimento.

## 📄 Licença

Nenhum arquivo de licença foi identificado na estrutura analisada. Antes de definir os termos de uso, distribuição e modificação do projeto, recomenda-se adicionar um arquivo `LICENSE` com a licença escolhida pelo responsável pelo repositório.

## 👨‍💻 Autor

Desenvolvido por **Emite028**.

- **Repositório:** [github.com/Emite028/PythonProject](https://github.com/Emite028/PythonProject)

---

<p align="center">
  Desenvolvido com Python para simplificar a montagem e a confirmação de pedidos.
</p>
