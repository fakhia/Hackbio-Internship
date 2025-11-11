# Hackbio-Internship
# HackBio Internship — Stage 0 Task 🧪  
### Project Title: What scRNA Tells Us About Cancer Evolution  

👩‍🔬 **Author:**  
**Fakhia Mubashir**  
B.Sc. Zoology | Computational Biology Enthusiast  
**Research Focus:** Ion Channels, Cancer Biology, and Membrane Protein Translation  

---

## 🧩 **Task Overview**
This repository contains the **Stage 0 Task** for the **HackBio Internship**.  
It includes:
- A short essay on **“What scRNA tells us about cancer evolution”**
- A simple Python code file (`simple_code.py`)
- Instructions and expected output  

---

## 📘 **Essay: What scRNA Tells Us About Cancer Evolution**

Single-cell RNA sequencing (scRNA-seq) has transformed our understanding of cancer by allowing us to study gene expression at the level of individual cells. Unlike bulk sequencing, which averages gene expression data across many cells, scRNA-seq reveals cellular heterogeneity — one of the key factors driving tumor growth, metastasis, and therapeutic resistance.  

Through scRNA-seq, scientists can trace how cancer cells evolve over time, mapping clonal trajectories and uncovering how environmental pressures such as immune response, nutrient availability, and hypoxia influence tumor adaptation.  

It also helps identify rare cell types within tumors that contribute to disease relapse or drug resistance. Integrating scRNA-seq data with genomic and proteomic analyses provides a more comprehensive view of how **tumor microenvironments** and **genetic variations** interact during cancer progression.  

Ultimately, scRNA-seq not only helps us understand the **evolutionary history of tumors**, but also guides the development of **personalized treatment strategies** that target specific cellular subpopulations responsible for malignancy.  

---

## 💻 **Python File: `simple_code.py`**

### 📄 **Description**
This Python script prints basic personal and biological information such as name, Slack username, country, hobby, and favorite gene with its nucleotide sequence.

---

### 🧠 **Code:**
```python
# simple_code.py
# HackBio Internship — Stage 0 Task
# Author: Fakhia Mubashir
# GitHub: https://github.com/fakiha-ch
# LinkedIn: www.linkedin.com/in/fakiha-ch-a9aa9b270/

def main():
    name = "Fakhia Mubashir"
    slack_username = "@fakhia_mubashir"
    country = "Pakistan"
    hobby = "Reading research papers and writing scientific essays"
    favorite_gene = "TRPV6"
    nucleotide_sequence = "ATGGCGGCGACCTTCGTGGCCGAGGCCATCGAGGCGGCCGTGGCGGTG"

    print("Name:", name)
    print("Slack Username:", slack_username)
    print("Country:", country)
    print("Hobby:", hobby)
    print("Favorite Gene:", favorite_gene)
    print("Nucleotide Sequence:", nucleotide_sequence)

if __name__ == "__main__":
    main()
