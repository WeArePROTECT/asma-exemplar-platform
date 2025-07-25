
# ASMA Project - Conrad Lab Metadata Template

This repository contains the standardized **metadata template** for Conrad Lab contributions to the **ASMA** (Airway Synthetic Microbial Atlas) project.

The file [`conrad_lab_metadata_template.csv`](./conrad_lab_metadata_template.csv) captures metadata fields specific to Conrad Lab sample and protocol descriptions, supporting consistent intake into the ASMA platform.

This metadata supports:
- Internal ASMA platform integration
- Downstream reproducibility and documentation
- Harmonization of metadata across contributing labs

---

## 📁 File Overview

- **Filename**: `conrad_lab_metadata_template.csv`
- **Each row = one sample or data processing instance**
- Structured to support per-sample metadata entries
- Designed to complement metadata from other ASMA contributors (e.g., Zengler Lab)

---

## 🧬 Metadata Field Dictionary

| Column Name | Description | Example Value |
|-------------|-------------|----------------|
| `sample_id` | Unique identifier assigned to each biospecimen sample. |  |
| `subject_id` | Unique code assigned to each human subject in the study. |  |
| `cup_weight_g` | Weight of the collection cup in grams used during sputum sampling. |  |
| `patient_status` | Clinical status of the patient at time of sampling (e.g., Untreated, On-treatment). |  |
| `collection_method` | Method used to collect the sputum sample (e.g., spontaneous, saline induction). |  |
| `sputum_collection_date` | Date the sputum sample was collected from the subject. |  |
| `day_of_sputm` | Relative day from baseline (D0) when sputum was collected. |  |
| `fzfshfz_frozenfresh_frozenhome` | Sample condition at collection: Fresh, Frozen, or Frozen at home. |  |
| `diagnosis` | Clinical diagnosis of the subject (e.g., CF, NCFB). |  |
| `date_of_gram_stain_culture` | Date associated with a clinical procedure or review, in YYYY-MM-DD format. |  |
| `day_of_gram_stain_culture` | Relative number of days from initial baseline sampling (D0). |  |
| `type_of_specimen` | Type of respiratory specimen collected (e.g., throat swab, expectorated sputum). |  |
| `staphylococcus_aureus` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `type_of_staphylococcus` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `pseudomonas_aeruginosa` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `pseudomonas_aeruginosa_mucoid` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `burkholderia_species` | Presence or absence of Burkholderia species. |  |
| `alcaligenes_achromobacter_xylosoxidans` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `stenotrophomonas_xanthomonasmaltophilia` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `escherichia_coli` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `streptococcus_pneumoniae` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `streptococcus_agalactiae` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `other_microorganisms` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `aspergillus_any_species` | Detection of any Aspergillus species in culture. |  |
| `candida_any_species` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `yeast_not_cryptococcus_species` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `other_bacterial_or` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `date_of_AFB_culture` | Date associated with a clinical procedure or review, in YYYY-MM-DD format. |  |
| `day_of_AFB_culture` | Relative number of days from initial baseline sampling (D0). |  |
| `type_of_specimen_2` | Type of respiratory specimen collected (e.g., throat swab, expectorated sputum). |  |
| `myco_abscessus` | Presence or identification of Mycobacterium species from culture. |  |
| `myco_aviumintracellulare` | Presence or identification of Mycobacterium species from culture. |  |
| `other_mycobacteria_species` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `date_of_pex` | Date associated with a clinical procedure or review, in YYYY-MM-DD format. |  |
| `day_of_pex_assessment` | Relative number of days from initial baseline sampling (D0). |  |
| `assessment_of_pulmonary` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `date_of_medication` | Date associated with a clinical procedure or review, in YYYY-MM-DD format. |  |
| `day_of_medication_review` | Relative number of days from initial baseline sampling (D0). |  |
| `antibiotic_status` | Summary of antibiotic exposure status (e.g., yes, no, unknown). |  |
| `inhaled_tobramycin_tobi` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `inhaled_aztreonam_cayston` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `inhaled_amikacin_arikayce` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `azithromycin_oral` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `sulfamethoxazoletrimethoprim_oral_bactrim` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `ciprooral` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `levaquinoral` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `augmentinoral` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `ethambutoloral` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `rifabutinoral` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `clofazimine_oral` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `other_abxoral` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `amikaciniv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `azithromycin_iv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `ceftazidimeiv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `clindamyciniv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `colistiniv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `doxycycline_iv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `levofloxacin_iv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `linezolidiv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `meropenem_iv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `piperacillintazobactam__iv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `sulfamethoxazole_and_trimethoprim` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `tigecyclineiv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `tobramyciniv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `vancomyciniv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `zosyniv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `other_abxiv` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `cftr_modulator_status` | Status of subject's CFTR modulator therapy at time of sampling. |  |
| `rhdnase_pulmozyme_dornase` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `inhhs_hypertonic_saline` | Use of inhaled hypertonic saline treatment. |  |
| `airway_clearance` | Use of techniques to clear mucus from the airways. |  |
| `lung_function_date_ucsd_only` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `lung_function_day` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `lung_function_age_years` | Clinical or laboratory-related variable; see study documentation for details. |  |
| `ht_cm` | Height of subject in centimeters. |  |
| `weight_kg` | Weight of subject in kilograms. |  |
| `sex_at_birth` | Sex assigned at birth. |  |
| `race` | Race of subject as self-reported. |  |
| `ethnicity` | Ethnicity of subject as self-reported. |  |
| `fev1_l` | Forced Expiratory Volume in 1 second, a key lung function metric. |  |
| `fev1_pp` | Forced Expiratory Volume in 1 second, a key lung function metric. |  |
| `fvc_l` | Forced Vital Capacity, used in pulmonary function tests. |  |
| `fvc_pp` | Forced Vital Capacity, used in pulmonary function tests. |  |

---

## 🛠️ Notes

- This template is **specific to Conrad Lab** metadata and should align with ASMA-wide metadata standards.
- If values are shared across multiple samples (e.g., same library prep protocol), consider recording them once and referencing via a `protocol_id`.
- Consistent use of controlled vocabulary (e.g., for `sample_type` or `data_type`) is encouraged.

---

## 🔗 Related Resources

- [ASMA Project Overview (UCB internal)](https://your.internal.link)
- [Protocols.io](https://www.protocols.io/)

---

## 📤 Contributions

This metadata format was developed by the ASMA Data Integration Team in collaboration with the Conrad Lab.  
Please contact the ASMA metadata team for suggestions, revisions, or questions.
