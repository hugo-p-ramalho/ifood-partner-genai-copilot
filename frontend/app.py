import streamlit as st, requests
st.title("iFood Partner Copilot")
nome = st.text_input("Nome do prato", "X-Burger")
preco = st.number_input("Preco", value=29.90)
cat = st.selectbox("Categoria", ["lanche", "japonesa", "italiana"])
if st.button("Gerar com IA"):
    res = requests.post("http://localhost:8000/gerar-cardapio", json={"nome_prato": nome, "preco_atual": preco, "categoria": cat}).json()
    st.success(res['nome_otimizado'])
    st.write(res['descricao_seo'])
    st.metric("Preco Sugerido", res['preco_sugerido'])
