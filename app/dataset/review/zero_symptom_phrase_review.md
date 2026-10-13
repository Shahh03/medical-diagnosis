# Zero-phrase review

Latest symptom-parser output: 406 total conditions, 76 with zero symptom phrases.

## Classification summary

- manual_override: 60
- source_field_fix: 5
- exclude_or_keep_zero: 6
- symptom_page: 5

## Records

### Acid and chemical burns
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Arthritis
- Category: `source_field_fix`
- Next action: Fix the upstream dataset field assignment/re-extraction, then rerun preprocessing.
- Reason: The symptoms field is generic, while a concrete joint symptom list is stored in warnings. Fix the source-field classification upstream.

### Blisters
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Bow legs and knock knees in children and young people
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Bowel incontinence
- Category: `source_field_fix`
- Next action: Fix the upstream dataset field assignment/re-extraction, then rerun preprocessing.
- Reason: The symptoms field is dominated by management/advice rather than a clean presentation. Revisit the source extraction rather than forcing a regex.

### Brain stem death
- Category: `exclude_or_keep_zero`
- Next action: Keep at zero and exclude from symptom-only classifier training unless the model design later adds non-symptom inputs.
- Reason: This is a postmortem/brain-function definition, not a conventional symptom-driven diagnosis target.

### Breast pain
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Breast swelling in men
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Cardiac arrest
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Chronic obstructive pulmonary disease (COPD)
- Category: `source_field_fix`
- Next action: Fix the upstream dataset field assignment/re-extraction, then rerun preprocessing.
- Reason: The symptoms field only gives a broad breathing-difficulty statement, while the warnings field contains the detailed presentation list. Reclassify source fields upstream.

### Chronic pain
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Coma
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Cough
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Croup
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Cuts and grazes
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Dementia
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Diabetic foot issues
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Diabetic retinopathy
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Diarrhoea in adults
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Diarrhoea in children and babies
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Discoid eczema
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Diverticular disease and diverticulitis
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Dizziness (lightheadedness)
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Dry mouth
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Earache
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Epilepsy
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Excessive sweating (hyperhidrosis)
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Farting
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Fever in adults
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Fever in children
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Flat feet in children and young people
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Ganglion cyst
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Ganglion cysts in children and young people
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Headaches
- Category: `symptom_page`
- Next action: Decide at training-set design time whether symptom-page labels should be included; do not force them through the disease parser now.
- Reason: This NHS page is itself a symptom label; including it can make evaluation trivial because the input symptom and class label are nearly identical.

### Heart failure
- Category: `source_field_fix`
- Next action: Fix the upstream dataset field assignment/re-extraction, then rerun preprocessing.
- Reason: The symptoms field only says there is a range of symptoms; the concrete breathlessness/cough/fatigue/swelling list is in warnings.

### Heart palpitations
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### High blood pressure (hypertension)
- Category: `exclude_or_keep_zero`
- Next action: Keep at zero and exclude from symptom-only classifier training unless the model design later adds non-symptom inputs.
- Reason: The page explicitly says high blood pressure often has no symptoms; severe-warning symptoms should not be treated as the ordinary presentation.

### Impetigo
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Intoeing (pigeon toe) in children and young people
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Itchy bottom
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Jellyfish and sea creature stings
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Kidney cancer
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Leg cramps
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Limb girdle muscular dystrophy
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Mouth ulcer
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Muscular dystrophy
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Neuroendocrine tumours
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Nipple discharge
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Nipple inversion (inside out nipple)
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Nosebleed
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Obesity
- Category: `exclude_or_keep_zero`
- Next action: Keep at zero and exclude from symptom-only classifier training unless the model design later adds non-symptom inputs.
- Reason: This condition is primarily identified by body composition/BMI rather than a symptom phrase from this source text.

### Pain in the ball of the foot
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Phobias
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Plantar heel pain
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Pleurisy
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Pneumonia
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Popliteal cysts in children and young people
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Positional talipes in children and young people
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Psoriasis
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Recurrent miscarriage
- Category: `exclude_or_keep_zero`
- Next action: Keep at zero and exclude from symptom-only classifier training unless the model design later adds non-symptom inputs.
- Reason: The condition is defined by pregnancy history rather than a current symptom presentation.

### Scabies
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Severe head injury
- Category: `source_field_fix`
- Next action: Fix the upstream dataset field assignment/re-extraction, then rerun preprocessing.
- Reason: The symptoms field is generic; the concrete neurological/red-flag presentation is in warnings.

### Shortness of breath
- Category: `symptom_page`
- Next action: Decide at training-set design time whether symptom-page labels should be included; do not force them through the disease parser now.
- Reason: This NHS page is itself a symptom label; decide separately whether symptom-page labels belong in the disease classifier.

### Sore throat
- Category: `symptom_page`
- Next action: Decide at training-set design time whether symptom-page labels should be included; do not force them through the disease parser now.
- Reason: This NHS page is itself a symptom label; decide separately whether symptom-page labels belong in the disease classifier.

### Stillbirth
- Category: `exclude_or_keep_zero`
- Next action: Keep at zero and exclude from symptom-only classifier training unless the model design later adds non-symptom inputs.
- Reason: This is an outcome/event definition rather than a symptom-driven condition label.

### Stomach ache and abdominal pain
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Sudden arrhythmic death syndrome (SADS)
- Category: `exclude_or_keep_zero`
- Next action: Keep at zero and exclude from symptom-only classifier training unless the model design later adds non-symptom inputs.
- Reason: This is a sudden-death/postmortem diagnosis and is not suitable for a symptom-only classifier.

### Swollen glands
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Thirst
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Toe walking in children and young people
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Toothache
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Urinary incontinence
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Vomiting in adults
- Category: `symptom_page`
- Next action: Decide at training-set design time whether symptom-page labels should be included; do not force them through the disease parser now.
- Reason: This NHS page is itself a symptom/presentation label; decide separately whether symptom-page labels belong in the disease classifier.

### Vomiting in children and babies
- Category: `symptom_page`
- Next action: Decide at training-set design time whether symptom-page labels should be included; do not force them through the disease parser now.
- Reason: This NHS page is itself a symptom/presentation label; decide separately whether symptom-page labels belong in the disease classifier.

### Warts and verrucas
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.

### Whooping cough
- Category: `manual_override`
- Next action: Add a curated manual symptom override using only phrases supported by the symptoms field.
- Reason: Clear condition-specific manifestations are present in the symptoms field, but the generic parser missed them. Add a source-grounded condition-specific override instead of widening global regex rules.
