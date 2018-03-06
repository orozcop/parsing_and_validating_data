# Parsing and Manipulating Data using Python
This project reads and writes CSV files by parsing data, checking its format and values, and then allocating it between a "clean names" file or an "invalid names" file.

The project makes use of Strings, Loops, Lists, Modules, Functions, Regular Expressions as well as Reading and Writing files to different directories while using appropriate modifiers.

The project reads files that contain millions of names that are correctly or incorrectly formatted and must be cleaned up. A clean name is defined as a name that only contains letters from a to z (lowercase and/or uppercase) or a hyphen. Poorly formatted names have symbols or other invalid characters. In that case, the name does not get formatted but rather it is put in a separate file called InvalidNames.csv. Names that are formatted correctly are put in CleanNames.csv

A dirty name or invalid name will consist of a name with randomly placed upper and lowercase letters as well, and is valid but needs to be reformatted. For example, 'joRdaN' should be reformatted to 'Jordan'. Therefore, a clean name should be formatted with an uppercase letter first and then followed by lowercase letters. In the case that a name is hyphenated, the name after the hyphen should also start with an uppercase letter. For example, 'Pitt-rivers' should be 'Pitt-Rivers'. Invalid names are entries in the list/file that are not names at all or names that contain invalid symbols, numbers or spaces. Examples of invalid names include 'J@ker', '123-123-1234' or even 'John Smith'.

