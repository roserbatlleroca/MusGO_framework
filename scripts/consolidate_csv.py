import yaml
import glob
import pandas as pd
from bs4 import BeautifulSoup
import datetime


def create_dataframe(files):
    # Read the input YAML file, transpose the rows and columns and save to dataframe
    df = pd.DataFrame()
    source_file = []
    for fname in files:
        with open(fname, 'r') as file:
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


def calculate_openness(df):
    openness_weights = {
        "sourcecode": 1, 
        "trainingdata": 1, 
        "modelweights": 1, 
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
        cumul_openness = round(cumul_openness/8*100,0) # Normalising openness level to 100 points
        openness.append(int(cumul_openness))
    # add the openness variable to the DataFrame
    df["openness"] = openness
    return df


def write_html(df):
    html_table = '<table>\n'
    html_table += '<thead>\n'
    html_table += '<tr class="main-header"><th>Project</th><th colspan="8">Essential</th><th colspan="5">Nice-to-have</th>\n'
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
        cells_n = ["modelcard", "datasheet", "package", "ux", "suppage"] # Nice-to-have categories
        # first row
        source_link = "https://github.com/roserbatlleroca/MusGO_framework/blob/main" + df.loc[p, "source.file"]
        source_file = source_link.split("/")[-1]
        #r1_html = '<tr class="row-a"><td class="name-cell"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(df.loc[p, "project.link"], df.loc[p, "project.notes"], p)
        r1_html = '<tr class="row-a"><td class="name-cell"><a target="_blank" href="{}" title="data: {}">{}</a></td>'.format(source_link, source_file, p)
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
        # second row
        #r2_html = '<tr class="row-b"><td class="org"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(df.loc[p, "org.link"], df.loc[p, "org.name"], df.loc[p, "org.name"])
        r2_html = '<tr class="row-b"><td class="org"><a target="_blank" href="{}" title="{}">{}</a></td>'.format(df.loc[p, "project.link"], df.loc[p, "project.notes"], df.loc[p, "org.name"])
        #r2_html += '<td colspan="3" class="llmbase">LLM base: {}</td><td colspan="3" class="rlbase">RL base: {}</td>'.format(df.loc[p, "project.llmbase"], df.loc[p, "project.rlbase"])
        #r2_html += '<td colspan="7"></td><td class="source-link"><a href="{}" title="{}" target="_blank">&sect;</a></td></tr>\n'.format(source_link, source_file)
        r2_html += '<td colspan="7"></td><td class="source-link"><a href="{}" title="{}" target="_blank">{}</a></td></tr>\n'.format(df.loc[p, "org.link"], df.loc[p, "org.name"], df.loc[p, "openness"])
        html_table += r2_html
    # closing tags
    html_table += '</tbody>\n'
    html_table += '</table>\n'
    return html_table

def write_simplified_html(df):
    html_table = '<table>\n'
    html_table += '<thead>\n'
    html_table += '<tr class="main-header"><th>Project</th><th colspan="8">Essential</th><th colspan="5">Nice-to-have</th>\n'
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
        cells_n = ["modelcard", "datasheet", "package", "ux", "suppage"] # Nice-to-have categories
        
        source_link = "https://github.com/roserbatlleroca/MusGO_framework/blob/main" + df.loc[p, "source.file"]
        source_file = source_link.split("/")[-1]
        r1_html = '<tr class="row-a"><td class="name-cell"><a target="_blank" href="{}" title="data: {}">{}</a></td>'.format(source_link, source_file, p)
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

def create_index(table):
    # read and parse the template file
    with open("./docs/template.html", "r") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    # find the target location
    target_element = soup.find(id="included-table")
    # Convert the HTML code string into a BeautifulSoup object and append it to the target element
    target_element.append(BeautifulSoup(table, 'html.parser'))
    # Add build time info
    utc_datetime = datetime.datetime.utcnow()
    build_message = utc_datetime.strftime("Table last built on %Y-%m-%d at %H:%M UTC")
    target_footer = soup.find(id="build-time")
    target_footer.string = build_message
    # write to disk
    with open("./docs/index.html", 'w') as f:
        f.write(str(soup))

def create_figure(figure):
    # read and parse the template file
    with open("./docs/template_figure.html", "r") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    # find the target location
    target_element = soup.find(id="included-table")
    # Convert the HTML code string into a BeautifulSoup object and append it to the target element
    target_element.append(BeautifulSoup(figure, 'html.parser'))
    # Add build time info
    utc_datetime = datetime.datetime.utcnow()
    build_message = utc_datetime.strftime("Figure last built on %Y-%m-%d at %H:%M UTC")
    target_footer = soup.find(id="build-time")
    target_footer.string = build_message
    # write to disk
    with open("./docs/figure.html", 'w') as f:
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
create_index(table)
figure = write_simplified_html(df)
create_figure(figure)

# csv filename
df.to_csv("./docs/df.csv", index=False)
