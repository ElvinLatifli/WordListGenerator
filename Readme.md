# WordList Generator

## Author

You can use this code as you wish. Don't get involved in illegal things :D

- Instagram: [@ltfl_elvin](https://instagram.com/ltfl_elvin)
- Telegram: [@HackerRick](https://t.me/HackerRick)

## Download Instructions

To use it on your Linux system, follow the steps below:
1. Download this project as zip and unzip it.
2. Navigate to the directory where you extracted the file in the console.
3. Enter the WordListGenerator directory and run the config.sh file.
4. If you encounter a permission error, use the following command:
    ```bash
    chmod +x config.sh
    ```

## How to Use?

### Linux

```bash
hackrick -n 3 -x 6 -i "12345" -w wordlist 
```
   where -n represents the minimum number of characters of the passwords to be generated. -x represents the maximum number of characters of passwords. The characters you write after -i will be used for the wordlist. -w specifies the name of the txt file.

 ### Windows

 ```bash
python main.py -n 3 -x 6 -i "12345" -w wordlist
 ```

  Replace -n with the minimum number of characters for passwords, -x with the maximum number of characters, -i with the characters to be used in the wordlist, and -w with the desired name of the output file.

```bash
 hackrick -n 3 -x 6 -i "12345" -w wordlist
 ```
This command generates a wordlist with passwords ranging from 3 to 6 characters, using the characters "12345", and saves it as "wordlist.txt"

## Additional Notes

- The tool provides an estimate of the password list size and prompts for confirmation before proceeding.
- Generating large wordlists may take some time. Avoid unnecessary large data inputs as it may strain your system.
- To terminate the process at any stage, use ctrl + c.
- For additional assistance, use the command hackrick -h.
- If you need help, just type hackrick -h

## Disclaimer

This tool is intended for educational and ethical purposes only. Misuse of this tool for illegal activities is strictly prohibited. The author and contributors are not responsible for any misuse or damage caused by this tool.



