# Practical Work 10 — Answers to the discussion questions

## Task 1. Why should surrounding whitespace be removed before checking a name?

A field that contains only spaces looks filled to a simple `if name:` check, but it holds no name. After `strip()`, `"   "` becomes `""` and is rejected with "Name is required!", exactly like an empty field.

Trimming also stores the clean value: `"  Ali "` becomes `"Ali"`. Without it, the same student could appear as two different names, and comparisons and searches would fail.

## Task 2. Does a valid email format guarantee that the mailbox exists?

No. The regular expression only checks the *shape* of the address: some characters, one `@`, a domain and a top-level domain such as `.com`. The address `nobody12345@gmail.com` passes the check but may not exist, and the domain may have no mail server.

The only reliable proof is to send a confirmation email with a link or a code and wait for the user to respond. Format validation catches typos early; it does not verify ownership.

## Task 3. How does checking the input type differ from checking the allowed range?

They are two different steps, done in this order:

1. **Presence** — is anything entered? If not: "Age is required!"
2. **Type** — can the text be converted to an integer? `"abc"` cannot: "Age must be a number!" (and `"20.5"` is not a whole number). Until this check passes, there is no number to compare.
3. **Range** — the value is a valid integer, but is it allowed by the business rule? `15` and `150` are integers, yet they fail "Age must be between 18 and 100!"

The type check answers *"is this a number at all?"*. The range check answers *"is this number acceptable?"*. The order matters, because comparing `"abc"` with 18 would crash or give a meaningless result.

## Task 5. Client-side and server-side validation

**What is client-side validation?**
Checks done by the browser *before* the form is sent: HTML attributes such as `required`, `type="email"`, `type="number"`, `min` and `max`, or JavaScript. They give instant feedback without a round trip. In our test, the browser refused to submit the form and showed "Please fill out this field." (screenshot `task5a_browser_blocks_submit.png`).

**What is server-side validation?**
Checks done by the server *after* it receives the request. In this work they live in `validators.py` and run for every POST, whatever the browser did. The server returns the error messages and does not accept the data.

**What does `required` do?**
It tells the browser that the field must not be empty. The browser blocks submission and highlights the field. It does **not** reject a value made only of spaces, and it does nothing outside the browser.

**Can browser validation be bypassed?** Yes, easily:

* remove the attributes in DevTools, or disable JavaScript;
* send the request directly, without any form:

  ```bash
  curl -X POST -d "student=&email=x&age=abc" http://127.0.0.1:5000/task5
  ```

* use an old or non-standard client, or a script or bot.

In Part B we removed the attributes (`/task5/without-html-validation`). The invalid values reached the server, and the server rejected them all: "Name is required!", "Invalid email!", "Age must be between 18 and 100!" (screenshot `task5b_server_rejects.png`).

**Why must the server validate input?**
The server cannot trust anything that comes from the client. Every rule that protects data integrity (required fields, formats, ranges) must be enforced where the data is processed and stored. Client-side validation is a convenience for honest users. Server-side validation is the actual protection. That is why all required validation in this work runs on the server.
