````md
# Introducción a GitHub y Streamlit

## ¿Qué es GitHub?

GitHub es una plataforma basada en la nube que permite almacenar, administrar y compartir proyectos de programación utilizando Git, un sistema de control de versiones.

GitHub es muy utilizado por desarrolladores, estudiantes y empresas porque facilita el trabajo colaborativo y el seguimiento de cambios en los proyectos.

### Funciones principales de GitHub
- Guardar proyectos en repositorios.
- Llevar control de versiones.
- Trabajar en equipo.
- Compartir código públicamente o de manera privada.
- Documentar proyectos mediante archivos README.

---

# ¿Qué es Git?

Git es un sistema de control de versiones que permite registrar cambios en archivos y proyectos de programación.

Con Git se pueden:
- Guardar versiones anteriores de un proyecto.
- Recuperar cambios.
- Trabajar con varias personas al mismo tiempo.
- Organizar el desarrollo de software.

---

# Conceptos básicos de GitHub

## Repositorio
Es el espacio donde se almacena un proyecto completo.

## Commit
Es un registro o “guardado” de los cambios realizados.

## Branch
Es una rama de trabajo independiente dentro del proyecto.

## Push
Permite subir cambios locales al repositorio en GitHub.

## Pull
Permite descargar cambios desde GitHub.

---

# Comandos básicos de Git

```bash
git init
````

Inicializa un repositorio local.

```bash
git status
```

Muestra el estado de los archivos.

```bash
git add .
```

Agrega archivos para preparar un commit.

```bash
git commit -m "Primer commit"
```

Guarda los cambios realizados.

```bash
git push
```

Sube cambios a GitHub.

```bash
git pull
```

Descarga cambios desde GitHub.

---

# ¿Qué es Streamlit?

Streamlit es una herramienta de Python que permite crear aplicaciones web interactivas de manera rápida y sencilla.

Es muy utilizada en:

* Ciencia de datos
* Machine Learning
* Dashboards
* Visualización de datos
* Aplicaciones de análisis

Con Streamlit se pueden convertir scripts de Python en aplicaciones web sin necesidad de saber desarrollo web avanzado.

---

# Instalación de Streamlit

Para instalar Streamlit se utiliza el siguiente comando:

```bash
pip install streamlit
```

---

# Primer programa en Streamlit

```python
import streamlit as st

st.title("Mi primera app")

st.write("Hola mundo desde Streamlit")
```

Para ejecutar la aplicación:

```bash
streamlit run app.py
```

---

# Componentes básicos de Streamlit

## Texto

```python
st.title("Título")
st.header("Encabezado")
st.write("Texto normal")
```

## Entrada de datos

```python
nombre = st.text_input("Escribe tu nombre")
```

## Botones

```python
if st.button("Aceptar"):
    st.write("Botón presionado")
```

## Mostrar tablas

```python
import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Ana", "Luis"],
    "Edad": [20, 22]
})

st.dataframe(df)
```

---

# Relación entre GitHub y Streamlit

GitHub y Streamlit se complementan muy bien porque:

* GitHub almacena el proyecto.
* Streamlit crea la aplicación.
* Se puede compartir el código y colaborar.
* Es posible publicar aplicaciones de Streamlit directamente desde GitHub.

---

# Publicar una aplicación Streamlit

## Pasos generales

1. Crear proyecto en Python.
2. Subir archivos a GitHub.
3. Crear cuenta en Streamlit Community Cloud.
4. Conectar el repositorio de GitHub.
5. Publicar la aplicación.

---

# Ventajas de usar GitHub y Streamlit

## GitHub

* Control de versiones.
* Trabajo colaborativo.
* Respaldo de proyectos.
* Portafolio profesional.

## Streamlit

* Fácil de usar.
* Desarrollo rápido.
* Ideal para análisis de datos.
* Interfaz interactiva.

---

# Conclusión

GitHub y Streamlit son herramientas muy importantes para estudiantes y desarrolladores. GitHub permite administrar y compartir proyectos mediante control de versiones, mientras que Streamlit facilita la creación de aplicaciones web interactivas usando Python. La combinación de ambas herramientas ayuda a desarrollar proyectos profesionales de análisis de datos y programación de manera más organizada y colaborativa.

```
```
