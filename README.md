<h1 align="center">Healthi Subnet</h1>

# Introduction
This repository contains the source code for the Healthi subnet running on top of [Bittensor](https://github.com/opentensor/bittensor). The primary focus of this subnet is using AI models for predictive diagnostics based on electronic health records data.

## Quickstart
This repository requires python3.10 or higher and Ubuntu 22.04/Debian 12. It is highly recommended to spin up a fresh Ubuntu 22.04 or Debian 12 machine for running the subnet neurons. Upgrading from python3.8 to python3.10 on Ubuntu 20.04 is known to cause issues with the installation of the python modules required by the miners.

> [!WARNING]  
> We are recommending to use python virtual environment (venv) when running either the validator or miner. Make sure the virtual environment is active prior to launching the pm2 instance.

Installation:
```
$ sudo apt update && sudo apt install jq npm python3.10-venv git && sudo npm install pm2 -g && pm2 update
$ git clone (add link later)
$ cd healthi
$ python3 -m venv .venv
```

```
Data Source and Privacy:

Authenticity and Privacy: We base our models on real inpatient data, enriched and anonymized through Generative Adversarial Networks (GANs). This preserves the integrity of data distributions while ensuring patient confidentiality.
API for Enhanced Data Utility:

Dynamic Data Handling: Our API generates and distributes unique, synthetic EHR sequences to validators, enhancing security and preventing replay attacks.
```
> [!NOTE]  
> During installation you might get an error "The virtual environment was not created successfully because ensurepip is not available". In this case, install the python3.11-venv (or python3.10-venv) package following the instructions on screen. After this, re-execute the `python3 -m venv .venv` command.

If you are not familiar with Bittensor, you should first perform the following activities:
- [Generate a new coldkey](https://docs.bittensor.com/getting-started/wallets#step-1-generate-a-coldkey)
- [Generate a new hotkey under your new coldkey](https://docs.bittensor.com/getting-started/wallets#step-2-generate-a-hotkey)
- [Register your new hotkey on our subnet 14](https://docs.bittensor.com/subnets/register-and-participate)

> [!NOTE]  
> Validators need to establish an internet connection with the miner. This requires ensuring that the port specified in --axon.port is reachable on the virtual machine via the internet. This involves either opening the port on the firewall or configuring port forwarding.

Run miner (if you run multiple miners, make sure the name and axon.port are unique):
```
$ cd llm-defender-subnet
$ source .venv/bin/activate
$ bash scripts/run_neuron.sh \
--name llm-defender-subnet-miner-0 \
--install_only 0 \
--max_memory_restart 10G \
--branch main \
--netuid 14 \
--profile miner \
--wallet.name YourColdkeyGoesHere \
--wallet.hotkey YourHotkeyGoesHere \
--axon.port 15000 \
```

Run validator (if you run multiple validators, make sure the name is unique):
```
$ cd llm-defender-subnet
$ source .venv/bin/activate
$ bash scripts/run_neuron.sh \
--name llm-defender-subnet-validator-0 \
--install_only 0 \
--max_memory_restart 5G \
--branch main \
--netuid 14 \
--profile validator \
--wallet.name YourColdkeyGoesHere \
--wallet.hotkey YourHotkeyGoesHere
```

Run auto-updater (only one instance needs to be running even if you have multiple PM2 instances active on the same machine):
```
$ cd llm-defender-subnet
$ source .venv/bin/activate
$ bash scripts/run_auto_updater.sh \
--update_interval 300 \
--branch main \
--pm2_instance_names llm-defender-subnet-validator-0 llm-defender-subnet-miner-0 \
--prepare_miners True
```
