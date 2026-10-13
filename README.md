# Medical Diagnosis AI

AI-powered medical diagnosis project that collects condition data from **NHS Inform**, stores structured records in **MongoDB Atlas**, preprocesses symptom text, and trains multiple NLP/deep-learning models to rank probable medical conditions from free-text symptoms.

> This project is an educational prototype and is not intended for real clinical diagnosis or emergency decision-making.

## Project Goals

The completed system will:

- collect NHS Inform A-Z condition pages through a Flask Data Handling API
- structure condition data into symptoms, causes, warnings, and recommendations
- store the reviewed condition dataset in MongoDB
- preprocess symptom text into model-ready representations
- train and compare TF-IDF + Logistic Regression, RNN, LSTM, and BERT/BioBERT models
- rank predicted conditions using Top-K probabilities
- retrieve warnings and recommendations from MongoDB for predicted conditions
- expose prediction through a Flask Model API
- store trained model files in MongoDB GridFS
- store model metadata and evaluation metrics in a `models` collection

## Current Progress

### Completed

- [x] Project structure and environment configuration
- [x] MongoDB Atlas connection
- [x] NHS Inform A-Z page collector
- [x] Flask Data Handling API for scraping
- [x] Raw NHS page collection
- [x] Manual semantic conditioning and quality review
- [x] Final five-field condition dataset
- [x] MongoDB import/upsert workflow
- [x] Text cleaning
- [x] Symptom phrase extraction
- [x] Manual symptom overrides
- [x] Final model-data preparation
- [x] Tokenization for classical/RNN pipelines
- [x] Lemmatization comparison and documented decision
- [x] Separate BERT/BioBERT text representation

### Current Stage

Preprocessing is complete.

The next stage is:

```text
Generate source-grounded training examples
        ↓
TF-IDF + Logistic Regression baseline
        ↓
RNN
        ↓
LSTM
        ↓
BERT / BioBERT
        ↓
Model evaluation and comparison
```

## Dataset Status

The manually reviewed condition dataset contains:

```text
406 reviewed conditions
```

After symptom extraction:

```text
390 conditions with extracted symptom phrases
```

After filtering unresolved/review-required records:

```text
374 trusted model-ready conditions
32 records held for review
```

No new medical symptoms are invented during preprocessing. Manual overrides are based only on source-grounded NHS content.

## MongoDB Schema

Database:

```text
medical_diagnosis_ai
```

### Conditions Collection

```json
{
  "condition": "Condition name",
  "symptoms": "Symptoms or clinical presentation",
  "causes": "Causes, mechanisms, triggers, or risk factors",
  "warnings": "Urgent or emergency escalation advice",
  "recommendations": "Treatment, management, prevention, or self-care"
}
```

`condition` and `symptoms` are required for retained records. Optional fields may be empty when reliable source content is unavailable.

### Models Collection

Planned schema:

```json
{
  "name": "model name",
  "type": "TF-IDF / RNN / LSTM / Transformer",
  "gridfs_id": "ObjectId",
  "labels": ["condition names"],
  "metrics": {
    "top_1_accuracy": 0.0,
    "top_3_accuracy": 0.0,
    "top_5_accuracy": 0.0
  },
  "created": "DateTime"
}
```

The serialized model file will be stored in MongoDB GridFS.

## Project Structure

```text
medical-diagnosis/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── data_handling_api.py
│   │
│   ├── dataset/
│   │   ├── input/
│   │   │   ├── conditioned/
│   │   │   │   ├── nhs_conditions_manual_final.json
│   │   │   │   ├── nhs_conditions_manual_final.csv
│   │   │   │   ├── nhs_conditions_manual_changes.json
│   │   │   │   └── nhs_conditions_manual_quality_report.json
│   │   │   └── scraped/
│   │   │       ├── nhs_all_pages.json
│   │   │       └── nhs_all_pages_errors.json
│   │   ├── output/
│   │   │   └── preprocessing/
│   │   │       ├── conditions_text_cleaned.json
│   │   │       ├── conditions_symptom_parsed.json
│   │   │       ├── conditions_symptom_parsed_with_manual_overrides.json
│   │   │       ├── conditions_model_ready.json
│   │   │       └── conditions_model_ready.csv
│   │   └── review/
│   │       ├── manual_symptom_overrides.json
│   │       ├── remaining_zero_phrase_review.json
│   │       ├── conditions_model_review.json
│   │       ├── lemmatization_comparison.json
│   │       └── lemmatization_token_changes.csv
│   │
│   ├── mongo/
│   │   ├── __init__.py
│   │   ├── mongodb.py
│   │   └── import_data.py
│   │
│   ├── page_collector/
│   │   ├── __init__.py
│   │   └── collect_nhs_pages.py
│   │
│   └── preprocessing/
│       ├── 1_text_cleaner.ipynb
│       ├── 2_symptom_parser.ipynb
│       ├── 2b_apply_manual_symptom_overrides.ipynb
│       └── 3_prepare_model_data.ipynb
│
├── .env
├── .gitignore
├── AMIT FINAL PROJECT PIPELINE.png
├── README.md
├── requirements.txt
└── run.py
```

## Data Acquisition

Source:

```text
https://www.nhsinform.scot/illnesses-and-conditions/a-to-z/
```

Flow:

```text
POST /api/data/scrape/nhs
        ↓
Flask Data Handling API
        ↓
NHS Inform A-Z page collector
        ↓
app/dataset/input/scraped/
        ↓
manual semantic conditioning/review
        ↓
app/dataset/input/conditioned/
        ↓
POST /api/data/import/conditions
        ↓
MongoDB conditions collection
```

## Flask Data Handling API

Start the application:

```powershell
python run.py
```

Default address:

```text
http://127.0.0.1:5000
```

Endpoints:

```text
GET  /health
GET  /api/data/health
POST /api/data/scrape/nhs
POST /api/data/import/conditions
```

Example:

```powershell
curl.exe -X POST http://127.0.0.1:5000/api/data/scrape/nhs
curl.exe -X POST http://127.0.0.1:5000/api/data/import/conditions
```

Direct execution is also supported:

```powershell
python app/page_collector/collect_nhs_pages.py
python app/mongo/import_data.py
```

## MongoDB Configuration

Create `.env` in the project root:

```env
MONGODB_URI=mongodb+srv://YOUR_USERNAME:YOUR_PASSWORD@YOUR_CLUSTER.mongodb.net/
MONGODB_DB=medical_diagnosis_ai
```

Never commit `.env`.

## Preprocessing Pipeline

```text
406 reviewed conditions
        ↓
1_text_cleaner.ipynb
        ↓
conditions_text_cleaned.json
        ↓
2_symptom_parser.ipynb
        ↓
conditions_symptom_parsed.json
        ↓
manual_symptom_overrides.json
        ↓
2b_apply_manual_symptom_overrides.ipynb
        ↓
conditions_symptom_parsed_with_manual_overrides.json
        ↓
3_prepare_model_data.ipynb
        ↓
374 trusted model-ready conditions
        ↓
conditions_model_ready.json
```

`3_prepare_model_data.ipynb` creates:

- `symptoms_canonical` — readable source-grounded symptom representation
- `symptoms_classical` — normalized text for TF-IDF / Logistic Regression
- `symptoms_tokens` — tokens for RNN/LSTM preprocessing
- `symptoms_bert` — natural text preserved for BERT/BioBERT tokenization

### Lemmatization Decision

Lemmatization is analyzed but currently **not applied** to the main model-ready dataset:

```python
FINAL_USE_LEMMATIZATION = False
```

The decision will be revisited as a controlled model-level ablation using the same evaluation split.

## Next Step: Training-Example Generation

The next notebook will generate multiple source-grounded examples from each condition's reviewed symptom phrases.

Only existing reviewed symptoms are combined. No synthetic medical facts or invented synonyms are added.

## Planned Modeling Pipeline

```text
Training-example generation
        ↓
TF-IDF + Logistic Regression
        ↓
RNN
        ↓
LSTM
        ↓
BERT / BioBERT
        ↓
Top-K evaluation
        ↓
Model comparison
        ↓
Best model / hybrid model
        ↓
GridFS storage
        ↓
Flask prediction API
```

Planned evaluation includes:

- Top-1 accuracy
- Top-3 accuracy
- Top-5 accuracy
- precision / recall / F1 where appropriate
- emergency-condition recall
- error analysis

## Installation

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

For Jupyter notebooks in VS Code, select the same virtual environment as the notebook kernel.

## Security

- keep MongoDB credentials in `.env`
- keep `.env` in `.gitignore`
- never commit passwords or connection strings
- rotate exposed credentials
- do not disable TLS certificate verification as a workaround

## Medical Safety

This project is for education and research only. Predictions must not be presented as confirmed diagnoses. Emergency warnings should be retrieved from reviewed NHS source data rather than invented by the model.
