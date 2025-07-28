# Unified Metadata Dictionary for ASMA Metadata Files

### `conrad_lab_metadata` Metadata Schema
| Column Name | Type |
|-------------|------|
| sample_id | STRING |
| subject_id | STRING |
| cup_weight_g | STRING |
| patient_status | STRING |
| collection_method | STRING |
| sputum_collection_date | STRING |
| day_of_sputm | STRING |
| fzfshfz_frozenfresh_frozenhome | STRING |
| diagnosis | STRING |
| date_of_gram_stain_culture | STRING |
| day_of_gram_stain_culture | STRING |
| type_of_specimen | STRING |
| staphylococcus_aureus | STRING |
| type_of_staphylococcus | STRING |
| pseudomonas_aeruginosa | STRING |
| pseudomonas_aeruginosa_mucoid | STRING |
| burkholderia_species | STRING |
| alcaligenes_achromobacter_xylosoxidans | STRING |
| stenotrophomonas_xanthomonasmaltophilia | STRING |
| escherichia_coli | STRING |
| streptococcus_pneumoniae | STRING |
| streptococcus_agalactiae | STRING |
| other_microorganisms | STRING |
| aspergillus_any_species | STRING |
| candida_any_species | STRING |
| yeast_not_cryptococcus_species | STRING |
| other_bacterial_or | STRING |
| date_of_AFB_culture | STRING |
| day_of_AFB_culture | STRING |
| type_of_specimen_2 | STRING |
| myco_abscessus | STRING |
| myco_aviumintracellulare | STRING |
| other_mycobacteria_species | STRING |
| date_of_pex | STRING |
| day_of_pex_assessment | STRING |
| assessment_of_pulmonary | STRING |
| date_of_medication | STRING |
| day_of_medication_review | STRING |
| antibiotic_status | STRING |
| inhaled_tobramycin_tobi | STRING |
| inhaled_aztreonam_cayston | STRING |
| inhaled_amikacin_arikayce | STRING |
| azithromycin_oral | STRING |
| sulfamethoxazoletrimethoprim_oral_bactrim | STRING |
| ciprooral | STRING |
| levaquinoral | STRING |
| augmentinoral | STRING |
| ethambutoloral | STRING |
| rifabutinoral | STRING |
| clofazimine_oral | STRING |
| other_abxoral | STRING |
| amikaciniv | STRING |
| azithromycin_iv | STRING |
| ceftazidimeiv | STRING |
| clindamyciniv | STRING |
| colistiniv | STRING |
| doxycycline_iv | STRING |
| levofloxacin_iv | STRING |
| linezolidiv | STRING |
| meropenem_iv | STRING |
| piperacillintazobactam__iv | STRING |
| sulfamethoxazole_and_trimethoprim | STRING |
| tigecyclineiv | STRING |
| tobramyciniv | STRING |
| vancomyciniv | STRING |
| zosyniv | STRING |
| other_abxiv | STRING |
| cftr_modulator_status | STRING |
| rhdnase_pulmozyme_dornase | STRING |
| inhhs_hypertonic_saline | STRING |
| airway_clearance | STRING |
| lung_function_date_ucsd_only | STRING |
| lung_function_day | STRING |
| lung_function_age_years | STRING |
| ht_cm | STRING |
| weight_kg | STRING |
| sex_at_birth | STRING |
| race | STRING |
| ethnicity | STRING |
| fev1_l | STRING |
| fev1_pp | STRING |
| fvc_l | STRING |
| fvc_pp | STRING |

### `zengler_additional_core` Metadata Schema
| Column Name | Type |
|-------------|------|
| sample_id | STRING |
| subject_id | FLOAT |
| sample_type | STRING |
| collection_site | STRING |
| collection_method | STRING |
| collection_date | FLOAT |
| storage_conditions | FLOAT |
| project_id | FLOAT |
| sequencing_platform | STRING |
| read_length | STRING |
| adapter_sequence | FLOAT |
| rRNA_depletion_protocol | FLOAT |
| host_depletion_method | FLOAT |
| submitted_by | STRING |
| processing_protocol | FLOAT |
| file_type | STRING |
| data_type | STRING |

### `zengler_metag` Metadata Schema
| Column Name | Type |
|-------------|------|
| dna_extraction_kit | STRING |
| input_sample_vol | STRING |
| depth_target | STRING |
| library_preparation_procotol | STRING |
| human_read_removal_tool | FLOAT |
| human_read_removal_tool_link | FLOAT |

### `zengler_metars` Metadata Schema
| Column Name | Type |
|-------------|------|
| rrna_depletion_protocol | STRING |
| library_preparation_protocol | STRING |
| depth_target | STRING |

### `zengler_metat` Metadata Schema
| Column Name | Type |
|-------------|------|
| rna_extraction_kit | STRING |
| input_sample_vol | STRING |
| depth_target | STRING |
| rrna_depletion_kit | STRING |
| library_preparation_protocol | STRING |
| cdna_conversion_method | FLOAT |
| strand_specific | FLOAT |
| fragment_size | FLOAT |
| rRNA_content_percent | FLOAT |
| mapping_rate_to_db | FLOAT |

### `zengler_sra` Metadata Schema
| Column Name | Type |
|-------------|------|
| sample_name | STRING |
| library_ID | STRING |
| library_number | STRING |
| omics_type | STRING |
| title | STRING |
| library_strategy | STRING |
| library_source | STRING |
| library_selection | STRING |
| library_layout | STRING |
| platform | STRING |
| instrument_model | STRING |
| design_description | STRING |
| protocols_io_id | STRING |
| filetype | STRING |
| filename | STRING |
| filename2 | STRING |