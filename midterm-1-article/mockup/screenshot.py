"""Renders rag_assistant_mockup.html to rag_assistant_mockup.png with headless Chromium (Playwright)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME if Path(CHROME).exists() else None)
    page = browser.new_page(viewport={"width": 1200, "height": 700}, device_scale_factor=2)
    page.goto((HERE / "rag_assistant_mockup.html").as_uri())
    page.screenshot(path=str(HERE / "rag_assistant_mockup.png"), full_page=True)
    browser.close()
print("saved", HERE / "rag_assistant_mockup.png")
