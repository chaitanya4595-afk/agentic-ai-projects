"""Shared paths for source checkouts and installed distributions."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path.cwd() / ".env")

DATA_DIR = Path(__file__).resolve().parent / "data"
CHROMA_DIR = str(Path(os.getenv("TELECOM_CHROMA_DIR", "chroma_store")).expanduser().resolve())
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
