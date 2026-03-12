from dataclasses import dataclass

@dataclass
class Config:
    default_results_dir: str = "test-results"

config = Config()
