using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace projectsc
{
    internal abstract class Person : IBirthday
    {
        string Name { get; set; }
        string LastName { get; set; }
        string PhoneNumber { get; set; }
        string Adress { get; set; }
        DateTime Date { get; set; }

        public Person(string Name, string LastName, string PhoneNumber, string Adress, DateTime Date)
        {
            if (PhoneNumber.Length != 12) throw new ArgumentException("Your number phones length most be 12 character!! ");
            foreach (char c in PhoneNumber)
            {
                if (char.IsDigit(c)) { }
                else
                {
                    throw new ArgumentException("your number cant be letter bro.");
                    break;
                }

            }
            this.Name = Name;
            this.LastName = LastName;
            this.PhoneNumber = PhoneNumber;
            this.Adress = Adress;
            this.Date = Date;
        }

        public void UpdateMobile(string PhoneNumber)
        {
            this.PhoneNumber = PhoneNumber;
        }
        public virtual void GetAdress() { Console.WriteLine(this.Adress); }

        void IBirthday.CalculateBirthday()
        {
            int comp = DateTime.Now.CompareTo(Date);

            int days = DateTime.Now.Day - Date.Day;
            int monds = DateTime.Now.Month - Date.Month;
            Console.WriteLine(days + " days and " + monds + " months to BirthDay.");
            if (comp == 0) { Console.WriteLine("Hppy BirthDay " + Name + " !!!"); }

            // if (comp > 0)
            //  { 
            //      TimeSpan dif = DateTime.Now - Date;
            //      Console.WriteLine(dif.TotalDays "days "); 
            //  }
            // if (comp < 0) { }
            // if (comp == 0) { Console.WriteLine("Hppy BirthDay " + Name + " !!!" ); }
        }

    }
}
