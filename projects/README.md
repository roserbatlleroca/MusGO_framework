
# How to conduct an evidence-based assessment with MusGO? 

The MusGO framework is designed to guide fair and transparent evaluations of openness in music-generative AI models. To ensure consistency and traceability, we encourage all contributors to follow an evidence-based approach.

You can find the complete definition and descriptions of all MusGO criteria on the [**MusGO Framework page**](https://roserbatlleroca.github.io/MusGO_framework/framework.html). To evaluate a new model or validate a current assessment, we recommend using the [MusGO checklist](https://roserbatlleroca.github.io/MusGO_framework/checklist.html) to guide your evaluation step-by-step. 

Once your assessment is complete, follow the instructions below to learn how to [add a new model](#adding-a-new-model) or [amend an existing evaluation](#amending-a-current-evaluation).


---

# How to contribute? 

## Adding a new model

Every analysed model is evaluated in a specific YAML file. To contribute to the openness analysis with a new model, please complete the following steps: 

#### 1. **Copy the Template**

Duplicate the file `_template.yaml` and rename it to:  `[model-name].yaml`  
Use lowercase and hyphens to separate words: 
> _Example:_ `stable-audio-open.yaml`

#### 2. **Fill in the Evaluation**

- Fill in all the project information: `name`, `link`, `license` and `org`. 
- For each of the **essential categories [1–8]**, classify as `open`, `partial`, or `closed`.
- For each **desirable category [9–13]**, classify as `star` (⭐) or `∅` (not applicable).
- Provide a **justification** in the `notes` field for each classification. You can also add a reference link to complement the information. 
  > _Example:_  If Training Data is `closed`, a note might say:  `"Dataset is closed and only briefly described."`
  > _Example:_  If Model Weights is `open`, a note might say:  `"Weights are available." and a link to the weights might be added.`

#### 3. **Submit a Pull Request**

Once your YAML file is complete:

1. Open a **pull request** with your new model file.
2. The repository maintainers will **review your submission**:
  - If everything looks good, your model will be merged into the leaderboard.
  - If we spot any missing info or inconsistencies, we’ll reach out to clarify or request edits. You may be asked to provide **additional context or evidence**, and suggestions may be revised **collaboratively** before being accepted.
3. Once all issues are addressed, the model will be officially added! Credit for the contribution will be reflected in the commit and PR history.


## Amending a current evaluation 


If you'd like to propose an update to the evaluation of a model already listed in the leaderboard, there are two main reasons this might apply:

1. **The model has changed** — A new version, component, or resource has been released that affects one or more categories.
2. **You disagree with a current classification** — You believe a category's score or justification is inaccurate or outdated.


#### How to proceed?

1. **Open an issue** detailing:
   - The **model name** and YAML file.
   - The **specific category (or categories)** you'd like to update.
   - The **reason for your proposal**, with clear references (e.g., links, publications, repo updates).
  
2. **Review and discussion**: The repository maintainers will review the issue:
   - If the proposal is valid, maintainers will **update the YAML file directly** or you will be invited to **submit a pull** request with your proposed changes.
   - If there are **questions, missing information, or doubts**, or if the maintainers **disagree with the proposed change**, they will **respond in the issue thread** to clarify concerns and open a discussion.
   - You may be asked to provide **additional context or evidence**, and suggestions may be revised **collaboratively** before being accepted or rejected.

3. **Resolution**
   - Once confirmed, the updated evaluation will be merged into the leaderboard.
   - Credit for the contribution will be reflected in the commit and PR history.

---

If you have any doubt or issue, do not heasitate to contact us at [roser.batlle@upf.edu](mailto:roser.batlle@upf.edu) and [laura.ibanez@upf.edu](mailto:laura.ibanez@upf.edu). Your contributions help us maintain fair and up-to-date openness assessments and promote transparency and openness in music-generative AI. Thank you for contributing to MusGO!
