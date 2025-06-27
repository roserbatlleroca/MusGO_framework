# How to contribute? 

Every analysed model is evaluated in a specific YAML file. To contribute to the openness analysis with a new model, please replicate the yaml file **_template.yaml** and fulfil it according to the MusGO framework criteria. Once all information is complete, request a pull-request. 

# Criteria 

## Essential 


#### **[1] Open source code.** Is the system source code, including the data processing, model architecture, training pipeline, and inference, openly available for inspection and use? 

✗ **System source code is closed.** The system's source code, including the data processing, model architecture, training pipeline and inference, is not available for inspection or use.

≃ **Some source code is provided.** Part of the source code is available, but significant gaps do not enable full reproducibility or understanding. For example, only certain parts of the system (e.g., inference or limited components of the training pipeline) are accessible, while the model architecture or key components for data processing are missing. 

✓ **System source code is fully available.** The complete source code, including the data processing, model architecture, training pipeline, and inference, is accessible for inspection and use. The code is shared in a well-organised and usable format, allowing detailed analysis.


#### **[2] Training data.** Is the training data of the model fully described, including sources, acquisition methods, and access conditions? Is training data available for inspection?

**✗ Training data of the model is not available nor described.** The training data is not disclosed, and no information about the data sources, acquisition methods, or access conditions is provided.
**≃ Some of the training data or information about the data is available.** Some of the training data of the model is available, or information about the data, such as its sources or a general description, is provided. However, the complete dataset is not provided, or information about the data is not complete. The level of detail provided does not allow for full reproducibility.
**✓ The training data of the model is fully available and described.** The training data used for the model is described in detail, including its sources, acquisition methods, and any permissions or licenses associated with its use. Although direct access to the data may be restricted due to copyright or other legal concerns, all sources and relevant access conditions are fully disclosed to allow for transparency and informed inspection.


#### **[3] Model weights.** Are the complete model weights (of the production-ready) model fully shared and accessible for inspection and use?

**✗ Model weights are not shared.** Weights of the production-ready model are not publicly available.

**≃ Model weights are partially shared.** Some or all model weights are publicly available, but there are limitations or restrictions on their accessibility. 

**✓ Model weights are fully shared.** The complete model weights are publicly available for inspection and use.

#### **[4] Code documentation.** Is the codebase accompanied by sufficient and complete documentation to allow for its replication, extension, or modification?

**✗ Code documentation is not available.** No documentation for the code is provided, making it difficult or impossible to replicate, extend, or modify the codebase. 

**≃ Some components of the codebase are documented.** Some parts of the code are documented, but the documentation is incomplete or lacks sufficient detail. Key sections might be explained, but replication or modification may still require significant effort. For instance, there could be minimal comments, but there may be no instructions or high-level overviews to guide users.

**✓ The codebase is fully documented.** All components of the codebase are accompanied by comprehensive documentation that includes clear instructions, explanations, and details on how the model can be replicated. This includes well-commented code, guides for configuration, and any necessary setup details to ensure the model is usable by others (i.e. environment requirements, specific configuration settings). While not essential, documentation may include details on how to extend or modify the codebase.

#### **[5] Training procedure.** Is the training procedure of the system fully documented to allow for replication and understanding of the system? 

**✗ Training procedure is not documented.** No documentation is provided for the system's training procedure. Important details like hardware requirements and model configuration are absent, making it difficult or impossible to replicate or fully understand the design and performance of the system.

**≃ Training procedure is partially documented.** Some aspects of the system's training procedure are documented, but the details are incomplete or unclear. For example, hardware requirements or training methods might be partially described, but critical aspects such as model configuration might be missing or insufficiently explained. Replication or a deeper understanding might still require significant effort or additional information from the authors.

**✓ Training procedure is fully documented.** The system's training procedure is thoroughly documented, including details such as hardware requirements and model configuration, allowing others to replicate the model and fully understand the system.

#### **[6] Evaluation procedure.** Is the evaluation procedure of the system fully documented to support reproducibility of evaluation results and performance? 

**✗ Evaluation procedure is not documented.** No information is provided about the evaluation procedure of the model. Key elements such as evaluation data, evaluation metrics, and evaluation procedure are not described. 

**≃ Evaluation procedure is partially documented.** Some aspects of the system’s evaluation procedure are documented, but the details are incomplete or unclear. For instance, evaluation data and evaluation metrics might be described, but the evaluation process might not be explained or documentation is insufficient. 

**✓ Evaluation procedure is fully documented.** The system’s evaluation procedure is comprehensibly documented, including details on evaluation data, evaluation metrics, and complete evaluation process, accompanied of necessary code.

#### **[7] Research paper.** Is there a publicly available and accessible research paper, or alternative technical report, that provides an overview of the introduced model? Is it peer-reviewed by an external group of reviewers? 

**✗ No peer-reviewed research paper or alternative technical report is available.** There is no publicly available publication or report that provides an overview of the introduced model.

**≃ A research paper or alternative technical report exists, but it is either not peer-reviewed or not accessible.** Any available research paper or technical report may describe an overview of the introduced model, but document is not peer-reviewed and/or not accessible. 

**✓ A peer-reviewed and accessible research paper is available.** An accessible peer-reviewed^ research paper exists and provides an overview of the introduced model.

^ If the peer-reviewed research paper is not available through open access publication, we consider the category to be “fully open” when a preprint of such research paper is available.

#### **[8] Licensing.** Is the system and its components licensed under a clear and adequate open framework, such as an OSI, RAIL license or other context-appropriate license?

**✗ No license available**. The system lacks context-appropriate licensing. 

**≃ System is only partially covered by an adequate license.** Some components of the system are covered by clear and adequate open license, such as OSI or RAIL license, but not all distributed materials.

**✓ System is covered by a clear and adequate open license.** The system and all distributed materials are fully covered by clear and adequate open license, such as OSI or RAIL license.

## Desirable 

#### [9] Model card. Is a model card or equivalent documentation provided? Does it offer comprehensive insight into the model’s architecture, training, tuning and evaluation?

⭑ **Model card(s) available.** Model card(s) or equivalent documentation is available, providing insights into architecture, architecture, training, tuning, evaluation or intended use cases and limitations.

#### [10] Datasheet. Does the model include datasheets or equivalent documentation that provide a systematic and standardized account of the data used for training, focusing on collection, curation, and relevant considerations such as consent and limitations?

⭑ **Datasheet(s) available.** Datasheets or equivalent documentation are available, offering an overview of data collection, curation, and considerations like consent, limitations, and selection strategies.

#### [11] Package. Is the model released as an indexed software package or provided through an equivalent developeroriented solution to ensure the accessibility, usability, and reproducibility of the model?

⭑ Packaged release available. A versioned software package release (e.g., PyPI, Conda, Homebrew) or equivalent solution is provided, ensuring easy installation, reproducibility, and usability.

#### [12] User-oriented application. Is the model accessible via a user-oriented interface, such as an API, a real-time implementation or a UX tool for creative contexts?

⭑ User-oriented application available. An accessible and user-oriented interface of the model exists, such as
an API, a real-time model implementation, or a UX tool designed to enhance usability in creative contexts (e.g.
for live performances or musicians’ creative processes).

#### [13] Supplementary material page. Is there a demo page that showcases its capabilities by providing sonified generated examples of the model and demonstrates how to use the model in practice?

⭑ Supplementary material page available. An accompanying website showcasing diverse examples, including
sonified outputs and/or detailed usage demonstrations. In addition, the page may include interactive elements
to help users understand the model’s capabilities and applications.