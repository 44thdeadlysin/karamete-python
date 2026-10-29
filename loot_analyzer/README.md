# karamete - python
py learning here
loot_analyzer.py:
# LOOT ANALYZER
Enter your 'loot' and get: its total number, the number of different items, and items you have just one of. The program ignores letter case and removes punctuation (.,!?) from the beginning and end of each item.
## Features:
1. Calculates number of items
2. Calculates number of different items
3. Calculates number of single items
## How to run
1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the following command:

   ```bash
   python loot_analyzer/loot_analyzer.py
   ```

4. Enter item names separated by spaces.
5. Press Enter to see the results.
## Example

```text
Enter loot: SWORD, sword! shield key
Total items: 4
Different items: 3
Single items: ['shield', 'key']
```