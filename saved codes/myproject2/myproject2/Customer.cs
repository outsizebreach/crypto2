
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace projectsc
{
    internal class Customer : Person
    {
        int CostomerCode;

        public Customer(string Name, string LastName, string PhoneNumber, string Adress, DateTime Date, int CostomerCode) : base(Name, LastName, PhoneNumber, Adress, Date)
        {
            this.CostomerCode = CostomerCode;
        }

        List<Customer> list = new List<Customer>();
        public static Customer operator +(Customer C1, Customer C2)
        {
            if (!C1.list.Contains(C1)) { C1.list.Add(C1); }


            C1.list.Add(C2);
            return C1;
        }
        //public List<Customer> operator +(Customer C1, Customer C2)
        //{
        //    List<Customer> A = new List<Customer>();
        //    A.Add(C1);
        //    A.Add(C2);
        //    return A;
        //}

    }
}
