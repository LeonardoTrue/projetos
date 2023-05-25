import sqlite3
from pathlib import Path
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
from PIL import Image



class InterfaceLogin:
    def __init__(self):
        self.crinado_tabela()
        self.root = Tk()
        self.config_tela()
        self.widgets_tela()
        self.root.mainloop()
    def config_tela(self):
        self.root.title("Painel de Login")
        self.root.resizable(width=FALSE,height=FALSE)
        largura = 750
        altura = 450
        largura_sistema = self.root.winfo_screenwidth()
        altura_sistema = self.root.winfo_screenheight()
        posy= altura_sistema/2 - altura/2
        posx= largura_sistema/2 - largura/2
        self.root.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))
        self.root.configure(bg="#363636")
    def widgets_tela(self):
        self.frame_principal = ctk.CTkFrame(self.root,width=400,height=250,corner_radius=20)
        self.frame_principal.place(relx=0.22,rely=0.2)
        self.label_login = ctk.CTkLabel(self.frame_principal,text="Login",font=("verdana", 10))
        self.label_login.place(relx=0.2,rely=0.3)
        self.entry_login = ctk.CTkEntry(self.frame_principal,placeholder_text="adicione seu Email")
        self.entry_login.place(relx=0.2,rely=0.4,relwidth=0.6,relheight=0.1)
        self.entry_login.bind("<Return>",self.mudar_entry1)

        self.label_senha = ctk.CTkLabel(self.frame_principal,text="Senha",font=("verdana", 10))
        self.label_senha.place(relx=0.2,rely=0.5)
        self.entry_senha = ctk.CTkEntry(self.frame_principal,placeholder_text="Senha",)
        self.entry_senha.place(relx=0.2,rely=0.6,relwidth=0.6,relheight=0.1)

        #imagEntrar = ctk.CTkImage(light_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\enter.png"),dark_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\enter.png"),)
        self.botao_entrar = ctk.CTkButton(self.frame_principal,command=self.validar_dados,corner_radius=20,hover_color="#2E8B57",text_color="#FFFFFF",fg_color="#3CB371",text="Entrar")
        self.botao_entrar.place(relx=0.29,rely=0.72,relwidth=0.43,relheight=0.08)
       
        self.botao_recuperar = ctk.CTkButton(self.frame_principal,command=self.recuperar_senha,corner_radius=20,hover=FALSE,hover_color="#2E8B57",text_color="#1E90FF",fg_color="transparent",text="esqueci minha senha",)
        self.botao_recuperar.place(relx=0.29,rely=0.80,relwidth=0.43,relheight=0.07)

        self.botao_cadastro = ctk.CTkButton(self.frame_principal,command=self.top_level,corner_radius=20,font=("Arial", 12),hover=FALSE,hover_color="#2E8B57",text_color="#32CD32",fg_color="transparent",text="fazer cadastro",)
        self.botao_cadastro.place(relx=0.30,rely=0.88,relwidth=0.39,relheight=0.06)

        imagemFrente = ctk.CTkImage(light_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\authentication.png"),dark_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\authentication.png"),size=(80,80))
        label_visual = ctk.CTkLabel(self.frame_principal,text="",image=imagemFrente)
        label_visual.place(relx=0.30,rely=0.02,relwidth=0.36,relheight=0.31)
    def mudar_entry1(self,event):
        self.entry_senha.focus()  
    def mudar_entrynomecadstro(self,event):
        self.entry_senhacadastro.focus()
    def mudar_entryconfirmarsenha(self,event):
        self.entry_senhaconfirmarcadastro.focus()
    def top_level(self):
        self.top = ctk.CTkToplevel()
        largura = 400
        altura = 250
        s_largira = self.top.winfo_screenwidth()
        s_altura = self.top.winfo_screenheight()
        px = s_largira/2 - largura/2
        py = s_altura/2 - altura/2
        self.top.geometry("%dx%d+%d+%d" % (largura,altura,px,py))
        self.top.grab_set()
        self.top.title("Fazer Cadastro")
        self.top.resizable(FALSE,FALSE)

        self.label_nomecadastro = ctk.CTkLabel(self.top,text="Nome",width=0.4,height=0.1)
        self.label_nomecadastro.place(relx=0.2,rely=0.23)
        self.entry_nomecadastro = ctk.CTkEntry(self.top,placeholder_text="Login de cadastro",corner_radius=20)
        self.entry_nomecadastro.place(relx=0.2,rely=0.3,relwidth=0.6,relheight=0.08)
        self.entry_nomecadastro.bind("<Return>",self.mudar_entrynomecadstro)
        # senha cadastro
        self.label_senhacadastro = ctk.CTkLabel(self.top,text="Senha",width=0.4,height=0.1)
        self.label_senhacadastro.place(relx=0.2,rely=0.4)
        self.entry_senhacadastro = ctk.CTkEntry(self.top,placeholder_text="Senha de acesso",corner_radius=20)
        self.entry_senhacadastro.place(relx=0.2,rely=0.47,relwidth=0.6,relheight=0.08)
        self.entry_senhacadastro.bind("<Return>",self.mudar_entryconfirmarsenha)
        # confirmar senha
        self.label_senhaconfirmarcadastro = ctk.CTkLabel(self.top,text="Confirmar senha ",width=0.4,height=0.1)
        self.label_senhaconfirmarcadastro.place(relx=0.2,rely=0.57)
        self.entry_senhaconfirmarcadastro = ctk.CTkEntry(self.top,placeholder_text="confirmar senha",corner_radius=20)
        self.entry_senhaconfirmarcadastro.place(relx=0.2,rely=0.64,relwidth=0.6,relheight=0.08)
        # IMAGEM1 CADASTRO 
        imagem_cadastro = ctk.CTkImage(size=(55,55),light_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\cadastra.png"),dark_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\cadastra.png"))
        self.label_imagem = ctk.CTkLabel(self.top,width=0.4,text="",height=0.5,image=imagem_cadastro)
        self.label_imagem.place(relx=0.43,rely=0.04)

        self.botao_confirmar = ctk.CTkButton(self.top,text="Confirmar",command=self.add_banco_de_dados,corner_radius=20,hover_color="#2E8B57",text_color="#FFFFFF",fg_color="#3CB371")
        self.botao_confirmar.place(relx=0.33,rely=0.75,relwidth=0.32,relheight=0.1) 

        self.variada = StringVar()
        self.label_caracter = ctk.CTkLabel(self.top,text_color="#FF0000",textvariable=self.variada,width=0.4,height=0.1)
        self.label_caracter.place(relx=0.81,rely=0.47)
        
    # fazer cadastro 
    def add_banco_de_dados(self):
        loginachado = []
        login = self.entry_nomecadastro.get()
        senha = self.entry_senhacadastro.get()
        self.conectando_db()
        if len(self.entry_senhacadastro.get()) < 8:
            self.variada.set("-8 caracteres")

        elif self.entry_senhacadastro.get() != self.entry_senhaconfirmarcadastro.get():
            AVISO = messagebox.showinfo("Aviso","As senhas Devem Ser Iguais")
        else:
            valores = self.cursor.execute("SELECT login_client FROM login WHERE login_client = ?",(login,)).fetchall()
            loginachado.append(valores)
            if len(loginachado[0]) > 0:
                AVISO = messagebox.showinfo("Aviso","Login ja Registrado!")
            else:
                imagem_cadastro = ctk.CTkImage(size=(55,55),light_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\confirmado.png"),dark_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\confirmado.png"))
                self.label_imagem = ctk.CTkLabel(self.top,width=0.4,text="",height=0.5,image=imagem_cadastro)
                self.label_imagem.place(relx=0.43,rely=0.04)
                self.cursor.execute("""INSERT OR IGNORE INTO login (login_client,senha)
                VALUES(?,?)""",(login,senha))
                self.con.commit()
        self.desconectando_db()
    def conectando_db(self):
        LOCAL = Path(__file__).parent
        NOME_DB = "system_login.db"
        ABSOLUTO = LOCAL / NOME_DB
        self.con = sqlite3.connect(ABSOLUTO)
        self.cursor = self.con.cursor()
    def desconectando_db(self):
        self.cursor.close()
        self.con.close()    
    def crinado_tabela(self):
        self.conectando_db()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS login(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login_client VARCHAR(20) UNIQUE NOT NULL,
        senha INTEGER NOT NULL)"""
        )
        self.con.commit()
        self.desconectando_db()
    
    def confirmar_recuperar_senha(self):
        novasenha = self.entry_novasenha.get()

        self.cursor.execute("""UPDATE login
        SET senha = ?
        WHERE login_client = ?""",(novasenha,self.loginRecuperacao,))
        self.con.commit()
        self.desconectando_db()
        aviso = messagebox.showinfo("Sucesso","Senha alterada")
        self.frame_recuperacaosenha.destroy()
    #validar se existe o registro 
    def validar_dados(self):
        listav = []
        login1 = self.entry_login.get()
        senha1 = self.entry_senha.get()
        self.conectando_db()
        wiew = self.cursor.execute("""SELECT login_client FROM login
        WHERE login_client = ?""",(login1,)).fetchall()
        listav.append(wiew)
        if len(listav[0]) == 0:
            AVISO = messagebox.showinfo("Aviso","Conta Nao Encontrada")
        else:
            valor = self.cursor.execute("""SELECT login_client,senha FROM login
            WHERE login_client = ?""",(login1,)).fetchall()
            for var in valor:
                nome,sen = var
                if int(senha1) == sen:
                    print("entrou")
                else:
                    AVISO = messagebox.showinfo("Aviso","Senha Invalida")
            



        self.desconectando_db()
    def recuperar_senha(self):
        self.frame_recuperacaosenha = ctk.CTkFrame(self.root,width=450,height=300,corner_radius=20)
        self.frame_recuperacaosenha.place(relx=0.19,rely=0.17)

        self.entry_recuperacao = ctk.CTkEntry(self.frame_recuperacaosenha,placeholder_text="adicione seu Login")
        self.entry_recuperacao.place(relx=0.2,rely=0.4,relwidth=0.6,relheight=0.1)

        imagem_recuperar_senha = ctk.CTkImage(light_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\mudarsenha.png"),dark_image=Image.open("C:\\Users\\Usuario\\projetos_estudos\\painel_login\\imagens\\mudarsenha.png"),size=(80,80))
        label_visualrecuperar = ctk.CTkLabel(self.frame_recuperacaosenha,text="",image=imagem_recuperar_senha)
        label_visualrecuperar.place(relx=0.30,rely=0.02,relwidth=0.36,relheight=0.31)

        self.botao_verificarlogin = ctk.CTkButton(self.frame_recuperacaosenha,command=self.verificar_login_recuperação,corner_radius=20,font=("Arial", 12),text="Confirmar",hover_color="#2E8B57",text_color="#FFFFFF",fg_color="#3CB371")
        self.botao_verificarlogin.place(relx=0.35,rely=0.60,relwidth=0.3,relheight=0.08)
    def verificar_login_recuperação(self):
        loginrecachado = []
        self.loginRecuperacao = self.entry_recuperacao.get()
        self.conectando_db()
        AC = self.cursor.execute("""SELECT login_client FROM login WHERE login_client = ?""",(self.loginRecuperacao,)).fetchall()
        loginrecachado.append(AC)
        if len(loginrecachado[0]) > 0:
            self.entry_recuperacao.destroy()
            self.botao_verificarlogin.destroy()
            self.entry_novasenha = ctk.CTkEntry(self.frame_recuperacaosenha,placeholder_text="Nova senha")
            self.entry_novasenha.place(relx=0.2,rely=0.4,relwidth=0.6,relheight=0.1)

            self.botao_novasenha = ctk.CTkButton(self.frame_recuperacaosenha,command=self.confirmar_recuperar_senha,corner_radius=20,font=("Arial", 12),text="Confirmar",hover_color="#2E8B57",text_color="#FFFFFF",fg_color="#3CB371")
            self.botao_novasenha.place(relx=0.35,rely=0.60,relwidth=0.3,relheight=0.08)
        else:
            print("nao")
        





tela = InterfaceLogin()
        

