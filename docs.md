# Documentation

vanilla.md is a lightweight, dependency-free Markdown renderer for the web.

## Introduction

The core philosophy of vanilla.md is to provide a "no-nonsense" experience. It parses Markdown directly in the browser using vanilla JavaScript, making it perfect for documentation sites, blogs, or simple content pages.

- **Zero Dependencies:** Pure Vanilla JS.
- **Lightweight:** Minimal footprint.
- **Semantic:** Outputs clean, valid HTML5.

## Installation

### CDN (Recommended)

Add the script to the end of your `&lt;body&gt;`.

```html
<script src="https://cdn.jsdelivr.net/gh/asapcommitz/vanilla@latest/runtime.js" defer></script>
```

### Manual Setup

1.  Download `runtime.js` from the repository.
2.  Include it in your specific project directory.
3. Link it via `<script src="runtime.js"></script>`.

## Usage

### Auto-fill

The simplest way is to use the `data-vanillamd-autofill` attribute on a container.

```html
<!-- Loads "content.md" automatically -->
<main data-vanillamd-autofill="content.md"></main>
```

### Custom Element

For more control, use the custom element directly.

```html
<mark-down src="posts/hello-world.md"></mark-down>
```

## Syntax Highlighting

Syntax highlighting (PrismJS) and the "Copy" button are **built-in**. No extra files required.

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

MIT License. &copy; 2026 vanilla.md

