rm hash.txt
rm tx.txt
md5sum ~/.vimrc | cut -d " " -f 1 >> hash.txt
cat hash.txt | python3 main.py >> tx.txt
print("https://explorer.bitcoin.com/bch/tx/" + $(cat tx.txt))