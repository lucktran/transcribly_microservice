import supabase

SUPABASE_URL =
SUPABASE_API_KEY =


def create_supabase_client():
    return supabase.create_client(SUPABASE_URL, SUPABASE_API_KEY)