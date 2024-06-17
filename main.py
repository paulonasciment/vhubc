import streamlit as st
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

produtos_e_servicos = ["Mascarenhas - Holding","Mascarenhas - Back Office","VHUB Gestao - BPO","VMG - Consultorias","C&G - Societário",
                       "Mascarenhas - Registro de Marca","VHUB Gestão - Conta Azul"]
meios_de_comunicacao = ["Whatsapp","Linkedin","Presencial","Instagram","Telefone"]
vendedores = ["Eduarda","Mario","Camilla","Ingrid","Maria Clara"]
empresas = ["VHUB - Gestão","Mascarenhas","VMG - Consultoria"]
fases = ["Cliente em potencial","Negócio Fechado","Integração"]
referencias = ["VHUB","Cliente novo"]
clientes = [
    "Ana Silva", "Bruno Souza", "Carlos Oliveira", "Daniela Pereira", "Eduardo Lima",
    "Fernanda Gomes", "Gabriel Fernandes", "Helena Costa", "Isabela Martins", "João Santos",
    "Karen Rocha", "Lucas Almeida", "Mariana Azevedo", "Nicolas Ribeiro", "Olivia Barros",
    "Pedro Cardoso", "Quintino Reis", "Rafaela Freitas", "Sandro Castro", "Tatiana Pinto",
    "Ulisses Araújo", "Valéria Cunha", "Wagner Monteiro", "Xavier Mendes", "Yasmin Nogueira",
    "Zara Teixeira", "Arthur Vieira", "Beatriz Silva", "Caio Ferreira", "Diana Mendes",
    "Elias Moreira", "Flávia Costa", "Gustavo Barros", "Hugo Batista", "Irene Carvalho",
    "Júlio Campos", "Larissa Souza", "Miguel Dias", "Natália Gomes", "Otávio Lopes",
    "Paula Martins", "Ricardo Rocha", "Simone Araujo", "Thiago Barbosa", "Vanessa Almeida",
    "Willian Freitas", "Ximena Ribeiro", "Yuri Lima", "Zeca Pereira", "Amanda Cardoso",
    "Bruno Araújo", "Camila Lima", "Douglas Gomes", "Elaine Costa", "Fábio Rocha",
    "Gabriela Ferreira", "Henrique Oliveira", "Isabel Mendes", "José Almeida", "Kelly Batista",
    "Leonardo Martins", "Marina Nogueira", "Nelson Santos", "Otávio Barros", "Priscila Pinto",
    "Rodrigo Teixeira", "Suzana Monteiro", "Tomás Castro", "Vitória Freitas", "William Costa",
    "Alexandre Cardoso", "Bárbara Mendes", "César Lima", "Débora Oliveira", "Eduardo Batista",
    "Francisco Souza", "Giovana Araujo", "Heloísa Barros", "Igor Santos", "Júlia Martins",
    "Letícia Pereira", "Matheus Gomes", "Núbia Cardoso", "Orlando Rocha", "Patrícia Costa",
    "Rafael Ferreira", "Sandra Mendes", "Túlio Lima", "Viviane Nogueira", "Wesley Oliveira",
    "Xênia Rocha", "Yago Ribeiro", "Zélia Barros", "Adriano Lima", "Brenda Ferreira",
    "Cláudio Souza", "Daniela Cardoso", "Emanuel Gomes", "Fabiana Oliveira", "Guilherme Batista"
]

venda_example = {
    "referencia":"",
    "cliente":"",
    "empresa":"",
    "contato_inicial":"",
    "produto_servico":"",
    "fase":"",
    "valor_estimado":""
}

def gerar_valor_estimado():
    return f"R${random.uniform(80, 300):.2f}"

# Função para gerar um exemplo de venda
def gerar_venda_example():
    return {
        "referencia": random.choice(referencias),
        "cliente": random.choice(clientes),
        "empresa": random.choice(empresas),
        "contato_inicial": random.choice(meios_de_comunicacao),
        "produto_servico": random.choice(produtos_e_servicos),
        "vendedor":random.choice(vendedores),
        "fase": random.choice(fases),
        "valor_estimado": gerar_valor_estimado(),
        "data":gerar_data_aleatoria()
    }
def gerar_data_aleatoria():
    # Define a data inicial (1 de janeiro)
    data_inicial = datetime(2024, 1, 1)
    # Define a data final (17 de julho)
    data_final = datetime(2024, 7, 17)
    # Calcula a diferença em dias entre as duas datas
    delta = data_final - data_inicial
    # Gera um número aleatório de dias dentro do intervalo
    dias_aleatorios = random.randint(0, delta.days)
    # Adiciona os dias aleatórios à data inicial para obter a data aleatória
    data_aleatoria = data_inicial + timedelta(days=dias_aleatorios)
    return data_aleatoria





st.set_page_config(page_title="Dashboard Vendas",layout="wide",page_icon=":bar_chart:")
st.title("Vendas VHUB")




vendedor,leads = st.tabs(['Vendedor','Leads'])
with leads:
    vendas_examples = [gerar_venda_example() for _ in range(40)]
    df = pd.DataFrame(vendas_examples)
    df_fechados = df[df["fase"] == "Negócio Fechado"]

    contagem_por_servico = df_fechados.value_counts("produto_servico")
    

    col1,col2= st.columns((2))

    with col1:
        st.write("Vendas por Empresa")
        st.bar_chart(contagem_por_servico)
        st.write("Entrada de Clientes por Empresa")
        entradas_por_escritorio = df[df["fase"] == "Negócio Fechado"].groupby("empresa").size().reset_index(name='entradas')
        st.table(entradas_por_escritorio)


    with col2:
         # 6. Histórico de vendas por mês de 2024
        st.write("Histórico de Vendas por Mês de 2024")
        vendas_por_mes_2024 = df[(df['fase'] == 'Negócio Fechado') & (df['data'].dt.year == 2024)].groupby(df['data'].dt.to_period("M")).size().reset_index(name='vendas')
        vendas_por_mes_2024['mes'] = vendas_por_mes_2024['data'].dt.month  # Adiciona uma coluna 'mes' com o número do mês
        print(vendas_por_mes_2024)
        st.bar_chart(vendas_por_mes_2024.set_index('mes')['vendas'])

        # 4. Histórico de leads em acompanhamento por mês
        st.write("Histórico de Leads em Acompanhamento por Mês")
        historico_leads_acompanhamento = df[df['fase'] == 'Cliente em potencial'].groupby(df['data'].dt.to_period("M")).size().reset_index(name='leads_acompanhamento')
        st.table(historico_leads_acompanhamento)

        # 5. Histórico de clientes em acompanhamento/Integração por mês
        st.write("Histórico de Clientes em Acompanhamento/Integração por Mês")
        historico_clientes_integ = df[df['fase'] == 'Integração'].groupby(df['data'].dt.to_period("M")).size().reset_index(name='clientes_integ')
        st.table(historico_clientes_integ)

            
       


with vendedor:

    vendas_examples = [gerar_venda_example() for _ in range(40)]
    df = pd.DataFrame(vendas_examples)
    df_fechados = df[df["fase"] == "Negócio Fechado"]
    col1,col2= st.columns((2))

    with col1:
        st.header("Leads por Serviço por Vendedor")
        leads_por_vendedor = df[df["fase"] == "Negócio Fechado"].groupby(["produto_servico", "vendedor"]).size().reset_index(name='leads')
        st.table(leads_por_vendedor)

    
    with col2:
        vendas_por_vendedor = df_fechados.value_counts("vendedor")

        print(vendas_por_vendedor)

        st.write("Vendas por Vendedor")
        st.bar_chart(vendas_por_vendedor)