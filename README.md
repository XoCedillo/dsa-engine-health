# engine_health

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

ML project to predict the health of engines


# Step-by-Step Guide to Setup

## 1. Install Conda
If you haven't already installed Conda, you can download and install Miniconda (a minimal Conda installer) or Anaconda (which includes more packages by default):

- **Miniconda (Recommended for most users):**
  
  Download Miniconda from the official website: [Miniconda Installation](https://docs.conda.io/en/latest/miniconda.html).

  Follow the installation instructions for your operating system.

- **Anaconda:**
  
  Download Anaconda from the official website: [Anaconda Installation](https://www.anaconda.com/products/individual).

  Follow the installation instructions for your operating system.

Now you have Conda installed and ready to use. You can create environments, install packages, and manage your Python projects efficiently.



## 2. Create a New Conda Environment
Once Conda is installed, you can create a Conda environment specifically for this project. This helps isolate project dependencies from other projects on your system:

- **Create the Environment:**

   This will create the environment using `environment.yml` file:
   ```bash
   make create_environment     
   ```


- **Activate the Environment:**

   Activate the newly created environment:
   ```bash
   conda activate dsa-engine-health
   ```

Now, your terminal prompt should indicate that you are working within the `dsa-engine-health` environment.


## 3. Install Packages
Now that your environment is active, you can start installing packages required for your project.  All you need to do is update the contents of your `environment.yml` file accordingly and then run the following command:

```bash
make requirements
```


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         engine_health and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── engine_health   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes engine_health a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

