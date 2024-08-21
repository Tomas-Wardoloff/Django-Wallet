# Django-Wallet 

This is a rework of a previous project where I designed a virtual wallet to track personal expenses and incomes. This time, the idea is to rebuild the project using [Django](https://www.djangoproject.com) and [Django REST framework](https://www.django-rest-framework.org/) to create a REST API. Here is the link to the first approach to this project: [Virtual-Wallet](https://github.com/Tomas-Wardoloff/Virtual-Wallet/). I also used a suggested project from [Roadmap.sh](https://roadmap.sh/) as a guideline for the development process: [Expense Tracker API](https://roadmap.sh/projects/expense-tracker-api).


## Table of contents

- [Features](#features)
- [Models](#models)
- [License](#license)
- [Authors](#authors)


## Features

The idea is to implement the following main features to the project:

1. **User registration**:
   
   The application allows users to create an account and register their personal details such as email address, first name, last name and password.

3. **Money accounts**:
   
    Testing different money manager apps, I found a really interesting feature using [Money Manager](https://realbyteapps.com). This application allows the user to register different money accounts, such as banks, cash, or savings, enabling them to track how much money they have in different accounts and where the incomes or expenses are coming from. I want to implement the same feature in my project.

4. **Transaction**:
   
    The application keeps a record of all transactions made, whether it is an income or expense. It tracks every financial operation that involves the movement of money. All the transactions include information such as the date, the amount of money involved, the category, the account where the money was taken or deposited, and a short description provided by the user. Users can filter their transactions based on the date or on the type.

6. **Categories**:
   
    The application provides a list of different categories to use for transactions, but users can also create their own categories. Categories have a name, a type ['Income', 'Expense'] and a foreing key to an user. If the forign key is null, the category is considered a default category

8. **Money Transfer**:

   The application allows users to transfer money from one of their accounts to another. Transfers store information about the date, the amount, the user, from wich account the money was taken, where it went and a description.

10. **Security**

    The application use JWT (JSON Web Token) to protect the endpoints and to identify the requester.


## Models

This time I am using a similar database to the one I used for the first approach of the project. However, this time the database has some additional tables such as Accounts and Transfers. The database comprises five main tables: Users, Transactions, Categories, Accounts, and Transfers.

- **CustomUser**
  
    The `CustomUser` model extends Django's built-in user model to store additional user-specific information. This model handles the authentication and authorization of users, storing essential details such as email, password, first_name, last_name and automatically assigns the username. By using a custom user model, the application allows for greater flexibility in managing user-related data.

  ```python
     class CustomUser(AbstractUser):
        email = models.EmailField(help_text='User email address',
                              verbose_name='Email', unique=True, blank=False, null=False)
        username = models.CharField(max_length=150, blank=True, null=True)
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name', 'last_name']

        objects = CustomUserManager()

        def __str__(self):
           return self.email

        def save(self, *args, **kwargs):
           self.username = f"user_{self.email}"
           super().save(*args, **kwargs)
  ```

- **Categories**
  
   The `Category` model is used to classify transactions into different types such as 'Income' and 'Expense'. Categories help users organize their financial records and provide insights into their spending and earning patterns.

  ```python
     class Category(models.Model):
        class CategoryType(models.TextChoices):
           INCOME = 'Income', 'Income'
           EXPENSE = 'Expense', 'Expense'
  
        name = models.CharField(max_length=50)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
        type = models.CharField(max_length=7, choices=CategoryType.choices)

        class Meta():
           db_table = 'categories'
           unique_together = ('user', 'name', 'type')

        def __str__(self) -> str:
           return self.name
  ```
  
- **Transactions**

   The `Transaction` model records all financial transactions. Each transaction is linked to a specific user and category, and it captures details such as the date, amount, and description.

  ```python
     class Transaction(models.Model):
        amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
        date = models.DateField()
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        user_account = models.ForeignKey(Account, on_delete=models.CASCADE)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        description = models.CharField(max_length=100, blank=True, null=True)

        class Meta():
           db_table = 'transactions'

        def __str__(self):
           if self.category.type == 'Income':
               return f'Income(ID: {self.id}, Amount: {self.amount}, User: {self.user}, Date: {self.date})'
           return f'Expense(ID: {self.id}, Amount: {self.amount}, User: {self.user}, Date: {self.date})'

        def clean(self):
           super().clean()
           if self.user != self.user_account.user:
              raise ValidationError({'user_account': 'The account does not belong to the user'})
           if self.category.user and self.user != self.category.user:
              raise ValidationError({'category': 'The category is not a default category or does not belong to the user'})

        def save(self, *args, **kwargs):
           self.clean()
           super().save(*args, **kwargs)
  ```


- **Accounts**

   The `Account` model represents different financial accounts users can have, such as bank accounts, cash holdings, or savings accounts. Each account is linked to a specific user and is used to track the balance and associated transactions.

  ```python
     class Account(models.Model):
        balance = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
        name = models.CharField(max_length=50)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

        class Meta():
           db_table = 'accounts'
           unique_together = ('user', 'name')

        def __str__(self):
           return "{0} - {1}".format(self.name, self.user)

        def update_balance(self, amount):
           self.balance += amount
           self.save()
  ```


- **Transfers**:

   The `Transfer` model handles the movement of money between different accounts owned by the same user. This model allows users to track internal transfers and manage their finances across multiple accounts.
  ```python
     class Transfer(models.Model):
        amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
        date = models.DateField()
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        from_user_account = models.ForeignKey(Account, related_name='transfers_out', on_delete=models.CASCADE)
        to_user_account = models.ForeignKey(Account, related_name='transfers_in', on_delete=models.CASCADE)
        description = models.CharField(max_length=100, blank=True, null=True)

        class Meta():
           db_table = 'transfers'

        def __str__(self):
           return f'Transfer(ID: {self.id}, Amount: ${self.amount}, User: {self.user}, Date: {self.date}, From: {self.from_user_account}, To: {self.to_user_account})'

        def clean(self):
           super().clean()
           if self.user != self.from_user_account.user or self.user != self.to_user_account.user:
               raise ValidationError('The accounts involved do not belong to the user')
           if self.from_user_account == self.to_user_account:
              raise ValidationError('The accounts involved are the same')

        def save(self, *args, **kwargs):
           self.clean()
           super().save(*args, **kwargs)
  ```


## License

Distributed under the GPL-2.0 License. See `LICENSE.md` for more information.


## Authors

- [@Tomas-Wardoloff](https://www.github.com/Tomas-Wardoloff)
