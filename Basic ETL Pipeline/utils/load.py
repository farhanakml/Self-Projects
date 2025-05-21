from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def save_to_csv(data, file_path):
    data.to_csv(file_path, index=False)
    return True

def save_to_google_sheets(data, spreadsheet_id, range_name):
    SERVICE_ACCOUNT_FILE = 'google-sheets-api.json'
 
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    credential = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    try:
        # Buat credentials dan service object
        credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()

        # Ubah DataFrame menjadi list of lists
        values = [data.columns.tolist()] + data.values.tolist()

        body = {'values': values}

        result = sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()

        print("✅ Data berhasil disimpan ke Google Sheets!")
        return True

    except Exception as e:
        print(f"❌ Terjadi kesalahan saat menyimpan ke Google Sheets: {e}")
        return False