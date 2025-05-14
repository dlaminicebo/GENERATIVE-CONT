import streamlit as st

# System messages defining roles
CREATOR_SYSTEM_MSG = """
Content Creator Agent: You are the Content Creator Agent. Your role is to draft content on topics involving Generative AI. 
Ensure the content is clear, concise, and technically accurate.
"""

CRITIC_SYSTEM_MSG = """
Content Critic Agent: You are the Content Critic Agent. Your role is to evaluate the content drafted by the Content Creator Agent. 
Provide feedback on language clarity and technical correctness, and suggest improvements.
"""

REFLECTION_SYSTEM_MSG = """
Reflection Agent: You are a reflective summary agent. Your role is to summarize the final content after all revisions. 
Make sure it is cohesive, well-written, and incorporates all feedback.
"""

# Initialize session state
if "turn" not in st.session_state:
    st.session_state.turn = 1
    st.session_state.draft = ""
    st.session_state.feedback = ""
    st.session_state.revised = ""
    st.session_state.final = ""

st.title("🤖 AI Agent Collaboration: Content Creator vs. Critic")

st.markdown("**Topic:** `Agent AI`")
st.markdown("---")

# Simulated conversation steps
if st.session_state.turn == 1:
    st.subheader("🔹 Turn 1: Initial Draft by Content Creator Agent")
    st.markdown(f"**System Message:** {CREATOR_SYSTEM_MSG}")
    st.session_state.draft = """
Generative AI refers to systems that can produce text, images, code, or other outputs based on prompts or input data. 
One emerging area is Agent AI—autonomous systems that use generative AI models to make decisions, perform tasks, and communicate across environments. 
These agents combine reasoning, memory, and language capabilities to simulate human-like interactions and automate workflows.
"""
    st.text_area("Drafted Content:", value=st.session_state.draft, height=150)
    if st.button("Proceed to Feedback"):
        st.session_state.turn += 1

elif st.session_state.turn == 2:
    st.subheader("🔹 Turn 2: Feedback from Content Critic Agent")
    st.markdown(f"**System Message:** {CRITIC_SYSTEM_MSG}")
    st.session_state.feedback = """
The draft is generally clear and provides a good introduction to Agent AI. However, consider:
1. Clarifying what "Agent AI" means earlier in the paragraph.
2. Defining how generative AI supports autonomy in agents.
3. Improving flow by connecting ideas more clearly.
4. Avoiding the vague phrase "across environments".
"""
    st.text_area("Critic Feedback:", value=st.session_state.feedback, height=150)
    if st.button("Proceed to Revision"):
        st.session_state.turn += 1

elif st.session_state.turn == 3:
    st.subheader("🔹 Turn 3: Revised Draft by Content Creator Agent")
    revised = """
Agent AI refers to autonomous systems that use generative AI models to reason, make decisions, and interact with users or other systems. 
These agents are powered by large language models that generate natural language, write code, and simulate conversation. 
By integrating memory, logic, and adaptive behavior, Agent AIs can automate workflows and perform complex tasks with minimal human input.
"""
    st.session_state.revised = revised
    st.text_area("Revised Content:", value=st.session_state.revised, height=150)
    if st.button("Proceed to Final Evaluation"):
        st.session_state.turn += 1

elif st.session_state.turn == 4:
    st.subheader("🔹 Turn 4: Final Feedback from Content Critic Agent")
    st.markdown(f"**System Message:** {CRITIC_SYSTEM_MSG}")
    final_feedback = """
Excellent improvement. The revised draft is technically accurate, with improved clarity and logical flow. 
It now defines Agent AI upfront and integrates how generative AI contributes to autonomy. The language is precise and informative.
No further changes needed.
"""
    st.text_area("Final Feedback:", value=final_feedback, height=150)
    if st.button("Proceed to Final Reflection"):
        st.session_state.turn += 1

elif st.session_state.turn == 5:
    st.subheader("🔹 Turn 5: Reflection & Final Output")
    st.markdown(f"**System Message:** {REFLECTION_SYSTEM_MSG}")
    st.success("✅ Reflection complete. Here is the final refined content in markdown:")
    
    final_markdown = """
## 🤖 Agent AI: Empowering Autonomy with Generative Intelligence

Agent AI refers to autonomous systems that use generative AI models to reason, make decisions, and interact with users or other systems.  
These agents are powered by large language models that generate natural language, write code, and simulate conversation.  
By integrating memory, logic, and adaptive behavior, Agent AIs can automate workflows and perform complex tasks with minimal human input.

This blend of reasoning and generative capabilities allows Agent AIs to function in dynamic environments, making them powerful tools across industries.
"""
    st.markdown(final_markdown)

    st.download_button("📥 Download Final Content (Markdown)", data=final_markdown, file_name="agent_ai.md")

# Optional reset
st.sidebar.button("🔄 Reset Conversation", on_click=lambda: st.session_state.clear())
