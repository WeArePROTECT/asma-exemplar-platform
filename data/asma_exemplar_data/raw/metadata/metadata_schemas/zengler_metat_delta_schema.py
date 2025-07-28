StructType([
    StructField('rna_extraction_kit', string, True),
    StructField('input_sample_vol', string, True),
    StructField('depth_target', string, True),
    StructField('rrna_depletion_kit', string, True),
    StructField('library_preparation_protocol', string, True),
    StructField('cdna_conversion_method', float, True),
    StructField('strand_specific', float, True),
    StructField('fragment_size', float, True),
    StructField('rRNA_content_percent', float, True),
    StructField('mapping_rate_to_db', float, True)
])