"""Takes the screenshots for the report: starts the app, fills every form in Chromium
(Playwright) and saves each page with the real address bar URL drawn on top.

Usage: pip install playwright pillow && python3 make_screenshots.py
"""
import threading
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
from werkzeug.serving import make_server

from app import app

HERE = Path(__file__).resolve().parent
OUT = HERE / "screenshots"
CHROME = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"  # used if present
PORT = 5059
BASE = f"http://127.0.0.1:{PORT}"


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    try:
        return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)
    except OSError:
        return ImageFont.load_default()


def with_address_bar(png, url):
    """Draw a light browser address bar with the page URL above the screenshot."""
    shot = Image.open(png)
    bar_h = 64
    img = Image.new("RGB", (shot.width, shot.height + bar_h), "#f1f1ef")
    draw = ImageDraw.Draw(img)
    for i, color in enumerate(("#e46a5f", "#e5b94a", "#67b45d")):
        draw.ellipse((22 + i * 26, 24, 38 + i * 26, 40), fill=color)
    draw.rounded_rectangle((110, 12, shot.width - 24, bar_h - 12), radius=18, fill="white", outline="#d6d5d0")
    draw.text((130, 20), url, fill="#202020", font=font(20))
    img.paste(shot, (0, bar_h))
    img.save(png)


def shoot(page, name):
    path = OUT / name
    page.screenshot(path=str(path), full_page=True)
    with_address_bar(path, page.url)
    print("saved", path.name, "→", page.url)


def main():
    OUT.mkdir(exist_ok=True)
    server = make_server("127.0.0.1", PORT, app)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=CHROME if Path(CHROME).exists() else None)
            page = browser.new_page(viewport={"width": 1000, "height": 640}, device_scale_factor=1)

            page.goto(BASE + "/student-search")
            page.fill("#student", "Ali")
            shoot(page, "task1_1_search_form.png")
            page.click("button")
            shoot(page, "task1_2_search_result_url.png")

            page.goto(BASE + "/register")
            page.fill("#first_name", "Ali")
            page.fill("#last_name", "Akhmetov")
            page.fill("#email", "ali@example.com")
            shoot(page, "task2_1_registration_form.png")
            page.click("button")
            shoot(page, "task2_2_registration_result.png")

            page.goto(BASE + "/calculator")
            page.fill("#a", "10")
            page.select_option("#operation", "+")
            page.fill("#b", "5")
            shoot(page, "task3_1_calculator_form.png")
            page.click("button")
            shoot(page, "task3_2_calculator_result_url.png")
            page.goto(BASE + "/calculate?a=10&b=0&operation=%2F")
            shoot(page, "task3_3_division_by_zero.png")

            page.goto(BASE + "/contact")
            page.fill("#name", "Dana")
            page.fill("#message", "I have a question about GET and POST.")
            shoot(page, "task4_1_contact_form.png")
            page.click("button")
            shoot(page, "task4_2_contact_result.png")
            page.goto(BASE + "/contact")
            page.click("button")
            shoot(page, "task4_3_contact_empty_fields.png")

            page.goto(BASE + "/demo")
            shoot(page, "task5_1_demo_page.png")
            page.fill("#course", "Web Programming")
            page.click("form[method=GET] button")
            shoot(page, "task5_2_demo_after_get.png")
            page.fill("#login", "student01")
            page.fill("#password", "secret123")
            page.click("form[method=POST] button")
            shoot(page, "task5_3_demo_after_post.png")
            browser.close()
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
