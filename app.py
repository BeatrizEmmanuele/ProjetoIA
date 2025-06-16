import streamlit as st # type: ignore
import pandas as pd # type: ignore
import datetime
import os
import google.generativeai as genai # type: ignore

api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)

def analisar_sentimento(texto):
    prompt = f"""
    Classifique o sentimento deste texto como: 
    Positivo, Neutro ou Negativo. Responda apenas com a palavra.
    Texto: "{texto}"
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        sentimento = response.text.strip().split('\n')[0]
        return sentimento
    except Exception as e:
        st.error(f"Erro ao conectar à API: {e}")
        return "Erro"


if os.path.exists('dados.csv'):
    dados = pd.read_csv('dados.csv')
else:
    dados = pd.DataFrame(columns=['Data', 'Relato', 'Sentimento'])


st.set_page_config(page_title="Diário Emocional com IA", layout="centered")
st.title("📓 Diário Emocional com IA")

st.write("🧠 Escreva como foi seu dia. A IA irá analisar seu sentimento como: Positivo, Negativo ou Neutro e criar um histórico emocional.")

relato = st.text_area("Como foi seu dia hoje?", height=200)

if st.button("Salvar no Diário"):
    if relato.strip() != "":
        with st.spinner("Analisando seu sentimento..."):
            sentimento = analisar_sentimento(relato)
        
        nova_linha = {
            'Data': datetime.date.today().strftime('%Y-%m-%d'),
            'Relato': relato,
            'Sentimento': sentimento
        }
        
        dados = pd.concat([dados, pd.DataFrame([nova_linha])], ignore_index=True)
        dados.to_csv('dados.csv', index=False)
        
        st.success("✅ Relato salvo com sucesso!")
        st.write(f"**Sentimento detectado:** {sentimento}")
    else:
        st.warning("⚠️ Por favor, escreva algo para salvar no diário.")


st.subheader("📊 Histórico de Sentimentos")

if not dados.empty:
    st.dataframe(dados.sort_values(by="Data", ascending=False))

    grafico = dados.groupby('Data')['Sentimento'].value_counts().unstack().fillna(0)
    st.bar_chart(grafico)
else:
    st.info("Ainda não há registros no diário.")
