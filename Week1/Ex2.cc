#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

void checkFlags(bool &decrypt, 
				bool &casing, 
				int argc, 
				char **argv)
{
  string dFlag{"-d"};
  string oFlag{"-o"};

  for (int iter = 0; iter < argc; ++iter)
  {
    if(!dFlag.compare(argv[iter]))
      decrypt = true;

    if(!oFlag.compare(argv[iter]))
      casing = true;
  }
}

void getKey(string &key, 
			string &refrence, 
			int argc, 
			char **argv, 
			bool decrypt)
{
  if (key.length() < 26)
  {
    int shift = atoi(argv[argc-1])%26;
    key = refrence;
    for (int i = 0; i < 26; ++i)
    {
      if (refrence[i]+shift <= 'z')
        key[i] = refrence[i] + shift;  
      else
        key[i] = refrence[i] + shift - 26;
        
    }
  }

  if (decrypt)
  {
    refrence = key;
    key = {"abcdefghijklmnopqrstuvwxyz"};
  }
}

string encode(string key, 
              string refrence, 
              bool casing)
{
  string codedMessage;
  string line;
  string newLine;

  while(true)
  {
    getline(cin, line);
    newLine = {};

    for (int iter = 0; iter < int(line.length()); ++iter)
      for (int counter = 0; counter < 26; ++counter)
          
        if (casing)
        {
          if (line[iter] < 65 or (line[iter] > 90 and line[iter] < 97) or line[iter] > 122)
          {
            newLine += line[iter];
            break;
          }
          else if (line[iter] == refrence[counter])
            newLine += key[counter];
          else if (line[iter] == refrence[counter] - 32)
            newLine += key[counter] - 32;
        }
        else if (line[iter] == refrence[counter] or line[iter] == refrence[counter] - 32)
            newLine += key[counter];

    codedMessage += newLine;

    if (cin.eof())
      break;

    codedMessage += "\n";
  }

  return codedMessage;
}

int main(int argc, char *argv[])
{
  if (argc > 1)
  {
    bool decrypt = false;
    bool casing = false;

    checkFlags(decrypt, casing, argc, argv);

    string key = argv[argc-1];
    string refrence{"abcdefghijklmnopqrstuvwxyz"};

    getKey(key, refrence, argc, argv, decrypt);

    cout << encode(key, refrence, casing);

  }
  else
    cout <<"Usage: substitution [-o] [-d] mapping \n"
      "Where: \n"
      "-o: keep non-letters as is, honor letter casing\n"
      "-d: decrypt"
      "mapping: 26 letter char-mapping or an int-value\n" 
      "\n"
      "En/Decrypts stdin to stdout. Only letters are \n"
      "encrypted, all other characters are silently\n"
      "ignored, unless -o was specified, in which case\n"
      "they are used as-is. When -o is specified, letter\n"
      "casing is honored, otherwise all letters are\n"
      "converted to lower-case letters. Use an int-value\n"
      "to do a letter shift (% 26, 0: a = a)Shift 3 is\n"
      "the classical Caesar encryption \n";
}

/*

command = input()

array = 'abcdefghijklmnopqrstuvwxyz'

key = command[len(command)-1]

if ord(key) > 47 and ord(key) < 58:
  key = int(key)
  array = array[-key:]+array[:-key]
  key = ['abcdefghijklmnopqrstuvwxyz', array]
  remainingLength = len(command)
  print(key)
else:
  key = ['abcdefghijklmnopqrstuvwxyz', command[len(command)-26:len(command)]]
  remainingLength = len(command)-25

print(key)

nonLetters = 'discard'
mode = 'e'

if command[remainingLength-4] == "-":

  if command[remainingLength-3] == 'd':
    mode = 'd'
    if command[remainingLength-7] == "-" and command[remainingLength-6] == 'o':
      nonLetters = 'keep'
      text = command[0:remainingLength-8]
    else:
      text = command[0:remainingLength-5]

  elif command[remainingLength-3] == 'o':
    nonLetters = 'keep'
    text = command[0:len(command)-5]
  else:
    text = command[0:len(command)-2]

else:
  text = command[0:len(command)-2]

if mode == "d":
  temp = key[0]
  key[0] = key[1]
  key[1] = temp

encodedText = ""

for symbol in text:

  if symbol.isalpha():

    if symbol.isupper():
      newSymbol = chr(ord(symbol) + 32)
      newSymbol = key[1][key[0].find(newSymbol)]
      if nonLetters == "keep":
        newSymbol = chr(ord(newSymbol) - 32)

    if symbol.islower():
      newSymbol = key[1][key[0].find(symbol)]

    encodedText += newSymbol

  elif nonLetters == "keep":
    encodedText += symbol


print('Result:\n' + encodedText)

*/