CC=g++
CFLAGS=-Wall -std=c++11

all: kamasutra

kamasutra: kamasutra.cpp
	$(CC) $(CFLAGS) -o kamasutra kamasutra.cpp

encryption: kamasutra
	./kamasutra -e keyfile.txt plaintext.txt ciphertext.txt

decryption: kamasutra
	./kamasutra -d keyfile.txt plaintext.txt ciphertext.txt

key:
	./kamasutra -k keyfile.txt

run: kamasutra
	./kamasutra

clean:
	rm -f kamasutra keyfile.txt
