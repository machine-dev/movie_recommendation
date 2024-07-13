def load_data(file_path):
    """
    Loads movie data from an Excel file.
    
    Parameters:
    - file_path: str, the path to the Excel file containing movie data
    
    Returns:
    - DataFrame: A pandas DataFrame containing the loaded movie data
    """
    import pandas as pd
    
    df = pd.read_excel(file_path)
    return df