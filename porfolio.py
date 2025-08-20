import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", page_icon=":wave:", layout="wide")

# --- LOAD ASSETS ---
profile_pic = Image.open(r"C:\Users\DELL\Pictures\Saved Pictures\sowmya.jpg")
resume_file = r"C:\Users\DELL\Documents\resume.pdf.pdf"

# --- HERO SECTION ---
st.title("Hi, I'm Sowmya👋")
st.subheader("Btech |CSE student| aspiring software engineer")

col1, col2 = st.columns([1, 2])
with col1:
    st.image(profile_pic, width=150)

with col2:
    st.write(
        """
        Welcome to my portfolio! I'm a passionate developer with experience in Python, web development,
        and building real-world applications. I love turning ideas into reality and collaborating on open-source.
        """
    )

# Resume Download
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.download_button(label="📄 Download Resume", data=PDFbyte, file_name="John_Doe_Resume.pdf", mime='application/octet-stream')

st.markdown("---")

# --- SKILLS ---
st.header("🛠️ Skills")
st.write("""
- **Languages:** Python, JavaScript, SQL
- **Frameworks:** Streamlit, Flask, Django, React
- **Tools:** Git, Docker, Postman
- **Databases:** MySQL, PostgreSQL, MongoDB
""")

st.markdown("---")
# --- EDUCATION ---
st.header("🎓 Education")

st.subheader("Bachelor of Technology in Computer Science")
st.write("Dhanekula institute of engineering and technology, vijayawada")
st.write("2023-2027")
st.write("- CGPA: 9.06/10")
st.write("- Relevant coursework: Data Structures, Algorithms, Web Development, Machine Learning")

st.subheader("Higher Secondary Education (12th Grade)")
st.write("Narayana Junior College, Vijayawada")
st.write("2021 – 2023")
st.write("- Percentage: 97%")
st.write("- Science stream with Mathematics, Physics, Chemistry")

st.subheader("Secondary School (10th Grade)")
st.write("viswavani EM high school, vijayawada")
st.write("2020-2021")
st.write("- GPA: 10/10")


# --- PROJECTS ---
st.header("💼 Projects")

projects = {
    "Portfolio Website": {
        "description": "This portfolio website built with Streamlit to showcase my work.",
        "url": "https://github.com/yourgithub/portfolio"
    },
    "Task Manager App": {
        "description": "A full-stack to-do app using Flask and React.",
        "url": "https://github.com/yourgithub/task-manager"
    },
    "ML Price Predictor": {
        "description": "Machine learning model to predict housing prices.",
        "url": "https://github.com/yourgithub/ml-price-predictor"
    }
}

for project, details in projects.items():
    st.subheader(project)
    st.write(details["description"])
    st.markdown(f"[🔗 GitHub Link]({details['url']})")

st.markdown("---")

# --- CONTACT ---
st.header("📫 Contact Me")
st.write("Feel free to reach out!")

contact_form = """
<form action="https://formsubmit.co/your_email@example.com" method="POST">
    <input type="text" name="name" placeholder="Your name" required><br><br>
    <input type="email" name="email" placeholder="Your email" required><br><br>
    <textarea name="message" placeholder="Your message here" required></textarea><br><br>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)