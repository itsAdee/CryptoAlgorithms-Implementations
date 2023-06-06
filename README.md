# CryptoAnalysisTasks
Creating basic substitution based cypher algorithms
## Task One: Cryptanalysis (2 marks)
There are two ciphertext files provided. These files are Ctext-1 and Ctext-2. They have been generated using a monoalphabetic cipher and a Vigenère cipher respectively.
You need to:
 Apply cryptanalysis to each of Ctext-1 & Ctext-2.
Present a report describing what steps you took to break each cipher, and why. Justify choices you have made.
 Include graphs (frequency distributions) as appropriate (in Report1.pdf).
 Provide plaintext and key for each cipher. You should include them as files Ptext-1.txt, Key-1.txt, Ptext-2.txt, and Key-2.txt, and give them in your report (Report1.pdf)
 Cite the tools or software used in your report.
 If you only provide final answer but without any proper analysis, then you will obtain 0.
## Task Two: Substitution Cipher (2 marks)
A substitution cipher by a keyword works as follows. If a keyword is “STRAWBERRY”, we remove the repeating characters in it to get “STAWBEY”. Then, we append the rest of the alphabet characters in reverse order (from ‘Z’ to ‘A’) to the keyword to construct a key i.e., “STAWBEYZXVURQPONMLKJIHGFDC” to form a complete substitution key. Finally, we encrypt a message by substituting its characters in the key as follows:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓

S T A W B E Y Z X V U R Q P O N M L K J I H G F D C
Your task is to implement the substitution cipher. In particular, your program should
be a command-line program;
take a keyword, which is typed through command-line interface, as input;
take a plaintext (message) file as input;
output a ciphertext as a file;
take a ciphertext file as input;
output a plaintext as a file;
handle any possible errors;
Write in C/C++ or Java;
be submitted with a clear readme.txt file.
NB: Ignore case. That is, you can choose whether you will input and output uppercase or lowercase characters. Also, keep (do not encrypt) special character such as full stops and commas.
## Task Three: Flipped Kamasutra Cipher (2 marks)
Implement Kama Sutra cipher, in C, C++, Java or Python. The name of your program should be Kamasutra.c or Kamasutra.cpp or Kamasutra.java or Kamasutra.py. Include in your report instructions on how to compile your code. You must include a Makefile that can be used to build your program. To build your program, one can just type:
make all
The command syntax of your program should be as follows:
kamasutra -k <keyfile.txt>
kamasutra -e <keyfile.txt> <plaintext.txt> <ciphertext.txt> kamasutra -d <keyfile.txt> <ciphertext.txt> <plaintext.txt>
where the -k option is to generate the keypair in a file called keyfile.txt, -e option is associated with encryption and the -d option is associated with decryption. The encryption and decryption processes take the keyfile.txt and a plaintext (or a ciphertext, resp.) to produce a ciphertext (or a plaintext, resp.). You may assume all input is lower case without punctuation. The description of the Kama Sutra cipher is as follows. In the 4th century BC, the Indian text “Kama Sutra" proposed a method of encrypting text. Each letter of the alphabet was paired with one other letter. A ciphertext was formed by replacing each letter in the plaintext with its paired letter. However, when a letter ‘f’ is found, then the paired letter will not be replaced. This is representing the ‘flipped’ version of Kamasutra. When this scheme is used in the English language, the number of possible keys is surprisingly high: around 7.9 × 1012. An exhaustive attack on such a scheme would be unwieldly using a modern computer, and it was certainly infeasible at the time this scheme was suggested. For example, suppose the keyfile is just a regular alphabet as follows.
abcdefghijklmnopqrstuvwxyz
Then, suppose the plaintext contains of the following
abab bcbc cdcd effe
The resulting ciphertext would be
baba adad dcdc effe
You also need to:
 First, generate a random keyfile keyfile.txt
 Generate the ciphertext file Ctext-3.txt obtained by encrypting Ptext-1.txt under the key in keyfile.txt
 In your report, describe the statistical properties of Ctext-3 and discuss how they compare them with those of Ctext-1 and Ctext-2, remembering that Ctext-1 and Ctext-3 are associated with the same plaintext. Include a comparative graph of the letter frequency distributions. Write your report in a file called Report2.pdf
 Discuss a way to decrypt the Kama Sutra cipher without using the key. Show your argument by decrypting the ciphertext Ctext-3 assuming that you don’t know the key. The discussion will need to be written in the same file Report2.pdf.
 To test the correctness of your program, one can just simply test with
kamasutra – d keyfile.txt Ctext-3.txt Output.txt
and verify whether the file Output.txt is identical with Ptext-1.txt by executing
diff Output.txt Ptext-1.txt
in the Linux environment.
