# Artificial Audio Quarto slides

A minimal 16:9 reveal.js template with FAU, LMS and Artificial Audio logos on the title slide, full-screen image dividers, single-column and two-column bullets, and a small page number. No recurring header, footer, toolbar or progress bar.

## Start a talk

Use GitHub's **Use this template** button to create your own repository, then clone it. Install [Quarto](https://quarto.org/docs/get-started/) and edit `slides.qmd`.

```sh
quarto preview slides.qmd
quarto render slides.qmd
```

The rendered deck is `_output/slides.html`. It embeds its assets for sharing as one HTML file. No Python, R, Node package installation or external fonts are required to render the supplied deck. YouTube playback requires internet access; math may also need internet for MathJax. Audio and video do not play in PDF exports.

## Layouts

Duplicate the slide blocks in `slides.qmd`. Level-two headings (`##`) start slides. Level-three headings (`###`) are subheadings. The title slide reads `title`, `subtitle`, `author` (a string or list of strings), `institute`, and `date` from the YAML at the top.

- **Image divider:** keep `.divider` and set `background-image` to your image. `cover` fills the browser viewport and may crop the edges. Adjust `background-position` if needed. Change `background-opacity` for readability.
- **Single column:** ordinary Markdown bullets, with one optional nested level.
- **Two columns:** the `.columns` and `.column` blocks provide two equal columns with a clear gap.

Colors, typography and content padding live in `theme/aa.scss`. The canvas has zero outer margin; the text retains a small inset for readability. Backgrounds fill any viewport, while the 16:9 content canvas scales proportionally.

## Present and export

Use arrow keys or Space to advance, **F** for browser full screen, **Esc** for the overview and **S** for speaker notes. For PDF, press **E** to enter print view and print with landscape orientation, no margins, and background graphics enabled. See [Quarto presenting slides](https://quarto.org/docs/presentations/revealjs/presenting.html).

## Assets

The FAU, LMS and AA logos are unchanged copies from `artificial-audio/pyfdn-tutorial-2026`, `assets/{fau_logo.png,lms_logo.svg,aa_logo.png}`. The example divider is the room rendering from `artificial-audio/artificial-audio.github.io`, `content/portfolio/RES/featured.jpg`. Replace it with an image appropriate to your talk. Institutional marks and supplied images retain their existing rights.

## Content demos

`slides.qmd` includes math and equation references, Python listings with stepped line highlighting, a Python-generated SVG figure, an executable-cell recipe, YouTube, local audio, captioned images, tables, incremental bullets, links, and speaker notes. Copy the relevant slide into your talk.

The figure and two-second 440 Hz tone are generated examples, included in `assets/`. To regenerate them with Python and Matplotlib:

```sh
python -m pip install matplotlib
python demos/make_assets.py
quarto render slides.qmd
```

Plain `python` / `.python` fences only display code. To execute code during rendering, remove `engine: markdown` from the slide YAML, use a `{python}` cell as shown in the deck, and install `jupyter` alongside your computation dependencies in the Python environment Quarto uses. The supplied deck does not execute Python during rendering.

See the [Quarto video guide](https://quarto.org/docs/authoring/videos.html) for the video shortcode and the [Reveal.js guide](https://quarto.org/docs/presentations/revealjs/) for line highlighting and incremental content. Speaker notes are hidden on the slides, but anyone with the HTML file can inspect them.

## AA color palette

`theme/aa-palette.scss` is the reusable palette, sampled from the AA logo. `theme/aa.scss` assigns those colors to presentation elements. Edit the palette to update the theme; each Sass token also has a CSS variable with the same name (`$aa-navy` → `--aa-navy`).

| Token | Hex | Use |
|:------|:----|:----|
| `aa-navy` | `#083959` | Body text, headings, dark backgrounds |
| `aa-cream` | `#FCF5ED` | Slide background, text on navy |
| `aa-teal` | `#2D9F84` | Bullet markers and chart accents |
| `aa-orange` | `#F57F33` | Highlights and chart accents |
| `aa-coral` | `#DF514D` | Secondary chart accents |
| `aa-blue` | `#22669F` | Chart series and emphasis |
| `aa-purple` | `#655485` | Additional chart series |

`aa-link` and `aa-muted` are darker derived colors for readable links, subheadings, and secondary text. Use the bright accents for graphics rather than small text on cream; pair chart colors with labels or line styles.

Reuse the presentation theme in another Quarto deck by copying both SCSS files and configuring:

```yaml
format:
  revealjs:
    theme: [default, theme/aa.scss, theme/aa-palette.scss]
```

For custom HTML/CSS, use `color: var(--aa-blue)` or `background: var(--aa-cream)`. To reuse only the palette in a different Quarto theme, list `theme/aa-palette.scss` after your own SCSS (Quarto evaluates theme defaults in reverse order). For Python figures, use the hex values above (for example, `ax.plot(x, y, color="#2D9F84")`) and save with `transparent=True` to blend into the slide background. Explicit Quarto `background-color` attributes take hex values, such as `#083959` for a navy divider.
