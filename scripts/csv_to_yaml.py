import csv
import ruamel.yaml as yaml
from ruamel.yaml.comments import CommentedMap
import os
import copy

# File paths
csv_file_path = './misc/openness_eval.csv'
yaml_template_path = './projects/_template.yaml'
output_yaml_path = './projects/'

initial_comments = """---
####################################################################################################################################
# Project template of the MusGO framework repository (https://github.com/roserbatlleroca/MusGO_framework/). 
# Note that this document has been adapted from previous work by Andreas Liesenfeld, Alianda Lopez, and Mark Dingemanse. 
# For more details, check out: http://opening-up-chatgpt.github.io  
####################################################################################################################################


# Thank you for contributing!
# In filling out this yaml file, please follow the criteria as described here: 
# https://github.com/roserbatlleroca/MusGO_framework/tree/main/projects#criteria

"""

# Load the YAML template
def load_yaml_template(template_path):
    with open(template_path, 'r') as template_file:
        yaml_data = yaml.YAML(typ='safe')
        return yaml_data.load(template_file)

# Write YAML data to file with spaces and comments
def write_yaml_file(data, output_path, modelname, comments):
    output_file = os.path.join(output_path, modelname + ".yaml")
    yaml_data = yaml.YAML()
    yaml_data.indent(mapping=2, sequence=4, offset=2)  # Set indentation

    # Apply comments to keys
    for key, comment in comments.items():
        if comment:
            data.yaml_set_comment_before_after_key(key, before=comment)

    with open(output_file, 'w') as yaml_file:
        yaml_file.write(initial_comments + '\n')
        yaml_data.dump(data, yaml_file)

# Parse CSV and transform into YAML structure
def csv_to_yaml(csv_path, yaml_template):
    with open(csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Get YAML template for each project
            project_data = CommentedMap(copy.deepcopy(yaml_template))
            comments = {}
            for key in project_data:
                comments[key] = ""

            # Fill in project details
            project_data['project']['name'] = row.get('Model', '')
            project_data['project']['link'] = row.get('Repository', '')
            project_data['project']['background'] = row.get('Why?', '')
            project_data['project']['license'] = row.get('[13] Notes', '')

            # Fill in organization details
            project_data.yaml_set_comment_before_after_key('org', before="\n")
            project_data['org']['name'] = row.get('Affiliation(s)', '')

            cells_e = ["sourcecode", "trainingdata", "modelweights", "codedoc", "trainprocedure", "evalprocedure", "paper", "license"]
            cells_e_names = ["Open Source Code", "Training data", "Model weights", "Code documentation", "Training procedure", "Evaluation procedure", "Research paper", "Licensing"]
            cells_n = ["modelcard", "datasheet", "package", "ux", "suppage"] # Nice-to-have categories
            cells_n_names = ["Model Card", "Datasheet", "Package", "User-oriented application", "Demo Page"]

            for i, cell in enumerate(cells_e):
                cell_e_name = cells_e_names[i]
                if "license" in cell:
                    cell_e_val = i + 6
                else:
                    cell_e_val = i + 1
                if "sourcecode" in cell:
                    project_data[cell]['link'] = row.get('Repository', '')
                elif "paper" in cell:
                    project_data[cell]['link'] = row.get('Preprint', '')
                project_data[cell]['class'] = row.get(f"[{cell_e_val}] {cell_e_name}", '')
                project_data[cell]['notes'] = row.get(f"[{cell_e_val}] Notes", '')
                project_data.yaml_set_comment_before_after_key(cell, before=f"\n[{i+1}] {cell_e_name}")

            for i, cell in enumerate(cells_n):
                cell_n_name = cells_n_names[i]
                cell_n_val = i + 8
                project_data[cell]['class'] = row.get(f"[{cell_n_val}] {cell_n_name}", '')
                project_data[cell]['notes'] = row.get(f"[{cell_n_val}] Notes", '')
                project_data.yaml_set_comment_before_after_key(cell, before=f"\n[{i+9}] {cell_n_name}")

            # Write YAML file with comments and spaces
            write_yaml_file(project_data, output_yaml_path, project_data['project']['name'].lower(), comments)
            print(f"YAML file for {project_data['project']['name']} created successfully.")

yaml_template = load_yaml_template(yaml_template_path)
csv_to_yaml(csv_file_path, yaml_template)  # Call csv_to_yaml only once with the correct path
