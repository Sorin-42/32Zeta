"""
Standalone launcher for the web UI (without the Discord bot).
Only search, download, and file management are available.
For full playback control, start the bot instead (python main.py) — the web UI runs at :5000 automatically.
"""
from zeta_bot.web_server import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
