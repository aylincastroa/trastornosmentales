import streamlit as st

st.set_page_config(page_title="Cuestionario sobre Trastornos Mentales", layout="centered")
st.title("🧠 Cuestionario sobre Trastornos Mentales")

# Lista de preguntas, opciones, respuestas y retroalimentación
questions = [
    {
        "question": "¿Cuál de los siguientes trastornos se caracteriza principalmente por períodos de euforia y depresión?",
        "options": ["Esquizofrenia", "Trastorno bipolar", "Trastorno obsesivo-compulsivo"],
        "answer": "Trastorno bipolar",
        "feedback": "El trastorno bipolar se caracteriza por cambios extremos en el estado de ánimo, desde la manía hasta la depresión."
    },
    {
        "question": "¿Qué es un síntoma común de la depresión mayor?",
        "options": ["Alucinaciones visuales", "Cambios extremos de identidad", "Pérdida de interés en actividades diarias"],
        "answer": "Pérdida de interés en actividades diarias",
        "feedback": "La anhedonia, o pérdida de interés en actividades placenteras, es un síntoma central de la depresión mayor."
    },
    {
        "question": "¿Cuál de estos trastornos se asocia con miedos intensos y persistentes a situaciones específicas?",
        "options
