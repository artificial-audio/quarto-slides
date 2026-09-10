# Artificial Audio Quarto slides

A minimal 16:9 reveal.js template with FAU, LMS and Artificial Audio logos on the title slide, full-screen image dividers, single-column and two-column bullets, and a small page number. No recurring header, footer, toolbar or progress bar.

## Start a talk

Use GitHub's **Use this template** button to create your own repository, then clone it. Install [Quarto](https://quarto.org/docs/get-started/) and edit `slides.qmd`.

```sh
quarto preview slides.qmd
quarto render slides.qmd
```

The rendered deck is `_output/slides.html`. It embeds its assets for sharing as one HTML file. No Python, R, Node package installation or external fonts are required.

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
