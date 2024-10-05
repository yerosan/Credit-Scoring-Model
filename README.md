# Credit Scoring Model Project
## Project Overview
This project aims to develop an advanced credit scoring model using transaction-level data. By leveraging modern methodologies such as the Recency, Frequency, Monetary (RFM) model, the project seeks to enhance traditional credit risk assessments through in-depth exploratory data analysis (EDA) and machine learning techniques.

## Table of Contents
- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Key Insights](#key-insights)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)



Folder Structure
The following is the high-level structure of the project:

```bash
.github/               - GitHub configuration files
.vscode/               - VSCode workspace settings
data/                  - Datasets used for model building (not included in the repository)
models/                - Saved machine learning models
notebooks/             - Jupyter notebooks for EDA and model experimentation
    └── EDA.ipynb      - Exploratory Data Analysis notebook
    └── README.md      - Notebook-specific documentation
scripts/               - Python scripts for data processing and model building
    └── eda.py         - EDA script in Python
    └── credit_risk.py - Understanding credit risk
src/                   - Source code for the core application logic
tests/                 - Unit and integration tests for the project
week6/                 - project env
.gitignore             - Files and directories to be ignored by Git
README.md              - Project-level documentation (this file)
requirements.txt       - Python dependencies for the project
```
Clone the repository:

```bash
git clone https://github.com/yerosan/Credit-Scoring-Model.git
cd Credit-Scoring-Model
```
Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `.week6\Scripts\activate`
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```
Usage
Running Exploratory Data Analysis (EDA)

To run the exploratory data analysis in Python, use the script eda.py:

```bash
python scripts/eda.py

```
Alternatively, you can explore the data analysis using the Jupyter notebook provided:

```bash
jupyter notebook notebooks/EDA.ipynb

```