INSTRUCTIONS.md

1. installer libcoap 

Sur mac/osx : `brew install libcoap`

Sur linux (par ex. sur la debian raspberry pi) :

````
sudo apt-get install build-essential autoconf automake libtool
git clone --recursive https://github.com/obgm/libcoap.git
cd libcoap
git checkout dtls
git submodule update --init --recursive
./autogen.sh
./configure --disable-documentation --disable-shared
make
sudo make install
````

2. Installer les dépendances:

`pip install requirements.txt` 





