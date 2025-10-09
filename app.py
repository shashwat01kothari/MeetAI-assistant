# app.py
import streamlit as st
from config import GEMINI_API_KEY

# Import agents
from agents.transcription_agent import AudioTranscriptionAgent
from agents.analysis_agent import AnalysisAgent
from agents.action_item_agent import ActionItemAgent
from agents.dependency_graph_agent import DependencyGraphAgent

# Import utility
from utils.file_handler import save_temp_file, remove_temp_file

# --- Streamlit UI Configuration ---
st.set_page_config(page_title="Meeting AI Assistant", layout="wide")
st.title("Meeting AI Assistant")
st.markdown("Convert meeting audio or text into summaries, action items, and insights.")

# --- Main Application Logic ---
if not GEMINI_API_KEY or "YOUR_GEMINI_API_KEY" in GEMINI_API_KEY:
    st.error("Please set your GEMINI_API_KEY in the .env file.")
else:
    # Initialize Agents
    transcription_agent = AudioTranscriptionAgent()
    analysis_agent = AnalysisAgent()
    action_item_agent = ActionItemAgent()
    graph_agent = DependencyGraphAgent()

    # --- Input Selection ---
    st.sidebar.title("Input Options")
    input_option = st.sidebar.radio("Choose input type", ("Upload Audio File", "Paste Text Transcript"))
    
    transcript = ""

    if input_option == "Upload Audio File":
        audio_file = st.sidebar.file_uploader("Upload an audio file (.wav, .mp3)", type=["wav", "mp3"])
        if st.sidebar.button("Process Audio") and audio_file:
            with st.spinner("Transcribing audio..."):
                temp_audio_path = save_temp_file(audio_file)
                if temp_audio_path:
                    transcript = transcription_agent.transcribe(temp_audio_path)
                    remove_temp_file(temp_audio_path)
                    st.session_state.transcript = transcript

    else: # Paste Text Transcript
        transcript_input = st.sidebar.text_area("Paste the meeting transcript here", height=300)
        if st.sidebar.button("Process Text") and transcript_input:
            st.session_state.transcript = transcript_input

    # --- Display and Process Transcript ---
    if 'transcript' in st.session_state and st.session_state.transcript:
        st.subheader("📝 Transcript")
        st.text_area("Full Transcript", st.session_state.transcript, height=200)
        
        with st.spinner("Analyzing transcript... This may take a moment."):
            analysis_output = analysis_agent.analyze(st.session_state.transcript)
            
            # --- MODIFIED AGENT CALL ---
            # The agent now returns a tuple (results, warning)
            action_items, ner_warning = action_item_agent.extract_action_items(st.session_state.transcript)
            
            summary_points = analysis_output.get("summary", [])
            insights_points = analysis_output.get("insights", [])

        st.subheader("📌 Key Summary Points")
        for point in summary_points:
            st.markdown(f"- {point}")
        
        st.subheader("✅ Action Items")

        # --- NEW: DISPLAY THE WARNING IN THE UI ---
        if ner_warning:
            st.warning(ner_warning)

        if action_items:
            st.table(action_items)
        else:
            st.info("No action items were identified.")
            
        st.subheader("💡 Insights & Risks")
        for point in insights_points:
            st.markdown(f"- {point}")

        st.subheader("📊 Task Dependency Graph")
        if action_items:
            graph_path = graph_agent.create_graph(action_items)
            if graph_path:
                with open(graph_path, "r", encoding="utf-8") as f:
                    st.components.v1.html(f.read(), height=520)
                remove_temp_file(graph_path)
        else:
            st.info("No graph to display as no action items were found.")