<div align="center">

# MusGO: A Community-Driven Framework For Assessing Openness in Music-Generative AI

**Roser Batlle-Roca**<sup>1</sup>, **Laura Ibáñez-Martínez**<sup>1</sup>,**Xavier Serra**<sup>1</sup>, **Emilia Gómez**<sup>1,2</sup>, **Martín Rocamora**<sup>1</sup>

<sup>1</sup>Music Technology Group, Universitat Pompeu Fabra, Barcelona

<sup>2</sup>Joint Research Centre, European Comission, Sevilla 


[![License: MIT](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![arXiv](https://img.shields.io/badge/arXiv-2507.X-<COLOR>.svg)]()


The **Music-Generative Open AI (MusGO)** framework is a community-driven framework built to assess openness in music-generative models. With a collaborative approach, it invites contributions from researchers and artists, supports public scrutiny, and enables tracking of model evolution to promote transparency, accountability, and responsible development. This article has been accepted at the 26th International Society for Music Information Retrieval (ISMIR) Conference. 

📍 View the **[MusGO leaderboard](https://roserbatlleroca.github.io/MusGO_framework/index.html)** to explore current model assessments.

</div>

---
## Abstract 

Since 2023, generative AI has rapidly advanced in the music domain. Despite significant technological advancements, music-generative models raise critical ethical challenges, including a lack of transparency and accountability, along with risks such as the replication of artists’ works, which highlights the importance of fostering openness. With upcoming regulations such as the EU AI Act encouraging open models, many generative models are being released labelled as ‘open’. However, the definition of an open model remains widely debated. In this article, we adapt a recently proposed evidence-based framework for assessing openness in LLMs to the music domain. Using feedback from a survey of 110 participants from the Music Information Retrieval (MIR) community, we refine the framework into MusGO (Music-Generative Open AI), which comprises 13 openness categories: 8 *essential* and 5 *desirable*. We evaluate 16 state-of-the-art generative models and provide an openness leaderboard that is fully open to public scrutiny and community contributions. Through this work, we aim to clarify the concept of openness in music-generative AI and promote its transparent and responsible development.

---

## The MusGO framework

MusGO is composed of **13 categories**: 8 _essential_ and 5 _desirable_. Essential categories follow an **openness-graded scale** of three levels: **closed** (🔴), **partial** (🟠) and **fully open** (🟢). Instead, desirable categories are binary, indicating whether the element exists (**⭐**) or not. Framework criteria is detailed [here](https://roserbatlleroca.github.io/MusGO_framework/framework.html).

### Essential Categories
Open source code • Training data • Model weights • Code documentation •  Training procedure • Evaluation procedure • Research paper • Licensing  

### Desirable Categories
Model card • Datasheet • Package • User-oriented application • Supplementary material page

## 🚀 Contribute

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


## 📚 Citation 

```
@article{batlleroca2025musgo,
  title={{MusGO}: A Community-Driven Framework For Assessing Openness in Music-Generative AI},
  author={Roser Batlle-Roca and Laura Ibáñez-Martínez and Xavier Serra and Emilia Gómez and Martín Rocamora},
  journal={Proceedings of the 26th International Society for Music Information Retrieval Conference, Daejeon, South Korea},
  year={2025}, 
  url={}, 
}
```


## Acknowledgements 
This repository is an adapted version of [Opening up ChatGPT: tracking openness of instruction-tuned LLMs](https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/). We are deeply grateful to the original creators, Andreas Liesenfeld, Alianda Lopez, and Mark Dingemanse, for their groundbreaking work on openness, transparency, and accountability in generative AI, which has inspired and shaped this project.

For more details, please refer to their papers:

- Liesenfeld, Andreas, Alianda Lopez, and Mark Dingemanse. 2023. *“Opening up ChatGPT: Tracking Openness, Transparency, and Accountability in Instruction-Tuned Text Generators.”* In *CUI '23: Proceedings of the 5th International Conference on Conversational User Interfaces*, July 19-21, Eindhoven. DOI: [10.1145/3571884.3604316](https://doi.org/10.1145/3571884.3604316).
- Andreas Liesenfeld and Mark Dingemanse. 2024. *“Rethinking open source generative AI: open washing and the EU AI Act.”* In *The 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24)*. DOI: [10.1145/3630106.3659005](https://doi.org/10.1145/3630106.3659005).
