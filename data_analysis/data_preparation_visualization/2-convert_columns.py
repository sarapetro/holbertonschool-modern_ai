def convert_columns(df):
  """Converts columns of the given dataset"""
  df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
  df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
  return df
