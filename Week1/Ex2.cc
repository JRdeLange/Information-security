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

  // We check the arguments on the commandl ine for the flags 
  // defined above
  for (int iter = 0; iter < argc; ++iter)
  {
    if(!dFlag.compare(argv[iter]))
      decrypt = true;

    if(!oFlag.compare(argv[iter]))
      casing = true;
  }
}

//this function reads the key from the command line
void getKey(string &key,   
      string &refrence, 
      int argc, 
      char **argv, 
      bool decrypt)
{
  // If we get an int as key we create a character map from this.
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

  //If the decrypt flag was used we swap the key and refrence.
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

// This loop reads line for line the input
  while(true)
  {
    getline(cin, line);
    newLine = {};

    // For each line it checks the characters against the refrence
    // We then replace it with the character in the key.
    for (int iter = 0; iter < int(line.length()); ++iter)
      for (int counter = 0; counter < 26; ++counter)
        // If the casing flag was used we use the same casing as the 
        // input  
        if (casing)
        {
          if (line[iter] < 65 or 
              (line[iter] > 90 and line[iter] < 97) or 
              line[iter] > 122)
          {
            newLine += line[iter];
            break;
          }
          else if (line[iter] == refrence[counter])
            newLine += key[counter];
          else if (line[iter] == refrence[counter] - 32)
            newLine += key[counter] - 32;
        }
        else if (line[iter] == refrence[counter] or 
            	line[iter] == refrence[counter] - 32)
            newLine += key[counter];

    codedMessage += newLine;

    // If we reach the end of the file we break from the while loop
    if (cin.eof())
      break;

    codedMessage += "\n";
  }

  return codedMessage;
}

int main(int argc, char *argv[])
{
  // If we receive no extra arguments we print the usage 
  // instructions

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