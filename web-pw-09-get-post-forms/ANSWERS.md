# Practical Work 9 — Short written answers

## 1. What is the difference between GET and POST?

**GET** is used to *retrieve* information. Its form values are appended to the URL as a query string, for example `/search?student=Ali`. A GET request has no body. It can be bookmarked, shared, cached and kept in the browser history, and repeating it should not change anything on the server. URL length is limited, so GET suits short values such as a search query or calculator numbers.

**POST** is used to *submit data for processing* on the server: registration, sending a message, logging in. Its form values travel in the **request body** (`application/x-www-form-urlencoded` for a normal HTML form), so the URL stays clean, for example `/register`. It is not bookmarked with the data, the browser warns before re-sending it, and it can carry large amounts of data.

In this work:

| Task | Method | URL after submit |
|---|---|---|
| Student Search | GET | `/search?student=Ali` |
| Calculator | GET | `/calculate?a=10&operation=%2B&b=5` |
| Registration | POST | `/register` |
| Contact Teacher | POST | `/contact` |

In the demo (Task 5), the GET form gives `/demo/get?course=Web+Programming`, while the POST form gives `/demo/post` with no values.

## 2. Where are form values transmitted?

* **GET:** in the **URL query string** after `?`, as `name=value` pairs joined by `&` and URL-encoded (`+` becomes `%2B`, a space becomes `+`). On the server they are read from the query parameters (`request.args` in Flask).
* **POST:** in the **body of the HTTP request**, after the headers, in the same `name=value&…` format. On the server they are read from the form data (`request.form` in Flask).

The `name` attribute of each `<input>` becomes the parameter name. That is why the search field is called `student`.

## 3. Why does POST not guarantee confidentiality?

POST only moves the values from the URL into the request body. It does **not encrypt** them. Over plain HTTP, anyone who can see the traffic can read the body: a shared Wi-Fi, a proxy, the network provider. The values can also be seen in the browser developer tools (Network tab) and in server logs, and an attacker can send any body they like.

Data is protected in transit only by **HTTPS (TLS)**, which encrypts the whole request, including the URL and the body. Even with HTTPS, GET values still end up in the browser history and in server logs. Therefore, passwords and personal data should be sent with **POST over HTTPS**.

Also, showing "Registration Successful!" does not mean the data was stored. In this work nothing is saved to a database; the server only receives the values and displays them.
