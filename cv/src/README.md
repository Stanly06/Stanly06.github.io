# CV source

`build_cv.py` holds the CV content (EN/ES) and writes HTML; `print.js` prints it to Letter PDF with Chromium (Playwright), keeping clickable links.

```bash
python cv/src/build_cv.py cv/src/out && node cv/src/print.js && cp cv/src/out/*.pdf cv/
```
