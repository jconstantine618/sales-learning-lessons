
import openai
import streamlit as st

# Constants
MODULE_COUNT = 10
QUESTIONS_PER_MODULE = 10

st.set_page_config(page_title="Carnegie Sales Manager Academy", layout="centered")

# Helper to show lessons
def show_lesson(module_num, principle_summary):
    st.header(f"Module {module_num}: {principle_summary['title']}")
    st.markdown(principle_summary['content'])

# Helper to show quiz
def show_quiz(module_num, quiz):
    st.subheader("Quiz Time!")
    score = 0
    for i, q in enumerate(quiz):
        st.markdown(f"**{i+1}. {q['question']}**")
        user_answer = st.radio("Choose one:", q['choices'], key=f"q{module_num}_{i}")
        if user_answer == q['answer']:
            score += 1
            st.success(f"Correct! {q['explanation_correct']}")
        else:
            st.error(f"Wrong. {q['explanation_wrong']}")
    st.markdown(f"### Your score for Module {module_num}: {score}/{len(quiz)}")

# Placeholder logic (replace with full module loading)
if __name__ == "__main__":
    st.title("Dale Carnegie 30 Principles: Sales Leader Training")
    module = st.selectbox("Choose a Module", list(range(1, MODULE_COUNT + 1)))
    show_lesson(module, {
        "title": f"Principle {module} (Placeholder)",
        "content": "This will be dynamically loaded from a principles data file."
    })
    sample_quiz = [{
        "question": "What does Carnegie say about criticism?",
        "choices": ["It builds trust", "It encourages resentment", "It improves performance"],
        "answer": "It encourages resentment",
        "explanation_correct": "Criticism puts people on the defensive and breeds resentment.",
        "explanation_wrong": "Criticism often causes resentment and defensiveness, not trust or improvement."
    }]
    show_quiz(module, sample_quiz)
