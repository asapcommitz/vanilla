# [untitled]markdown

[untitled]markdown is a lightweight, dependency-free Markdown renderer for the web. It uses a custom HTML element `<mark-down>` to fetch and render Markdown files directly in your HTML.

## Demo

See `index.html` for a working demo that loads `content.md`.

## Running Locally

Because [untitled]markdown uses the `fetch` API to load Markdown files, you need to use a local web server to view your project. Opening the HTML file directly from your filesystem (`file://...`) will not work due to browser security policies.

You can use any simple web server. If you have Python installed, you can run one easily.

1.  **Navigate to your project directory** in your terminal.
2.  **Start the server** with this command:

    ```bash
    python3 -m http.server
    ```
    If you have Python 2, the command is `python -m SimpleHTTPServer`.

3.  **Open your browser** and go to `http://localhost:8000`.

You should now see your `index.html` page with the rendered Markdown content.

## Usage

For detailed usage instructions, please see the [documentation](docs.html).