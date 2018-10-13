# save_file_hash
This repository is a sample code to save hash value of a file to blockchain.

## Install latest bitcash library

`bitcash` is a library to make bch transaction by python.
You can install it by pip, but the version is old now.
So you have to download and install from github repository.

```bash
git clone https://github.com/sporestack/bitcash.git
cd bitcash
sudo python3 setup.py install
```

## Clone this repository
```bash
git clone https://github.com/TonyMooori/save_file_hash.git
cd save_file_hash
```

## Make bch wallet, and send some money
Next, we have to make a bch wallet for making transaction.
Execute main.py.

```bash
python3 main.py
>Making and saving new wallet...
>Send some money to bitcoincash:qzuagk4vvp8hmfzrwcgd9fmnuwvce6p6kv704adgav
```

Private key of this wallet is saved in `private.secret`.
Send some money to displayed wallet.
If there is no money, you cannot make transaction.
But it doesn't take so much money(about 0.2 cent/transaction).
About 10 cent is enough to demonstrate.

## Edit autosave.xsh
`autosave.xsh` is a script that acquires the hash value of the file and save it in the transaction.
If you prefer bash, you should write shell script.
This is a sample to save the hash value of `.vimrc`.

```xonsh
rm hash.txt
rm tx.txt
md5sum ~/.vimrc | cut -d " " -f 1 >> hash.txt
cat hash.txt | python3 main.py >> tx.txt
print("https://explorer.bitcoin.com/bch/tx/" + $(cat tx.txt))
```

`main.py` is a program that saves the input string in the transaction and display the transaction id.

## Execute autosave.xsh
Then execute `autosave.xsh`.

```bash
>xonsh autosave.xsh
https://explorer.bitcoin.com/bch/tx/ed1787e799e5fcb20eaeb891d060ec63e01a117a98f41e0c19d5776e9ee5c046
```

You can find the hash value on the blockchain!
If you want to save regularly, add job to crontab.
