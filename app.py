import streamlit as st

def show_header(text_title: str):
    # Layout: logo + title side by side
    col1, col2 = st.columns([1, 6])
    
    with col1:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/32/Universidad_Panamericana_Logo_Dorado.jpg",
            width=100
        )
        
    with col2:
        st.title(text_title)
        st.caption("📘 Developed for: *Business Intelligence (Graduate Level)*")
        st.caption("Instructor: Edgar Avalos-Gauna (2025), Universidad Panamericana")


# Containers correctos
head_c = st.container()
main_c = st.container()

# Header
with head_c:
    show_header('Mi primer tablero en Streamlit')

# Main content
with main_c:
    st.markdown('**Hola** Mundo!!!')
