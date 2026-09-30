"""Console commands; load models only after parsing command-line options."""
import argparse
from pathlib import Path
import subprocess
import sys


def chat():
    parser = argparse.ArgumentParser(description="Chat with telecom support in your terminal.")
    parser.parse_args()
    from .main import main

    main()


def web():
    parser = argparse.ArgumentParser(description="Launch the telecom Streamlit app.")
    _, streamlit_args = parser.parse_known_args()
    app = Path(__file__).resolve().with_name("app.py")
    raise SystemExit(subprocess.call([
        sys.executable, "-m", "streamlit", "run", str(app), *streamlit_args,
    ]))


def ingest():
    parser = argparse.ArgumentParser(description="Embed the bundled telecom knowledge sources.")
    parser.add_argument("source", choices=["all", "faq", "tickets", "pdf"], nargs="?", default="all")
    args = parser.parse_args()
    from importlib import import_module

    sources = ["faq", "tickets", "pdf"] if args.source == "all" else [args.source]
    for source in sources:
        import_module(f".ingest_{source}", __package__).main()
