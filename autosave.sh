rm hash.txt
rm tx.txt
sha256sum ~/.vimrc | cut -d " " -f 1 >> hash.txt
cat hash.txt | python3 main.py >> tx.txt
echo "https://explorer.bitcoin.com/bch/tx/$(cat tx.txt))"

