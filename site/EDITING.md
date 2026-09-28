# Editing the site content

All the timeline content lives in **`site/src/entries/`** — one Markdown file
per step. To change the site you only edit these files; no code required.

## Add a new entry

1. Copy an existing file, e.g. `step-04.md` → `step-05.md`.
2. Edit the section at the top (between the `---` lines). This is the card:

   ```yaml
   ---
   step: 5                       # order number (higher = newer, shown first)
   date: "2025 · Step 05"        # small label on the card
   title: "My new milestone"     # card + journal heading
   tag: "some_folder/"           # little code-style tag on the card
   image: "timeline/step-5.svg"  # card image (see below)
   summary: "One-line description shown on the card."
   ---
   ```

3. Write the journal below the second `---` in plain Markdown.

That's it — the timeline, mini-rail, and journal update automatically.

## Writing the journal (Markdown)

- **Paragraphs**: just type text, leave a blank line between paragraphs.
- **Subheading**: `### My subheading`
- **Bold / italic**: `**bold**`, `*italic*`
- **Code block** (with an optional filename label above it):

  ```
  `path/to/file.py`

  ```python
  print("hello")
  ```
  ```

- **Image or plot** (with a caption): put an italic line right under it:

  ```
  ![alt text](/classical-autonomy-stack/timeline/my-photo.jpg)
  *This caption shows under the image.*
  ```

## Wrapping text around an image

To put an image beside text (text flows around it), use an HTML `<figure>` with
`class="wrap-right"` (or `wrap-left`) directly in the Markdown:

```html
<figure class="wrap-right">
  <img src="/classical-autonomy-stack/timeline/my-plot.svg" alt="...">
  <figcaption>Optional caption.</figcaption>
</figure>

Your paragraphs after this will wrap around the image on the right...
```

Use `class="wrap-left"` to float it to the left instead. To force following
content below the image (stop wrapping), add `<div class="clear"></div>`.

## Adding images / plots

1. Put the file in **`site/public/timeline/`** (jpg, png, svg…).
2. Reference it:
   - As the **card image**: set `image: "timeline/my-photo.jpg"` in the top section.
   - Inside the **journal**: use the full path
     `/classical-autonomy-stack/timeline/my-photo.jpg`.

## Preview locally

```bash
cd site
npm install     # first time only
npm run dev     # open the printed http://localhost:4321/... URL
```

## Publish

Commit and push to `main`; GitHub Actions builds and deploys automatically:

```bash
git add -A
git commit -m "Add step 5"
git push
```
