import streamlit as st
import pandas as pd
import numpy as np
#import seaborn as sns
#import openpyxl
#import matplotlib.pyplot as plt
#from datetime import datetime
#from datetime import timedelta
import plotly.express as px
import datetime
import plotly.graph_objects as go

def isnotNaN(x):
    return x == x


ref_energ_kcal = 2000
ref_carbo_g = 300
ref_prot_g = 50
ref_gord_sat_g = 20
ref_fibra_g = 25
ref_sod_mg = 2000
ref_colest_mg = 300
ref_calcio_mg = 1000
ref_ferro_mg = 14
ref_potassio_mg = 3500
ref_vit_k_mg = 120

dados = pd.read_excel("Ficha_tec_prep_10.11_v21.xlsx", sheet_name=None)
nomes = list(dados.keys())

paginas = ["Início", "Análise Descritiva Produtos","Sobre o Desenvolvedor"]

pagina = st.sidebar.radio("Selecione uma página", paginas)

if pagina == "Início":
    st.title("Deploy Informações Nutricionais")

    st.subheader("Powered By Streamlit")

    st.markdown("---")

    st.markdown("Web App para Análise Descritiva das informações nutricionais dos alimentos. Selecione o que deseja visualizar no menu ao lado.")


elif pagina == "Análise Descritiva Produtos":
    data = datetime.datetime.now()
    
    st.markdown("# Análise Descritiva")
    data = str(data.day) + "/" + str(data.month) + "/" + str(data.year)
    data
    st.markdown("---")
    #dados = pd.read_excel("Ficha_tec_prep_10.11_v21.xlsx", sheet_name=None)
    selecione = list(dados.keys())
    st.markdown("## O que deseja analisar? ")
    nome = st.selectbox("", selecione)
    
    
    st.markdown("### Informações Base do Alimento: ")
    
    tipo = dados[nome].iloc[2,1]
    rendimento = dados[nome].iloc[2,3]
    custo_total = dados[nome].iloc[2,5]
    categoria = dados[nome].iloc[3,1]
    rendimento_g = dados[nome].iloc[3,3]
    custo_porcao = dados[nome].iloc[3,5]
    setor = dados[nome].iloc[4,1]
    peso_porcao = dados[nome].iloc[4,3]
    tempo_preparo = dados[nome].iloc[4,5]
    
    
       
    ingrediente = []
    unidade = []
    quantidade_liquida = []
    fator_de_correcao = []
    quantidade_bruta = []
    custo_unitario = []
    dados[nome].iloc[:,0] = dados[nome].iloc[:,0].replace(0,np.nan)
    
    kpil, kpim, kpin = st.columns(3)
    kpil.metric(label="Tipo", value=tipo)
    kpim.metric(label="Rendimento (Porções)", value="%.2f" %rendimento)
    kpin.metric(label="Custo Total", value="R$ %.2f" %custo_total)
    
    kpil3, kpim3, kpin3 = st.columns(3)
    kpil3.metric(label="Categoria", value=categoria)
    kpim3.metric(label="Rendimento (g)", value="%.2f" %rendimento_g)
    kpin3.metric(label="Custo Por Porção", value="R$ %.2f" %custo_porcao)
    
    kpil2, kpim2, kpin2 = st.columns(3)
    kpil2.metric(label="Setor", value=setor)
    kpim2.metric(label="Peso Por Porção (g)", value="%.2f" %peso_porcao)
    if isnotNaN(tempo_preparo):
        kpin2.metric(label="Tempo de Preparo (Min)", value="%.0f" %tempo_preparo)
    else:
        kpin2.metric(label = "Tempo de Preparo (Min)", value = "Desconhecido")
    st.markdown("---")
    st.markdown("### Valor Nutricional da Porção: ")
    
    for pos, i in enumerate(dados[nome].iloc[7:18,:].index):
        if isnotNaN(dados[nome].iloc[i,0]):
            ingrediente.append(dados[nome].iloc[i,0])
            unidade.append(dados[nome].iloc[i,1])
            quantidade_liquida.append(dados[nome].iloc[i,2])
            fator_de_correcao.append(dados[nome].iloc[i,3])
            quantidade_bruta.append(dados[nome].iloc[i,4])
            custo_unitario.append(dados[nome].iloc[i,5])

    ingrediente = pd.Series(ingrediente, name = "ingrediente")
    unidade = pd.Series(unidade, name = "unidade")
    quantidade_liquida = pd.Series(quantidade_liquida, name = "quantidade_liquida")
    fator_de_correcao = pd.Series(fator_de_correcao, name = "fator_de_correcao")
    quantidade_bruta = pd.Series(quantidade_bruta, name = "quantidade_bruta")
    custo_unitario = pd.Series(custo_unitario, name = "custo_unitario")


    dados_2 = pd.concat([ingrediente,unidade,quantidade_liquida,
              fator_de_correcao, quantidade_bruta, custo_unitario], axis = 1)
    
    
    #dados_2


    

    alimento = []
    quantidade_g = []
    energia_kcal = []
    carbo_g = []
    protei_g = []
    lipid_g = []
    gord_sat_g = []
    colest_g = []
    fibra_g = []
    calcio_mg = []
    ferro_mg = []
    sodio_mg = []
    potassio_mg = []
    vit_k_mg = []

    for i in dados[nome].iloc[20:31,:].index:
        if isnotNaN(dados[nome].iloc[i,0]):
            alimento.append(dados[nome].iloc[i,0])
            quantidade_g.append(dados[nome].iloc[i,1])
            energia_kcal.append(dados[nome].iloc[i,2])
            carbo_g.append(dados[nome].iloc[i,3])
            protei_g.append(dados[nome].iloc[i,4])
            lipid_g.append(dados[nome].iloc[i,5])
            gord_sat_g.append(dados[nome].iloc[i,6])
            colest_g.append(dados[nome].iloc[i,7])
            fibra_g.append(dados[nome].iloc[i,8])
            calcio_mg.append(dados[nome].iloc[i,9])
            ferro_mg.append(dados[nome].iloc[i,10])
            sodio_mg.append(dados[nome].iloc[i,11])
            potassio_mg.append(dados[nome].iloc[i,12])
            vit_k_mg.append(dados[nome].iloc[i,13])


    alimento = pd.Series(alimento, name = "alimento")
    quantidade_g = pd.Series(quantidade_g, name = "quantidade_g")
    energia_kcal = pd.Series(energia_kcal, name = "energia_kcal")
    carbo_g = pd.Series(carbo_g, name = "carbo_g")
    protei_g = pd.Series(protei_g, name = "protei_g")
    lipid_g = pd.Series(lipid_g, name = "lipid_g")
    gord_sat_g = pd.Series(gord_sat_g, name = "gord_sat_g")
    colest_g = pd.Series(colest_g, name = "colest_g")
    fibra_g = pd.Series(fibra_g, name = "fibra_g")
    calcio_mg = pd.Series(calcio_mg, name = "calcio_mg")
    ferro_mg = pd.Series(ferro_mg, name = "ferro_mg")
    sodio_mg = pd.Series(sodio_mg, name = "sodio_mg")
    potassio_mg = pd.Series(potassio_mg, name = "potassio_mg")
    vit_k_mg = pd.Series(vit_k_mg, name = "vit_k_mg")

    dados_3 = pd.concat([alimento, quantidade_g, energia_kcal,
              carbo_g, protei_g, lipid_g,
              gord_sat_g, colest_g,
              fibra_g, calcio_mg, ferro_mg,
              sodio_mg, potassio_mg, vit_k_mg], axis = 1)
    
    # dados_3
    energy = energia_kcal[len(energia_kcal)-1]
    carboid = carbo_g[len(carbo_g)-1]
    prot = protei_g[len(protei_g)-1]
    gord_sat = gord_sat_g[len(gord_sat_g)-1]
    fibra = fibra_g[len(fibra_g)-1]
    sod = sodio_mg[len(sodio_mg)-1]
    col = colest_g[len(colest_g)-1]
    cal = calcio_mg[len(calcio_mg)-1]
    ferro = ferro_mg[len(ferro_mg)-1]
    potass = potassio_mg[len(potassio_mg)-1]
    vit_k = vit_k_mg[len(vit_k_mg)-1]
    lipideos = lipid_g[len(lipid_g)-1]
    
    kpil, kpim, kpin = st.columns(3)
    kpil.metric(label="Energia (Kcal)", value="%.0f" % energy)
    kpim.metric(label="Carboidratos (g)", value="%.0f" %carboid)
    kpin.metric(label="Proteínas (g)", value="%.0f" %prot)
    
    kpil2, kpim2, kpin2 = st.columns(3)
    kpil2.metric(label="Gordura Saturada (g)", value="%.0f" % gord_sat)
    kpim2.metric(label="Fibra (g)", value="%.0f" %fibra)
    kpin2.metric(label="Sódio (mg)", value="%.0f" %sod)
    
    kpil3, kpim3, kpin3 = st.columns(3)
    kpil3.metric(label="Colesterol (g)", value="%.0f" % col)
    kpim3.metric(label="Cálcio (mg)", value="%.0f" %cal)
    kpin3.metric(label="Ferro (mg)", value="%.0f" %ferro)
    
    kpil4, kpim4, kpinull4 = st.columns(3)
    kpil4.metric(label="Potássio (mg)", value="%.0f" % potass)
    kpim4.metric(label="Vitamina K (mg)", value="%.0f" %vit_k)
    
    st.markdown("---")
    st.markdown("## Comparação com porção Diária")
    st.markdown("Valores diários dados como referência do site: https://www.in.gov.br/en/web/dou/-/instrucao-normativa-in-n-75-de-8-de-outubro-de-2020-282071143")
    perc_energy = round(100*energy/ref_energ_kcal,0)
    perc_carboid = round(100*carboid/ref_carbo_g,0)
    perc_prot = round(100*prot/ref_prot_g,0)
    perc_gord_sat = round(100*gord_sat/ref_gord_sat_g,0)
    perc_fibra = round(100*fibra/ref_fibra_g,0)
    perc_sod = round(100*sod/ref_sod_mg,0)
    perc_col = round(100*col/ref_colest_mg,0)
    perc_cal = round(100*cal/ref_calcio_mg,0)
    perc_ferro = round(100*ferro/ref_ferro_mg,0)
    perc_potassio = round(100*potass/ref_potassio_mg,0)
    perc_vit_k = round(100*vit_k/ref_vit_k_mg,0)
    
    lista_series = [perc_energy, perc_carboid,
                            perc_prot, perc_gord_sat,
                            perc_fibra, perc_sod,
                            perc_col, perc_cal,
                            perc_ferro, perc_potassio,
                            perc_vit_k]
    
    lista_nomes = ["Energia", "Carboidratos", 
                            "Proteínas", "Gorduras Saturadas",
                            "Fibras", "Sódio", "Colesterol",
                            "Cálcio", "Ferro", "Potássio",
                            "Vitamina K"]
    
    series = pd.Series(lista_series, name = "(%) do Valor Diário")
    
    nomes_ = pd.Series(lista_nomes, name = "Nutriente")
    
    data_fram = pd.concat([nomes_, series], axis = 1)
    
    kpil, kpim, kpin = st.columns(3)
    kpil.metric(label="Energia (%)", value="%.0f" % perc_energy)
    kpim.metric(label="Carboidratos (%)", value="%.0f" %perc_carboid)
    kpin.metric(label="Proteínas (%)", value="%.0f" %perc_prot)
    
    kpil2, kpim2, kpin2 = st.columns(3)
    kpil2.metric(label="Gordura Saturada (%)", value="%.0f" % perc_gord_sat)
    kpim2.metric(label="Fibra (%)", value="%.0f" %perc_fibra)
    kpin2.metric(label="Sódio (%)", value="%.0f" %perc_sod)
    
    kpil3, kpim3, kpin3 = st.columns(3)
    kpil3.metric(label="Colesterol (%)", value="%.0f" % perc_col)
    kpim3.metric(label="Cálcio (%)", value="%.0f" %perc_cal)
    kpin3.metric(label="Ferro (%)", value="%.0f" %perc_ferro)
    
    kpil4, kpim4, kpinull4 = st.columns(3)
    kpil4.metric(label="Potássio (%)", value="%.0f" % perc_potassio)
    kpim4.metric(label="Vitamina K (%)", value="%.0f" %perc_vit_k)



    
    fig = px.bar(data_fram, x="Nutriente", y=data_fram["(%) do Valor Diário"],
                      title='Percentual do Valor Diário',
                      color_discrete_sequence=["darkgreen"])
    fig.update_layout(title={
                              "x": 0.5,
                              'xanchor': 'center',
                              'yanchor': 'top'},
        )
    st.plotly_chart(fig, use_container_width=True)
    
    
    st.markdown("---")
    st.markdown("## Descritivo das porções")
    dados_2
    dados_3
    
    total = carboid + prot + lipideos
    
    labels = ['Carboidratos','Proteínas','Lipídeos']
    values = [carboid, prot, lipideos]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
   
    
    fig.update_layout(title_text = "Proporção de Macronutrientes na Porção",
                      title={
                              "x": 0.5,
                              'xanchor': 'center',
                              'yanchor': 'top',
                              },
        )
    st.plotly_chart(fig, use_container_width=True)
    
elif pagina == "Sobre o Desenvolvedor":
    st.markdown("""# Sobre o Desenvolvedor
    ---
Olá, meu nome é André Carpinteiro do Amaral, me formo em Engenharia Aeronáutica este ano pela Universidade Federal de Itajubá. Ao longo da graduação ministrei aulas voluntárias em um curso assistencial, fui tutor pela universidade e participei de dois projetos de extensão, um na área de Motores à Combustão e outro na área de Análise de Dados de Vibração. Atualmente estou estagiando na Embraer S/A na área de Desenvolvimento de Produtos e estou estudando Ciência de Dados na FLAI e na Digital House.

Sou entusiasta de ciência de dados, machine learning e novas tendências tecnológicas.

Se conecte comigo e me encontre no linkedin:


- [Linkedin](https://www.linkedin.com/in/andre-amaral-gb/) 

""")
        
