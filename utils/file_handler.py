# utils/file_handler.py
import tempfile
import os

def save_temp_file(uploaded_file):
    """
    Saves a Streamlit UploadedFile to a temporary file on disk.

    Args:
        uploaded_file: The file object from st.file_uploader.

    Returns:
        str: The path to the temporary file.
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        print(f"Error saving temporary file: {e}")
        return None

def remove_temp_file(file_path: str):
    """
    Removes a file from the given path.

    Args:
        file_path (str): The path to the file to be removed.
    """
    try:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error removing temporary file: {e}")