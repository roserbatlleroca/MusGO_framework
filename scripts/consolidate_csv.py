# ! Note that this code has been adapted from previous work by Andreas Liesenfeld, Alianda Lopez, and Mark Dingemanse. 
# For more details, check out: http://opening-up-chatgpt.github.io  

import yaml
import glob
import html
import os
import re
import unicodedata
import pandas as pd
from bs4 import BeautifulSoup
import datetime

def split_multi(value):
    """Split a comma-separated multi-value field (e.g. project.apptype or
    project.architecture) into a list of trimmed, non-empty values.
    Models with a single value just return a one-item list."""
    if not value:
        return []
    return [v.strip() for v in str(value).split(",") if v.strip()]

def slugify(name):
    """Turn a project name into a URL-friendly slug for its model page,
    e.g. "Stable Audio Open" -> "stable-audio-open", "YuE (乐)" -> "yue"."""
    # Drop accents/non-latin characters (e.g. "乐"), keep the ascii base
    normalized = unicodedata.normalize("NFKD", str(name))
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    slug = ascii_only.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug or "model"

def create_dataframe(files):
    # read the input YAML file, transpose the rows and columns and save to dataframe
    df = pd.DataFrame()
    source_file = []
    for fname in files:
        with open(fname, 'r', encoding='utf-8') as file:
            file_df = pd.json_normalize(yaml.safe_load(file))
        # append transposed row to df
        source_file.append(fname[1:])
        df = pd.concat([df, file_df], axis=0)
    df["source.file"] = source_file
    # get rid of rows without a project_name
    df = df.replace({None: ""})
    df = df[df["project.name"] != ""]
    df.set_index("project.name", inplace = True)
    return df

# get opennes score for each project based on the classes of the essential categories
def calculate_openness(df):
    openness_weights = {
        "sourcecode": 2, 
        "trainingdata": 2, 
        "modelweights": 2, 
        "codedoc": 1, 
        "trainprocedure": 1, 
        "evalprocedure": 1, 
        "paper": 1,
        "license": 1, 
    }
    class_values = {
        "open": 1,
        "partial": 0.5,
        "closed": 0,
    }
    openness = []
    projects = df.index.tolist()
    for p in projects:
        cumul_openness = 0
        for v, w in openness_weights.items():
            vclass = df.loc[p, v + ".class"]
            vvalue = class_values[vclass] if vclass in class_values else 0
            cumul_openness += w * vvalue
        cumul_openness = round(cumul_openness/11*100,0) # Normalising openness level to 100 points
        openness.append(int(cumul_openness))
    # add the openness variable to the DataFrame
    df["openness"] = openness
    return df


def write_html(df):
    html_table = '<table>\n'
    html_table += '<thead>\n'
    html_table += '<tr class="main-header"><th>Project</th><th colspan="8">Essential</th><th colspan="5">Desirable</th>\n'
    html_table += '<tr class="second-header"><th></th><th>Source code</th>' \
              '<th>Training data</th>' \
              '<th>Model weights</th>' \
              '<th>Code<br>documentation</th>' \
              '<th>Training<br>procedure</th>' \
              '<th>Evaluation<br>procedure</th>' \
              '<th>Research paper</th>' \
              '<th>License</th>' \
              '<th>Model card</th>' \
              '<th>Datasheet</th>' \
              '<th>Package</th>' \
              '<th>UX<br>application</th>' \
              '<th>Supplementary<br>material page</th>\n'
    html_table += '</thead>\n'
    html_table += '<tbody>\n'
    # loop through projects
    projects = df.index.tolist()
    for p in projects:
        cells_e = ["sourcecode", "trainingdata", "modelweights", "codedoc", "trainprocedure", "evalprocedure", "paper", "license"] # Essential categories
        cells_n = ["modelcard", "datasheet", "package", "ux", "suppage"] # Desirable categories
        # first row
        source_link = "https://github.com/roserbatlleroca/MusGO_framework/blob/main" + df.loc[p, "source.file"]
        source_file = source_link.split("/")[-1]
        model_page_link = "models/{}/".format(slugify(p))
        # Attributes that power the leaderboard's sort/filter controls on the front end
        row_year = df.loc[p, "project.year"] if "project.year" in df.columns and pd.notna(df.loc[p, "project.year"]) else ""
        row_apptype = df.loc[p, "project.apptype"] if "project.apptype" in df.columns and pd.notna(df.loc[p, "project.apptype"]) else ""
        row_architecture = df.loc[p, "project.architecture"] if "project.architecture" in df.columns and pd.notna(df.loc[p, "project.architecture"]) else ""
        row_attrs = ""
        if row_year != "":
            row_attrs += ' data-year="{}"'.format(html.escape(str(row_year)))
        # Multi-value tags (e.g. "text-to-music, audio-to-audio") are normalised
        # into a comma-separated attribute with no extra spaces, so the front-end
        # JS can split on "," and treat each tag independently for filtering.
        apptype_list = split_multi(row_apptype)
        if apptype_list:
            row_attrs += ' data-apptype="{}"'.format(html.escape(",".join(apptype_list)))
        architecture_list = split_multi(row_architecture)
        if architecture_list:
            row_attrs += ' data-architecture="{}"'.format(html.escape(",".join(architecture_list)))
        # Clicking the model name now opens its dedicated model page (same tab);
        # the YAML source link now lives on that page itself.
        r1_html = '<tr class="row-a"{}><td class="name-cell"><a href="{}" title="View {} model page">{}</a></td>'.format(row_attrs, model_page_link, p, p)
        for c in cells_e:
            cl = df.loc[p, c + ".class"]
            link = df.loc[p, c + ".link"]
            notes = df.loc[p, c + ".notes"]
            symbol = "&#10004;&#xFE0E" if cl == "open" else "~" if cl == "partial" else "&#10008;" if cl == "closed" else "?"
            r1_html += '<td class="{} data-cell"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(cl, link, notes, symbol)
        for c in cells_n:
            cl = df.loc[p, c + ".class"]
            link = df.loc[p, c + ".link"]
            notes = df.loc[p, c + ".notes"]
            # Use a yellow star if the category exists; otherwise, leave it blank.
            symbol = "&#11088;" if cl == "star" else "&#8709;"
            r1_html += '<td class="{} data-cell"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(cl, link, notes, symbol)

        r1_html += "</tr>\n"
        html_table += r1_html
        # second row - now includes year before organization
        year = df.loc[p, "project.year"] if "project.year" in df.columns and pd.notna(df.loc[p, "project.year"]) else ""
        org_name = df.loc[p, "org.name"]
        # Combine year and organization with space, year gets fixed width
        year_org_display = f'<span style="display:inline-block;min-width:36px">{year}</span>{org_name}' if year else org_name
        
        r2_html = '<tr class="row-b"><td class="org"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(df.loc[p, "project.link"], df.loc[p, "project.notes"], year_org_display)
        r2_html += '<td colspan="7"></td><td class="source-link"><a href="{}" title="{}" target="_blank"></a></td></tr>\n'.format(df.loc[p, "org.link"], df.loc[p, "org.name"])
        html_table += r2_html
    # closing tags
    html_table += '</tbody>\n'
    html_table += '</table>\n'
    return html_table

def write_simplified_html(df):
    html_table = '<table>\n'
    html_table += '<thead>\n'
    html_table += '<tr class="main-header"><th>Project</th><th colspan="8">Essential</th><th colspan="5">Desirable</th>\n'
    html_table += '<tr class="second-header"><th></th><th>Source code</th>' \
              '<th>Training data</th>' \
              '<th>Model weights</th>' \
              '<th>Code<br>documentation</th>' \
              '<th>Training<br>procedure</th>' \
              '<th>Evaluation<br>procedure</th>' \
              '<th>Research paper</th>' \
              '<th>License</th>' \
              '<th>Model card</th>' \
              '<th>Datasheet</th>' \
              '<th>Package</th>' \
              '<th>UX<br>application</th>' \
              '<th>Supplementary<br>material page</th>\n'
    html_table += '</thead>\n'
    html_table += '<tbody>\n'
    # loop through projects
    projects = df.index.tolist()
    for p in projects:
        # add data by looping through each row and converting it 2 rows for the html table.
        # also add classes to the <td> elements for colour coding and links to source of the class judgement: https://github.com/liesenf/awesome-open-chatgpt/issues/12
        cells_e = ["sourcecode", "trainingdata", "modelweights", "codedoc", "trainprocedure", "evalprocedure", "paper", "license"] # Essential categories
        cells_n = ["modelcard", "datasheet", "package", "ux", "suppage"] # Desirable categories
        
        source_link = "https://github.com/roserbatlleroca/MusGO_framework/blob/main" + df.loc[p, "source.file"]
        source_file = source_link.split("/")[-1]
        row_year = df.loc[p, "project.year"] if "project.year" in df.columns and pd.notna(df.loc[p, "project.year"]) else ""
        row_apptype = df.loc[p, "project.apptype"] if "project.apptype" in df.columns and pd.notna(df.loc[p, "project.apptype"]) else ""
        row_architecture = df.loc[p, "project.architecture"] if "project.architecture" in df.columns and pd.notna(df.loc[p, "project.architecture"]) else ""
        row_attrs = ""
        if row_year != "":
            row_attrs += ' data-year="{}"'.format(html.escape(str(row_year)))
        # Multi-value tags (e.g. "text-to-music, audio-to-audio") are normalised
        # into a comma-separated attribute with no extra spaces, so the front-end
        # JS can split on "," and treat each tag independently for filtering.
        apptype_list = split_multi(row_apptype)
        if apptype_list:
            row_attrs += ' data-apptype="{}"'.format(html.escape(",".join(apptype_list)))
        architecture_list = split_multi(row_architecture)
        if architecture_list:
            row_attrs += ' data-architecture="{}"'.format(html.escape(",".join(architecture_list)))
        r1_html = '<tr class="row-a"{}><td class="name-cell"><a target="_blank" href="{}" title="data: {}">{}</a></td>'.format(row_attrs, source_link, source_file, p)
        for c in cells_e:
            cl = df.loc[p, c + ".class"]
            link = df.loc[p, c + ".link"]
            notes = df.loc[p, c + ".notes"]
            symbol = "&#10004;&#xFE0E" if cl == "open" else "~" if cl == "partial" else "&#10008;" if cl == "closed" else "?"
            r1_html += '<td class="{} data-cell"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(cl, link, notes, symbol)
        for c in cells_n:
            cl = df.loc[p, c + ".class"]
            link = df.loc[p, c + ".link"]
            notes = df.loc[p, c + ".notes"]
            # Use a yellow star if the category exists; otherwise, leave it blank.
            symbol = "&#11088;" if cl == "star" else "&#8709;"
            r1_html += '<td class="{} data-cell"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(cl, link, notes, symbol)
        
    # closing tags
    html_table += '</tbody>\n'
    html_table += '</table>\n'
    return html_table

CATEGORY_META = {
    "essential": [
        ("sourcecode", "Source code"),
        ("trainingdata", "Training data"),
        ("modelweights", "Model weights"),
        ("codedoc", "Code documentation"),
        ("trainprocedure", "Training procedure"),
        ("evalprocedure", "Evaluation procedure"),
        ("paper", "Research paper"),
        ("license", "Licensing"),
    ],
    "desirable": [
        ("modelcard", "Model card"),
        ("datasheet", "Datasheet"),
        ("package", "Package"),
        ("ux", "User-oriented application"),
        ("suppage", "Supplementary material page"),
    ],
}

def field(df, p, col):
    """Safely read a df field for project p, returning '' if missing/NaN."""
    if col not in df.columns:
        return ""
    val = df.loc[p, col]
    return val if pd.notna(val) and val != "" else ""

def build_category_row(df, p, key, label, kind):
    cl = field(df, p, key + ".class")
    link = field(df, p, key + ".link")
    notes = field(df, p, key + ".notes")
    if kind == "essential":
        if cl == "open":
            badge_class, badge_text = "open", "&#10004;&#xFE0E; Open"
        elif cl == "partial":
            badge_class, badge_text = "partial", "~ Partial"
        elif cl == "closed":
            badge_class, badge_text = "closed", "&#10008; Closed"
        else:
            badge_class, badge_text = "na", "? Unclassified"
    else:
        if cl == "star":
            badge_class, badge_text = "open", "&#11088; Included"
        else:
            badge_class, badge_text = "na", "&#8709; Not included"

    # status badge itself becomes the source link when one is available
    if link:
        badge_html = '<a class="openness {}" href="{}" target="_blank">{}</a>'.format(
            badge_class, html.escape(str(link), quote=True), badge_text)
    else:
        badge_html = '<span class="openness {}">{}</span>'.format(badge_class, badge_text)

    row = '<tr>'
    row += '<td class="cat-name">{}</td>'.format(html.escape(label))
    row += '<td class="cat-status">{}</td>'.format(badge_html)
    row += '<td class="cat-notes">{}</td>'.format(html.escape(str(notes)) if notes else '')
    row += '</tr>'
    return row

def build_category_table(df, p, section_key):
    rows = "".join(build_category_row(df, p, key, label, section_key) for key, label in CATEGORY_META[section_key])
    table = '<table class="category-table"><thead><tr>'
    table += '<th>Category</th><th>Status</th><th>Notes</th>'
    table += '</tr></thead><tbody>{}</tbody></table>'.format(rows)
    return table

def build_model_page_content(df, p):
    slug = slugify(p)
    org_name = field(df, p, "org.name")
    org_link = field(df, p, "org.link")
    year = field(df, p, "project.year")
    description = field(df, p, "project.description")
    apptypes = split_multi(field(df, p, "project.apptype"))
    architectures = split_multi(field(df, p, "project.architecture"))

    website = field(df, p, "project.link")
    repo = field(df, p, "sourcecode.link")
    paper_link = field(df, p, "paper.link")
    demo_link = field(df, p, "ux.link") or field(df, p, "suppage.link")

    content = '<h1>{}</h1>'.format(html.escape(str(p)))

    meta_parts = []
    if org_name:
        if org_link:
            meta_parts.append('<strong><a href="{}" target="_blank">{}</a></strong>'.format(html.escape(str(org_link), quote=True), html.escape(str(org_name))))
        else:
            meta_parts.append('<strong>{}</strong>'.format(html.escape(str(org_name))))
    if year:
        meta_parts.append(str(year))
    if meta_parts:
        content += '<p class="model-meta">{}</p>'.format(" &middot; ".join(meta_parts))

    if description:
            content += '<p class="highlight">{}</p>'.format(html.escape(str(description)))

    if apptypes or architectures:
        content += '<div class="model-tags"><strong>Application types:</strong> '
        for a in apptypes:
            content += '<span class="model-tag">{}</span>'.format(html.escape(a))
        content += '</div><div class="model-tags"><strong>Architecture:</strong>'
        for a in architectures:
            content += '<span class="model-tag">{}</span>'.format(html.escape(a))
        content += '</div>'

    

    # Only the links that actually exist for this model appear as buttons,
    # and "Back to leaderboard" always last.
        link_items = []
    if website:
        link_items.append(('Website', website, True))
    if repo:
        link_items.append(('Repository', repo, True))
    if paper_link:
        link_items.append(('Paper', paper_link, True))
    if demo_link:
        link_items.append(('Demo', demo_link, True))
    # link_items.append(('Raw YAML file', yaml_url, True))
    link_items.append(('Back to leaderboard', '../../index.html', False))

    content += '<nav class="model-links" aria-label="Model links">'
    for label, url, external in link_items:
        target_attr = ' target="_blank"' if external else ''
        content += '<a href="{}"{}>{}</a>'.format(html.escape(str(url), quote=True), target_attr, html.escape(label))
    content += '</nav>'

    content += '<div class="category-section"><h2>Essential categories</h2>'
    content += build_category_table(df, p, "essential")
    content += '</div>'

    content += '<div class="category-section"><h2>Desirable categories</h2>'
    content += build_category_table(df, p, "desirable")
    content += '</div>'

    yaml_url = "https://github.com/roserbatlleroca/MusGO_framework/blob/main" + df.loc[p, "source.file"]
    content += '<div>'
    content += f'<p class="model-meta"><a href={yaml_url}>Raw YAML file with complete evaluation.</a></p></div>'

    return content

def create_model_pages(df):
    template_path = "./docs/model_template.html"
    if not os.path.exists(template_path):
        print(
            "\n[WARNING] Skipping individual model pages: '{}' was not found.\n"
            "          Make sure model_template.html has been added to your docs/ folder "
            "(same location as template.html), then re-run this script.\n".format(template_path)
        )
        return
    with open(template_path, "r", encoding='utf-8') as f:
        base_html = f.read()
    utc_datetime = datetime.datetime.utcnow()
    build_message = utc_datetime.strftime("Model page last updated on %Y-%m")
    projects = df.index.tolist()
    pages_written = 0
    for p in projects:
        slug = slugify(p)
        soup = BeautifulSoup(base_html, "html.parser")
        # <title> stays the same across all model pages (matches the main site);
        # no per-model override needed here.
        target = soup.find(id="model-page")
        if target is None:
            print("[WARNING] model_template.html has no element with id=\"model-page\"; skipping {}.".format(p))
            continue
        target.clear()
        target.append(BeautifulSoup(build_model_page_content(df, p), 'html.parser'))
        build_time_el = soup.find(id="build-time")
        if build_time_el is not None:
            build_time_el.string = build_message
        out_dir = os.path.join("./docs/models", slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding='utf-8') as f:
            f.write(str(soup))
        pages_written += 1
    print("Wrote {} individual model pages to ./docs/models/".format(pages_written))

def create_index(table, model_count):
    # read and parse the template file
    with open("./docs/template.html", "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    # find the target location
    target_element = soup.find(id="included-table")
    # Convert the HTML code string into a BeautifulSoup object and append it to the target element
    target_element.append(BeautifulSoup(table, 'html.parser'))
    # Fill in the live count of evaluated models
    model_count_element = soup.find(id="model-count")
    if model_count_element is not None:
        model_count_element.string = str(model_count)
    # Add build time info
    utc_datetime = datetime.datetime.utcnow()
    build_message = utc_datetime.strftime("Table last built on %Y-%m")
    target_footer = soup.find(id="build-time")
    target_footer.string = build_message
    # write to disk
    with open("./docs/index.html", 'w', encoding='utf-8') as f:
        f.write(str(soup))

def create_figure(figure):
    # read and parse the template file
    with open("./docs/template_figure.html", "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    # find the target location
    target_element = soup.find(id="included-table")
    # Convert the HTML code string into a BeautifulSoup object and append it to the target element
    target_element.append(BeautifulSoup(figure, 'html.parser'))
    # Add build time info
    utc_datetime = datetime.datetime.utcnow()
    build_message = utc_datetime.strftime("Figure last built on %Y-%m")
    target_footer = soup.find(id="build-time")
    target_footer.string = build_message
    # write to disk
    with open("./docs/figure.html", 'w', encoding='utf-8') as f:
        f.write(str(soup))

#the path of the csv files to combine
path = r'./projects' 
all_files = glob.glob(path + "/*.yaml")

print('files:', all_files)

df = create_dataframe(all_files)
df = calculate_openness(df)
# Add a column to count the number of stars
nice_to_have_cols = ["modelcard", "datasheet", "package", "ux", "suppage"]
df["star_count"] = df[ [f"{col}.class" for col in nice_to_have_cols] ].apply(lambda row: sum(1 for x in row if x == "star"), axis=1)

# sort by openness, star count and project name
df = df.sort_values(by=["openness", "star_count", "project.name"], ascending=[False, False, True])

table = write_html(df)
create_index(table, len(df))
figure = write_simplified_html(df)
create_figure(figure)
create_model_pages(df)

print(f"\nCurrently, there are {len(df)} models evaluated with MusGO.")

# csv filename
df.to_csv("./docs/df.csv", index=False)
