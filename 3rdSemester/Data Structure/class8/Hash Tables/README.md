## Getting Started

Welcome to the VS Code Java world. Here is a guideline to help you get started to write Java code in Visual Studio Code.

## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies

Meanwhile, the compiled output files will be generated in the `bin` folder by default.

> If you want to customize the folder structure, open `.vscode/settings.json` and update the related settings there.

## Dependency Management

The `JAVA PROJECTS` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-dependency#manage-dependencies).

## About the code

### HashTable.java

In the HashTable class I created a total of 4 attributes, 1 constructor, 2 private methods and 9 public methods.

#### Attributes

- **List< List< String > > table**
  - The variable to store tables of Lists of Strings
- **int rangeWords**
  - A variable to store the quantity of words put on this specific table
- **List< Integer > tokens**
  - To store the ASCII value of all characters of any word combined
- **static int range**
  - Stores the amount of words put on all tables created

#### Constructor

The constructor initializes a List of Strings and add this list to the table.
This is the first and only list created statically, all other lists will be created dynamically.

#### Methods

All the magic happens underlying the two private methods that will be used by the the user via the public one.

###### Private Ones

- **int hashFunction(String word)**
  - It's a function that takes a String as a parameter and returns a primitive int value that corresponds to the aggregated ASCII value of the entire String.
  - For that I created a int variable called sum and initialized it at 0. I then created a _for loop_ that goes from 0 to the length of the String minus one; for each loop, I initialize a int variable called count that receives the char at the position i of the String, then it is summed to the sum variable.
  - Lastly, I return the variable sum.
- **void checkLists(String word)**
  - It's a function that takes a String as a parameter and checks whether that String should be added to the table or not;
  - Firstly, it checks whether rangeWords is equal to 0 or not;
    - **If it equals 0** it means it is the first word being put in the table. So I create a variable int called token and I give this token the value calculated in the hashFunction of that given String.
    - I then add this token to the tokens list, create a list of Strings called list that will point to the list created on the constructor. Lastly I add the String to the list.
    - **If it does not equal 0** then I check whether the variable tokens has the value returned by hashFunction of that given String. If it returns true, it means that a String with the exact same aggregated ASCII value has been added already, meaning a list for that ASCII value already exists;
    - Knowing that I just create a list of Strings called list, point it to the list on the table that on a specific index - _since the index of any given token in the token list is equal to the index of any list of strings in the table list, getting the index of the token is going to give the index of the string list_ - that I can get by referencing the index of the value returned by the hashFunction of the given String. Then I just have to add the String to that list.
    - **If the value is not contained in the tokens list** I then create another variable called token that receives the value returned by the hashFunction of the given String, add that value to the tokens list, create a new list of strings that receives a new LinkedList of Strings, I add this list to the table and finally add the String to the list.

###### Public ones

They are: search, add, remove, getAll, getList I and II, countWords and countLists

- **boolean search(String word)**
  - A function that receives a String as a parameter and returns whether that word is contained in any part of the table or not.
  - To do so, I firstly created a if statement that checks if the function indexOf used on the table tokens taken as parameter this.hashFunction(word) will return -1 or not. _If it returns -1 it means that the word is not in the list, because no past word that has been put in the table had this aggregated ASCII value_. If it's true, then I instantly return false without making any real search, else I then create a variable called index that receives the value of the index of this given word. I create a list of Strings called list that points to the list in the table on that specific index and then I return list.contains(word). _this function will map through that list comparing every object in the list until one of then matches the given String. If it doesn't find any, it means that I have added a String that the aggregated ASCII value is the same as this String, but they are different Strings, so they will be placed together._
- **void add(String word)**
  - A function that adds a String to the table;
  - It first checks if the given String doesn't exist in the table through the search method. **If not,** it invokes the checkLists method and passes the given String as a param and adds 1 to the rangeWords and range variables. **If it passes,** I print out a message telling that it's already on the list.
- **void remove(String word)**
  - A function that removes a String from the table;
  - It first checks if the given String already exists in the table through the search method. **If it passes,** I create a variable int called index that receives the index of the token on that given String, then I create a list of Strings called list that points to the list in the table that has that same index and I then remove the given String from the list. Lastly I take 1 from range and rangeWords.
- **List< String > getAll()**
  - It's a function that returns all the Strings in the table in a single list of Strings;
  - I first create a list of Strings called words that receives a new ArrayList of Strings. Then, I create a for loop that goes from 0 until the size of the table minus 1. For each loop, I use the _addAll_ function on the words list passing as a param the index of the table at position i. - _This means that the function will look at each individual list inside the table and add all Strings inside those lists to the end of the words list_ - Lastly I return the list words.
- **List< String > getList(int index)**
  - It is a function that takes a int value as a param and returns a list of Strings;
  - The given integer is used as the index where to take the list from the table. A list of String called words is the n created, this list points to the table at the given index.
- **List < String > getList(String word)**
  - Similar to the function above, but takes a String as a param instead;
  - It converts the String into its aggregated ASCII value to discover in which list this String is to return the list of that String.
- **int countWords()**
  - A function that simply returns the variable rangeWords;
- **int countLists()**
  - A function that simply returns the function _size()_ of the table;
