<div align="center">

# MusGO: A Community-Driven Framework For Assessing Openness in Music-Generative AI

**Roser Batlle-Roca**<sup>1</sup>, **Laura Ibáñez-Martínez**<sup>1</sup>, **Xavier Serra**<sup>1</sup>, **Emilia Gómez**<sup>1,2</sup>, **Martín Rocamora**<sup>1</sup>

<sup>1</sup>Music Technology Group, Universitat Pompeu Fabra, Barcelona<br>
<sup>2</sup>Joint Research Centre, European Commission, Sevilla 

The **Music-Generative Open AI (MusGO)** framework is a community-driven framework built to assess openness in music-generative models. With a collaborative approach, it invites contributions from researchers and artists, supports public scrutiny, and enables tracking of model evolution to promote transparency, accountability, and responsible development. 

📍 View the **[MusGO leaderboard](https://roserbatlleroca.github.io/MusGO_framework/index.html)** to explore current model assessments.

[![License: MIT](https://img.shields.io/badge/License-Apache_2.0-green.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17706575.svg)](https://doi.org/10.5281/zenodo.17706575)

</div>

---

## The MusGO framework

MusGO is composed of **13 categories**: 8 _essential_ and 5 _desirable_. Essential categories follow an **openness-graded scale** of three levels: **closed** (🔴), **partial** (🟠) and **fully open** (🟢). Instead, desirable categories are binary, indicating whether the element exists (**⭐**) or not. Framework criteria is detailed [here](https://roserbatlleroca.github.io/MusGO_framework/framework.html).

### Essential Categories
Open source code • Training data • Model weights • Code documentation •  Training procedure • Evaluation procedure • Research paper • Licensing  

### Desirable Categories
Model card • Datasheet • Package • User-oriented application • Supplementary material page

## Contribute

To help expand or refine the MusGO leaderboard, you can contribute by: 

- **Adding a new model** to the leaderboard. 
- **Proposing updates or modifications** to the evaluation of exisiting models. 

To get started, head over to our [**How to contribute?** page](projects/README.md). It includes:

- Instructions for submitting models via pull request
- Guidelines for proposing changes or opening issues
- A checklist to support evidence-based assessments


 Your feedback helps us maintain fair and up-to-date openness assessments. Thank you for contributing to the improvement of MusGO!

## 💬 Any doubts or thoughts? Help us improve!

We’d love to hear your feedback, questions, or suggestions for improving the MusGO framework and the evaluation process. We encourage you to open up issues to: 
- Flag a particular assessment in the current evaluations. 
- Suggest improvements to the evaluation framework. 
- Ask questions about how to interpret the categories. 

You can also contact us directly at [roser.batlle@upf.edu](mailto:roser.batlle@upf.edu) and [laura.ibanez@upf.edu](mailto:laura.ibanez@upf.edu). 

## Relationship to MusGU+

MusGO has a sister framework, <strong><a href="https://github.com/lauraibnz/MusGU-plus">MusGU+</a></strong> (Music-Generative Usable+ AI), which adopts the same composite and graded evaluation approach, but shifts the focus from openness toward practical suitability for musicians. While MusGO focuses on openness and responsible research practices, MusGU+ focuses on whether generative music systems can be adapted, used, and controlled in real-world creative workflows. Together, the two frameworks offer complementary perspectives on generative music AI.

## Citation 

The article _MusGO: A Community-Driven Framework For Assessing Openness in Music-Generative AI_ was accepted at the **26th International Society for Music Information Retrieval (ISMIR) Conference**. If our work is relevant to you, please cite it as follows: 

```
@inproceedings{batlleroca2025musgo,
  author       = {Roser Batlle{-}Roca and Laura Ib{\'{a}}{\~{n}}ez{-}Mart{\'{\i}}nez and
                  Xavier Serra and Emilia G{\'{o}}mez and Mart{\'{\i}}n Rocamora},
  title        = {MusGO: {A} Community-Driven Framework for Assessing Openness in Music-Generative {AI}},
  booktitle    = {Proceedings of the 26th International Society for Music Information Retrieval Conference, {ISMIR} 2025, Daejeon, South Korea, September 21-25, 2025},
  pages        = {727--738},
  year         = {2025},
  url          = {https://doi.org/10.5281/zenodo.17706575},
  doi          = {10.5281/ZENODO.17706575},
  biburl       = {https://dblp.org/rec/conf/ismir/Batlle-RocaISGR25.bib},
}
```


## Acknowledgements 
This repository is an adapted version of [Opening up ChatGPT: tracking openness of instruction-tuned LLMs](https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/). We are deeply grateful to the original creators, Andreas Liesenfeld, Alianda Lopez, and Mark Dingemanse, for their groundbreaking work on openness, transparency, and accountability in generative AI, which has inspired and shaped this project.

For more details, please refer to their papers:

- Liesenfeld, Andreas, Alianda Lopez, and Mark Dingemanse. 2023. *“Opening up ChatGPT: Tracking Openness, Transparency, and Accountability in Instruction-Tuned Text Generators.”* In *CUI '23: Proceedings of the 5th International Conference on Conversational User Interfaces*, July 19-21, Eindhoven. DOI: [10.1145/3571884.3604316](https://doi.org/10.1145/3571884.3604316).
- Andreas Liesenfeld and Mark Dingemanse. 2024. *“Rethinking open source generative AI: open washing and the EU AI Act.”* In *The 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24)*. DOI: [10.1145/3630106.3659005](https://doi.org/10.1145/3630106.3659005).

This work has been supported by _IA y Música: Cátedra en Inteligencia Artificial y Música_ (TSI-100929-2023-1), funded by the Secretaría de Estado de Digitalización e Inteligencia Artificial and the European Union-Next Generation EU, and _IMPA: Multimodal AI for Audio Processing_ (PID2023-152250OB-I00), funded by the Ministry of Science, Innovation and Universities of the Spanish Government, the Agencia Estatal de Investigación (AEI) and cofinanced by the European Union.

We also thank our colleagues at the Music Technology Group at Universitat Pompeu Fabra for their thoughtful insights, constructive discussions and active engagement throughout the development of this work.

<p align="center">
  <img src="docs/fig/MTG-logo.png" width="340">
</p>
