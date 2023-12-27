public class Bank {
    private List<Account> accounts;
    private List<Customer> customers;
    private List<Transaction> transactionHistory;
    public void CreateAccount(Account account) {
        accounts.Add(account);
    }
    public void CreateCustomer(Customer customer) {
        customers.Add(customer);
    }
    public void AddToTransactionHistory(Transaction transaction) {
        transactionHistory.Add(transaction);
    }
    public void Deposit(Account account, double amount) {
        Transaction transaction = new Transaction();
        transaction.To = account;
        transaction.Amount = amount;
        transaction.Type = TransactionType.Deposit;
        transaction.Date = DateTime.Now;
        AddToTransactionHistory(transaction);
        transaction.start();
    }

    public void Withdraw(Account account, double amount) {
        Transaction transaction = new Transaction();
        transaction.From = account;
        transaction.Amount = amount;
        transaction.Type = TransactionType.Withdraw;
        transaction.Date = DateTime.Now;
        AddToTransactionHistory(transaction);
        transaction.start();
    }

    public void Transfer(Account from, Account to, double amount) {
        Transaction transaction = new Transaction();
        transaction.From = from;
        transaction.To = to;
        transaction.Amount = amount;
        transaction.Type = TransactionType.Transfer;
        transaction.Date = DateTime.Now;
        AddToTransactionHistory(transaction);
        transaction.start();
    }

    public void PrintTransactionHistory(Account account) {
        foreach (Transaction transaction in transactionHistory) {
            if (transaction.From == account || transaction.To == account) {
                Console.WriteLine(transaction);
            }
        }
    }


}
public class Account {
    
}
public class Transaction {

}
public class Customer {

}

public class Program{
    
}