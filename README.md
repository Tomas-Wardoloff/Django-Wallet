# Django-Wallet 

This is a personal project where I design a virtual wallet to track personal expenses and incomes. This is a rework of a previous project, but this time the idea is to rebuild the project using [Django](https://www.djangoproject.com) to improve my skills as a Backend Developer. Here is the link to the first approach to this project: [Virtual-Wallet](https://github.com/Tomas-Wardoloff/Virtual-Wallet/)


## Table of contents

- [Description of the project](#description-of-the-project)
- [Database](#database)
- [License](#license)
- [Authors](#authors)


## Description of the project

The idea is to implement the following main features to the project:

1. **User registration**:  

   The application allows users to create an account and register their personal details such as email address, password, and nationality.

2. **Money accounts**:
    Testing different money manager apps, I found a really interesting feature using [Money Manager](https://realbyteapps.com). This application allows the user to register different money accounts, such as banks, cash, or savings, that enable tracking how much money you have in different accounts and where the incomes or expenses are coming from. I want to implement the same feature in my project.

3. **Transaction loggin**:

    The application keeps a record of all transactions made, whether it is an income or expense. It tracks every financial operation that involves the movement of money. All the transactions include information such as the date, the amount of money involved, the category, the account where the money was taken or deposited, and a short description provided by the user.

4. **Categories**

    The application provides a list of different categories to use for transactions, but users can also create their own categories.

5. **Money Transfer**:

    The application allows users to transfer money from one of their accounts to another.. 


## Database

This time I am using a similar database to the one I used for the first approach of the project. However, this time the database has some additional tables such as Accounts and Transfers. For the representation, I utilized an entity-relationship diagram, which is a concept I learned while studying Information Systems Engineering. The database comprises five main tables: Users, Transactions, Categories, Accounts, and Transfers.

- **Users**
    The Users table will store information about each user, such as their email, password and nacionaliry. Each user will have a unique identifier, which will serve as the primary key for this table

- **Categories**
    This table only stores information about the different categories that users can use to identify their transactions. Like the Users table, it has a unique identifier. Users can create their own categories, which is why this table has a foreign key that references the Users table. The categories with UserId = NULL are accessible to all users.
  
- **Transactions**
    This table stores information about each transaction made by the users. This table has two foreign keys: one references the Users table so each transaction is associated with a particular user, and the other references the Categories table. This table also stores the date, the amount, and a short description.

- **Accounts**
    Similar to the Transactions table, this table will have two foreign keys, one references one of the User account where the money is comming from and the other one references the User account where the money is going. Also this table store the date, the amount and a short description. All the transfers are from one User account to another account of the same user


## License

Distributed under the MIT License. See `LICENSE.md` for more information.


## Authors

- [@Tomas-Wardoloff](https://www.github.com/Tomas-Wardoloff)
