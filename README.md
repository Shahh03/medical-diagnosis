# Medical Diagnosis AI

AI-powered medical diagnosis project that uses medical condition data from **NHS Inform**, stores the structured dataset in **MongoDB Atlas**, and will later use NLP and deep learning models to predict probable medical conditions from free-text symptoms.

## Project Objective

The final system is intended to:

- collect medical condition data from NHS Inform
- store structured condition data in MongoDB
- preprocess and normalize medical text
- train baseline, RNN, LSTM, and Transformer-based models
- predict probable conditions from free-text symptoms and user metadata
- rank predicted conditions by probability
- return warnings and recommendations for predicted conditions
- expose the workflow through Flask APIs
- store trained model files in MongoDB GridFS

## Current Progress

### Completed

- [x] Created the project structure
- [x] Configured environment variables with `.env`
- [x] Connected the project to MongoDB Atlas
- [x] Built the NHS Inform A-Z page collector
- [x] Collected NHS Inform condition pages
- [x] Extracted the required medical fields
- [x] Manually reviewed and cleaned the extracted dataset
- [x] Removed unsuitable hub, overview, support, and non-condition pages
- [x] Validated the final dataset
- [x] Imported the final dataset into MongoDB Atlas
- [x] Added a unique index for condition names
- [x] Verified the data in MongoDB Atlas Data Explorer

## Current Dataset

The final MongoDB `conditions` collection contains **406 documents**.

Each document follows this schema:

```json
{
  "condition": "Condition name",
  "symptoms": "List or description of symptoms",
  "causes": "Causes, triggers, or risk factors",
  "warnings": "Emergency or escalation advice",
  "recommendations": "Treatment, management, or self-care advice"
}
```

`condition` and `symptoms` are required for retained records.

`causes`, `warnings`, and `recommendations` may be empty when the NHS source does not provide reliable information for that field.

## MongoDB

Database:

```text
medical_diagnosis_ai
```

Collection:

```text
conditions
```

Current document count:

```text
406
```

The `condition` field has a unique index to prevent duplicate condition records.

## Project Structure

```text
medical-diagnosis/
│
├── app/
│   ├── api/
│   │
│   ├── database/
│   │   ├── mongodb.py
│   │   └── import_conditions.py
│   │
│   └── dataset/
│       └── nhs_conditions_manual_final.json
│
├── data/
│   └── raw/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Data Acquisition

The source is the NHS Inform A-Z conditions section:

```text
https://www.nhsinform.scot/illnesses-and-conditions/a-to-z/
```

Current acquisition pipeline:

```text
NHS Inform A-Z
      ↓
Discover condition pages
      ↓
Collect page content
      ↓
Extract required medical fields
      ↓
Manual semantic review and cleanup
      ↓
Final 406-condition dataset
      ↓
MongoDB Atlas
```

The extracted fields are:

- `condition`
- `symptoms`
- `causes`
- `warnings`
- `recommendations`

Missing optional medical information is left empty rather than invented.

## MongoDB Connection

Create a `.env` file in the project root:

```env
MONGODB_URI=mongodb+srv://YOUR_USERNAME:YOUR_PASSWORD@YOUR_CLUSTER.mongodb.net/
MONGODB_DB=medical_diagnosis_ai
```

Do not commit `.env` to Git.

Test the connection:

```powershell
python -m app.database.mongodb
```

Expected output:

```text
MongoDB connection successful
Database: medical_diagnosis_ai
```

## Importing Conditions

The importer is:

```text
app/database/import_conditions.py
```

It:

1. loads the final JSON dataset
2. validates the expected schema
3. checks required fields
4. checks duplicate condition names
5. creates a unique index on `condition`
6. inserts or updates records using MongoDB upserts

Run:

```powershell
python -m app.database.import_conditions
```

Current successful result:

```text
Loaded 406 conditions
Dataset validation passed

Import complete
----------------
Dataset: 406
MongoDB total: 406
```

Because the importer uses upserts, rerunning it updates existing conditions instead of creating duplicates.

## Next Step

The next stage is **Data Preprocessing**.

According to the project specification, this stage will:

- clean the medical text
- tokenize text
- normalize symptoms and useful medical phrases
- prepare model-ready symptom input
- preserve the original MongoDB condition records
- prepare data for the baseline TF-IDF + Logistic Regression classifier

The planned modeling pipeline is:

```text
TF-IDF + Logistic Regression
            ↓
           RNN
            ↓
          LSTM
            ↓
    BERT / BioBERT
            ↓
Model comparison
            ↓
Top-K probability ranking
```

## Remaining Project Components

- Preprocessing API using Flask
- baseline TF-IDF + Logistic Regression model
- RNN model
- LSTM model
- Transformer model using BERT or BioBERT
- model comparison
- Top-K accuracy evaluation
- emergency recall evaluation
- probability ranking
- Flask prediction/model API
- MongoDB `models` collection
- GridFS model storage
- experimentation and evaluation report
- final architecture and model documentation

## Security

- keep MongoDB credentials in `.env`
- keep `.env` in `.gitignore`
- never commit passwords or connection credentials
- rotate credentials immediately if they are exposed
