import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus    # ← add this
import logging

logging.basicConfig(level=logging.INFO)

DB_HOST     = "18.136.157.135"
DB_PORT     = "3306"
DB_USER     = "dm_team"
DB_PASSWORD = "DM!$Team@&27920!"
DB_NAME     = "project_itsm"
TABLE_NAME  = "dataset_list"

def sql_to_csv():
    try:
        print("🚀 Script Started...")

        # ✅ Escape special characters in password
        password = quote_plus(DB_PASSWORD)

        print("🔄 Step 1: Connecting to MySQL...")
        connection_url = (
            f"mysql+pymysql://{DB_USER}:{password}"
            f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            f"?connect_timeout=30"
        )
        engine = create_engine(
            connection_url,
            pool_pre_ping=True
        )

        # Test connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("✅ Connected successfully!")

        # Fetch data
        print("🔄 Step 2: Fetching data...")
        df = pd.read_sql(f"SELECT * FROM {TABLE_NAME}", engine)
        print(f"✅ Got {len(df)} rows, {len(df.columns)} columns!")

        # Save CSV
        print("🔄 Step 3: Saving CSV...")
        df.to_csv("tickets.csv", index=False)
        print("✅ Saved → E:\\ISTM_ML\\Data\\tickets.csv")

        # Preview
        print("\n--- Preview ---")
        print(df.head())

    except Exception as e:
        print(f"\n❌ ERROR TYPE : {type(e).__name__}")
        print(f"❌ ERROR MSG  : {e}")

if __name__ == "__main__":
    sql_to_csv()
    print("\n🏁 Script Finished!")