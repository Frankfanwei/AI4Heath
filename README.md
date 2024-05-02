<h1 align="center">Healthi Subnet</h1>

# Introduction
This repository contains the source code for the Healthi subnet running on top of [Bittensor](https://github.com/opentensor/bittensor). The primary focus of this subnet is using AI models for predictive diagnostics based on electronic health records data.

## Quickstart
This repository requires python3.10 or higher and Ubuntu 22.04/Debian 12. It is highly recommended to spin up a fresh Ubuntu 22.04 or Debian 12 machine for running the subnet neurons. Upgrading from python3.8 to python3.10 on Ubuntu 20.04 is known to cause issues with the installation of the python modules required by the miners.

> [!WARNING]  
> We are recommending to use python virtual environment (venv) when running either the validator or miner. Make sure the virtual environment is active prior to launching the pm2 instance.

Installation:
```
$ sudo apt update && sudo apt install jq npm python3.10-dev python3.10-venv git && sudo npm install pm2 -g && pm2 update
$ git clone (add link later)
$ cd healthi
$ python3 -m venv .venv
```


> [!NOTE]  
> During installation you might get an error "The virtual environment was not created successfully because ensurepip is not available". In this case, install the python3.11-venv (or python3.10-venv) package following the instructions on screen. After this, re-execute the `python3 -m venv .venv` command.

If you are not familiar with Bittensor, you should first perform the following activities:
- [Generate a new coldkey](https://docs.bittensor.com/getting-started/wallets#step-1-generate-a-coldkey)
- [Generate a new hotkey under your new coldkey](https://docs.bittensor.com/getting-started/wallets#step-2-generate-a-hotkey)
- [Register your new hotkey on our subnet 14](https://docs.bittensor.com/subnets/register-and-participate)

## Subnet register

Testnet:
```
btcli subnet register --netuid 133 --wallet.name {cold_wallet_name} --wallet.hotkey {hotkey_name} --subtensor.network test
```
> [!NOTE]  
> Validators need to establish an internet connection with the miner. This requires ensuring that the port specified in --axon.port is reachable on the virtual machine via the internet. This involves either opening the port on the firewall or configuring port forwarding.

Run miner (if you run multiple miners, make sure the name and axon.port are unique):
```
$ cd llm-defender-subnet
$ source .venv/bin/activate
$ bash scripts/run_neuron.sh \
--name test2-miner \
--install_only 0 \
--max_memory_restart 10G \
--branch main \
--netuid 133 \
--profile miner \
--wallet.name {coldwallet_name} \
--wallet.hotkey {hotwallet_name} \
--subtensor.network test \
--validator_min_stake 20000 \
--axon.port 1234 
```

Run validator on testnet (if you run multiple validators, make sure the name is unique):
```
$ cd healthi
$ source .venv/bin/activate
$ bash scripts/run_neuron.sh \
--name healthi_validator \
--install_only 0 \
--max_memory_restart 5G \
--netuid 133 \
--profile validator \
--wallet.name {coldwallet_name} \
--wallet.hotkey {hotwallet_name} \
--subtensor.network test
```

Run auto-updater (only one instance needs to be running even if you have multiple PM2 instances active on the same machine):
```
$ cd healthi
$ source .venv/bin/activate
$ bash scripts/run_auto_updater.sh \
--update_interval 300 \
--branch main \
--pm2_instance_names llm-defender-subnet-validator-0 llm-defender-subnet-miner-0 \
--prepare_miners True
```

# FAQ

<details>
  <summary>How does rewarding work?</summary>
  <br>
  <p>
    Miners are rewarded for accurately predicting future health conditions based on the analysis of electronic health record (EHR) sequences, and the top 20% miner will be rewarded more than others.
  </p>
</details>

<details>
  <summary>What is the expected data input and output as a miner?</summary>
  <br>
  <p>
As a miner, your input will consist of sequences from Electronic Health Records (EHR) encoded with International Statistical Classification of Diseases and Related Health Problems (ICD-10) codes.
e.g., 
The task involves predicting the likelihood of the following 14 diseases for each patient within the next year. The output should be an array or list of probabilities, ordered specifically as follows:
    <ol>
        <li>Hypertension</li>
        <li>Diabetes</li>
        <li>Asthma</li>
        <li>Chronic Obstructive Pulmonary Disease (COPD)</li>
        <li>Atrial Fibrillation</li>
        <li>Coronary Heart Disease</li>
        <li>Stroke</li>
        <li>Anxiety and Depression</li>
        <li>Dementia</li>
        <li>Myocardial Infarction</li>
        <li>Chronic Kidney Disease</li>
        <li>Thyroid Disorder</li>
        <li>Heart Failure</li>
    </ol>
    These predictions help to prioritize interventions and manage care effectively by predicting potential health risks.
  </p>
</details>

<details>
  <summary>Compute Requirements</summary>
  <br>
  <p>
  The computational requirements for participating as a miner or validator in our network are minimal. Our system does not require GPU capabilities, and it runs effectively on a virtual private server (VPS) configured with 4 virtual CPUs and 24 GB RAM. While miners are free to utilize GPU resources, the key to achieving higher rewards within our subnet lies in developing superior predictive models rather than relying on computational power.
  </p>
</details>

<details>
  <summary>Data source and how do we prevent data exploitation?</summary>
  <br>
  <p>
Our data is derived from authentic inpatient records, which are anonymized through the application of Generative Adversarial Networks (GANs). This approach preserves the integrity of the original data distributions while ensuring patient confidentiality. To prevent data exploitation and enhance security, our API continuously generates unique, synthetic EHR sequences for validators,  safeguarding against replay attacks.
  </p>
</details>

<details>
  <summary>Can I be a miner with little knowledge?</summary>
  <br>
  <p>
    Predicting on markets is very hard, but we want to help those who want to contribute to the network by providing models that can be used. These models can be used to build upon, or just run yourself to try and compete.

    You can participate by running these pre-built & pre-trained models provided to all miners [here](https://huggingface.co/Taoshi/model_v4).

    These model are already built into the core logic of `neurons/miner.py` for you to run and compete as a miner. All you need to do is run `neurons/miner.py` and specify the model you want to run as an argument through --base_model:
    --base_model model_v4_1

  </p>

</details>

<details>
  <summary>How can I fine-tune my own model.</summary>
  <br>
  <p>
  We provide fine-tuning data , miners are encouraged to use their 
  </p>
</details>

