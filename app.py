import streamlit as st

# Configuração da página (título da aba e layout)
st.set_page_config(
    page_title="Calculadora Interativa",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Interativa")
st.write("Insira os números, escolha a operação e clique em **Calcular**!")

st.divider()

# 2. Entrada dos dois números
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro número:", value=0.0, format="%.2f")

with col2:
    num2 = st.number_input("Segundo número:", value=0.0, format="%.2f")

# 3. Seleção da operação matemática
operacao = st.radio(
    "Escolha a operação:",
    options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"],
    horizontal=True
)

st.divider()

# 4 e 5. Botão de ação, lógica e efeitos visuais
if st.button("Calcular", type="primary", use_container_width=True):
    # Tratamento especial de divisão por zero
    if operacao == "Divisão (/)" and num2 == 0:
        st.error("⚠️ Ops! Não é possível dividir por zero. Escolha outro valor para o segundo número.")
    else:
        # Dispara o efeito visual de balões celebrando o sucesso
        st.balloons()

        # Processamento das operações
        if operacao == "Soma (+)":
            resultado = num1 + num2
            simbolo = "+"
        elif operacao == "Subtração (-)":
            resultado = num1 - num2
            simbolo = "-"
        elif operacao == "Multiplicação (*)":
            resultado = num1 * num2
            simbolo = "×"
        elif operacao == "Divisão (/)":
            resultado = num1 / num2
            simbolo = "÷"

        # Exibição estilizada em grande destaque
        st.metric(label="Resultado", value=f"{resultado:.2f}")
        st.success(f"Cálculo realizado com sucesso: {num1} {simbolo} {num2} = {resultado:.2f}")

#Feito
