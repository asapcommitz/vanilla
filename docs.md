# Documentation

[untitled]markdown is a lightweight, dependency-free Markdown renderer for the web.

## Introduction

The core philosophy of [untitled]markdown is to provide a "no-nonsense" experience. It parses Markdown directly in the browser using vanilla JavaScript, making it perfect for documentation sites, blogs, or simple content pages.

- **Zero Dependencies:** Pure Vanilla JS.
- **Lightweight:** Minimal footprint.
- **Semantic:** Outputs clean, valid HTML5.

## Installation

### CDN (Recommended)

Add the script to the end of your `&lt;body&gt;`.

```html
<script src="runtime.js" defer></script>
```

### Manual Setup

1.  Download `runtime.js` from the repository.
2.  Include it in your specific project directory.
3.  Link it via `<script src="runtime.js"></script>`.

## Usage

### Auto-fill

The simplest way is to use the `data-untitledmarkdown-autofill` attribute on a container.

```html
<!-- Loads "content.md" automatically -->
<main data-untitledmarkdown-autofill="content.md"></main>
```

### Custom Element

For more control, use the custom element directly.

```html
<mark-down src="posts/hello-world.md"></mark-down>
```

## Syntax Highlighting

We recommend `highlight.js` for code blocks.

```html
<!-- Include styles -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/default.min.css">

<!-- Include script -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

<!-- Initialize -->
<script>
  // Waif for content to load or use a callback in a real app
  hljs.highlightAll();
</script>
```

## Styling

The renderer outputs standard tags (`p`, `h1`, `code`, etc.), allowing full styling control via CSS.

```css
mark-down blockquote {
  border-left: 4px solid #000;
  padding-left: 1rem;
  font-style: italic;
}
```

## License

MIT License. &copy; 2026 [untitled]computer.
