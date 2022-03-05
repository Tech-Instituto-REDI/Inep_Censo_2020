#!/usr/bin/env python
# coding: utf-8

# <pre>
# <img align="center" width="300" src="https://institutoredi.org/assets/images/logo-instituto-redi.png">
# </pre>
# 
# <pre>
# <img align="left" width="150" src="https://camo.githubusercontent.com/bdc6a3b8963aa99ff57dfd6e1e4b937bd2e752bcb1f1936f90368e5c3a38f670/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d434325323042592d2d5341253230342e302d6c69676874677265792e737667">
# </pre>

# ### **Programa para unificar as bases no formato "XLSX" (Excel) de Indicadores de FLuxo da Educação Superior**

# | Descrição                                       |              |           
# |:----------------------------------------------- | -------------|
# | Responsável                                     | André Santos |
# | Data de acesso                                  | 26/Fev/2022  |
# | Horas trabalhadas (coleta, tratamento e script) | 2h           |
# | Dados publicados                                | 21/Out/2020  |
# | Dados atualizados                               | 17/Fev/2022  |
# 
# Fonte: [Ministério da Educação](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-de-fluxo-da-educacao-superior)

# ### **SOBRE**
# 
# Indicadores de fluxo de ingressantes de cursos de graduação produzidos a partir das informações coletadas pelo Censo da Educação Superior, tendo como forma de análise o acompanhamento longitudinal em uma trajetória cronológica dos estudantes quando ingressam em um curso de graduação até a sua saída, seja por meio da conclusão ou da desistência do curso.
# 
# Esses indicadores servem de base para diferentes análises, bem como para medida da eficiência de cada curso, podendo ser combinados com outros indicadores ou insumos, auxiliando na criação de novos parâmetros de controle de eficiência do curso, além de qualificar a oferta e a demanda desses cursos. Além disso, eles subsidiam discussões acerca da eficácia do sistema de ensino superior, principalmente quanto à capacidade deste para formar pessoas.
# 
# Essa classe de indicadores educacionais tem como unidade de análise o curso de graduação, abrangendo três dimensões principais do vínculo do estudante ao curso: permanência, desistência e conclusão. 
# 
# Permanência no curso de ingresso: corresponde aos estudantes que possuem vínculos ativos com o seu curso de ingresso em um determinado ano de referência.
# 
# Desistência do curso de ingresso: corresponde aos estudantes que encerram seu vínculo com o seu curso de ingresso em um determinado ano de referência, seja por meio da desvinculação ou da transferência para outro curso da mesma instituição de educação superior.
# 
# Conclusão no curso de ingresso: corresponde aos estudantes que se formam no seu curso de ingresso em um determinado ano de referência.
# 
# [Metodologia de cálculo dos Indicadores de Fluxo da Educação Superior](https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2017/metodologia_indicadores_trajetoria_curso.pdf)
# 

# ### DICIONÁRIO DE BANCO DE DADOS DE INDICADORES DE TRAJETÓRIA POR CURSO
# 
# |POSIÇÃO|NOME DA VARIÁVEL|DESCRIÇÃO|TIPO|TAM1|F/V2|DESCRIÇÃO DAS CATEGORIAS |
# |:------|:---------------|:--------|:---|:---|:---|:------------------------|
# **DADOS DA IES**
# 1|CO_IES|Código único de identificação da instituição de educação superior em que o curso está localizado no último ano de análise.|Num|8|V|
# 2|NO_IES|Nome da instituição de educação superior em que o curso está localizado no último ano de análise.|Char|200|V|
# 3|TP_CATEGORIA_ADMINISTRATIVA|Código da categoria Administrativa da IES no último ano de análise.|Num|1|F|1. Pública Federal; 2. Pública Estadual; 3. Pública Municipal; 4. Privada com fins lucrativos; 5. Privada sem fins lucrativos; 7. Especial
# 4|TP_ORGANIZACAO_ACADEMICA|Código da organização acadêmica no último ano de análise.|Num|1|F|1. Universidade; 2. Centro Universitário; 3. Faculdade; 4. Instituto Federal de Educação, Ciência e Tecnologia                                ; 5. Centro Federal de Educação Tecnológica
# **DADOS DO CURSO**
# 5|CO_CURSO|Código único de identificação do curso gerado pelo E-MEC, com a informação do último ano de análise.|Num|8|V|
# 6|NO_CURSO|Nome do curso com a informação do último ano de análise.|Num|200|V|
# 7|CO_REGIAO|Código da Região Geográfica do local de oferta do curso gerado pelo E-MEC no último ano de análise.|Num|1|F|1. Região Norte; 2. Região Nordeste; 3. Região Sudeste; 4. Região Sul; 5. Região Centro-Oeste
# 8|CO_UF|Código da Unidade da Federação do local de oferta do curso gerado pelo E-MEC no último ano de análise.|Num|2|F|
# 9|CO_MUNICIPIO|Código do município do local de oferta do curso gerado pelo E-MEC no último ano de análise.|Num|7|F|
# 10|TP_GRAU_ACADEMICO|Código do grau acadêmico conferido ao diplomado pelo curso no último ano de análise.|Num|1|F|1. Bacharelado; 2. Licenciatura; 3. Tecnológico
# 11|TP_MODALIDADE_ENSINO|Código da modalidade de ensino do curso no último ano de análise.|Num|1|F|1. Presencial; 2. Curso a distância
# 12|CO_CINE_AREA_GERAL|Código da área geral conforme adaptação da Classificação Internacional Normalizada da Educação Cine/Unesco|Num|1|F|
# 13|NO_CINE_AREA_GERAL|Nome da área geral conforme adaptação da Classificação Internacional Normalizada da Educação Cine/Unesco|Char|120|V|
# 14|CO_CINE_ROTULO|Código de identificação do curso, conforme adaptação da Classificação Internacional Normalizada da Educação Cine/Unesco|Num|7|V|
# 15|NO_CINE_ROTULO|Nome de identificação do curso, conforme adaptação da Classificação Internacional Normalizada da Educação Cine/Unesco|Char|120|V|
# 16|NU_ANO_INGRESSO|Ano de ingresso do aluno no curso.|Num|4|F|
# 17|NU_ANO_REFERENCIA|Ano de referência do vínculo do ingressante.|Num|4|F|
# 18|NU_PRAZO_INTEGRALIZAÇÃO|Prazo mínimo de integralização de curso de graduação em número de anos|Num|2|F|
# 19|NU_ANO_INTEGRALIZACAO|Ano previsto de integralização do aluno ao curso.|Num|4|F|
# 20|NU_PRAZO_ACOMPANHAMENTO|Prazo máximo de integralização de curso de graduação em número de anos|Num|2|F|
# 21|NU_ANO_MAXIMO_ACOMPANHAMENTO|Ano máximo de acompanhamento da situação de vínculo do aluno.|Num|4|F|
# 22|QT_INGRESSANTE|Número de ingressantes do curso no ano de ingresso da coorte.|Num|8|V|
# 23|QT _PERMANENCIA|Número de estudantes que permaneceram no curso de graduação no ano de referência da análise|Num|8| V|
# 24|QT _CONCLUINTE|Número de estudantes que concluíram o curso de graduação no ano de referência da análise|Num|8|V|
# 25|QT _DESISTENCIA|Número de estudantes que desistiram do curso de graduação no ano de referência da análise|Num|8|V|
# 26|QT _FALECIDO|Número de estudantes que faleceram no ano de referência da análise|Num|8|V|
# **INDICADORES DE TRAJETÓRIA**
# 27|TAP|Taxa de Permanência|Num|5|V|Percentual de ingressantes que estão com vínculo ativo no curso no ano de referência
# 28|TCA|Taxa de Conclusão Acumulada|Num|5|V|Percentual de ingressantes que concluíram o curso até o ano de referência
# 29|TDA|Taxa de Desistência Acumulada|Num|5|V|Percentual de ingressantes que desistiram do curso até o ano de referência
# 30|TCAN|Taxa de Conclusão Anual|Num|5|V|Percentual de ingressantes que concluíram o curso no ano de referência
# 31|TADA|Taxa de Desistência Anual|Num|5|V|Percentual de ingressantes que desistiram do curso no ano de referência
# 

# In[1]:


# Bibliotecas necessárias
import pandas as pd   # Manipulação da base de dados
import os             # Apontar para o diretório onde estão os arquivos
import time           # Calcula o tempo por bloco


# In[2]:


# Diretório dos arquivos
os.chdir('C:/Users/andre/Documents/REDI/Indicadores_Educacionais_Indicadores_Fluxo_Educacao_Superior_2010_2016')


# In[3]:


# Bases
s = time.time()
df1 = pd.read_excel("indicadores_trajetoria_educacao_superior_2010_2019.xlsx")
df2 = pd.read_excel("indicadores_trajetoria_educacao_superior_2011_2020.xlsx")
df3 = pd.read_excel("indicadores_trajetoria_educacao_superior_2012_2020.xlsx")
df4 = pd.read_excel("indicadores_trajetoria_educacao_superior_2013_2020.xlsx")
df5 = pd.read_excel("indicadores_trajetoria_educacao_superior_2014_2020.xlsx")
df6 = pd.read_excel("indicadores_trajetoria_educacao_superior_2015_2020.xlsx")
df7 = pd.read_excel("indicadores_trajetoria_educacao_superior_2016_2020.xlsx")
e = time.time()
print("Loading Time = {}".format(e-s)) # time: 480 seconds
df1.head()


# In[4]:


# Total de observações (linhas) por base
s = time.time()
print('df1:', len(df1))
print('df2:', len(df2))
print('df3:', len(df3))
print('df4:', len(df4))
print('df5:', len(df5))
print('df6:', len(df6))
print('df7:', len(df7))
print('Soma dfs:', len(df1)+len(df2)+len(df3)+len(df4)+len(df5)+len(df6)+len(df7))
e = time.time()
print("Loading Time = {}".format(e-s)) # time: 1 second


# In[5]:


# Merge dfs
s = time.time()
data_frames = [df1, df2, df3, df4, df5, df6, df7]
df = pd.concat(data_frames)
print(len(df))
e = time.time()
print("Loading Time = {}".format(e-s)) # time: 1 second
df


# In[6]:


# Salvar csv
s = time.time()
df.to_csv("indicadores_trajetoria_educacao_superior_2010_2016.csv", index=False)
e = time.time()
print("Loading Time = {}".format(e-s)) # time: 27 second


# ## Referências
# * [Instituto REDI](https://institutoredi.org/)
# * [Tech-Instituto-REDI](https://github.com/Tech-Instituto-REDI)
# * [Resultados do Censo da Educação Superior 2020 disponíveis](https://www.gov.br/inep/pt-br/assuntos/noticias/censo-da-educacao-superior/resultados-do-censo-da-educacao-superior-2020-disponiveis)
# 
# ## Agradecimentos
# * [Reluze](https://www.instagram.com/reluze.co/)
# * [AMORA AMIGURUMI](https://www.instagram.com/accounts/login/?next=/amoralove_amigurumi/)
# * [TIÊ MODA SUSTENTÁVEL](https://www.instagram.com/accounts/login/?next=/tiemaisum/)
# * [Fabrikei](https://www.instagram.com/accounts/login/?next=/fabrikei/)
# * [UHNIKA](https://www.instagram.com/accounts/login/?next=/uhnika/)
# * [GOTHA ATELIER](https://www.instagram.com/accounts/login/?next=/gothaatelier/)
# * [Galeria Garimpo](https://www.instagram.com/accounts/login/?next=/galeriagarimpo/)
# * [C.ALMA](https://www.instagram.com/accounts/login/?next=/calmabelezanatural/)
# 
# 
# ## Licença
# O uso deste programa, está disponível sob a [ Licença Creative Commons Atribuição Internacional, v4.0 (CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). Os arquivos utilizados com origem de outros projetos estão sujeitos às suas próprias licenças.
# 
# <pre>
# <img align="left" width="100" src="https://licensebuttons.net/l/by-sa/4.0/88x31.png">
# </pre>
# 
# ## Autor
# #### __André Luis M. F. dos Santos__ | andre@institutoredi.org
