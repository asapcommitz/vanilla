
# [untitled]markdown Documentation

Welcome to the official documentation for [untitled]markdown, a lightweight and dependency-free Markdown renderer for the web.

## <a name="introduction"></a>Introduction

[untitled]markdown is a simple yet powerful tool that allows you to render Markdown files directly in your HTML without any complex setup or dependencies. It's built with vanilla JavaScript and is designed to be as easy to use as possible.

The core philosophy of [untitled]markdown is to provide a "no-nonsense" Markdown experience. It's perfect for project documentation, personal blogs, or any scenario where you want to write in Markdown and have it seamlessly appear on your webpage.

## <a name="features"></a>Features

*   **Zero Dependencies:** Written entirely in vanilla JavaScript.
*   **Easy to Use:** Just one script tag and a custom HTML element.
*   **Lightweight:** The runtime is small and fast.
*   **Custom Elements:** Uses a simple `<mark-down>` custom element.
*   **Extensible:** Easily styled with CSS.
*   **Syntax Highlighting:** Supports automatic syntax highlighting with a library like `highlight.js`.

## <a name="installation"></a>Installation

Getting started with [untitled]markdown is incredibly simple. You can use it by directly linking to the `runtime.js` file from a CDN, or by hosting the file yourself.

### Using the CDN (Recommended)

This is the easiest way to get started. Just add this script tag to the bottom of your `<body>` section. It will automatically fetch the latest version of [untitled]markdown.

```html
<script src="https://cdn.jsdelivr.net/gitlab/untitledcomputer/untitledmarkdown/raw/main/runtime.js" defer></script>
```

### Self-Hosting

If you prefer to host the file yourself:

1.  **Download `runtime.js`:**
    You can download the `runtime.js` file from the official repository or clone the entire project.

2.  **Include it in your HTML:**
    Place the `runtime.js` script tag at the bottom of your `<body>` section.

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>My Awesome Page</title>
    </head>
    <body>
      <!-- Your content here -->
      <script src="runtime.js"></script>
    </body>
    </html>
    ```

## <a name="how-it-works"></a>How It Works

[untitled]markdown works by automatically finding a placeholder element in your HTML and injecting your Markdown content into it. All you need to do is add a special data attribute to an element, and the runtime script does the rest.

By default, it turns an empty element with the `data-untitledmarkdown-autofill` attribute into a rendered Markdown viewer.

## <a name="usage"></a>Usage

The easiest way to use [untitled]markdown is to add the `data-untitledmarkdown-autofill` attribute to an empty container element in your HTML, like `<main>`, `<div>`, or `<article>`. The script will automatically load and render the specified Markdown file into this element.

```html
<!-- This will automatically load "content.md" into the main element -->
<main data-untitledmarkdown-autofill="content.md"></main>
```

If you leave the attribute value empty, it will default to loading a file named `content.md` from the same directory.

```html
<!-- This also loads "content.md" -->
<main data-untitledmarkdown-autofill></main>
```

### Manual Usage

For more complex layouts where you might need multiple Markdown sources on a single page, you can still manually place the `<mark-down>` custom element.

```html
<main>
  <mark-down src="path/to/your/content.md"></mark-down>
</main>

<aside>
  <mark-down src="path/to/another/file.md"></mark-down>
</aside>
```

### Syntax Highlighting

For syntax highlighting in your code blocks, you can use a library like `highlight.js`.

1.  **Include `highlight.js`:**
    Add the `highlight.js` library and a stylesheet of your choice to your HTML.

    ```html
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    ```

2.  **Initialize `highlight.js`:**
    After the [untitled]markdown runtime, add a script to initialize `highlight.js`.

    ```html
    <script src="runtime.js"></script>
    <script>hljs.highlightAll();</script>
    ```

## <a name="customization"></a>Customization

You can easily style the rendered HTML using CSS. The rendered elements are standard HTML tags (`<h1>`, `<p>`, `<ul>`, etc.), so you can target them directly in your stylesheet.

```css
/* Example: Style all paragraphs rendered by [untitled]markdown */
mark-down p {
  line-height: 1.6;
  color: #333;
}

/* Example: Style blockquotes */
mark-down blockquote {
  border-left: 4px solid #ccc;
  padding-left: 1rem;
  color: #666;
  font-style: italic;
}
```

## <a name="troubleshooting"></a>Troubleshooting

### Markdown file not loading

*   **Check the path:** Ensure the `src` attribute in your `<mark-down>` element points to the correct path of your Markdown file.
*   **CORS Policy:** If you are loading the file from a different domain, you might encounter a CORS (Cross-Origin Resource Sharing) error. For security reasons, browsers restrict cross-origin HTTP requests. Make sure the server hosting the Markdown file has the correct CORS headers. For local development, running a local server can solve this issue.

### Content not rendering correctly

*   **Check your Markdown syntax:** Make sure your Markdown is well-formed.
*   **Script position:** Ensure the `runtime.js` script is included at the end of the `<body>` tag.

### Syntax highlighting not working

*   **Check `highlight.js`:** Make sure you have included the `highlight.js` library and a theme stylesheet.
*   **Initialization:** Ensure you are calling `hljs.highlightAll()` after the [untitled]markdown runtime script.

## <a name="contributing"></a>Contributing

Contributions are welcome! If you have a feature request, bug report, or want to contribute to the code, please feel free to open an issue or submit a pull request on the project's repository.

## <a name="license"></a>License

[untitled]markdown is open-source software licensed under the MIT License.
