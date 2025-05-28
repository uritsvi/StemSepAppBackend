from fastapi import FastAPI, Depends
from supabase import create_client, Client

# Initialize FastAPI app
app = FastAPI()

# Supabase configuration
SUPABASE_URL = "https://your-supabase-url.supabase.co"
SUPABASE_KEY = "your-supabase-key"

# Create Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Dependency to provide Supabase client
def get_db():
    return supabase

@app.get("/")
def read_root(db: Client = Depends(get_db)):
    # Example query to Supabase
    data = db.table("example_table").select("*").execute()
    return {"message": "Hello, FastAPI!", "data": data.data}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None, db: Client = Depends(get_db)):
    # Example query to Supabase
    data = db.table("items").select("*").eq("id", item_id).execute()
    return {"item_id": item_id, "q": q, "data": data.data}