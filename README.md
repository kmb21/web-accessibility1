
# Accessibility Remediation Toolkit

> **A GUI-based Python tool for automating HTML accessibility remediation using BeautifulSoup, Regex, and language detection.**

---

## Overview

**Accessibility Remediation Toolkit** is a desktop Python application that simplifies and accelerates the process of making HTML documents accessible. Designed with educators, developers, and accessibility specialists in mind, this tool helps automate the tedious task of identifying and correcting non-compliant HTML elements—making your web content screen-reader friendly and WCAG-compliant with minimal effort.

The intuitive GUI, powered by `tkinter`, allows users of all technical backgrounds to operate the tool seamlessly, while the backend logic handles complex remediation using `BeautifulSoup`, `regex`, and `langdetect`.

---

## 🚀 Key Features

* **Intelligent HTML Remediation**
  Automatically scans and replaces non-semantic HTML tags (e.g., `<b>`, `<i>`, `<font>`) with their accessible equivalents (e.g., `<strong>`, `<em>`).

* **User-Friendly Interface**
  Built using `tkinter`, the application offers an easy-to-use GUI requiring no command-line interaction.

* **Language Detection Support**
  Integrates `langdetect` to automatically insert appropriate `lang` attributes into HTML elements, improving screen reader performance.

* **Structure-Preserving Extraction**
  Extracts text, tables, and images while preserving semantic layout and metadata integrity.

* **Configurable and Modular Design**
  Easily modify rules or extend remediation logic by editing the helper modules.

* **Scalable & Batch-Capable**
  Process individual files or scale up to large directories of documents efficiently.

---

## Built With

| Category        | Tools / Libraries     |
| --------------- | --------------------- |
| GUI             | `tkinter`             |
| HTML Parsing    | `BeautifulSoup` (bs4) |
| Text Processing | `regex`, `langdetect` |
| Language        | Python 3.8+           |

---

## Folder Structure

```
.
├── dist/
│   └── GUI/
│       └── GUI.exe        # Executable launcher for the app
├── GUI.py                # Main application entry point (tkinter-based GUI)
├── accessibilitySoup.py # Orchestrates tag cleanup using helper methods
├── replaceHelper.py      # Tag replacement logic using BeautifulSoup, regex, and langdetect
├── templates/            # (Optional) Folder for custom remediation templates
└── README.md
```

---

## Installation

### Quick Start

1. **Download and unzip** the package.
2. Navigate into the `dist/GUI/` folder.
3. Run the `GUI` executable (or `GUI.py` if running from source).
4. Upload an HTML file and let the tool handle the remediation!

### Running from Source

Make sure you have Python 3.8+ and the following packages installed:

```bash
pip install beautifulsoup4 langdetect
```

Then, run:

```bash
python GUI.py
```

---

## Sample Output

| Original HTML                    | Remediated Output                      |
| -------------------------------- | -------------------------------------- |
| `<b>Important</b>`               | `<strong>Important</strong>`           |
| `<font color="red">Alert</font>` | `<span style="color:red">Alert</span>` |
| `lang` attribute missing         | Automatically added via langdetect     |

---

## Code Sample

```python
from bs4 import BeautifulSoup
from langdetect import detect

def add_lang_tag(html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all():
        if tag.name == 'p' and not tag.has_attr('lang'):
            tag['lang'] = detect(tag.text)
    return str(soup)
```

More resources:

* [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Tkinter Official Docs](https://docs.python.org/3/library/tk.html)

---

## Troubleshooting

* **Missing Dependencies**: Ensure you've installed `bs4` and `langdetect`.
* **Encoding Errors**: Use UTF-8 encoded files.
* **Permission Issues**: Try running the app with elevated privileges.

---

## App Preview

![Accessibility script](https://github.com/kmb21/web-accessibility1/assets/113995857/a26935cf-ade8-4005-8176-dd07cf259b89)

---

## Contributors

* **Maxwell Kumbong** – Developer & Accessibility Advocate
  *Contributions welcome! Fork the repo and submit a PR.*

---

## License

This project is licensed under the **MIT License**.


