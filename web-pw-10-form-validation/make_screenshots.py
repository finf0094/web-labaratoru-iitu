"""Takes the screenshots for the report: starts the app, submits the test inputs of every
task in Chromium (Playwright) and saves each page with the real address bar URL on top.
For Task 5A, where the browser blocks the submission, the browser's own validation message
is written under the address bar (native validation bubbles are not captured in screenshots).

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
PORT = 5071
BASE = f"http://127.0.0.1:{PORT}"


def font(size):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except OSError:
        return ImageFont.load_default()


def with_address_bar(png, url, note=None):
    shot = Image.open(png)
    bar_h = 64 + (40 if note else 0)
    img = Image.new("RGB", (shot.width, shot.height + bar_h), "#f1f1ef")
    draw = ImageDraw.Draw(img)
    for i, color in enumerate(("#e46a5f", "#e5b94a", "#67b45d")):
        draw.ellipse((22 + i * 26, 24, 38 + i * 26, 40), fill=color)
    draw.rounded_rectangle((110, 12, shot.width - 24, 52), radius=18, fill="white", outline="#d6d5d0")
    draw.text((130, 20), url, fill="#202020", font=font(20))
    if note:
        draw.rectangle((0, 64, shot.width, bar_h), fill="#fdf6e3")
        draw.text((24, 72), note, fill="#6b4e00", font=font(17))
    img.paste(shot, (0, bar_h))
    img.save(png)


def shoot(page, name, note=None):
    path = OUT / name
    page.screenshot(path=str(path), full_page=True)
    with_address_bar(path, page.url, note)
    print("saved", path.name)


def submit_single(page, number, field, value, name):
    page.goto(f"{BASE}/task{number}")
    page.fill(f"#{field}", value)
    page.click("button")
    shoot(page, name)


def fill_registration(page, url, student, email, age):
    page.goto(BASE + url)
    page.fill("#student", student)
    page.fill("#email", email)
    page.fill("#age", age)


def main():
    OUT.mkdir(exist_ok=True)
    server = make_server("127.0.0.1", PORT, app)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=CHROME if Path(CHROME).exists() else None)
            page = browser.new_page(viewport={"width": 1000, "height": 560})

            for value, label in (("", "empty"), ("   ", "only_spaces"), ("Ali", "ali"), ("Aigerim", "aigerim")):
                submit_single(page, 1, "student", value, f"task1_{label}.png")
            for value, label in (("student@gmail.com", "valid"), ("studentgmail.com", "no_at"),
                                 ("student@", "no_domain"), ("", "empty")):
                submit_single(page, 2, "email", value, f"task2_{label}.png")
            for value, label in (("20", "20"), ("15", "15"), ("150", "150"), ("abc", "abc"), ("", "empty")):
                submit_single(page, 3, "age", value, f"task3_{label}.png")

            fill_registration(page, "/task4", "Ali", "ali@gmail.com", "20")
            page.click("button")
            shoot(page, "task4_example_a_valid.png")
            fill_registration(page, "/task4", "", "invalid-email", "15")
            page.click("button")
            shoot(page, "task4_example_b_all_errors.png")

            # Part A: the browser refuses to send the form and shows its own message.
            fill_registration(page, "/task5", "", "invalid-email", "15")
            page.click("button")
            message = page.eval_on_selector("#student", "el => el.validationMessage")
            shoot(page, "task5a_browser_blocks_submit.png",
                  note=f"Form NOT sent (URL unchanged). Browser message for Full Name: \"{message}\"")
            # Part B: attributes removed, the same values reach the server and are rejected there.
            fill_registration(page, "/task5/without-html-validation", "", "invalid-email", "15")
            page.click("button")
            shoot(page, "task5b_server_rejects.png")
            browser.close()
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()
