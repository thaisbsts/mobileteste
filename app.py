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
    logged_in = st.session_state.get('logged_in', False)
    
    if not logged_in:
        logged_in = login()  # Verifica o login
        
        # Atualiza a variável de sessão com o status de login
        st.session_state['logged_in'] = logged_in
    
    if logged_in:
        # Limpa a tela de login
        st.empty()
        
        st.title("Meu Aplicativo Streamlit")
        
        # Conteúdo dinâmico da página
        page = st.sidebar.radio("Selecione uma página", ["Home", "Library", "Tutorials", "Development", "Download"])
        
        if page == "Home":
            st.write("Conteúdo da página Home")
        elif page == "Library":
            st.write("Conteúdo da página Library")
        elif page == "Tutorials":
            st.write("Conteúdo da página Tutorials")
        elif page == "Development":
            st.write("Conteúdo da página Development")
        elif page == "Download":
            st.write("Conteúdo da página Download")

if __name__ == "__main__":
    main()
