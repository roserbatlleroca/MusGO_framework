# MusGO Framework: Assessing Openness in Music-Generative AI 
We introduce the **Music-Generative Open AI (MusGO)** framework, a community-driven framework built to assess openness in music-generative models. 

❗ Note that this repository is part of the article 'MusGO: A Community-Driven Framework for Asssessing Openness in Music-Generative AI' submitted at ACM Conference on Fairness, Accountability, and Transparency (FAccT '25), which is currently under review.

### Abstract 
Since 2023, the music domain has witnessed a notable rise in generative AI, marked by the emergence of highly promising models. Despite their significant advances, music-generative models raise critical ethical challenges concerning multiple stakeholders and traditional music creative practices. The lack of transparency and the need for accountability and mitigating risks, such as the potential replication of artists’ works, underscore the importance of fostering openness in music-generative models. With upcoming regulations such as the EU AI Act encouraging open models, several generative models are being released claiming to be ‘open’. However, what exactly constitutes an open model continues to be widely debated. In this article, we adopt and adapt a recently proposed evidence-based framework for assessing openness in LLMs to the music domain. We scrutinise the proposed framework with a survey of 110 participants from the Music Information Retrieval (MIR) community, refining the assessment criteria based on their feedback. Our revised framework __MusGO__ (Music-Generative Open AI) comprises 13 categories, distinguished between *essential* (8) and *nice-to-have* (5), based on the level of relevance established from the survey. We evaluate 16 state-of-the-art generative models, offering an in-depth analysis of their openness across these criteria. Our evaluation indicates that while open models are available, the community must be aware of \textit*open-washing*. As part of our contribution, we provide an openness leaderboard, showcasing the degree of openness of the analysed models, and making it fully open to public scrutiny and community contribution. Through this work, we aim to clarify the concept of openness in music-generative AI and promote its transparent and responsible development.


## The MusGO framework

MusGO is composed of **13 categories**:

- **8 essential categories**:
1. *Open source code*  
2. *Training data*  
3. *Model weights*  
4. *Code documentation*  
5. *Training procedure*  
6. *Evaluation procedure*  
7. *Research paper*  
8. *Licensing*  
- **5 nice-to-have categories**:
9. *Model card*  
10. *Datasheet*  
11. *Package*  
12. *User-oriented application*  
13. *Supplementary material page*  

Essential categories follow an **openness-graded scale** of three levels: **closed** (🔴), **partial** (🟠) and **fully open** (🟢). 

Nice-to-have categories are binary, indicating whether the element exists (**⭐**) or not.


## Acknowledgements 
This repository is an adapted version of [Opening up ChatGPT: tracking openness of instruction-tuned LLMs](https://github.com/opening-up-chatgpt/opening-up-chatgpt.github.io/). We are deeply grateful to the original creators, Andreas Liesenfeld, Alianda Lopez, and Mark Dingemanse, for their groundbreaking work on openness, transparency, and accountability in generative AI, which has inspired and shaped this project.

For more details, please refer to their papers:

- Liesenfeld, Andreas, Alianda Lopez, and Mark Dingemanse. 2023. *“Opening up ChatGPT: Tracking Openness, Transparency, and Accountability in Instruction-Tuned Text Generators.”* In *CUI '23: Proceedings of the 5th International Conference on Conversational User Interfaces*, July 19-21, Eindhoven. DOI: [10.1145/3571884.3604316](https://doi.org/10.1145/3571884.3604316).
- Andreas Liesenfeld and Mark Dingemanse. 2024. *“Rethinking open source generative AI: open washing and the EU AI Act.”* In *The 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24)*. DOI: [10.1145/3630106.3659005](https://doi.org/10.1145/3630106.3659005).
