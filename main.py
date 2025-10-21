from ui_module import jarvis_ui
import datetime
import webbrowser
import os
import subprocess
import requests


def run_jarvis(query):
    query = query.lower()

    # Define site mappings
    sites = {
        "youtube": "https://youtube.com",
        "wikipedia": "https://wikipedia.org",
        "google": "https://google.com"
    }

    for key, url in sites.items():
        if f"open {key}" in query:
            return f"Opening {key}...", webbrowser.open(url)

    if "time" in query:
        return f"The time is {datetime.datetime.now().strftime('%I:%M %p')}"

    if "search" in query:
        search_query = query.replace("search", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        return f"Searching for {search_query}"

    if "joke" in query:
        return "Why don’t skeletons fight each other? Because they don’t have the guts!"



    return "I'm not sure how to respond to that."

if __name__ == "__main__":
    jarvis_ui(run_callback=run_jarvis)
