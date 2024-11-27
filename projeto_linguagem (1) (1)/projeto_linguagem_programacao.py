import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

import mysql.connector

conexao_banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="barbearia"
)
cursor = conexao_banco.cursor()

def home():
    esconder_frames()
    framehome.pack()
    janela.title("Menzinho Barber - Home")

def cadastrar():
    esconder_frames()
    framecadastrar.pack()
    janela.title("Menzinho Barber - Cadastro")

def alterar():
    esconder_frames()
    framealterar.pack()
    janela.title("Menzinho Barber - Alterar")    



def excluir():
    esconder_frames()
    frame_excluir.pack()
    janela.title("Menzinho Barber - Excluir")  


def excluir_funcionario():
    esconder_frames()
    frame_excluir_funcionario.pack()
    janela.title("Menzinho Barber - Excluir funcionário")  


def excluir_cliente():
    esconder_frames()
    frame_excluir_cliente.pack()
    janela.title("Menzinho Barber - Excluir cliente")  




def agendamento():
    esconder_frames()
    frameagendamento.pack()
    janela.title("Menzinho Barber - Gerenciar agendamentos") 

   

def adicionar_horario():
    esconder_frames()
    frame_agendarhorario.pack()


def alterar_horario():
    esconder_frames()
    frame_alterarhorario.pack()

def cadastrar_funcionario():
    esconder_frames()
    framecadastrar_funcionario.pack()
    janela.title("Menzinho Barber - Cadastro Funcionário")

def cadastro_funcionario_idcorreto():
    esconder_frames()
    framecadastro_funcionario_idcorreto.pack()


def cadastro_funcionario_idincorreto():
    esconder_frames()   
    framecadastro_funcionario_idincorreto.pack()


def cadastrar_cliente():
    esconder_frames()
    framecadastrar_cliente.pack()
    janela.title("Menzinho Barber - Cadastro Cliente")

def cadastro_cliente_idcorreto():
    esconder_frames()
    framecadastro_cliente_idcorreto.pack()

def cadastro_cliente_idincorreto():
    esconder_frames()
    framecadastro_cliente_idincorreto.pack()




def cadastrar_servico():
    esconder_frames()
    framecadastrar_servico.pack()
    janela.title("Menzinho Barber - Cadastro Cliente")


def alterar_cliente():
    esconder_frames()
    framealterar_cliente.pack()
    janela.title("Menzinho Barber - Alterar Cliente")


def alterar_funcionario():
    esconder_frames()
    framealterar_funcionario.pack()
    janela.title("Menzinho Barber - Alterar Funcionário")


def exibir():
    esconder_frames()
    frameexibir.pack()
    janela.title("Menzinho Barber - Exibir")  

def exibir_funcionario():
    esconder_frames()
    frameexibir_funcionario.pack()
    janela.title("Menzinho Barber - Exibir funcionário") 

    for item in tabela_funcionarios.get_children():
        tabela_funcionarios.delete(item)
    

    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    

    for funcionario in funcionarios:
        tabela_funcionarios.insert("", "end", values=funcionario)






def exibir_cliente():
    esconder_frames()
    frameexibir_cliente.pack()
    janela.title("Menzinho Barber - Exibir cliente") 
        

    for item in tabela_clientes.get_children():
        tabela_clientes.delete(item)
    

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    

    for cliente in clientes:
        tabela_clientes.insert("", "end", values=cliente)

def exibir_servico():
    esconder_frames()
    frameexibir_servico.pack()
    janela.title("Menzinho Barber - Exibir serviços") 
        

    for item in tabela_servicos.get_children():
        tabela_servicos.delete(item)
    

    cursor.execute("SELECT * FROM servicos")
    servicos = cursor.fetchall()
    

    for servico in servicos:
        tabela_servicos.insert("", "end", values=servico)


def confirmar_id_funcionario():
    id_funcionario = id_funcionarioo.get() 
    if id_funcionario == '':
        cadastro_funcionario_idincorreto() 
        return
    cursor.execute(f"SELECT * FROM funcionarios WHERE id_funcionario = {id_funcionario}")
    dados_funcionario = cursor.fetchall()
    if not dados_funcionario:
        cadastro_funcionario_idcorreto()
    else:
        cadastro_funcionario_idincorreto()


def confirmar_id_cliente():
    id_cliente = idcliente1.get() 
    if id_cliente == '':
        cadastro_funcionario_idincorreto() 
        return
    cursor.execute(f"SELECT * FROM clientes WHERE id_cliente = {id_cliente}")
    dados_cliente = cursor.fetchall()
    if not dados_cliente:
        cadastro_cliente_idcorreto()
    else:
        cadastro_cliente_idincorreto()

def adicionar_funcionario():
    id_funcionario = id_funcionarioo.get() 
    nome_funcionario = nomefuncionario1.get()
    cargo_funcionario=cargofuncionario1.get()
    telefone_funcionario=telefonefuncionario1.get()
    cursor.execute(f"INSERT INTO funcionarios (id_funcionario, nome, cargo, telefone) VALUES ({id_funcionario}, '{nome_funcionario}', '{cargo_funcionario}', '{telefone_funcionario}')")
    conexao_banco.commit() 
    id_funcionarioo.delete(0, tk.END)
    nomefuncionario1.delete(0, tk.END)
    cargofuncionario1.delete(0, tk.END)
    telefonefuncionario1.delete(0, tk.END)  
    home()
    messagebox.showinfo("Sucesso", "Funcionário adicionado  com sucesso!")

def adicionar_cliente():
    id_cliente=idcliente1.get()
    nome_cliente=nomecliente1.get()
    telefone_cliente=telefonecliente1.get()
    cursor.execute(f"INSERT INTO clientes (id_cliente,nome,telefone) VALUES ({id_cliente}, '{nome_cliente}', '{telefone_cliente}') ")
    conexao_banco.commit()
    home()
    idcliente1.delete(0, tk.END)
    nomecliente1.delete(0, tk.END)
    telefonecliente1.delete(0, tk.END)  
    messagebox.showinfo("Sucesso", "Cliente adicionado  com sucesso!")


def confirmar_id_alteracaofuncionario():
    id_funcionario=id_funcionario2.get()
    if id_funcionario=='':
        texto=tk.Label(framealterar_funcionario,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='Você precisa digitar um ID')
        texto.grid(row=5, column=0, padx=10, pady=10)
        return
    else:
        cursor.execute(f"SELECT * FROM funcionarios WHERE id_funcionario = {id_funcionario}")
        dados_funcionario = cursor.fetchall()
        if not dados_funcionario:
            aviso = tk.Label(framealterar_funcionario,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text=' ID não existe no sistema. ')  
            aviso.grid(row=5, column=0, padx=10, pady=10)
        else:
            idcorreto_alteracaofuncionario()



def idcorreto_alteracaofuncionario():
    esconder_frames()
    opcoes_alteracao_funcionario.pack()

def alteracao_nome_funcionario():
    esconder_frames()
    alteracao_nomefuncionario.pack()

def confirmar_alteracao_nomefuncionario():
    id_funcionario=id_funcionario2.get()
    nomefuncionario=nomefuncionario2.get()
    if nomefuncionario=='':
        texto=tk.Label(alteracao_nomefuncionario,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='Você precisa digitar um nome')  
        texto.grid(row=5, column=0, padx=10, pady=10)
    else:
        cursor.execute(f"UPDATE funcionarios SET nome = '{nomefuncionario}' WHERE id_funcionario = {id_funcionario}")
        conexao_banco.commit()
        home()
        messagebox.showinfo("Sucesso", "Nome do funcionário alterado com sucesso!")

def alteracao_cargo_funcionario():
    esconder_frames()
    alteracao_cargofuncionario.pack()

def confirmar_alteracao_cargofuncionario():
    id_funcionario=id_funcionario2.get()
    cargofuncionario=cargofuncionario2.get()
    if cargofuncionario=='':
        texto=tk.Label(alteracao_cargofuncionario,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='Você precisa digitar um cargo')  
        texto.grid(row=5, column=0, padx=10, pady=10)
    else:
        cursor.execute(f"UPDATE funcionarios SET cargo = '{cargofuncionario}' WHERE id_funcionario = {id_funcionario}")
        conexao_banco.commit()
        home()  
        messagebox.showinfo("Sucesso", "Cargo do funcionário alterado com sucesso!")  

def alteracao_telefone_funcionario():
    esconder_frames()
    alteracao_telefonefuncionario.pack()

def confirmar_alteracao_telefonefuncionario():
    id_funcionario=id_funcionario2.get()
    telefonefuncionario=telefonefuncionario2.get()
    cursor.execute(f"UPDATE funcionarios SET telefone = {telefonefuncionario} WHERE id_funcionario = {id_funcionario}")
    conexao_banco.commit()
    home()   
    messagebox.showinfo("Sucesso", "Telefone do funcionário alterado com sucesso!")


def confirmar_id_alteracaocliente():
    id_cliente=id_cliente2.get()
    if id_cliente=='':
        texto=tk.Label(framealterar_cliente,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='Você precisa digitar um ID')
        texto.grid(row=5, column=0, padx=10, pady=10)
        return
    else:
        cursor.execute(f"SELECT * FROM clientes WHERE id_cliente = {id_cliente}")
        dados_cliente = cursor.fetchall()
        if not dados_cliente:
            aviso = tk.Label(framealterar_cliente,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text=' ID não existe no sistema. ')  
            aviso.grid(row=5, column=0, padx=10, pady=10)
        else:
            idcorreto_alteracao_cliente()



def idcorreto_alteracao_cliente():
    esconder_frames()
    opcoes_alteracao_cliente.pack()

def alteracao_nome_cliente():
    esconder_frames()
    alteracao_nomecliente.pack()

def confirmar_alteracao_nomecliente():
    id_cliente=id_cliente2.get()
    nomecliente=nomecliente2.get()
    if nomecliente=='':
        texto=tk.Label(alteracao_nomecliente,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='Você precisa digitar um nome')  
        texto.grid(row=5, column=0, padx=10, pady=10)
    else:
        cursor.execute(f"UPDATE clientes SET nome = '{nomecliente}' WHERE id_cliente = {id_cliente}")
        conexao_banco.commit()
        home()
        messagebox.showinfo("Sucesso", "Nome do cliente alterado com sucesso!")

def alteracao_telefone_cliente():
    esconder_frames()
    alteracao_telefonecliente.pack()

def confirmar_alteracao_telefonecliente():
    id_cliente=id_cliente2.get()
    telefonecliente=telefonecliente2.get()
    cursor.execute(f"UPDATE clientes SET telefone = {telefonecliente} WHERE id_cliente = {id_cliente}")
    conexao_banco.commit()
    home()  
    messagebox.showinfo("Sucesso", "Telefone do cliente alterado com sucesso!")

def confirmar_excluirfuncionario():
    id_funcionario=id_funcionario3.get()
    if id_funcionario=='':
        texto=tk.Label(frame_excluir_funcionario,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='Você precisa digitar um ID')
        texto.grid(row=5, column=0, padx=10, pady=10)
        return
    else:
        cursor.execute(f"SELECT * FROM funcionarios WHERE id_funcionario = {id_funcionario}")
        dados_funcionario = cursor.fetchall()
        if not dados_funcionario:
            aviso = tk.Label(frame_excluir_funcionario,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text=' ID não existe no sistema. ')  
            aviso.grid(row=5, column=0, padx=10, pady=10)
        else:
            cursor.execute(f"DELETE FROM funcionarios WHERE id_funcionario = {id_funcionario}")
            conexao_banco.commit()
            home()
            messagebox.showinfo("Sucesso", "Funcionário excluido com sucesso!")
def confirmar_excluircliente():
    id_cliente=id_cliente3.get()
    if id_cliente=='':
        texto=tk.Label(frame_excluir_cliente,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='Você precisa digitar um ID')
        texto.grid(row=5, column=0, padx=10, pady=10)
        return
    else:
        cursor.execute(f"SELECT * FROM clientes WHERE id_cliente = {id_cliente}")
        dados_cliente = cursor.fetchall()
        if not dados_cliente:
            aviso = tk.Label(frame_excluir_cliente,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text=' ID não existe no sistema. ')  
            aviso.grid(row=5, column=0, padx=10, pady=10)
        else:
            cursor.execute(f"DELETE FROM clientes WHERE id_cliente = {id_cliente}")
            conexao_banco.commit()
            home()
            messagebox.showinfo("Sucesso", "Funcionário excluido com sucesso!")

def confirmar_id_servico():
    id_servico = idservico1.get() 
    if id_servico == '':
        cadastro_servico_idincorreto() 
        return
    cursor.execute(f"SELECT * FROM servicos WHERE id_servico = {id_servico}")
    dados_servico = cursor.fetchall()
    if not dados_servico:
        cadastro_servico_idcorreto()
    else:
        cadastro_servico_idincorreto()

def cadastro_servico_idincorreto():
    esconder_frames()
    framecadastro_servico_idincorreto.pack()


def cadastro_servico_idcorreto():
    esconder_frames()
    framecadastro_servico_idcorreto.pack()


def adicionar_servico():
    id_servico=idservico1.get()
    nome_servico=nomeservico1.get()
    preco_servico=precoservico1.get()
    cursor.execute(f"INSERT INTO servicos (id_servico,nome,preco) VALUES ({id_servico}, '{nome_servico}', '{preco_servico}') ")
    conexao_banco.commit()
    home()
    messagebox.showinfo("Sucesso", "Serviço adicionado com sucesso!")
    idservico1.delete(0, tk.END)
    nomeservico1.delete(0, tk.END)
    precoservico1.delete(0, tk.END)  

def alterar_servico():
    esconder_frames()
    framealterar_servico.pack()

def confirmar_id_alteracaoservico():
    id_servico=id_servico2.get()
    if id_servico=='':
        texto=tk.Label(framealterar_servico,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='Você precisa digitar um ID')
        texto.grid(row=5, column=0, padx=10, pady=10)
        return
    else:
        cursor.execute(f"SELECT * FROM servicos WHERE id_servico = {id_servico}")
        dados_servico = cursor.fetchall()
        if not dados_servico:
            aviso = tk.Label(framealterar_servico,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text=' ID não existe no sistema. ')  
            aviso.grid(row=5, column=0, padx=10, pady=10)
        else:
            idcorreto_alteracao_servico()

def idcorreto_alteracao_servico():
    esconder_frames()
    opcoes_alteracao_servico.pack()

def alteracao_nome_servico():
    esconder_frames()
    framealteracao_nomeservico.pack()

def alteracao_preco_servico():
    esconder_frames()
    framealteracao_precoservico.pack()

def confirmar_alteracao_nomeservico():
    id_servico=id_servico2.get()
    nome_servico=nomeservico2.get()
    cursor.execute(f"UPDATE servicos SET nome = '{nome_servico}' WHERE id_servico = {id_servico}")
    conexao_banco.commit()
    home()  
    messagebox.showinfo("Sucesso", "Nome do serviço alterado com sucesso!")

def confirmar_alteracao_precoservico():
    id_servico=id_servico2.get()
    preco_servico=precoservico2.get()
    cursor.execute(f"UPDATE servicos SET preco = '{preco_servico}' WHERE id_servico = {id_servico}")
    conexao_banco.commit()
    home()  
    messagebox.showinfo("Sucesso", "Preço do serviço alterado com sucesso!")



def excluir_servico():
    esconder_frames()
    frame_excluir_servico.pack()
    janela.title("Menzinho Barber - Excluir serviço")  

def confirmar_excluirservico():
    id_servico=id_servico3.get()
    if id_servico=='':
        texto=tk.Label(frame_excluir_servico,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='Você precisa digitar um ID')
        texto.grid(row=5, column=0, padx=10, pady=10)
        return
    else:
        cursor.execute(f"SELECT * FROM servicos WHERE id_servico = {id_servico}")
        dados_servico = cursor.fetchall()
        if not dados_servico:
            aviso = tk.Label(frame_excluir_servico,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text=' ID não existe no sistema. ')  
            aviso.grid(row=5, column=0, padx=10, pady=10)
        else:
            cursor.execute(f"DELETE FROM servicos WHERE id_servico = {id_servico}")
            conexao_banco.commit()
            home()
            messagebox.showinfo("Sucesso", "Serviço excluido com sucesso!")




def validar_hora(hora_str):
    if len(hora_str) != 5 or hora_str[2] != ':':
        return False
    horas, minutos = hora_str.split(':')
    if not (horas.isdigit() and minutos.isdigit()):
        return False
    horas, minutos = int(horas), int(minutos)
    return 0 <= horas <= 23 and 0 <= minutos <= 59


def verificar_id_existente(id, tabela, coluna):
    query = f"SELECT 1 FROM {tabela} WHERE {coluna} = %s"
    cursor.execute(query, (id,))
    return cursor.fetchone() is not None


def agendar():
    id_agendamento = id_agendamento_entry.get()
    id_funcionario = id_funcionario_entry.get()
    id_servico = id_servico_entry.get()
    id_cliente = id_cliente_entry.get()
    data_agendamento = data_entry.get()
    hora_agendamento = hora_entry.get()


    if not id_agendamento or not id_funcionario or not id_servico or not id_cliente or not data_agendamento or not hora_agendamento:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return


    if not validar_hora(hora_agendamento):
        messagebox.showerror("Erro", "Hora inválida! Use o formato HH:MM.")
        return

    cursor.execute("SELECT 1 FROM agendamentos WHERE id_agendamento = %s", (id_agendamento,))
    if cursor.fetchone():
        messagebox.showerror("Erro", "O ID do agendamento já existe.")
        return


    if not verificar_id_existente(id_funcionario, "funcionarios", "id_funcionario"):
        messagebox.showerror("Erro", "O ID do funcionário não existe. Insira um ID válido.")
        return

    if not verificar_id_existente(id_servico, "servicos", "id_servico"):
        messagebox.showerror("Erro", "O ID do serviço não existe. Insira um ID válido.")
        return

    if not verificar_id_existente(id_cliente, "clientes", "id_cliente"):
        messagebox.showerror("Erro", "O ID do cliente não existe. Insira um ID válido.")
        return


    query = f"""
        INSERT INTO agendamentos (id_agendamento, id_funcionario, id_servico, id_cliente, data, hora)
        VALUES ({id_agendamento}, {id_funcionario}, {id_servico}, {id_cliente}, '{data_agendamento}','{hora_agendamento}' )
    """
    cursor.execute(query)
    conexao_banco.commit()
    home()

    messagebox.showinfo("Sucesso", "Agendamento realizado com sucesso!")


    id_agendamento_entry.delete(0, tk.END)
    id_funcionario_entry.delete(0, tk.END)
    id_servico_entry.delete(0, tk.END)
    id_cliente_entry.delete(0, tk.END)
    data_entry.set_date("") 
    hora_entry.delete(0, tk.END)
    



campo_selecionado = None

def configurar_alteracao(campo):

    global campo_selecionado
    campo_selecionado = campo 
    instrucoes_label.config(text=f"Digite o novo valor para {campo.replace('_', ' ')}:")


def alterar_campo():

    global campo_selecionado


    if not campo_selecionado:
        messagebox.showerror("Erro", "Selecione um campo para alterar.")
        return

    id_agendamento = id_agendamento_entry2.get()
    novo_valor = valor_alterar_entry.get()

    if not id_agendamento:
        messagebox.showerror("Erro", "Informe o ID do agendamento para alterar.")
        return

    cursor.execute(f"SELECT 1 FROM agendamentos WHERE id_agendamento = {id_agendamento}")
    if not cursor.fetchone():
        messagebox.showerror("Erro", "O ID do agendamento não existe.")
        return

    if campo_selecionado in ["id_cliente", "id_funcionario", "id_servico"]:
        if not novo_valor:
            messagebox.showerror("Erro", f"O campo {campo_selecionado} não pode ser vazio.")
            return
        tabela = campo_selecionado.replace("id_", "") + "s" 
        if not verificar_id_existente(novo_valor, tabela, campo_selecionado):
            messagebox.showerror("Erro", f"O {campo_selecionado} informado não existe.")
            return

    elif campo_selecionado == "data_agendamento":
        if not novo_valor:
            messagebox.showerror("Erro", "A data não pode ser vazia.")
            return

    elif campo_selecionado == "hora_agendamento":
        if not validar_hora(novo_valor):
            messagebox.showerror("Erro", "Hora inválida! Use o formato HH:MM.")
            return

    update_query = f"UPDATE agendamentos SET {campo_selecionado} = '{novo_valor}' WHERE id_agendamento = {id_agendamento}"
    

    cursor.execute(update_query)
    conexao_banco.commit()


    messagebox.showinfo("Sucesso", f"{campo_selecionado.replace('_', ' ').capitalize()} alterado com sucesso!")


    id_agendamento_entry.delete(0, tk.END)
    valor_alterar_entry.delete(0, tk.END)
    home()


def remover_horario():
    esconder_frames()
    frame_removerhorario.pack()

def excluir_agendamento():
    id_agendamento = id_agendamento_entry3.get()

    if not id_agendamento:
        messagebox.showerror("Erro", "Por favor, informe o ID do agendamento.")
        return

    cursor.execute(f"SELECT 1 FROM agendamentos WHERE id_agendamento = {id_agendamento}")
    if not cursor.fetchone():
        messagebox.showerror("Erro", "O ID do agendamento não existe.")
        return


    cursor.execute(f"DELETE FROM agendamentos WHERE id_agendamento = {id_agendamento}")
    conexao_banco.commit()
    home()

    messagebox.showinfo("Sucesso", "Agendamento excluído com sucesso!")


    id_agendamento_entry.delete(0, tk.END)


def exibir_horarios():

    esconder_frames()
    frame_exibirhorario.pack()
    janela.title("Menzinho Barber - Exibir Agendamentos")


    for item in tabela_agendamentos.get_children():
        tabela_agendamentos.delete(item)


    consulta = """
        SELECT agendamentos.id_agendamento,clientes.nome,funcionarios.nome,servicos.nome,agendamentos.data,agendamentos.hora
        FROM agendamentos
        JOIN clientes  ON agendamentos.id_cliente = clientes.id_cliente
        JOIN funcionarios  ON agendamentos.id_funcionario = funcionarios.id_funcionario
        JOIN servicos  ON agendamentos.id_servico = servicos.id_servico
        ORDER BY agendamentos.data , agendamentos.hora 
    """
    cursor.execute(consulta)
    agendamentos = cursor.fetchall()


    for agendamento in agendamentos:
        tabela_agendamentos.insert("", "end", values=agendamento)







def esconder_frames():
    for i in [framehome, framecadastrar, framecadastrar_funcionario, framecadastrar_cliente,
                  frameexibir, frameexibir_funcionario, frameexibir_cliente, framealterar,
                  framealterar_funcionario, framealterar_cliente,framecadastro_cliente_idcorreto,
                  framecadastro_cliente_idincorreto,framecadastro_funcionario_idcorreto,
                  framecadastro_funcionario_idincorreto,alteracao_nomefuncionario,
                  opcoes_alteracao_funcionario,framealterar_cliente,opcoes_alteracao_cliente,
                  alteracao_nomecliente,alteracao_cargofuncionario,alteracao_telefonefuncionario,alteracao_telefonecliente,
                  frame_excluir_funcionario,frame_excluir,frame_excluir_cliente, framecadastrar_servico,framecadastro_servico_idcorreto,
                  framecadastro_servico_idincorreto, frameagendamento, framealterar_servico, framealteracao_nomeservico,opcoes_alteracao_servico
                  ,frame_excluir_servico,framealteracao_precoservico,frameexibir_servico,frame_agendarhorario,frame_alterarhorario,frame_exibirhorario,
                  frame_removerhorario]:
        i.pack_forget()

    
    




janela = tk.Tk()
janela.geometry("800x600")


framehome = tk.Frame(janela)
titulo = tk.Label(framehome, text='Opções: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(framehome, text="Cadastrar", command=cadastrar)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(framehome, text="Alterar", command=alterar)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = tk.Button(framehome, text="Excluir", command=excluir)
botao.grid(row=3, column=0, padx=10, pady=10)

botao = tk.Button(framehome, text="Gerenciar agendamentos", command=agendamento)
botao.grid(row=4, column=0, padx=10, pady=10)

botao = tk.Button(framehome, text="Exibir", command=exibir)
botao.grid(row=5, column=0, padx=10, pady=10)

framehome.pack()  


framecadastrar = tk.Frame(janela)
titulo = tk.Label(framecadastrar, text='Opções: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(framecadastrar, text="Cadastrar funcionário", command=cadastrar_funcionario)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(framecadastrar, text="Cadastrar Cliente", command=cadastrar_cliente)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = tk.Button(framecadastrar, text="Cadastrar serviço", command=cadastrar_servico)
botao.grid(row=3, column=0, padx=10, pady=10)


botao = tk.Button(framecadastrar, text="Voltar para o menu", command=home)
botao.grid(row=4, column=0, padx=10, pady=10)




framecadastrar_funcionario=tk.Frame(janela)


titulo = tk.Label(framecadastrar_funcionario, text='Formulário: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

id_funcionarioo = tk.Entry(framecadastrar_funcionario,width=25, bg='white', font=('Comic Sans MS', '10'))
id_funcionarioo.grid(row=1,column=1, padx=10, pady=10)
id = tk.Label(framecadastrar_funcionario,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='ID do funcionário:')
id.grid(row=1, column=0, padx=10, pady=10)
botao=tk.Button(framecadastrar_funcionario,text="Confirmar", command=confirmar_id_funcionario)
botao.grid(row=2,column=0, padx=10, pady=10)
botao2=tk.Button(framecadastrar_funcionario,text="Voltar para o menu", command=home)
botao2.grid(row=2,column=1, padx=10, pady=10)


framecadastro_funcionario_idcorreto=tk.Frame(janela)

nomefuncionario1 = tk.Entry(framecadastro_funcionario_idcorreto,width=25, bg='white', font=('Comic Sans MS', '10'))
nomefuncionario1.grid(row=0,column=1, padx=10, pady=10)
nome = tk.Label(framecadastro_funcionario_idcorreto,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Nome do funcionário:')
nome.grid(row=0, column=0, padx=10, pady=10)

cargofuncionario1 = tk.Entry(framecadastro_funcionario_idcorreto,width=25, bg='white', font=('Comic Sans MS', '10'))
cargofuncionario1.grid(row=1,column=1, padx=10, pady=10)
cargo = tk.Label(framecadastro_funcionario_idcorreto,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Cargo do funcionário:')
cargo.grid(row=1, column=0, padx=10, pady=10)

telefonefuncionario1 = tk.Entry(framecadastro_funcionario_idcorreto,width=25, bg='white', font=('Comic Sans MS', '10'))
telefonefuncionario1.grid(row=2,column=1, padx=10, pady=10)
telefone = tk.Label(framecadastro_funcionario_idcorreto,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Telefone do funcionário:')
telefone.grid(row=2, column=0, padx=10, pady=10)
botao=tk.Button(framecadastro_funcionario_idcorreto,text="confirmar", command=adicionar_funcionario)
botao.grid(row=3,column=0, padx=10, pady=10)
botao2=tk.Button(framecadastro_funcionario_idcorreto,text="Cancelar e voltar para menu",command=home)
botao2.grid(row=4,column=0, padx=10, pady=10)







framecadastro_funcionario_idincorreto=tk.Frame(janela)

aviso = tk.Label(framecadastro_funcionario_idincorreto,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='ID vazio ou já cadastrado no sistema')  
aviso.grid(row=0, column=0, padx=10, pady=10)

botao=tk.Button(framecadastro_funcionario_idincorreto,text="Voltar para cadastro",command=cadastrar_funcionario)
botao.grid(row=1,column=0, padx=10, pady=10)

botao2=tk.Button(framecadastro_funcionario_idincorreto,text="Voltar para menu",command=home)
botao2.grid(row=3,column=0, padx=10, pady=10)




framecadastrar_cliente=tk.Frame(janela)
titulo = tk.Label(framecadastrar_cliente, text='Formulário: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

idcliente1 = tk.Entry(framecadastrar_cliente,width=25, bg='white', font=('Comic Sans MS', '10'))
idcliente1.grid(row=1,column=1, padx=10, pady=10)
id = tk.Label(framecadastrar_cliente,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='ID do cliente:')
id.grid(row=1, column=0, padx=10, pady=10)
botao=tk.Button(framecadastrar_cliente,text="confirmar", command=confirmar_id_cliente)
botao.grid(row=2,column=0, padx=10, pady=10)
botao2=tk.Button(framecadastrar_cliente,text="Voltar para o menu", command=home)
botao2.grid(row=2,column=1, padx=10, pady=10)



framecadastro_cliente_idcorreto=tk.Frame(janela)

nomecliente1 = tk.Entry(framecadastro_cliente_idcorreto,width=25, bg='white', font=('Comic Sans MS', '10'))
nomecliente1.grid(row=2,column=1, padx=10, pady=10)
nome = tk.Label(framecadastro_cliente_idcorreto,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Nome do cliente:')
nome.grid(row=2, column=0, padx=10, pady=10)
telefonecliente1 = tk.Entry(framecadastro_cliente_idcorreto,width=25, bg='white', font=('Comic Sans MS', '10'))
telefonecliente1.grid(row=4,column=1, padx=10, pady=10)
telefone = tk.Label(framecadastro_cliente_idcorreto,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Telefone do cliente:')
telefone.grid(row=4, column=0, padx=10, pady=10)
botao=tk.Button(framecadastro_cliente_idcorreto,text="confirmar", command=adicionar_cliente)
botao.grid(row=5,column=0, padx=10, pady=10)
botao2=tk.Button(framecadastro_cliente_idcorreto,text="Cancelar e voltar para menu",command=home)
botao2.grid(row=6,column=0, padx=10, pady=10)


framecadastro_cliente_idincorreto=tk.Frame(janela)
aviso = tk.Label(framecadastro_cliente_idincorreto,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='ID vazio ou já cadastrado no sistema ')  
aviso.grid(row=0, column=0, padx=10, pady=10)
botao=tk.Button(framecadastro_cliente_idincorreto,text="Voltar para cadastro",command=cadastrar_cliente)
botao.grid(row=1,column=0, padx=10, pady=10)
botao2=tk.Button(framecadastro_cliente_idincorreto,text="Voltar para menu",command=home)
botao2.grid(row=3,column=0, padx=10, pady=10)

framecadastrar_servico=tk.Frame(janela)
titulo = tk.Label(framecadastrar_servico, text='Formulário: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

idservico1 = tk.Entry(framecadastrar_servico,width=25, bg='white', font=('Comic Sans MS', '10'))
idservico1.grid(row=1,column=1, padx=10, pady=10)
id = tk.Label(framecadastrar_servico,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='ID do serviço:')
id.grid(row=1, column=0, padx=10, pady=10)
botao=tk.Button(framecadastrar_servico,text="confirmar", command=confirmar_id_servico)
botao.grid(row=2,column=0, padx=10, pady=10)
botao2=tk.Button(framecadastrar_servico,text="Voltar para o menu", command=home)
botao2.grid(row=2,column=1, padx=10, pady=10)

framecadastro_servico_idcorreto=tk.Frame(janela)
nomeservico1 = tk.Entry(framecadastro_servico_idcorreto,width=25, bg='white', font=('Comic Sans MS', '10'))
nomeservico1.grid(row=0,column=1, padx=10, pady=10)
nome = tk.Label(framecadastro_servico_idcorreto,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Nome do serviço:')
nome.grid(row=0, column=0, padx=10, pady=10)

precoservico1 = tk.Entry(framecadastro_servico_idcorreto,width=25, bg='white', font=('Comic Sans MS', '10'))
precoservico1.grid(row=1,column=1, padx=10, pady=10)
cargo = tk.Label(framecadastro_servico_idcorreto,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Preço do serviço:')
cargo.grid(row=1, column=0, padx=10, pady=10)


botao=tk.Button(framecadastro_servico_idcorreto,text="confirmar", command=adicionar_servico)
botao.grid(row=3,column=0, padx=10, pady=10)
botao2=tk.Button(framecadastro_servico_idcorreto,text="Cancelar e voltar para menu",command=home)
botao2.grid(row=4,column=0, padx=10, pady=10)

framecadastro_servico_idincorreto=tk.Frame(janela)
aviso = tk.Label(framecadastro_servico_idincorreto,font=('Arial', '11', 'bold'), fg='red', bg='#191970', text='ID vazio ou já cadastrado no sistema ')  
aviso.grid(row=0, column=0, padx=10, pady=10)
botao=tk.Button(framecadastro_servico_idincorreto,text="Voltar para cadastro",command=cadastrar_servico)
botao.grid(row=1,column=0, padx=10, pady=10)
botao2=tk.Button(framecadastro_servico_idincorreto,text="Voltar para menu",command=home)
botao2.grid(row=3,column=0, padx=10, pady=10)






framealterar=tk.Frame(janela)

titulo = tk.Label(framealterar, text='Opções: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(framealterar, text="Alterar funcionário", command=alterar_funcionario)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(framealterar, text="Alterar Cliente", command=alterar_cliente)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = tk.Button(framealterar, text="Alterar serviço", command=alterar_servico)
botao.grid(row=3, column=0, padx=10, pady=10)

botao = tk.Button(framealterar, text="Voltar para o menu", command=home)
botao.grid(row=4, column=0, padx=10, pady=10)

framealterar_servico=tk.Frame(janela)
titulo = tk.Label(framealterar_servico, text='Coloque o ID do serviço que você deseja alterar: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

id_servico2 = tk.Entry(framealterar_servico,width=25, bg='white', font=('Comic Sans MS', '10'))
id_servico2.grid(row=1,column=1, padx=10, pady=10)
id = tk.Label(framealterar_servico,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='ID do serviço:')
id.grid(row=1, column=0, padx=10, pady=10)
botao=tk.Button(framealterar_servico,text="Confirmar", command=confirmar_id_alteracaoservico)
botao.grid(row=2,column=0, padx=10, pady=10)
botao2=tk.Button(framealterar_servico,text="Voltar para o menu", command=home)
botao2.grid(row=2,column=1, padx=10, pady=10)

opcoes_alteracao_servico=tk.Frame(janela)
titulo = tk.Label(opcoes_alteracao_servico, text='Opções: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_servico, text="Alterar nome do serviço", command=alteracao_nome_servico)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_servico, text="Alterar preço do serviço", command=alteracao_preco_servico)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_servico, text="Voltar para menu", command=home)
botao.grid(row=3, column=0, padx=10, pady=10)

framealteracao_nomeservico=tk.Frame(janela)
nomeservico2 = tk.Entry(framealteracao_nomeservico,width=25, bg='white', font=('Comic Sans MS', '10'))
nomeservico2.grid(row=2,column=1, padx=10, pady=10)
nome = tk.Label(framealteracao_nomeservico,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Novo nome do serviço:')
nome.grid(row=2, column=0, padx=10, pady=10)
botao=tk.Button(framealteracao_nomeservico,text="Confirmar", command=confirmar_alteracao_nomeservico)
botao.grid(row=3,column=0, padx=10, pady=10)
botao2=tk.Button(framealteracao_nomeservico,text="Voltar para o menu", command=home)
botao2.grid(row=3,column=1, padx=10, pady=10)

framealteracao_precoservico=tk.Frame(janela)
precoservico2 = tk.Entry(framealteracao_precoservico,width=25, bg='white', font=('Comic Sans MS', '10'))
precoservico2.grid(row=2,column=1, padx=10, pady=10)
nome = tk.Label(framealteracao_precoservico,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Novo preço do serviço:')
nome.grid(row=2, column=0, padx=10, pady=10)
botao=tk.Button(framealteracao_precoservico,text="Confirmar", command=confirmar_alteracao_precoservico)
botao.grid(row=3,column=0, padx=10, pady=10)
botao2=tk.Button(framealteracao_precoservico,text="Voltar para o menu", command=home)
botao2.grid(row=3,column=1, padx=10, pady=10)





framealterar_funcionario=tk.Frame(janela)
titulo = tk.Label(framealterar_funcionario, text='Coloque o ID do funcionário que você deseja alterar: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

id_funcionario2 = tk.Entry(framealterar_funcionario,width=25, bg='white', font=('Comic Sans MS', '10'))
id_funcionario2.grid(row=1,column=1, padx=10, pady=10)
id = tk.Label(framealterar_funcionario,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='ID do funcionário:')
id.grid(row=1, column=0, padx=10, pady=10)
botao=tk.Button(framealterar_funcionario,text="Confirmar", command=confirmar_id_alteracaofuncionario)
botao.grid(row=2,column=0, padx=10, pady=10)
botao2=tk.Button(framealterar_funcionario,text="Voltar para o menu", command=home)
botao2.grid(row=2,column=1, padx=10, pady=10)

opcoes_alteracao_funcionario=tk.Frame(janela)
titulo = tk.Label(opcoes_alteracao_funcionario, text='Opções: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_funcionario, text="Alterar nome", command=alteracao_nome_funcionario)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_funcionario, text="Alterar cargo", command=alteracao_cargo_funcionario)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_funcionario, text="Alterar telefone", command=alteracao_telefone_funcionario)
botao.grid(row=3, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_funcionario, text="Voltar para menu", command=home)
botao.grid(row=4, column=0, padx=10, pady=10)

alteracao_nomefuncionario=tk.Frame(janela)
nomefuncionario2 = tk.Entry(alteracao_nomefuncionario,width=25, bg='white', font=('Comic Sans MS', '10'))
nomefuncionario2.grid(row=2,column=1, padx=10, pady=10)
nome = tk.Label(alteracao_nomefuncionario,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Novo nome do funcionário:')
nome.grid(row=2, column=0, padx=10, pady=10)
botao=tk.Button(alteracao_nomefuncionario,text="Confirmar", command=confirmar_alteracao_nomefuncionario)
botao.grid(row=3,column=0, padx=10, pady=10)
botao2=tk.Button(alteracao_nomefuncionario,text="Voltar para o menu", command=home)
botao2.grid(row=3,column=1, padx=10, pady=10)

alteracao_cargofuncionario=tk.Frame(janela)
cargofuncionario2 = tk.Entry(alteracao_cargofuncionario,width=25, bg='white', font=('Comic Sans MS', '10'))
cargofuncionario2.grid(row=2,column=1, padx=10, pady=10)
nome = tk.Label(alteracao_cargofuncionario,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Novo cargo do funcionário:')
nome.grid(row=2, column=0, padx=10, pady=10)
botao=tk.Button(alteracao_cargofuncionario,text="Confirmar", command=confirmar_alteracao_cargofuncionario)
botao.grid(row=3,column=0, padx=10, pady=10)
botao2=tk.Button(alteracao_cargofuncionario,text="Voltar para o menu", command=home)
botao2.grid(row=3,column=1, padx=10, pady=10)

alteracao_telefonefuncionario=tk.Frame(janela)
telefonefuncionario2 = tk.Entry(alteracao_telefonefuncionario,width=25, bg='white', font=('Comic Sans MS', '10'))
telefonefuncionario2.grid(row=2,column=1, padx=10, pady=10)
telefone = tk.Label(alteracao_telefonefuncionario,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Novo telefone do funcionário:')
telefone.grid(row=2, column=0, padx=10, pady=10)
botao=tk.Button(alteracao_telefonefuncionario,text="Confirmar", command=confirmar_alteracao_telefonefuncionario)
botao.grid(row=3,column=0, padx=10, pady=10)
botao2=tk.Button(alteracao_telefonefuncionario,text="Voltar para o menu", command=home)
botao2.grid(row=3,column=1, padx=10, pady=10)





framealterar_cliente=tk.Frame(janela)
titulo = tk.Label(framealterar_cliente, text='Coloque o ID do cliente que você deseja alterar: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

id_cliente2 = tk.Entry(framealterar_cliente,width=25, bg='white', font=('Comic Sans MS', '10'))
id_cliente2.grid(row=1,column=1, padx=10, pady=10)
id = tk.Label(framealterar_cliente,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='ID do cliente:')
id.grid(row=1, column=0, padx=10, pady=10)
botao=tk.Button(framealterar_cliente,text="Confirmar", command=confirmar_id_alteracaocliente)
botao.grid(row=2,column=0, padx=10, pady=10)
botao2=tk.Button(framealterar_cliente,text="Voltar para o menu", command=home)
botao2.grid(row=2,column=1, padx=10, pady=10)

opcoes_alteracao_cliente=tk.Frame(janela)

titulo = tk.Label(opcoes_alteracao_cliente, text='Opções: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_cliente, text="Alterar nome", command=alteracao_nome_cliente)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_cliente, text="Alterar telefone", command=alteracao_telefone_cliente)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = tk.Button(opcoes_alteracao_cliente, text="Voltar para menu", command=home)
botao.grid(row=3, column=0, padx=10, pady=10)

alteracao_nomecliente=tk.Frame(janela)
nomecliente2 = tk.Entry(alteracao_nomecliente,width=25, bg='white', font=('Comic Sans MS', '10'))
nomecliente2.grid(row=2,column=1, padx=10, pady=10)
nome = tk.Label(alteracao_nomecliente,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Novo nome do funcionário:')
nome.grid(row=2, column=0, padx=10, pady=10)
botao=tk.Button(alteracao_nomecliente,text="Confirmar", command=confirmar_alteracao_nomecliente)
botao.grid(row=3,column=0, padx=10, pady=10)
botao2=tk.Button(alteracao_nomecliente,text="Voltar para o menu", command=home)
botao2.grid(row=3,column=1, padx=10, pady=10)


alteracao_telefonecliente=tk.Frame(janela)
telefonecliente2 = tk.Entry(alteracao_telefonecliente,width=25, bg='white', font=('Comic Sans MS', '10'))
telefonecliente2.grid(row=2,column=1, padx=10, pady=10)
telefone = tk.Label(alteracao_telefonecliente,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Novo telefone do cliente:')
telefone.grid(row=2, column=0, padx=10, pady=10)
botao=tk.Button(alteracao_telefonecliente,text="Confirmar", command=confirmar_alteracao_telefonecliente)
botao.grid(row=3,column=0, padx=10, pady=10)
botao2=tk.Button(alteracao_telefonecliente,text="Voltar para o menu", command=home)
botao2.grid(row=3,column=1, padx=10, pady=10)



frame_excluir=tk.Frame(janela)

titulo = tk.Label(frame_excluir, text='Opções: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(frame_excluir, text="Excluir funcionário", command=excluir_funcionario)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(frame_excluir, text="Excluir Cliente", command=excluir_cliente)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = tk.Button(frame_excluir, text="Excluir serviço", command=excluir_servico)
botao.grid(row=3, column=0, padx=10, pady=10)

botao = tk.Button(frame_excluir, text="Voltar para o menu", command=home)
botao.grid(row=4, column=0, padx=10, pady=10)

frame_excluir_servico=tk.Frame(janela)
titulo = tk.Label(frame_excluir_servico, text='Coloque o ID do funcionário que você deseja excluir: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

id_servico3 = tk.Entry(frame_excluir_servico,width=25, bg='white', font=('Comic Sans MS', '10'))
id_servico3.grid(row=1,column=1, padx=10, pady=10)
id = tk.Label(frame_excluir_servico,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='ID do serviço:')
id.grid(row=1, column=0, padx=10, pady=10)
botao=tk.Button(frame_excluir_servico,text="Confirmar", command=confirmar_excluirservico)
botao.grid(row=2,column=0, padx=10, pady=10)
botao2=tk.Button(frame_excluir_servico,text="Voltar para o menu", command=home)
botao2.grid(row=2,column=1, padx=10, pady=10)





frame_excluir_funcionario=tk.Frame(janela)
titulo = tk.Label(frame_excluir_funcionario, text='Coloque o ID do funcionário que você deseja excluir: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

id_funcionario3 = tk.Entry(frame_excluir_funcionario,width=25, bg='white', font=('Comic Sans MS', '10'))
id_funcionario3.grid(row=1,column=1, padx=10, pady=10)
id = tk.Label(frame_excluir_funcionario,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='ID do funcionário:')
id.grid(row=1, column=0, padx=10, pady=10)
botao=tk.Button(frame_excluir_funcionario,text="Confirmar", command=confirmar_excluirfuncionario)
botao.grid(row=2,column=0, padx=10, pady=10)
botao2=tk.Button(frame_excluir_funcionario,text="Voltar para o menu", command=home)
botao2.grid(row=2,column=1, padx=10, pady=10)


frame_excluir_cliente=tk.Frame(janela)
titulo = tk.Label(frame_excluir_cliente, text='Coloque o ID do cliente que você deseja excluir: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

id_cliente3 = tk.Entry(frame_excluir_cliente,width=25, bg='white', font=('Comic Sans MS', '10'))
id_cliente3.grid(row=1,column=1, padx=10, pady=10)
id = tk.Label(frame_excluir_cliente,font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='ID do cliente:')
id.grid(row=1, column=0, padx=10, pady=10)
botao=tk.Button(frame_excluir_cliente,text="Confirmar", command=confirmar_excluircliente)
botao.grid(row=2,column=0, padx=10, pady=10)
botao2=tk.Button(frame_excluir_cliente,text="Voltar para o menu", command=home)
botao2.grid(row=2,column=1, padx=10, pady=10)


frameagendamento=tk.Frame(janela)

titulo = tk.Label(frameagendamento, text='Opções: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(frameagendamento, text="Agendar horário", command=adicionar_horario)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(frameagendamento, text="Alterar horários", command=alterar_horario)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = tk.Button(frameagendamento, text="Excluir horários", command=remover_horario)
botao.grid(row=3, column=0, padx=10, pady=10)

botao = tk.Button(frameagendamento, text="Exibir o agendamento", command=exibir_horarios)
botao.grid(row=4, column=0, padx=10, pady=10)

botao = tk.Button(frameagendamento, text="Voltar para o menu", command=home)
botao.grid(row=5, column=0, padx=10, pady=10)

frame_agendarhorario=tk.Frame(janela)

tk.Label(frame_agendarhorario, text="ID do Agendamento:").grid(row=0, column=0, padx=10, pady=5)
id_agendamento_entry = tk.Entry(frame_agendarhorario)
id_agendamento_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_agendarhorario, text="ID do Funcionário:").grid(row=1, column=0, padx=10, pady=5)
id_funcionario_entry = tk.Entry(frame_agendarhorario)
id_funcionario_entry.grid(row=1, column=1, padx=10, pady=5)


tk.Label(frame_agendarhorario, text="ID do Serviço:").grid(row=2, column=0, padx=10, pady=5)
id_servico_entry = tk.Entry(frame_agendarhorario)
id_servico_entry.grid(row=2, column=1, padx=10, pady=5)


tk.Label(frame_agendarhorario, text="ID do Cliente:").grid(row=3, column=0, padx=10, pady=5)
id_cliente_entry = tk.Entry(frame_agendarhorario)
id_cliente_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame_agendarhorario, text="Data do Agendamento:").grid(row=4, column=0, padx=10, pady=5)
data_entry = DateEntry(frame_agendarhorario, date_pattern="yyyy-MM-dd")  
data_entry.grid(row=4, column=1, padx=10, pady=5)


tk.Label(frame_agendarhorario, text="Hora do Agendamento (HH:MM):").grid(row=5, column=0, padx=10, pady=5)
hora_entry = tk.Entry(frame_agendarhorario)
hora_entry.grid(row=5, column=1, padx=10, pady=5)


tk.Button(frame_agendarhorario, text="Agendar", command=agendar).grid(row=6, column=0, columnspan=2, pady=10)

botao2=tk.Button(frame_agendarhorario,text="Voltar para o menu", command=home)
botao2.grid(row=7,column=1, padx=10, pady=10)




frame_alterarhorario=tk.Frame(janela)

tk.Label(frame_alterarhorario, text="Informe o ID do Agendamento:").grid(row=0, column=0, padx=10, pady=5)
id_agendamento_entry2 = tk.Entry(frame_alterarhorario)
id_agendamento_entry2.grid(row=0, column=1, padx=10, pady=5)


tk.Button(frame_alterarhorario, text="Alterar ID do Cliente", command=lambda: configurar_alteracao("id_cliente")).grid(row=1, column=0, padx=10, pady=5)
tk.Button(frame_alterarhorario, text="Alterar ID do Funcionário", command=lambda: configurar_alteracao("id_funcionario")).grid(row=1, column=1, padx=10, pady=5)
tk.Button(frame_alterarhorario, text="Alterar ID do Serviço", command=lambda: configurar_alteracao("id_servico")).grid(row=2, column=0, padx=10, pady=5)
tk.Button(frame_alterarhorario, text="Alterar Data", command=lambda: configurar_alteracao("data")).grid(row=2, column=1, padx=10, pady=5)
tk.Button(frame_alterarhorario, text="Alterar Hora", command=lambda: configurar_alteracao("hora ")).grid(row=3, column=0, columnspan=2, pady=5)

instrucoes_label = tk.Label(frame_alterarhorario, text="Escolha o campo que deseja alterar:")
instrucoes_label.grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(frame_alterarhorario, text="Novo Valor:").grid(row=5, column=0, padx=10, pady=5)
valor_alterar_entry = tk.Entry(frame_alterarhorario)
valor_alterar_entry.grid(row=5, column=1, padx=10, pady=5)


alterar_btn = tk.Button(frame_alterarhorario, text="Confirmar Alteração", command=alterar_campo)
alterar_btn.grid(row=6, column=0, columnspan=2, pady=10)

botao2=tk.Button(frame_alterarhorario,text="Voltar para o menu", command=home)
botao2.grid(row=7,column=1, padx=10, pady=10)


frame_removerhorario=tk.Frame(janela)

tk.Label(frame_removerhorario, text="Informe o ID do Agendamento para excluir:").grid(row=0, column=0, padx=10, pady=5)
id_agendamento_entry3 = tk.Entry(frame_removerhorario)
id_agendamento_entry3.grid(row=0, column=1, padx=10, pady=5)

excluir_btn = tk.Button(frame_removerhorario, text="Excluir Agendamento", command=excluir_agendamento)
excluir_btn.grid(row=1, column=0, columnspan=2, pady=10)

frame_exibirhorario=tk.Frame(janela)
colunas = ("ID", "Cliente", "Funcionário", "Serviço", "Data", "Hora")
tabela_agendamentos = ttk.Treeview(frame_exibirhorario, columns=colunas, show="headings", height=8)

tabela_agendamentos.heading("ID", text="ID")
tabela_agendamentos.heading("Cliente", text="Cliente")
tabela_agendamentos.heading("Funcionário", text="Funcionário")
tabela_agendamentos.heading("Serviço", text="Serviço")
tabela_agendamentos.heading("Data", text="Data")
tabela_agendamentos.heading("Hora", text="Hora")


tabela_agendamentos.column("ID", width=50, anchor="center")
tabela_agendamentos.column("Cliente", width=150, anchor="w")
tabela_agendamentos.column("Funcionário", width=150, anchor="w")
tabela_agendamentos.column("Serviço", width=150, anchor="w")
tabela_agendamentos.column("Data", width=100, anchor="center")
tabela_agendamentos.column("Hora", width=80, anchor="center")

tabela_agendamentos.pack(pady=10)

botao_voltar = tk.Button(frame_exibirhorario, text="Voltar", command=home)
botao_voltar.pack(pady=10)





frameexibir=tk.Frame(janela)

titulo = tk.Label(frameexibir, text='Opções: ')  
titulo.grid(row=0, column=0, padx=10, pady=10)

botao = tk.Button(frameexibir, text="Mostrar lista de funcionários", command=exibir_funcionario)
botao.grid(row=1, column=0, padx=10, pady=10)

botao = tk.Button(frameexibir, text="Mostrar lista de clientes", command=exibir_cliente)
botao.grid(row=2, column=0, padx=10, pady=10)

botao = tk.Button(frameexibir, text="Mostrar lista de serviços", command=exibir_servico)
botao.grid(row=3, column=0, padx=10, pady=10)


botao = tk.Button(frameexibir, text="Voltar para o menu", command=home)
botao.grid(row=4, column=0, padx=10, pady=10)

frameexibir_funcionario=tk.Frame(janela)
titulo = tk.Label(frameexibir_funcionario, text='Funcionários cadastrados: ')
titulo.pack(pady=10)

colunas = ("ID", "Nome", "Cargo", "Telefone")
tabela_funcionarios = ttk.Treeview(frameexibir_funcionario, columns=colunas, show="headings", height=8)


tabela_funcionarios.heading("ID", text="ID")
tabela_funcionarios.heading("Nome", text="Nome")
tabela_funcionarios.heading("Cargo", text="Cargo")
tabela_funcionarios.heading("Telefone", text="Telefone")


tabela_funcionarios.column("ID", width=50, anchor="center")
tabela_funcionarios.column("Nome", width=150, anchor="w")
tabela_funcionarios.column("Cargo", width=100, anchor="w")
tabela_funcionarios.column("Telefone", width=100, anchor="center")

tabela_funcionarios.pack(pady=10)

botao_voltar = tk.Button(frameexibir_funcionario, text="Voltar", command=home)
botao_voltar.pack(pady=10)





frameexibir_cliente=tk.Frame(janela)
titulo = tk.Label(frameexibir_cliente, text='Clientes cadastrados: ')
titulo.pack(pady=10)


colunas = ("ID", "Nome", "Telefone")
tabela_clientes = ttk.Treeview(frameexibir_cliente, columns=colunas, show="headings", height=8)

tabela_clientes.heading("ID", text="ID")
tabela_clientes.heading("Nome", text="Nome")
tabela_clientes.heading("Telefone", text="Telefone")


tabela_clientes.column("ID", width=50, anchor="center")
tabela_clientes.column("Nome", width=150, anchor="w")
tabela_clientes.column("Telefone", width=100, anchor="center")

tabela_clientes.pack(pady=10)

botao_voltar = tk.Button(frameexibir_cliente, text="Voltar", command=exibir)
botao_voltar.pack(pady=10)



frameexibir_servico=tk.Frame(janela)
titulo = tk.Label(frameexibir_servico, text='Serviços cadastrados: ')
titulo.pack(pady=10)


colunas = ("ID", "Nome", "Preco")
tabela_servicos = ttk.Treeview(frameexibir_servico, columns=colunas, show="headings", height=8)

tabela_servicos.heading("ID", text="ID")
tabela_servicos.heading("Nome", text="Nome")
tabela_servicos.heading("Preco", text="Preço")

tabela_servicos.column("ID", width=50, anchor="center")
tabela_servicos.column("Nome", width=150, anchor="w")
tabela_servicos.column("Preco", width=100, anchor="center")

tabela_servicos.pack(pady=10)


botao_voltar = tk.Button(frameexibir_servico, text="Voltar", command=exibir)
botao_voltar.pack(pady=10)













janela.mainloop()
