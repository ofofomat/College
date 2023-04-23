### Hash Tables

#### 17/04/23

---

They allow us to divide the elements in the table in categories to make it easier for us to search through them. Making searches less time-consuming

###### Hash function

It's a function that takes a element and sets which category should it be in.

###### Hash table

It's the part where the element should be stored in.

Ideally the function should generate different indexes to different elements, but, sometimes, it does not happen. When two identical indexes are created we call it a **crash**. To solve it we combine a hash table with another data structure, such as lists, queues, stacks or a tree.
