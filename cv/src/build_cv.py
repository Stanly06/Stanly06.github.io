"""Build Stanly Fernández CV (EN/ES) as HTML, printed to PDF with Chromium: python build_cv.py <out_dir>"""
import sys, pathlib, html

PLATFORM = "https://stanly06.github.io/rd-intelligence/"
CONTACT = [("sffernandez06@gmail.com", "mailto:sffernandez06@gmail.com"),
           ("linkedin.com/in/stanly-fernandez-data", "https://www.linkedin.com/in/stanly-fernandez-data/"),
           ("github.com/Stanly06", "https://github.com/Stanly06"),
           ("stanly06.github.io", "https://stanly06.github.io/")]

CV = {
"en": dict(
  file="Stanly_Fernandez_CV_EN.pdf", lang="en",
  title="Data Analyst | Business Intelligence | Data Engineering (Databricks)",
  location="Santiago de los Caballeros, Dominican Republic",
  h=dict(summary="Professional Summary", skills="Technical Skills", exp="Professional Experience", proj="Projects", edu="Education", cert="Certifications", share="Knowledge Sharing"),
  summary="Data Analyst and Industrial Engineer with 7+ years of experience in manufacturing operations, turning production and quality data into KPIs, reports and dashboards that support management decisions. Skilled in Power BI (DAX, Power Query), SQL and Python, with hands-on data engineering experience building automated, incremental pipelines in Databricks with PySpark, Auto Loader, Delta Lake and the Medallion Architecture. Google Data Analytics and Google Business Intelligence certified, with an MBA and a Master's in Big Data & Business Intelligence.",
  skills=[("Business Intelligence","Power BI, DAX, Power Query, Data Modeling, KPI Design, Dashboard Development, Data Visualization, Advanced Excel"),
          ("Data Engineering","Databricks, PySpark, Spark SQL, Delta Lake (MERGE), Auto Loader, Medallion Architecture (Bronze, Silver, Gold), Unity Catalog, ETL Pipelines, Lakeflow Jobs (Databricks Jobs), REST API Ingestion, Data Profiling, Data Quality Validation"),
          ("SQL & Programming","SQL (PostgreSQL), JOINs, CTEs, Window Functions, Subqueries, Python (pandas, NumPy, Matplotlib), JavaScript (Chart.js), Git, GitHub"),
          ("Cloud","Azure Databricks, Azure Data Lake, Microsoft Fabric (in training)"),
          ("Operations & Quality","Six Sigma, Kaizen, 5S, Quality Control (DPU, CPK), Root Cause Analysis, Production Planning, SAP"),
          ("Languages","Spanish (Native), English (Professional Working Proficiency)")],
  jobs=[("Quality Control & Production Assistant","CdF Domitab SA","Santiago de los Caballeros, Dominican Republic","Feb 2023 – Present",[
          "Designed and deployed Power BI dashboards using DAX measures and Power Query transformations, cutting manual reporting time by 30% and giving production and finance teams real-time visibility into KPIs.",
          "Built SQL-based data pipelines consolidating attendance, efficiency and quality records across departments, reducing report preparation time from several hours to under 15 minutes per cycle.",
          "Conducted end-to-end data analysis, including data cleaning, data modeling and aggregation, to identify production bottlenecks, enabling process adjustments that improved throughput by approximately 15%.",
          "Collaborated with IT to automate data collection workflows across 4 production modules, replacing error-prone manual inputs and improving data reliability by 20%.",
          "Created daily production reports by area and module for the production manager and monitored attendance, production effectiveness and efficiency indicators.",
          "Conducted quality audits on tobacco varieties to evaluate quality and yields, and delivered reports and audit findings to management, finance and senior stakeholders.",
          "Prepared and analyzed quality samples for external clients and monitored classification and packaging processes against quality standards."]),
        ("Production Team Leader","La Aurora Cigars","Santiago de los Caballeros, Dominican Republic","Nov 2021 – Feb 2023",[
          "Analyzed production scheduling data to optimize line balancing, identifying supply gaps 48 hours in advance and reducing material shortages by approximately 25%.",
          "Led and coordinated teams in the primary process area (classification, fermentation, stemming and selection), managing the weekly production schedule and material supply to the cigar-making area.",
          "Applied Six Sigma, Kaizen and 5S, supported by data analysis, to standardize quality checkpoints and reduce process waste.",
          "Tracked and reported weekly production KPIs to operations management, enabling data-driven staffing and throughput decisions that improved weekly output targets by 10–15%."]),
        ("Quality Auditor","La Aurora Cigars","Guazumal, Tamboril, Dominican Republic","May 2018 – Nov 2021",[
          "Collected and analyzed quality samples across production stages, calculating DPU and CPK metrics to monitor process performance and detect early defect trends.",
          "Developed structured quality reports with Six Sigma tools, identifying root causes of recurring defects and contributing to process improvements that reduced defect rates by over 18%.",
          "Maintained quality databases and enforced data integrity across inspection records, enabling consistent trend analysis and audit readiness."])],
  projects=[("RD Economic & Financial Intelligence Platform","Databricks, PySpark, Auto Loader, Delta Lake, Unity Catalog, Lakeflow Jobs, Power BI","2026",
          ("Live platform: stanly06.github.io/rd-intelligence", PLATFORM),[
          "Built an end-to-end Databricks lakehouse that integrates 6 official Dominican sources (Central Bank exchange rate since 1991, CPI and family basket, MICM fuel prices, Pro Consumidor, MEM electricity and Ministry of Agriculture market prices) into Bronze, Silver and Gold Delta tables.",
          "Automated file acquisition from the national open-data portal API (datos.gob.do) and institutional sites into an append-only archive, with incremental, exactly-once ingestion using Auto Loader and SHA-256 file lineage.",
          "Enforced data-quality rules with rejected-record logging and reconciliation checks; Gold KPIs match officially published values (e.g., 5,550 of 5,550 monthly CPI changes).",
          "Orchestrated 26 tasks in 6 parallel chains with a weekly Lakeflow Job and published the results in a bilingual (ES/EN) web platform and a Power BI report."]),
        ("MLB Performance Intelligence Platform","Databricks, PySpark, Delta Lake, Lakeflow Jobs, scikit-learn","2026",
          ("Live platform: stanly06.github.io/mlb-intelligence","https://stanly06.github.io/mlb-intelligence/?lang=en"),[
          "Built a Databricks lakehouse on the MLB Stats API (7,400+ games, 2024–2026) with Auto Loader and incremental Delta MERGE through Bronze, Silver and Gold: team, player and country KPIs.",
          "Wrote 14 data-quality checks; records and runs reconcile 90 of 90 with official MLB standings.",
          "Trained a win-probability model (56.0% accuracy vs 52.9% baseline on an unseen season) and orchestrated a daily 13-task Lakeflow Job that refreshes a bilingual website."]),
        ("SQL Analytics: Music Store and Netflix Catalog","PostgreSQL","",("github.com/Stanly06","https://github.com/Stanly06"),[
          "Answered 11 business questions on an 11-table music store database using JOINs, subqueries, CTEs, ROW_NUMBER() and recursive CTEs.",
          "Answered 15 business questions on 8,800+ Netflix titles using CTEs, RANK() and string functions (STRING_TO_ARRAY, UNNEST, SPLIT_PART)."]),
        ("Power BI Dashboards: Video Game Sales and Infant Mortality","Power BI, DAX, Power Query","",("github.com/Stanly06","https://github.com/Stanly06"),[
          "Built interactive reports with KPI cards, stacked charts, maps, scatter plots and slicers, using Power Query segmentation and DAX measures to compare regions, platforms and countries."])],
  edu=["MBA + Master's in Big Data & Business Intelligence | ENEB, European Business School of Barcelona (Universidad Isabel I) | Jun 2023 – Jun 2026",
       "B.S. Industrial Engineering | Universidad Autónoma de Santo Domingo (UASD) | 2014 – 2021"],
  certs=["Google Business Intelligence Professional Certificate – Google / Coursera","Google Data Analytics Professional Certificate – Google / Coursera",
         "Data Science with Python","Professional Course in Forecasting Methods: Calculations & Interpretation","EF SET English Certificate (B1)",
         "In progress: Microsoft PL-300 Power BI Data Analyst; Databricks Certified Data Engineer Associate; Microsoft Fabric Data Engineering"],
  share=("Author of a Databricks Data Engineer Associate study guide, a 100-question Power BI interview guide and project walkthrough videos on YouTube (", "youtube.com/@stanlyfernandez2887", ")."),
),
"es": dict(
  file="Stanly_Fernandez_CV_ES.pdf", lang="es",
  title="Analista de Datos | Business Intelligence | Ingeniería de Datos (Databricks)",
  location="Santiago de los Caballeros, República Dominicana",
  h=dict(summary="Perfil Profesional", skills="Habilidades Técnicas", exp="Experiencia Profesional", proj="Proyectos", edu="Educación", cert="Certificaciones", share="Divulgación"),
  summary="Analista de Datos e Ingeniero Industrial con más de 7 años de experiencia en operaciones de manufactura, convirtiendo datos de producción y calidad en KPIs, reportes y dashboards que apoyan las decisiones de la gerencia. Dominio de Power BI (DAX, Power Query), SQL y Python, con experiencia práctica en ingeniería de datos construyendo pipelines automatizados e incrementales en Databricks con PySpark, Auto Loader, Delta Lake y Arquitectura Medallion. Certificado en Google Data Analytics y Google Business Intelligence; con MBA y Máster en Big Data y Business Intelligence.",
  skills=[("Business Intelligence","Power BI, DAX, Power Query, Modelado de Datos, Diseño de KPIs, Desarrollo de Dashboards, Visualización de Datos, Excel Avanzado"),
          ("Ingeniería de Datos","Databricks, PySpark, Spark SQL, Delta Lake (MERGE), Auto Loader, Arquitectura Medallion (Bronze, Silver, Gold), Unity Catalog, Pipelines ETL, Lakeflow Jobs (Databricks Jobs), Ingesta desde API REST, Perfilado de Datos, Validación de Calidad de Datos"),
          ("SQL y Programación","SQL (PostgreSQL), JOINs, CTEs, Funciones de Ventana, Subconsultas, Python (pandas, NumPy, Matplotlib), JavaScript (Chart.js), Git, GitHub"),
          ("Nube","Azure Databricks, Azure Data Lake, Microsoft Fabric (en formación)"),
          ("Operaciones y Calidad","Six Sigma, Kaizen, 5S, Control de Calidad (DPU, CPK), Análisis de Causa Raíz, Planificación de la Producción, SAP"),
          ("Idiomas","Español (nativo), Inglés (nivel profesional)")],
  jobs=[("Asistente de Control de Calidad y Producción","CdF Domitab SA","Santiago de los Caballeros, República Dominicana","Feb 2023 – Actualidad",[
          "Diseñé e implementé dashboards en Power BI con medidas DAX y transformaciones en Power Query, reduciendo 30% el tiempo de reportes manuales y dando a producción y finanzas visibilidad de KPIs en tiempo real.",
          "Construí pipelines de datos en SQL que consolidan registros de asistencia, eficiencia y calidad entre departamentos, bajando la preparación de reportes de varias horas a menos de 15 minutos por ciclo.",
          "Realicé análisis de datos de punta a punta, con limpieza, modelado y agregación, para identificar cuellos de botella, lo que permitió ajustes de proceso que mejoraron el rendimiento cerca de 15%.",
          "Colaboré con TI para automatizar la captura de datos en 4 módulos de producción, reemplazando registros manuales propensos a errores y mejorando 20% la confiabilidad de los datos.",
          "Elaboré reportes diarios de producción por área y módulo para el gerente de producción y monitoreé los indicadores de asistencia, efectividad y eficiencia.",
          "Realicé auditorías de calidad a variedades de tabaco para evaluar calidad y rendimientos, y presenté reportes y hallazgos a gerencia, finanzas y alta dirección.",
          "Preparé y analicé muestras de calidad para clientes externos y supervisé los procesos de clasificación y empaque según los estándares de calidad."]),
        ("Líder de Producción","La Aurora Cigars","Santiago de los Caballeros, República Dominicana","Nov 2021 – Feb 2023",[
          "Analicé datos de programación de la producción para optimizar el balanceo de líneas, detectando faltantes con 48 horas de anticipación y reduciendo cerca de 25% la falta de materiales.",
          "Lideré y coordiné equipos en el área de proceso primario (clasificación, fermentación, despalillado y selección), gestionando el programa semanal de producción y el abastecimiento al área de elaboración de cigarros.",
          "Apliqué Six Sigma, Kaizen y 5S, apoyado en análisis de datos, para estandarizar puntos de control de calidad y reducir desperdicios.",
          "Reporté KPIs semanales de producción a la gerencia de operaciones, apoyando decisiones de personal y rendimiento que subieron 10–15% las metas semanales de producción."]),
        ("Auditor de Calidad","La Aurora Cigars","Guazumal, Tamboril, República Dominicana","May 2018 – Nov 2021",[
          "Recolecté y analicé muestras de calidad en las etapas de producción, calculando DPU y CPK para medir el desempeño del proceso y detectar tendencias de defectos a tiempo.",
          "Elaboré reportes de calidad con herramientas Six Sigma, identificando causas raíz de defectos recurrentes y contribuyendo a mejoras que redujeron más de 18% la tasa de defectos.",
          "Mantuve las bases de datos de calidad y aseguré la integridad de los registros de inspección, permitiendo análisis de tendencias y preparación para auditorías."])],
  projects=[("RD Economic & Financial Intelligence Platform","Databricks, PySpark, Auto Loader, Delta Lake, Unity Catalog, Lakeflow Jobs, Power BI","2026",
          ("Plataforma en vivo: stanly06.github.io/rd-intelligence", PLATFORM + "?lang=es"),[
          "Construí un lakehouse de punta a punta en Databricks que integra 6 fuentes oficiales dominicanas (tasa de cambio del Banco Central desde 1991, IPC y canasta familiar, combustibles del MICM, Pro Consumidor, electricidad del MEM y precios de mercado del Ministerio de Agricultura) en tablas Delta Bronze, Silver y Gold.",
          "Automaticé la descarga de archivos desde la API del portal de datos abiertos (datos.gob.do) y los sitios de las instituciones hacia un archivo histórico que no se sobrescribe, con ingesta incremental exactamente una vez mediante Auto Loader y trazabilidad SHA-256 por archivo.",
          "Apliqué reglas de calidad de datos con registro de rechazados y conciliaciones; los KPIs de Gold coinciden con los valores oficiales publicados (ej. 5,550 de 5,550 variaciones mensuales del IPC).",
          "Orquesté 26 tareas en 6 cadenas paralelas con un Job semanal de Lakeflow y publiqué los resultados en una plataforma web bilingüe (ES/EN) y un reporte de Power BI."]),
        ("MLB Performance Intelligence Platform","Databricks, PySpark, Delta Lake, Lakeflow Jobs, scikit-learn","2026",
          ("Plataforma en vivo: stanly06.github.io/mlb-intelligence","https://stanly06.github.io/mlb-intelligence/?lang=es"),[
          "Construí un lakehouse en Databricks sobre la API de MLB (7,400+ juegos, 2024–2026) con Auto Loader y MERGE incremental en Bronze, Silver y Gold: KPIs de equipos, jugadores y países.",
          "Escribí 14 controles de calidad; récord y carreras coinciden 90 de 90 con las posiciones oficiales de MLB.",
          "Entrené un modelo de victoria (56.0% de acierto vs 52.9% base en una temporada no vista) y orquesté un Job diario de 13 tareas que actualiza una web bilingüe."]),
        ("Análisis SQL: Tienda de Música y Catálogo de Netflix","PostgreSQL","",("github.com/Stanly06","https://github.com/Stanly06"),[
          "Respondí 11 preguntas de negocio sobre una base de datos de 11 tablas usando JOINs, subconsultas, CTEs, ROW_NUMBER() y CTEs recursivos.",
          "Respondí 15 preguntas de negocio sobre más de 8,800 títulos de Netflix usando CTEs, RANK() y funciones de texto (STRING_TO_ARRAY, UNNEST, SPLIT_PART)."]),
        ("Dashboards en Power BI: Ventas de Videojuegos y Mortalidad Infantil","Power BI, DAX, Power Query","",("github.com/Stanly06","https://github.com/Stanly06"),[
          "Construí reportes interactivos con tarjetas de KPI, gráficos apilados, mapas, dispersión y segmentadores, usando segmentación en Power Query y medidas DAX para comparar regiones, plataformas y países."])],
  edu=["MBA + Máster en Big Data y Business Intelligence | ENEB, Escuela de Negocios Europea de Barcelona (Universidad Isabel I) | Jun 2023 – Jun 2026",
       "Ingeniería Industrial | Universidad Autónoma de Santo Domingo (UASD) | 2014 – 2021"],
  certs=["Google Business Intelligence Professional Certificate – Google / Coursera","Google Data Analytics Professional Certificate – Google / Coursera",
         "Data Science with Python","Curso Profesional en Métodos de Pronósticos: Cálculos e Interpretaciones","EF SET English Certificate (B1)",
         "En preparación: Microsoft PL-300 Power BI Data Analyst; Databricks Certified Data Engineer Associate; Microsoft Fabric Data Engineering"],
  share=("Autor de una guía de estudio para Databricks Data Engineer Associate, una guía de 100 preguntas de entrevista de Power BI y videos explicativos de proyectos en YouTube (", "youtube.com/@stanlyfernandez2887", ")."),
)}

CSS = """
@page{size:Letter;margin:0.4in 0.55in 0.4in 0.55in}
*{box-sizing:border-box}
body{font-family:Carlito,Calibri,"Liberation Sans",sans-serif;font-size:10pt;line-height:1.2;color:#1a1a1a;margin:0}
a{color:inherit;text-decoration:none}
a.u{color:#1F3864;text-decoration:underline;text-decoration-color:#9fb1d0}
header{text-align:center;margin-bottom:4pt}
h1{font-size:19pt;color:#1F3864;margin:0;letter-spacing:.02em}
.title{font-weight:700;font-size:11pt;margin:1pt 0}
.contact{font-size:9pt;color:#333}
h2{font-size:10.4pt;color:#1F3864;text-transform:uppercase;margin:6pt 0 2.5pt;padding-bottom:1.5pt;border-bottom:1.3pt solid #1F3864;letter-spacing:.02em}
p{margin:0}
ul{margin:1pt 0 0;padding-left:13pt}
li{margin:0 0 .6pt}
.role{font-weight:700;margin-top:3pt}
.meta{font-style:italic;color:#555;font-size:9.6pt}
.link{font-size:9.6pt}
.keep{break-inside:avoid}
h2{break-after:avoid}
"""

def a(text, href, cls="u"):
    return f'<a class="{cls}" href="{html.escape(href)}">{html.escape(text)}</a>'

def page(c):
    e = html.escape
    contact = " | ".join([e(c["location"])] + [a(t, h) for t, h in CONTACT])
    out = [f'<!doctype html><html lang="{c["lang"]}"><head><meta charset="utf-8"><title>Stanly Fernández — CV</title><style>{CSS}</style></head><body>',
           f'<header><h1>STANLY FERNÁNDEZ</h1><div class="title">{e(c["title"])}</div><div class="contact">{contact}</div></header>',
           f'<h2>{e(c["h"]["summary"])}</h2><p>{e(c["summary"])}</p>',
           f'<h2>{e(c["h"]["skills"])}</h2><ul>' + "".join(f"<li><b>{e(k)}:</b> {e(v)}</li>" for k, v in c["skills"]) + "</ul>",
           f'<h2>{e(c["h"]["exp"])}</h2>']
    for role, org, loc, dates, bullets in c["jobs"]:
        out.append(f'<div class="keep"><div class="role">{e(role)} | {e(org)}</div><div class="meta">{e(loc)} | {e(dates)}</div><ul>' + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul></div>")
    out.append(f'<h2>{e(c["h"]["proj"])}</h2>')
    for name, stack, year, (lt, lh), bullets in c["projects"]:
        head = f'{e(name)} | {e(stack)}' + (f' | {e(year)}' if year else "")
        out.append(f'<div class="keep"><div class="role">{head}</div><div class="link">{a(lt, lh)}</div><ul>' + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul></div>")
    out.append(f'<h2>{e(c["h"]["edu"])}</h2><ul>' + "".join(f"<li>{e(x)}</li>" for x in c["edu"]) + "</ul>")
    out.append(f'<h2>{e(c["h"]["cert"])}</h2><ul>' + "".join(f"<li>{e(x)}</li>" for x in c["certs"]) + "</ul>")
    s1, link, s2 = c["share"]
    out.append(f'<div class="keep"><h2>{e(c["h"]["share"])}</h2><p>{e(s1)}{a(link, "https://www.youtube.com/@stanlyfernandez2887")}{e(s2)}</p></div></body></html>')
    return "".join(out)

if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    for k, c in CV.items():
        (out / f"cv_{k}.html").write_text(page(c), encoding="utf-8")
        print(out / f"cv_{k}.html")
