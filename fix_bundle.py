
import os

with open('prism-plugins.css', 'r') as f:
    css_content = f.read()

with open('prism-syntax-highlighting.js', 'r') as f:
    prism_js_content = f.read()

os.system("git checkout 5ac73b3 -- runtime.js")

with open('runtime.js', 'r') as f:
    runtime_js_content = f.read()

css_content_escaped = css_content.replace('\\', '\\\\').replace('`', '\\`')
css_content_escaped = css_content_escaped.replace('${', '\\${')

bundled_content = f"""/**
 * [untitled]markdown runtime
 * Bundled with PrismJS and default plugins
 */

(function() {{
// 1. Inject CSS
const style = document.createElement('style');
style.textContent = `{css_content_escaped}`;
document.head.appendChild(style);

// 2. PrismJS Logic
{prism_js_content}

// 3. Runtime Logic
{runtime_js_content}
}})();
"""

with open('runtime.js', 'w') as f:
    f.write(bundled_content)

print("Bundling complete.")
