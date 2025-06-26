import streamlit as st

# Título
st.title("Cuestionario sobre Trastornos Mentales")

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
        "options": ["Fobia específica", "Trastorno de personalidad antisocial", "Trastorno de pánico"],
        "answer": "Fobia específica",
        "feedback": "Las fobias específicas implican un miedo irracional y desproporcionado ante un objeto o situación concreta."
    },
    {
        "question": "¿Qué caracteriza principalmente al trastorno obsesivo-compulsivo (TOC)?",
        "options": ["Delirios de persecución", "Impulsividad extrema", "Pensamientos repetitivos no deseados y conductas rituales"],
        "answer": "Pensamientos repetitivos no deseados y conductas rituales",
        "feedback": "El TOC incluye obsesiones (pensamientos intrusivos) y compulsiones (acciones repetitivas) para reducir la ansiedad."
    },
    {
        "question": "¿Cuál es un síntoma típico de la esquizofrenia?",
        "options": ["Manía", "Alucinaciones auditivas", "Conductas repetitivas"],
        "answer": "Alucinaciones auditivas",
        "feedback": "Las alucinaciones auditivas, como oír voces que no existen, son comunes en personas con esquizofrenia."
    },
    {
        "question": "¿Qué caracteriza a un ataque de pánico?",
        "options": ["Cambios de humor prolongados", "Episodios repentinos de miedo intenso", "Pérdida gradual del interés social"],
        "answer": "Episodios repentinos de miedo intenso",
        "feedback": "El trastorno de pánico implica ataques repentinos de miedo o malestar intenso, acompañados de síntomas físicos."
    },
    {
        "question": "¿Cuál de los siguientes trastornos suele comenzar en la infancia y se caracteriza por dificultades para comunicarse?",
        "options": ["Trastorno del espectro autista", "Trastorno de ansiedad generalizada", "Trastorno narcisista de la personalidad"],
        "answer": "Trastorno del espectro autista",
        "feedback": "El autismo se presenta desde edades tempranas y afecta la comunicación, la interacción social y el comportamiento."
    },
    {
        "question": "¿Qué es común en el trastorno de ansiedad generalizada (TAG)?",
        "options": ["Estados maníacos", "Preocupación constante e incontrolable", "Cambios extremos de identidad"],
        "answer": "Preocupación constante e incontrolable",
        "feedback": "El TAG implica una ansiedad crónica y excesiva por diversos aspectos de la vida diaria."
    },
    {
        "question": "¿Qué profesional está capacitado para diagnosticar y tratar trastornos mentales con medicación?",
        "options": ["Psicólogo clínico", "Trabajador social", "Psiquiatra"],
        "answer": "Psiquiatra",
        "feedback": "Solo el psiquiatra, por ser médico, puede recetar medicamentos para trastornos mentales."
    },
    {
        "question": "¿Qué factor puede contribuir al desarrollo de un trastorno mental?",
        "options": ["Mal clima", "Exposición prolongada al estrés", "Edad adulta"],
        "answer": "Exposición prolongada al estrés",
        "feedback": "El estrés crónico, junto con factores genéticos y ambientales, puede aumentar el riesgo de desarrollar un trastorno mental."
    }
]

# Estado de la sesión
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.correct = False
    st.session_state.answered = False

q_idx = st.session_state.question_index

if q_idx < len(questions):
    q = questions[q_idx]
    st.subheader(f"Pregunta {q_idx + 1}:")
    st.write(q["question"])

    selected = st.radio("Selecciona tu respuesta:", q["options"], key=q_idx)

    if st.button("Responder", key=f"submit_{q_idx}") and not st.session_state.answered:
        st.session_state.answered = True
        if selected == q["answer"]:
            st.success("✅ ¡Correcto!")
            st.info(q["feedback"])
            st.session_state.correct = True
        else:
            st.error("❌ Incorrecto.")
            st.info(q["feedback"])
            st.session_state.correct = False

    if st.session_state.answered and st.session_state.correct:
        if st.button("Siguiente"):
            st.session_state.question_index += 1
            st.session_state.answered = False
            st.experimental_rerun()
else:
    st.balloons()
    st.success("🎉 ¡Felicidades! Has completado todas las preguntas del cuestionario.")
