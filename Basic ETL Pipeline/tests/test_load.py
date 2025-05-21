import os
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from utils.load import save_to_csv, save_to_google_sheets

def test_save_to_csv(tmp_path):
    df = pd.DataFrame({"A": [1, 2]})
    file_path = tmp_path / "test.csv"
    save_to_csv(df, file_path)

    assert os.path.exists(file_path)
    loaded_df = pd.read_csv(file_path)
    assert loaded_df.equals(df)

def save_to_google_sheets(dataframe, spreadsheet_id, range_name):
    try:
        SERVICE_ACCOUNT_FILE = './google-sheets-credentials.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        values = dataframe.astype(str).values.tolist()  # convert df to list of strings
        body = {'values': values}

        sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()

        print("✅ Data berhasil disimpan ke Google Sheets.")
        return True
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat menyimpan ke Google Sheets: {e}")
        return False


