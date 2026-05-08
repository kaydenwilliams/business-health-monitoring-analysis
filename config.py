from urllib.parse import quote_plus
FRED_API_KEY = "71ee4ffd9fa766eb701a63380af24291"

password = quote_plus("P@ssw0rd!")
DB_CONNECTION = f"mysql+pymysql://root:{password}@localhost/business_health"