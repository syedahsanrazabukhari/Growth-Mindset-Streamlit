import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge 🌱", layout="centered")

st.title("🌱 Growth Mindset Challenge")
st.subheader("Believe in your ability to grow!")

st.markdown("""
A **growth mindset** means you believe your abilities can be developed with dedication and hard work.

### 💡 Why Adopt a Growth Mindset?
- Embrace challenges
- Learn from mistakes
- Persist through difficulties
- Celebrate effort, not just results
- Keep an open mind

### 🧠 How to Practice It?
- Set learning goals
- Reflect on your progress
- Ask for feedback
- Stay positive

---

🌟 *Your journey isn't about proving how smart you are, it's about learning and growing.*

""")

if st.button("I'm Ready to Grow! 🚀"):
    st.success("That's the spirit! Keep going, you're on the path to success. 💪")
