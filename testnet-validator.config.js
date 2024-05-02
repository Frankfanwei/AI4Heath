module.exports = {
    apps: [
        {
            "name"                  : "testnet-validator",
            "script"                : "/home/ubuntu/healthi-subnet/healthi/neurons/validator.py",
            "interpreter"           : "/bin/python",
            "args"                  : "--netuid 133 --wallet.name testnet-validator --wallet.hotkey default --subtensor.network test --logging.debug",
            "max_memory_restart"    : "5G"
        }
    ]
}
