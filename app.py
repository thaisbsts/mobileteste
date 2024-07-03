import streamlit as st

def login():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Login")
    
    if login_button:
        # Verifica se o usuário e senha são válidos (neste exemplo, qualquer coisa é válida)
        if username != "" and password != "":
            st.success("Login realizado com sucesso!")
            return True
        else:
            st.error("Usuário ou senha incorretos. Tente novamente.")
    
    return False

def main():
    # Variável de sessão para controlar se o usuário está logado ou não
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        if login():  # Verifica o login
            st.session_state.logged_in = True
    
    if st.session_state.logged_in:
        st.title("Meu Aplicativo Streamlit")
        
        # Conteúdo da página Home (ou outra página principal que você deseje exibir)
        st.write("Conteúdo da página Home")

if __name__ == "__main__":
    main()
