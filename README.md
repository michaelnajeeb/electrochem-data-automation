# **electrochem-data-automation**
This repository contains python scripts to help automate electrochemical analysis of battery cell data. 

# **Electrochemical Data Automation**

This project automates the processing of electrochemical test data from .txt files. It integrates with Google Drive and Google Sheets to create a fully automated pipeline that will:
- Monitor a Google Drive folder for new `.txt` test data files.
- Extract metadata (cell ID, active material mass) from a Google spreadsheet.
- Merges the `.txt` file data with metadata from the Google spreadsheet.
- Normalizes capacity (mAh/g).
- Outputs:
  - A combined CSV (electrochemical data + metadata).
  - A Voltage vs Capacity plot.
- Stores outputs in organized Google Drive subfolders based on date generated.

---

## **Folder Structure in Google Drive**

- **Cell Cycler Data (.txt)**  
  _Input folder._ Drop raw `.txt` files to be processed here.  

- **Combined Data**  
  _Output folder._ Processed CSV files containing both electrochemical data and metadata are saved here, organized by date generated.  

- **Generated Figures**  
  _Output folder._ Generated Voltage vs Capacity plots are saved here, organized by date generated.  

- **Cell Tracker v3**  
  _Google Sheet._ Stores cell metadata (one tab per lab user).

---

## **Getting Started**

### **1. Clone the repository**

```bash
git clone https://github.com/michaelnajeeb/electrochem-data-automation.git
cd electrochem-data-automation
```

### **2. Set up Python env**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **3. Add Google credentials**

1. Log into Google Cloud https://console.cloud.google.com
2. Create a Google Cloud Project: Click the project selector > New Project > Name Project > Create
3. Enable required APIs: APIs & Services > Library > Enable both Google Drive API & Google Sheet API
4. Create a Service Account: APIs & Services > Credentials > Create Credentials > Service Account > Name Service Account > Done
5. Generate a JSON key for the service account: Service Accounts tab > Select new account > Keys > Add Key > Create new key > JSON > Download to electrochem-data-automation folder > Rename to "credentials.json"
6. Share the Shared Drive with the service account
7. Copy the folder IDs and replace variables in electrochemical_data_automation.py

### **4. Verify Google access**

verify service account has access to Google drive and Google sheet by running:
```bash
python google_access_verification.py
```

the python script will print the sheetname and a list of .txt files to verify access.

### **5. Run the pipeline**

run the following python script:
```bash
python electrochemical_data_automation.py
```