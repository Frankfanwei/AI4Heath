<h1 align="center">Healthi Subnet</h1>

<p align="center">
  <a href="">Website</a>
  ·
  <a href="">Twitter</a>
    ·
  <a href="https://huggingface.co/Healthi">HuggingFace</a>
    .
  <a href="#FAQ">FAQ</a>

  ·  
</p>

# Introduction
This repository contains the source code for the Healthi subnet running on top of [Bittensor](https://github.com/opentensor/bittensor). The primary objective of this subnet is to leverage AI models for predictive diagnostics using electronic health records (EHRs).

In the rapidly evolving healthcare technology sector, the integration of Artificial Intelligence (AI) is revolutionizing preventive medicine, particularly through predictive diagnostics. The growing availability of patient data, especially EHRs, offers a substantial opportunity to harness AI for predicting health outcomes. This subnet on the Bittensor network incentivizes miners based on the performance of their AI models in clinical prediction tasks assigned by the subnet validators, such as disease forecasting using EHRs. This network aims to employ these high-performing AI models developed by miners to improve patient outcomes, enhance healthcare delivery, and foster personalized clinical risk management.

# Quickstart
This repository requires Python 3.10 or higher and Ubuntu 22.04/Debian 12.

Installation (skip the first line if bittensor is already installed):
```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/opentensor/bittensor/master/scripts/install.sh)"
$ sudo apt update && sudo apt install jq npm python3.10-dev python3.10-venv git && sudo npm install pm2 -g && pm2 update
$ git clone https://github.com/Healthi-Labs/healthi-subnet.git
$ cd healthi-subnet
$ python3 -m venv .venv
```

If you are not familiar with Bittensor, you should first perform the following activities:
- [Generate a new coldkey](https://docs.bittensor.com/getting-started/wallets#step-1-generate-a-coldkey)
- [Generate a new hotkey under your new coldkey](https://docs.bittensor.com/getting-started/wallets#step-2-generate-a-hotkey)
- [Register your new hotkey on our subnet](https://docs.bittensor.com/subnets/register-and-participate)

# Subnet register

Testnet:
```
btcli subnet register --netuid 133 --wallet.name {cold_wallet_name} --wallet.hotkey {hot_wallet_name} --subtensor.network test
```
> [!NOTE]  
> Validators need to establish an internet connection with the miner. This requires ensuring that the port specified in --axon.port is reachable on the virtual machine via the internet. This involves either opening the port on the firewall or configuring port forwarding.

Run miner (if you run multiple miners, make sure the name and axon.port are unique):
```
$ cd healthi-subnet
$ source .venv/bin/activate
$ bash scripts/run_neuron.sh \
--name healthi_miner \
--install_only 0 \
--max_memory_restart 10G \
--branch main \
--netuid 133 \
--profile miner \
--wallet.name {cold_wallet_name} \
--wallet.hotkey {hot_wallet_name} \
--subtensor.network test \
--validator_min_stake 20000 \
--axon.port 12345 
```

Run validator on testnet (if you run multiple validators, make sure the name is unique):
```
$ cd healthi-subnet
$ source .venv/bin/activate
$ bash scripts/run_neuron.sh \
--name healthi_validator \
--install_only 0 \
--max_memory_restart 5G \
--netuid 133 \
--profile validator \
--wallet.name {cold_wallet_name} \
--wallet.hotkey {hot_wallet_name} \
--subtensor.network test
```

Auto-updater: We only recommend validators to run the auto-updater code as this might overwrite the codes modified by miners:
```
$ cd healthi-subnet
$ source .venv/bin/activate
$ bash scripts/run_auto_updater.sh \
--update_interval 300 \
--branch main \
--pm2_instance_names healthi_validator \
--prepare_miners False
```

<h1 id="FAQ">FAQ</h1>

<details>
  <summary>How does rewarding work?</summary>
  <br>
  <p>
    Miners are rewarded for their accurate predictions of future health conditions based on electronic health record (EHR) sequences analysis. The top 20% of miners receive significantly higher rewards than others.
  </p>
</details>

<details>
  <summary>What is the expected data input and output as a miner?</summary>
  <br>
  <p>
    As a miner, your input will consist of sequences of Electronic Health Records (EHR) encoded with International Statistical Classification of Diseases and Related Health Problems (ICD-10) codes. In the following example, the patient visited the hospital twice, receiving two diagnoses each time:
    <br><br>
    <strong>Example Input:</strong>
    <pre>
[['D693', 'I10'], ['Z966', 'A047']]
    </pre>
    Our current disease prediction task involves predicting the likelihood of the following 14 diseases within the next year. Outputs should be an array or list of probabilities in the order listed below:
    <ol>
      <li>Hypertension</li>
      <li>Diabetes</li>
      <li>Asthma</li>
      <li>Chronic Obstructive Pulmonary Disease</li>
      <li>Atrial Fibrillation</li>
      <li>Coronary Heart Disease</li>
      <li>Stroke</li>
      <li>Anxiety and Depression</li>
      <li>Dementia</li>
      <li>Myocardial Infarction</li>
      <li>Chronic Kidney Disease</li>
      <li>Thyroid Disorder</li>
      <li>Heart Failure</li>
      <li>Cancer</li>
    </ol>
    <strong>Example Output:</strong>
    <pre>
[0.0027342219837009907, 0.012263162061572075, 0.01795087940990925, 0.016055596992373466, 0.010267915204167366, 0.0002267731324536726, 0.02317667566239834, 0.39082783460617065, 0.017462262883782387, 0.033581722527742386, 0.014757075347006321, 0.03425902500748634, 0.015123098157346249, 0.028889883309602737]
    </pre>
  </p>
</details>

<details>
  <summary>Compute Requirements</summary>
  <br>
  <p>
  The computational requirements for participating as a miner or validator in our network are minimal. Our system does not require GPU capabilities, and it runs effectively on a virtual private server (VPS) configured with 4 virtual CPUs and 24 GB RAM. While miners are free to utilize GPU resources, the key to achieving higher rewards within our subnet lies in developing superior predictive models rather than having more computational power.
  </p>
</details>

<details>
  <summary>Data source and how do we prevent data exploitation?</summary>
  <br>
  <p>
Our data originates from authentic inpatient records, which are anonymized using Generative Adversarial Networks (GANs) to preserve the original data distributions while ensuring patient confidentiality. To prevent data exploitation and enhance security, our API continuously generates unique, synthetic EHR sequences for validators, protecting against replay attacks.
  </p>
</details>

<details>
  <summary>How can I fine-tune my model?</summary>
  <br>
  <p>
    Fine-tuning data is provided at https://github.com/Healthi-Labs/healthi-subnet/blob/main/healthi/base/data/trainset.parquet. We also encourage miners to obtain EHR data from their own sources for fine-tuning.
  </p>
</details>


