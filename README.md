Miner needs update:
1. healthi.base.protocol line44–45 (analyzer)
2. healthi.core.miners.analyzers.disease_prediction.model
3. healthi.core.miners.miner.py line 317—337 (analyzer exute), line 339, 359 (subnet id blacklist)

Validator needs update:
1. healthi.core.validators.validator.py
    1. def process_responses  line 174,  process responses (get, validate, calculate score, etc)
    2. def get_api_prompt (from API get data here) and get local data
    3. _get_remote_miner_blacklist (not sure)
    4. serve_prompt? which one use it?
2. healthi.neurons.validator.py 
    1. (HealthiProtocol) Line 99,  
    2. validator.serve_prompt line 78
3. healthi.core.validator   scoring and penalty


