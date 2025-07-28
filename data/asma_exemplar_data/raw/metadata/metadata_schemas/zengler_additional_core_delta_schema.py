StructType([
    StructField('sample_id', string, True),
    StructField('subject_id', float, True),
    StructField('sample_type', string, True),
    StructField('collection_site', string, True),
    StructField('collection_method', string, True),
    StructField('collection_date', float, True),
    StructField('storage_conditions', float, True),
    StructField('project_id', float, True),
    StructField('sequencing_platform', string, True),
    StructField('read_length', string, True),
    StructField('adapter_sequence', float, True),
    StructField('rRNA_depletion_protocol', float, True),
    StructField('host_depletion_method', float, True),
    StructField('submitted_by', string, True),
    StructField('processing_protocol', float, True),
    StructField('file_type', string, True),
    StructField('data_type', string, True)
])