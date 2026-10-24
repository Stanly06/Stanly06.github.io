const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
  for (const [k,f] of [["en","Stanly_Fernandez_CV_EN.pdf"],["es","Stanly_Fernandez_CV_ES.pdf"]]) {
    const p = await b.newPage(); await p.goto('file://' + __dirname + '/out/cv_' + k + '.html'); await p.waitForTimeout(300);
    await p.pdf({path: __dirname + '/out/' + f, format:'Letter', printBackground:true, preferCSSPageSize:true}); }
  await b.close(); })();
