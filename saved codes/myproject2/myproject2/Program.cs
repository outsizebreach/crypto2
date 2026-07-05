using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.ConstrainedExecution;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace projectsc
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Customer C1 = new Customer("name1", "LastName1", "9846741", " Adress1", new DateTime(2000, 6, 1), 6561);
            Customer C2 = new Customer("name2", "LastName2", "9846742", " Adress2", new DateTime(2000, 6, 2), 6562);
            Customer C3 = new Customer("name3", "LastName3", "9846743", " Adress3", new DateTime(2000, 6, 3), 6563);
            List<Customer> C = new List<Customer>();
            C3 = C1 + C2;
            Car car = new Car();
            
        }
    }
}

enum Education
{
    diplom, //high school diploma
    Fdiplom, //Associate Degree
    lisans, //Bachelors degree
    Flisans, //Masters degree
    docter //Doctoral degree
}
enum Company
{
    Saipa,
    Irankhodro,
    BahmanMotor,
    KermanMotor
}
// DateTime date1 = new DateTime(2024, 5, 22, 14, 30, 0)         2024/5/22  14:30 pm

enum Color
{
    red, green, blue, yello, white, black, other
}

   