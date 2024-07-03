import streamlit as st

def main():
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
