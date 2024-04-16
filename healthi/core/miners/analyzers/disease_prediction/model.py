import time
import secrets
import bittensor as bt
from healthi.base.protocol import HealthiProtocol
from healthi.base.utils import sign_data


class DiseasePredictor:
    """This class is responsible for completing disease prediction
    
    The DiseasePredictor class contains all of the code for a Miner neuron
    to generate the predicted label.

    Methods:
        execute:
            Executes the prediction within the predictor
    
    """

    def __init__(self, wallet: bt.wallet, subnet_version: int, wandb_handler, miner_uid: int):
        # Parameters
        self.wallet = wallet
        self.miner_hotkey = self.wallet.hotkey.ss58_address
        self.subnet_version = subnet_version
        self.miner_uid = miner_uid
        # ADD MODEL HERE
    

    def execute(self, synapse: HealthiProtocol) -> dict:
        # Responses are stored in a dict
        output = {"analyzer": "Disease Prediction", "prompt": synapse.prompt, "predicted_label": None}

        engine_confidences = []

        # Execute Model Here
        output['predicted_label'] = XXX
        

        # Add subnet version and UUID to the output
        output["subnet_version"] = self.subnet_version
        output["synapse_uuid"] = synapse.synapse_uuid
        output["nonce"] = secrets.token_hex(24)
        output["timestamp"] = str(int(time.time()))
        
        data_to_sign = f'{output["synapse_uuid"]}{output["nonce"]}{output["timestamp"]}'

        # Generate signature for the response
        output["signature"] = sign_data(self.wallet, data_to_sign)

        synapse.output = output

        return output