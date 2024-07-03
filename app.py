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
    logged_in = login()  # Verifica o login
    
    if logged_in:
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
