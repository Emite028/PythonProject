import customtkinter as ctk
from tkinter import messagebox

# --- CONFIGURAÇÕES INICIAIS DO TEMA ---
# Define o modo escuro e o tema de cores base (azul)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class HamburgueriaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("🍔 Burger Master - Terminal de Vendas")

        # Comando para iniciar a janela já maximizada (tela cheia)
        self.after(0, lambda: self.state('zoomed'))

        # --- PALETA DE CORES PERSONALIZADA ---
        self.COR_PRIMARIA = "#FF8C00"  # Laranja para botões e destaques
        self.COR_SUCESSO = "#27AE60"  # Verde para o botão de finalizar e total
        self.COR_FUNDO_CARD = "#2B2B2B"  # Cinza escuro para os cards de cada lanche
        self.COR_TEXTO_PRECO = "#F1C40F"  # Amarelo para destacar o valor do item

        # --- BANCO DE DADOS (DICIONÁRIO DE PRODUTOS) ---
        self.menu_itens = {
            "🔥 MAIS VENDIDOS": [
                ("Smash Burger", 22.00), ("Bacon Deluxe", 35.00),
                ("Monster Burger", 55.00)
            ],
            "Basicamente Burgers": [
                ("Cheddar Melt", 32.00), ("Veggie Power", 28.00),
                ("Duplo Egg", 38.00)
            ],
            "Acompanhamentos": [
                ("Batata Palito", 15.00), ("Batata Rústica", 18.00),
                ("Onion Rings", 20.00)
            ],
            "Bebidas": [
                ("Coca-Cola 350ml", 7.00), ("Suco Natural", 10.00),
                ("Cerveja Artesanal", 18.00)
            ]
        }

        # Variáveis de controle do pedido
        self.carrinho = []
        self.total_valor = 0.0

        # --- ESTRUTURA DE LAYOUT (GRID) ---
        # Coluna 0 (Menu) cresce para ocupar o espaço; Coluna 1 (Carrinho) fica fixa
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)

        # --- SEÇÃO 1: CARDÁPIO (ESQUERDA) ---
        # CTkScrollableFrame cria uma área com barra de rolagem automática
        self.scroll_menu = ctk.CTkScrollableFrame(self,
                                                  label_text="CARDÁPIO EXCLUSIVO",
                                                  label_font=("Ubuntu", 28, "bold"),
                                                  label_text_color=self.COR_PRIMARIA,
                                                  fg_color="#1A1A1A")
        self.scroll_menu.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Chama a função que desenha os botões e lanches na tela
        self.renderizar_menu()

        # --- SEÇÃO 2: PAINEL LATERAL (DIREITA) ---
        self.frame_lateral = ctk.CTkFrame(self, width=450, fg_color="#222222", corner_radius=15)
        self.frame_lateral.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        ctk.CTkLabel(self.frame_lateral, text="🛒 MEU CARRINHO",
                     font=("Ubuntu", 22, "bold"), text_color="white").pack(pady=20)

        # Campo de texto onde os itens adicionados serão listados
        self.lista_carrinho_txt = ctk.CTkTextbox(self.frame_lateral, width=400, height=350,
                                                 font=("Consolas", 14), fg_color="#1A1A1A",
                                                 border_color=self.COR_PRIMARIA, border_width=1)
        self.lista_carrinho_txt.pack(padx=20, pady=5)
        self.lista_carrinho_txt.configure(state="disabled")  # Impede que o usuário digite dentro

        # Exibição do Valor Total
        self.label_total = ctk.CTkLabel(self.frame_lateral, text="R$ 0.00",
                                        font=("Ubuntu", 42, "bold"), text_color=self.COR_SUCESSO)
        self.label_total.pack(pady=10)

        # --- SEÇÃO 3: FORMA DE PAGAMENTO ---
        self.frame_pag = ctk.CTkFrame(self.frame_lateral, fg_color="transparent")
        self.frame_pag.pack(pady=10, fill="x", padx=30)

        ctk.CTkLabel(self.frame_pag, text="PAGAMENTO:", font=("Ubuntu", 14, "bold")).pack(anchor="w")

        # StringVar armazena qual opção de rádio está selecionada
        self.metodo_pagamento = ctk.StringVar(value="Pix")
        for m in ["Cartão de Débito", "Cartão de Crédito", "Pix", "Dinheiro"]:
            ctk.CTkRadioButton(self.frame_pag, text=m, variable=self.metodo_pagamento,
                               value=m, hover_color=self.COR_PRIMARIA,
                               fg_color=self.COR_PRIMARIA).pack(pady=3, anchor="w")

        # --- BOTÕES DE AÇÃO ---
        # Botão Principal de Finalizar
        self.btn_finalizar = ctk.CTkButton(self.frame_lateral, text="CONFIRMAR PEDIDO",
                                           width=350, height=70, font=("Ubuntu", 20, "bold"),
                                           fg_color=self.COR_SUCESSO, hover_color="#1E8449",
                                           command=self.finalizar, corner_radius=10)
        self.btn_finalizar.pack(pady=20)

        # Botão discreto para limpar o carrinho
        self.btn_limpar = ctk.CTkButton(self.frame_lateral, text="Limpar Carrinho",
                                        fg_color="transparent", text_color="#E74C3C",
                                        hover_color="#3D1A1A", command=self.limpar_carrinho)
        self.btn_limpar.pack(pady=5)

    def renderizar_menu(self):
        """ Percorre o dicionário de itens e cria os 'Cards' visuais para cada um """
        for categoria, itens in self.menu_itens.items():
            # Título da Categoria
            ctk.CTkLabel(self.scroll_menu, text=categoria, font=("Ubuntu", 20, "bold"),
                         text_color="white").pack(pady=(30, 15), anchor="w", padx=20)

            for nome, preco in itens:
                # O Card: um pequeno container arredondado para cada item
                card = ctk.CTkFrame(self.scroll_menu, fg_color=self.COR_FUNDO_CARD,
                                    height=80, corner_radius=12)
                card.pack(fill="x", padx=20, pady=8)

                # Nome do Produto (posicionado com .place para design livre)
                ctk.CTkLabel(card, text=nome, font=("Ubuntu", 18, "bold"),
                             text_color="white").place(x=20, y=15)

                # Preço em Amarelo
                ctk.CTkLabel(card, text=f"R$ {preco:.2f}", font=("Ubuntu", 18),
                             text_color=self.COR_TEXTO_PRECO).place(x=20, y=42)

                # Botão de "+" para adicionar ao carrinho
                # O uso do 'lambda n=nome, p=preco' é vital para que o Python saiba qual item exato foi clicado
                btn = ctk.CTkButton(card, text="➕", width=50, height=50,
                                    fg_color="#3D3D3D", hover_color=self.COR_PRIMARIA,
                                    command=lambda n=nome, p=preco: self.adicionar(n, p))
                btn.place(relx=0.97, rely=0.5, anchor="e")

    def adicionar(self, nome, preco):
        """ Adiciona o item à lista interna e atualiza a interface """
        self.carrinho.append((nome, preco))
        self.atualizar_carrinho()

    def atualizar_carrinho(self):
        """ Limpa a caixa de texto e redesenha a lista de itens e o total """
        self.lista_carrinho_txt.configure(state="normal")  # Habilita para edição temporária
        self.lista_carrinho_txt.delete("1.0", "end")  # Limpa tudo

        total = 0
        for item, preco in self.carrinho:
            # Formatação: Nome alinhado à esquerda e preço alinhado à direita
            linha = f" {item.ljust(22)} R$ {preco:>7.2f}\n"
            self.lista_carrinho_txt.insert("end", linha)
            total += preco

        self.total_valor = total
        self.label_total.configure(text=f"R$ {total:.2f}")  # Atualiza o texto do valor total
        self.lista_carrinho_txt.configure(state="disabled")  # Bloqueia novamente

    def limpar_carrinho(self):
        """ Pergunta se o usuário tem certeza e limpa a lista """
        if messagebox.askyesno("Limpar", "Deseja remover todos os itens do carrinho?"):
            self.carrinho = []
            self.atualizar_carrinho()

    def finalizar(self):
        """ Valida o pedido, verifica pagamento e exibe mensagem final """
        if not self.carrinho:
            messagebox.showwarning("Ops!", "Seu carrinho está vazio.")
            return

        metodo = self.metodo_pagamento.get()
        msg = f"PEDIDO REALIZADO!\n\nTotal: R$ {self.total_valor:.2f}\nPagamento: {metodo}"

        # Lógica especial para dinheiro conforme solicitado
        if metodo == "Dinheiro":
            msg += "\n\n⚠️ DIRIJA-SE AO BALCÃO PARA PAGAR."

        messagebox.showinfo("Burger Master", msg)

        # Reinicia o sistema para o próximo cliente
        self.carrinho = []
        self.atualizar_carrinho()


if __name__ == "__main__":
    app = HamburgueriaApp()
    app.mainloop()