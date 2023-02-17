# Implementing an expiring web cache and tracker

In this tasks, we will implement a `get_page` function (prototype: `def get_page(url: str) -> str:)`. The core of the function is very simple. It uses the `requests` module to obtain the HTML content of a particular URL and returns it.

Start in a new file named `web.py` and do not reuse the code written in `exercise.py`.

Inside `get_page` track how many times a particular URL was accessed in the key `"count:{url}"` and cache the result with an expiration time of <b>10 seconds</b>.

<em>Bonus</em>: implement this use case with decorators
