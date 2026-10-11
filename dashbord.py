
import streamlit as st
from supervisor import SupervisorAgent

st.set_page_config(
    page_title="AI Banking Assistant",
    page_icon="🏦",
    layout="wide",
)

# Initialize supervisor and chat history
if "supervisor" not in st.session_state:
    st.session_state.supervisor = SupervisorAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.title("🏦 AI Banking Assistant")
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Transactions",
        "Fraud Detection",
        "Loan Calculator",
        "AI Banking Chat",
    ],
)

st.title("🏦 AI Banking Assistant")
st.caption("Multi-agent banking demonstration")

if page == "Dashboard":
    st.subheader("Welcome to your banking dashboard")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Customer", "Arun")
    with col2:
        st.metric("Account", "XXXX1234")

    st.info("Demo account balance: ₹25,000")
    st.write("Use the sidebar to access the specialist agents.")

elif page == "Transactions":
    st.subheader("📜 Transaction History")
    if st.button("Show Transaction History"):
        with st.spinner("Loading transactions..."):
            try:
                answer = st.session_state.supervisor.process_query(
                    "Show my transaction history"
                )
                st.write(answer)
            except Exception as error:
                st.error(f"Error: {error}")

elif page == "Fraud Detection":
    st.subheader("🛡️ Fraud Detection")
    st.warning(
        "Demo screening only. A flagged transaction is not proof of fraud."
    )

    if st.button("Scan Transactions", type="primary"):
        with st.spinner("Scanning..."):
            try:
                answer = st.session_state.supervisor.process_query(
                    "Check suspicious transactions"
                )
                st.write(answer)
            except Exception as error:
                st.error(f"Error: {error}")

elif page == "Loan Calculator":
    st.subheader("💳 Loan Eligibility")
    st.caption("Demo assessment only; not an actual bank approval.")

    if st.button("Calculate Demo Eligibility", type="primary"):
        with st.spinner("Calculating..."):
            try:
                answer = st.session_state.supervisor.process_query(
                    "Calculate my loan eligibility"
                )
                st.write(answer)
            except Exception as error:
                st.error(f"Error: {error}")

elif page == "AI Banking Chat":
    st.subheader("💬 Chat with your AI Banking Assistant")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask a banking question...")

    if prompt:
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = st.session_state.supervisor.process_query(
                        prompt
                    )
                    answer = str(answer) if answer is not None else (
                        "The agent returned no response."
                    )
                    st.markdown(answer)

                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )
                except Exception as error:
                    st.error(f"Request failed: {error}")

st.sidebar.divider()
st.sidebar.caption("Student Project | Sample Data")
