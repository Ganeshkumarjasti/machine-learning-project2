from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact",
["tarin_file_path","test_file_path","is_ingested", "message"])