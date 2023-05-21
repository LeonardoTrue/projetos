from babel import numbers
import customtkinter as custom
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from pathlib import Path
from tkcalendar import Calendar,DateEntry
import sqlite3
import time 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import webbrowser
import os
from PIL import Image


tab = "dados_cliente"
tab1 = "dados_projetos"
class Programa:  
    def __init__(self):
        self.root = Tk()
        self.criando_tabela()
        self.criar_tabela_projetos()
        self.configuraçao_tela()
        self.widgets_config()
        self.widgets_aba2()
        self.aba3_wd()
        self.info_visual()
        self.root.mainloop()
    def configuraçao_tela(self):
        custom.set_appearance_mode("dark")
        largura = 1080
        altura = 750
        altura_sistema = self.root.winfo_screenheight()
        largura_sistema = self.root.winfo_screenwidth()
        posx = largura_sistema/2 - largura/2
        posy = altura_sistema/2 - altura/2
        self.root.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy)) 
        self.root.title("Gerenciador de Projetos") 
        self.root.configure(bg="#1C1C1C")
        self.root.iconbitmap("C:\\Users\\Usuario\\projetos_estudos\\Gerenciadormarcenaria\\imagens\\enquete.ico")

    def widgets_config(self):
        self.abas = custom.CTkTabview(self.root,border_width=1,)
        self.abas.place(relx=0.01,rely=0.0,relwidth=0.98, relheight=0.98)
        self.aba1 = self.abas.add("informaçoes do Cliente")
        self.aba2 = self.abas.add("Detalhes do Projeto")
        self.aba3 = self.abas.add("Projetos")
        self.abas.set("informaçoes do Cliente")

        self.label_nome = custom.CTkLabel(self.aba1,text="Nome*",font=("Arial", 15, "bold"),anchor="w")
        self.label_nome.place(relx=0.01,rely=0.01, relwidth=0.08,relheight=0.08)
        

        self.entry_nome = custom.CTkEntry(self.aba1,placeholder_text="Nome completo")
        self.entry_nome.place(relx=0,rely=0.08, relwidth=0.4,relheight=0.04)   
        self.entry_nome.bind("<Return>",self.mudar_entry)
        

        self.label_doc = custom.CTkLabel(self.aba1,text="Rg:",font=("Arial", 15, "bold"),anchor="w")
        self.label_doc.place(relx=0.01,rely=0.13, relwidth=0.08,relheight=0.08)

        self.entry_doc = custom.CTkEntry(self.aba1,placeholder_text="Documento de Identificação")
        self.entry_doc.place(relx=0,rely=0.21, relwidth=0.4,relheight=0.04)
        self.entry_doc.bind("<Return>",self.mudar_entry2)

        self.label_endereco = custom.CTkLabel(self.aba1,text="Endereço:",font=("Arial", 15, "bold"),anchor="w")
        self.label_endereco.place(relx=0.01,rely=0.26, relwidth=0.2,relheight=0.04)

        self.entry_endereco = custom.CTkEntry(self.aba1,placeholder_text="exe: Rua Mariana numero 123")
        self.entry_endereco.place(relx=0,rely=0.32, relwidth=0.4,relheight=0.04)   
        self.entry_endereco.bind("<Return>",self.mudar_entry3)

        self.label_bloco = custom.CTkLabel(self.aba1,text="Bloco:",font=("Arial", 15, "bold"),anchor="w")
        self.label_bloco.place(relx=0.01,rely=0.40, relwidth=0.08,relheight=0.04)

        self.entry_bloco = custom.CTkEntry(self.aba1,placeholder_text="bloco: A",)
        self.entry_bloco.place(relx=0,rely=0.45, relwidth=0.06,relheight=0.04) 
        self.entry_bloco.bind("<Return>",self.mudar_entry4)  

        self.label_apto = custom.CTkLabel(self.aba1,text="Apartamento:",font=("Arial", 15, "bold"),anchor="w")
        self.label_apto.place(relx=0.2,rely=0.40, relwidth=0.3,relheight=0.04)

        self.entry_apto = custom.CTkEntry(self.aba1,placeholder_text="123")
        self.entry_apto.place(relx=0.2,rely=0.45, relwidth=0.08,relheight=0.04) 
        self.entry_apto.bind("<Return>",self.mudar_entry5)

        self.label_codigo = custom.CTkLabel(self.aba1,text="Codigo*",font=("Arial", 15, "bold"),anchor="w")
        self.label_codigo.place(relx=0.01,rely=0.52, relwidth=0.3,relheight=0.04)

        self.entry_codigo = custom.CTkEntry(self.aba1,placeholder_text="0",)
        self.entry_codigo.place(relx=0.01,rely=0.58, relwidth=0.08,relheight=0.04)
        # BOTOES
        self.botao_finalizar = custom.CTkButton(self.aba1, text="Finalizar",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,
                                                command=self.add_banco) 
        self.botao_finalizar.place(relx=0.80,rely=0.01,relwidth=0.14,relheight=0.06)

        self.botao_limpar = custom.CTkButton(self.aba1, text="Limpar",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,
                                                command=self.limpar_campos) 
        self.botao_limpar.place(relx=0.65,rely=0.01,relwidth=0.14,relheight=0.06)

        #self.lista_clientes = ttk.Treeview()
    def widgets_aba2(self):
        self.label_ambiente = custom.CTkLabel(self.aba2,text="Ambiente",font=("Arial", 15, "bold"),anchor="w")
        self.label_ambiente.place(relx=0.01,rely=0.01, relwidth=0.13,relheight=0.09)

        self.entry_ambiente = custom.CTkEntry(self.aba2,placeholder_text="exe: sala,cozinha,quarto")
        self.entry_ambiente.place(relx=0,rely=0.08, relwidth=0.4,relheight=0.04)
        self.entry_ambiente.bind("<Return>",self.pular_entry) 

        self.label_cor = custom.CTkLabel(self.aba2,text="Cor:",font=("Arial", 15, "bold"),anchor="w")
        self.label_cor.place(relx=0.01,rely=0.13, relwidth=0.08,relheight=0.08)

        self.entry_cor = custom.CTkEntry(self.aba2,placeholder_text="exe: branco")
        self.entry_cor.place(relx=0,rely=0.21, relwidth=0.4,relheight=0.04)
        self.entry_cor.bind("<Return>",self.pular_entry1)

        self.label_observacao = custom.CTkLabel(self.aba2,text="Observação:",font=("Arial", 15, "bold"),anchor="w")
        self.label_observacao.place(relx=0.01,rely=0.26, relwidth=0.2,relheight=0.04)

        self.entry_observacao = custom.CTkEntry(self.aba2,placeholder_text="exe: fazer movel do banheiro")
        self.entry_observacao.place(relx=0,rely=0.32, relwidth=0.4,relheight=0.04)
        self.entry_observacao.bind("<Return>",self.pular_entry2)   

        self.label_puxador = custom.CTkLabel(self.aba2,text="Puxador:",font=("Arial", 15, "bold"),anchor="w")
        self.label_puxador.place(relx=0.5,rely=0.01, relwidth=0.12,relheight=0.08)

        self.entry_puxador = custom.CTkEntry(self.aba2,placeholder_text="exe: alça")
        self.entry_puxador.place(relx=0.5,rely=0.08, relwidth=0.4,relheight=0.04) 

        self.label_data = custom.CTkLabel(self.aba2,text="Data:",font=("Arial", 15, "bold"),anchor="w")
        self.label_data.place(relx=0.01,rely=0.37, relwidth=0.2,relheight=0.04)

        self.entry_data = custom.CTkEntry(self.aba2,placeholder_text="exe: 00/00/0000")
        self.entry_data.place(relx=0,rely=0.44, relwidth=0.4,relheight=0.04)
        self.entry_data.bind("<Return>",self.pular_entry3)

        self.label_codigopro = custom.CTkLabel(self.aba2,text="Codigo Projeto*:",font=("Arial", 15, "bold"),anchor="w")
        self.label_codigopro.place(relx=0.01,rely=0.50, relwidth=0.2,relheight=0.04)

        self.entry_codigopro = custom.CTkEntry(self.aba2,placeholder_text="0")
        self.entry_codigopro.place(relx=0,rely=0.55, relwidth=0.08,relheight=0.04)
        self.entry_codigopro.bind("<Return>",self.pular_entry4)

        self.botao_finalizarp = custom.CTkButton(self.aba2, text="Finalizar",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,
          command=self.inserir_tabela_projetos                                   ) 
        self.botao_finalizarp.place(relx=0.2,rely=0.6, relwidth=0.15,relheight=0.06)

        self.botao_finalizarp = custom.CTkButton(self.aba3, text="Buscar Projeto",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,
                                          ) 
        self.botao_finalizarp.place(relx=0.5,rely=0.6, relwidth=0.20,relheight=0.06)
        ## PARTE CALENDARIO
        self.calendarioaba2 = Calendar(self.aba2,locale="pt_br",bg="#FF00FF")
        self.calendarioaba2.place(relx=0.5,rely=0.16,relwidth=0.4, relheight=0.4)

        self.botao_inserirdata = custom.CTkButton(self.aba2, text="Confirmar",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,
                                                command=self.mostrar_data_calendario) 
        self.botao_inserirdata.place(relx=0.76,rely=0.6, relwidth=0.15,relheight=0.06)

        self.botao_limpar = custom.CTkButton(self.aba2, text="Limpar",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,
                                                command=self.limpar_camposprojetos) 
        self.botao_limpar.place(relx=0.60,rely=0.60,relwidth=0.14,relheight=0.06)


     # INICIO BACK END
    def mostrar_data_calendario(self):
        self.data_escolhida = self.calendarioaba2.get_date()
        self.entry_data.delete(0, 999)
        self.entry_data.insert(0,str(self.data_escolhida))

    def conectar_bd(self):
        LOCAL = Path(__file__).parent
        NOME_DB = "dados_cli.db"
        CAMINHO = LOCAL / NOME_DB
        self.con = sqlite3.connect(CAMINHO)
        self.cursor = self.con.cursor()
    def desconectar_bd(self):
        self.cursor.close()
        self.con.close()
    def Treview_configs_clientes(self):
        self.lista_projetos_clientes = ttk.Treeview(self.frame_top1,columns=("col1","col2","col3","col4","col5","col6"))
        self.lista_projetos_clientes.place(relx=0.01,rely=0.48,relwidth=0.953,relheight=0.50)
        self.lista_projetos_clientes.heading("#0",text="")
        self.lista_projetos_clientes.heading("#1",text="Codigo")
        self.lista_projetos_clientes.heading("#2",text="Nome")
        self.lista_projetos_clientes.heading("#3",text="Rg")
        self.lista_projetos_clientes.heading("#4",text="Endereço")
        self.lista_projetos_clientes.heading("#5",text="Bloco")
        self.lista_projetos_clientes.heading("#6",text="Apto")

        self.strvariada = StringVar()

        self.lista_projetos_clientes.column("#0",width=5)
        self.lista_projetos_clientes.column("#1",width=20)
        self.lista_projetos_clientes.column("#2",width=100)
        self.lista_projetos_clientes.column("#3",width=80)
        self.lista_projetos_clientes.column("#4",width=100)
        self.lista_projetos_clientes.column("#5",width=10)
        self.lista_projetos_clientes.column("#6",width=10)
        self.lista_projetos_clientes.bind("<Double-1>",self.duplo_clique_cliente)
        self.escrol_cliente = ttk.Scrollbar(self.frame_top1)
        self.escrol_cliente.place(relx=0.96,rely=0.48,relwidth=0.03,relheight=0.50)
        self.lista_projetos_clientes.configure(yscrollcommand=self.escrol_cliente)

        self.botao_apagar = custom.CTkButton(self.aba3, text="Excluir",command=self.excluir_elementos,fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15) 
        self.botao_apagar.place(relx=0.01,rely=0.15, relwidth=0.15,relheight=0.06)
        
        self.botao_alterar = custom.CTkButton(self.aba3,command=self.alterar_elementos_cli, text="Alterar",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15) 
        self.botao_alterar.place(relx=0.01,rely=0.21, relwidth=0.15,relheight=0.06)
        self.adicionar_treview_clientes()
    def Treview_configs_projetos(self):
        self.lista_projetos_pro = ttk.Treeview(self.frame_top1,columns=("col1","col2","col3","col4","col5","col6"))
        self.lista_projetos_pro.place(relx=0.01,rely=0.48,relwidth=0.953,relheight=0.50)
        self.lista_projetos_pro.heading("#0",text="")
        self.lista_projetos_pro.heading("#1",text="Codigo")
        self.lista_projetos_pro.heading("#2",text="Cor")
        self.lista_projetos_pro.heading("#3",text="Data")
        self.lista_projetos_pro.heading("#4",text="Observação")
        self.lista_projetos_pro.heading("#5",text="Ambiente")
        self.lista_projetos_pro.heading("#6",text="Puxador")

        self.strvariada = StringVar()

        self.lista_projetos_pro.column("#0",width=5)
        self.lista_projetos_pro.column("#1",width=20)
        self.lista_projetos_pro.column("#2",width=80)
        self.lista_projetos_pro.column("#3",width=20)
        self.lista_projetos_pro.column("#4",width=100)
        self.lista_projetos_pro.column("#5",width=100)
        self.lista_projetos_pro.column("#6",width=80)
        self.lista_projetos_pro.bind("<Double-1>",self.duplo_clique_projeto)
        self.escrol_projeto = ttk.Scrollbar(self.frame_top1)
        self.escrol_projeto.place(relx=0.96,rely=0.48,relwidth=0.03,relheight=0.50)
        self.lista_projetos_pro.configure(yscrollcommand=self.escrol_projeto)

        self.botao_apagar = custom.CTkButton(self.aba3, text="Alterar",command=self.alterar_elemento_projeto,fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15) 
        self.botao_apagar.place(relx=0.01,rely=0.21, relwidth=0.15,relheight=0.06)

        self.botao_alterar = custom.CTkButton(self.aba3,command=self.excluir_elementospro, text="Excluir",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15) 
        self.botao_alterar.place(relx=0.01,rely=0.15, relwidth=0.15,relheight=0.06)

        self.adicionar_treview_projetos()
    def info_visual(self):
        self.avisos_telacli = custom.CTkTextbox(self.aba1,font=("Arial", 20),text_color="#00BFFF",border_spacing=6)
        self.avisos_telacli.place(relx=0.52,rely=0.1,relwidth=0.6,relheight=0.50)
        msgTC = f"Informaçoes importantes\n\n" + "Os Campos nome e Codigo nao devem estar vazio\n\n"+"Os Codigos dos Clientes devem ser Unicos.\nNao São Aceitos Codigos Repetidos\n\n"+"Recomendado: Codigo do Cliente.\ne Codigo de Detalhes dos Projeto serem iguais\n\n"+"Botao 'Limpar' Esvazia todos os campos Preenchidos\n"+"Botao 'Finalizar' Guarda as Informasões Do Cliente "
        f"dgfgdfgdg"
        self.avisos_telacli.insert("0.0",msgTC)
        self.avisos_telacli.configure(state="disabled")

        
    def aba3_wd(self):
        self.frame_top1 = custom.CTkFrame(self.aba3,corner_radius=15,border_width=3)
        self.frame_top1.place(relx=0.2,rely=0.01,relwidth=0.79,relheight=0.98)

        self.text_b = custom.CTkTextbox(self.frame_top1,border_width=1,font=("Arial",25),text_color="#FFFFFF",corner_radius=10,border_spacing=5)
        self.text_b.place(relx=0.01,rely=0.02,relwidth=0.98,relheight=0.44)
        ## add text na textBox
        self.botao_tab_clientes = custom.CTkButton(self.aba3, text="Informações Clientes",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,
                             command=self.Treview_configs_clientes    ) 
        self.botao_tab_clientes.place(relx=0.01,rely=0.02, relwidth=0.15,relheight=0.06)

        self.botao_tab_projeto = custom.CTkButton(self.aba3, text="Informações Projetos",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,
                    command=self.Treview_configs_projetos      ) 
        self.botao_tab_projeto.place(relx=0.01,rely=0.09, relwidth=0.15,relheight=0.06)



        self.botao_pdf = custom.CTkButton(self.aba3,command=self.gerar_pdf, text="Gerar PDF",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15) 
        self.botao_pdf.place(relx=0.01,rely=0.27, relwidth=0.15,relheight=0.06)
    def duplo_clique_cliente(self,enevt): 
        self.text_b.delete("0.0", "end")
        self.lista_projetos_clientes.selection()   
        for valor in self.lista_projetos_clientes.selection():
            self.codigoi,self.nomei,self.rgi,self.enderecoi,self.blocoi,self.aptoi, = self.lista_projetos_clientes.item(valor,"values")
            self.msg = f"""                                Informaçoes Do Cliente                                           
Codigo: {self.codigoi}\n   
Nome: {self.nomei}\n
Rg: {self.rgi}   \n
Endereço: {self.enderecoi}\n       
Bloco: {self.blocoi}  \n
Apto: {self.aptoi}"""
            self.text_b.insert("0.0", self.msg)
        self.buscar_dados_para_pdf()
    def duplo_clique_projeto(self,event):
        self.text_b.delete("0.0","end")
        self.lista_projetos_pro.selection()
        for valor in self.lista_projetos_pro.selection():
            self.codigop,self.corp,self.datap,self.observacaop,self.ambientep,self.puxadorp = self.lista_projetos_pro.item(valor,"values")
            self.msgprojeto = f"""                                Informaçoes Do Projeto\n
                                            
Codigo: {self.codigop}\n 
Cor: {self.corp}\n
Data Inicio: {self.datap}\n   
Observaçoes: {self.observacaop}\n       
Ambiente: {self.ambientep}\n  
Puxador: {self.puxadorp}\n"""
            self.text_b.insert("0.0",self.msgprojeto)
    def criando_tabela(self):
        self.conectar_bd()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tab}(
        codigo INTEGER UNIQUE,
        nome VARCHAR(100) NOT NULL,
        rg INTEGER,
        endereco VARCHAR(100) NOT NULL,
        bloco INTEGER NOT NULL,
        apto INTEGER NOT NULL,
        PRIMARY KEY (codigo)
        )""")
        self.con.commit()
        self.desconectar_bd()
    def variaveis(self):
        self.nome = self.entry_nome.get()
        self.docu = self.entry_doc.get()
        self.endereco = self.entry_endereco.get()
        self.bloco = self.entry_bloco.get()
        self.apto = self.entry_apto.get()
        self.codigo = self.entry_codigo.get()
    def add_banco(self):
        self.variaveis()
        if self.entry_codigo.get() == "" or self.entry_nome.get() == "":
            msg = "Preencha os campos obrigatorios (nome,codigo)"
            messagebox.showinfo("Aviso!!",msg)
            
        else:
            self.conectar_bd()
            self.cursor.execute(f"""INSERT OR IGNORE INTO {tab}(codigo,nome,rg,endereco,bloco,apto)
            VALUES (?,?,?,?,?,?)""",(self.codigo,self.nome,self.docu,self.endereco,self.bloco,self.apto))
            self.con.commit()
            self.desconectar_bd()
            self.limpar_campos()
    def limpar_campos(self):
        self.entry_nome.delete(0,999)
        self.entry_doc.delete(0,999)
        self.entry_endereco.delete(0,999)
        self.entry_bloco.delete(0,999)
        self.entry_apto.delete(0,999)
        self.entry_codigo.delete(0,999)
    def limpar_camposprojetos(self):
        self.entry_ambiente.delete(0,999)
        self.entry_codigopro.delete(0,999)
        self.entry_cor.delete(0,999)
        self.entry_puxador.delete(0,999)
        self.entry_observacao.delete(0,999)
        self.entry_data.delete(0,999)    
    def criar_tabela_projetos(self):
        self.conectar_bd()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tab1}(
        codigo INTEGER UNIQUE,
        cor VARCHAR(50),
        data VARCHAR(30),
        observacao VARCHAR(100),
        ambiente VARCHAR(100),
        puxador VARCHAR(40),
        PRIMARY KEY (codigo)
        )"""
)
        self.con.commit()
        self.desconectar_bd()
    def inserir_tabela_projetos(self):
        if self.entry_codigopro.get() == "":
            msg = "O Campo codigo nao pode esta Vázio"
            messagebox.showinfo("Aviso!!",msg)
        else:
            self.amb = self.entry_ambiente.get()
            self.cor = self.entry_cor.get()
            self.observacao = self.entry_observacao.get()
            self.data = self.entry_data.get()
            self.puxador = self.entry_puxador.get()
            self.codigo2 = self.entry_codigopro.get()
            self.conectar_bd()
            self.cursor.execute(f"""INSERT OR IGNORE INTO {tab1}(codigo,cor,data,observacao,ambiente,puxador)
            VALUES (?,?,?,?,?,?)""",(self.codigo2,self.cor,self.data,self.observacao,self.amb,self.puxador,))
            self.con.commit()
            self.desconectar_bd()
            self.limpar_camposprojetos()

    def adicionar_treview_clientes(self):
        self.conectar_bd()
        dados = self.cursor.execute(f"""SELECT codigo,nome,rg,endereco,bloco,apto FROM {tab}
        ORDER BY nome ASC""").fetchall()
        for v in dados:
            self.lista_projetos_clientes.insert("", END, values=v)
        
        self.desconectar_bd()
    def adicionar_treview_projetos(self):
        self.lista_projetos_pro.delete(*self.lista_projetos_pro.get_children())
        self.conectar_bd()
        dados = self.cursor.execute(f"""SELECT codigo,cor,data,observacao,ambiente,puxador FROM {tab1}""").fetchall()
        for v in dados:
            self.lista_projetos_pro.insert("", END, values=v)
        
        self.desconectar_bd()
    def excluir_elementos(self):
        self.conectar_bd()
        self.cursor.execute(f"""DELETE FROM {tab} WHERE codigo = ?""",(self.codigoi,))
        self.text_b.delete("0.0","end")
        self.con.commit()
        self.desconectar_bd()
        self.lista_projetos_clientes.delete(*self.lista_projetos_clientes.get_children())
        self.adicionar_treview_clientes()
    def excluir_elementospro(self):
        self.conectar_bd()
        self.cursor.execute(f"""DELETE FROM {tab1} WHERE codigo = ?""",(self.codigop,))
        self.text_b.delete("0.0","end")
        self.con.commit()
        self.desconectar_bd()
        self.lista_projetos_pro.delete(*self.lista_projetos_pro.get_children())
        self.adicionar_treview_projetos()
    def alterar_elementos_cli(self):
         for v in self.lista_projetos_clientes.selection():
            self.limpar_campos()

            c1,c2,c3,c4,c5,c6 = self.lista_projetos_clientes.item(v,"values")
            self.entry_nome.insert(0,c2)
            self.entry_doc.insert(0,c3)
            self.entry_endereco.insert(0,c4)
            self.entry_bloco.insert(0,c5)
            self.entry_apto.insert(0,c6)
            self.entry_codigo.insert(0,c1)
            self.abas.set("informaçoes do Cliente")

            self.botao_salvar = custom.CTkButton(self.aba1, command=self.salvar_alteracao_cli,text="Salvar Alteração",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,) 
            self.botao_salvar.place(relx=0.80,rely=0.62,relwidth=0.14,relheight=0.06)
    def salvar_alteracao_cli(self):
        self.nome = self.entry_nome.get()
        self.docu = self.entry_doc.get()
        self.endereco = self.entry_endereco.get()
        self.bloco = self.entry_bloco.get()
        self.apto = self.entry_apto.get()
        self.codigo = self.entry_codigo.get()
        self.conectar_bd()
        self.cursor.execute(f"""UPDATE {tab}
        SET nome = ?, rg = ?, endereco = ?, bloco = ?,apto = ?
        WHERE codigo = ?""",(self.nome,self.docu,self.endereco,self.bloco,self.apto,self.codigo))
        self.con.commit()
        self.desconectar_bd()
        self.limpar_campos()
        self.lista_projetos_clientes.delete(*self.lista_projetos_clientes.get_children())
        self.adicionar_treview_clientes()
        time.sleep(0.3)
        self.abas.set("Projetos")
        self.text_b.delete("0.0","end")
        self.botao_salvar.destroy()
    def alterar_elemento_projeto(self):
        self.limpar_camposprojetos()
        for v in self.lista_projetos_pro.selection():
            v1,v2,v3,v4,v5,v6 = self.lista_projetos_pro.item(v,"values")
            self.entry_ambiente.insert(0,v5)
            self.entry_cor.insert(0,v2)
            self.entry_observacao.insert(0,v4)
            self.entry_data.insert(0,v3)
            self.entry_puxador.insert(0,v6)
            self.entry_codigopro.insert(0,v1)
            self.abas.set("Detalhes do Projeto")
            self.botao_salvar_altprojeto = custom.CTkButton(self.aba2, text="Salvar Alteração",fg_color="#696969",text_color="#FFFFFF",border_width=2,border_color="#000000",corner_radius=15,
                                  command=self.salvar_alteracao_projeto              ) 
            self.botao_salvar_altprojeto.place(relx=0.60,rely=0.6, relwidth=0.15,relheight=0.06) 
    def salvar_alteracao_projeto(self):
        self.limpar_campos()
        self.amb = self.entry_ambiente.get()
        self.cor = self.entry_cor.get()
        self.observacao = self.entry_observacao.get()
        self.data = self.entry_data.get()
        self.puxador = self.entry_puxador.get()
        self.codigo2 = self.entry_codigopro.get()
        self.conectar_bd()
        self.cursor.execute(f"""UPDATE {tab1}
        SET cor = ?, data = ?, observacao = ?, ambiente = ?,puxador = ?
        WHERE codigo = ?""",(self.cor,self.data,self.observacao,self.amb,self.puxador,self.codigo2))
        self.con.commit()
        self.desconectar_bd()
        self.limpar_campos()
        self.lista_projetos_pro.delete(*self.lista_projetos_pro.get_children())
        self.adicionar_treview_projetos()
        time.sleep(0.3)
        self.abas.set("Projetos")
        self.text_b.delete("0.0","end")
        self.botao_salvar_altprojeto.destroy()
    def buscar_dados_para_pdf(self):
        for v in self.lista_projetos_clientes.selection():
            self.d1,self.d2,self.d3,self.d4,self.d5,self.d6 = self.lista_projetos_clientes.item(v,"values")
        self.conectar_bd()
        valor = self.cursor.execute(f"""SELECT codigo,cor,data,observacao,ambiente,puxador FROM {tab1}
             WHERE codigo = ? """,(self.d1,)).fetchall()   
        for item in valor:
            self.p1,self.p2,self.p3,self.p4,self.p5,self.p6 = item
        self.desconectar_bd()
    def gerar_pdf(self):   
        c = canvas.Canvas("relatoriodeProjeto.pdf",pagesize=A4)
        c.setFont("Helvetica-Bold",22)
        c.drawString(160,790, "Informações Do Projeto")
        ### PARTE CLIENTE ###
        c.setFont("Helvetica-Bold",19)
        c.drawString(20,730,"Codigo:")
        c.drawString(20,700,"Nome:")
        c.drawString(20,670,"Rg:")
        c.drawString(20,640,"Endereço:")
        c.drawString(20,610,"Bloco:")
        c.drawString(20,580,"Apto:")
        c.line(18,560,560,560)
        c.setFont("Helvetica",16)
        c.drawString(135,730,self.d1)
        c.drawString(135,700,self.d2)
        c.drawString(135,670,self.d3)
        c.drawString(135,640,self.d4)
        c.drawString(135,610,self.d5)
        c.drawString(135,580,self.d6)
        ###  PARTE PROJETO ###
        c.setFont("Helvetica-Bold",19)
        c.drawString(20,540,"Cor:")
        c.drawString(20,510,"Data:")
        c.drawString(20,480,"Observação:")
        c.drawString(20,450,"Ambiente:")
        c.drawString(20,420,"Puxador:")
        c.setFont("Helvetica",16)
        c.drawString(135,540,self.p2)
        c.drawString(135,510,self.p3)
        c.drawString(136,480,self.p4)
        c.drawString(135,450,self.p5)
        c.drawString(135,420,self.p6)
        c.showPage()
        c.save()
        os.environ["BROWSER"] = "chrome"
        webbrowser.open("relatoriodeProjeto.pdf")
    def mudar_entry(self,event):
        self.entry_doc.focus()    
    def mudar_entry2(self,event):
        self.entry_endereco.focus()
    def mudar_entry3(self,event):
        self.entry_bloco.focus()
    def mudar_entry4(self,event):
        self.entry_apto.focus()   
    def mudar_entry5(self,event):
        self.entry_codigo.focus()
    def pular_entry(self,event):
        self.entry_cor.focus()
    def pular_entry1(self,event):
        self.entry_observacao.focus()
    def pular_entry2(self,event):
        self.entry_data.focus()
    def pular_entry3(self,event):
        self.entry_codigopro.focus()
    def pular_entry4(self,event):
        self.entry_puxador.focus()


clientes =  Programa()
