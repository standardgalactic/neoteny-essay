# Neoteny Essay — LaTeX → PDF on GitHub Pages

This repository compiles LaTeX sources in `/src` with **LuaLaTeX + BibTeX**, then publishes the resulting PDFs and an auto-generated `index.html` to **GitHub Pages**.

Site URL (after first successful deploy):  
`https://standardgalactic.github.io/neoteny-essay/`

---

## How it works

- A GitHub Actions workflow installs TeX Live and runs `latexmk -lualatex -bibtex` for each `*.tex` in `/src`.
- Compiled PDFs are placed in `/build`.
- `scripts/generate_index.py` scans `/build` and creates `/build/index.html` with links to all PDFs.
- The `/build` directory is deployed to GitHub Pages.

---

## Local build

```bash
sudo apt-get install texlive-full latexmk python3
latexmk -lualatex -bibtex -interaction=nonstopmode -output-directory=build src/neoteny_extended.tex
python3 scripts/generate_index.py build
# Open build/index.html
```

---

## Add more papers

Drop additional `.tex` and `.bib` files into `/src`. As long as each `.tex` references its `.bib` via `\bibliography{...}`, the workflow will produce a matching `.pdf` and list it on the index.
