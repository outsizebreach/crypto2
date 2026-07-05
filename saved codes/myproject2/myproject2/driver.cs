using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace projectsc
{
    internal class Driver : Person
    {
        int DriverCode { get; set; }
        int MelliCod { get; set; }
        Education Education { get; set; }
        int Percent { get; set; }
        //List<double> Daramad { get; set; }

        public Driver(string Name, string LastName, string PhoneNumber, string Adress, DateTime Date, int DriverCode,
            int MelliCod, Education Education, int Percent) : base(Name, LastName, PhoneNumber, Adress, Date)
        {

            this.DriverCode = DriverCode;
            this.MelliCod = MelliCod;
            this.Education = Education;
            this.Percent = Percent;
        }
        public virtual double CalculateSalary<T>(List<T> daramad)
        {
            double salary = 0;
            foreach (T t in daramad)
            {
                double d = Convert.ToDouble(t);
                salary += d;
            }
            return salary * Percent / 100;
        }

        public override void GetAdress() { base.GetAdress(); }
        //void CalculateBirthday() { }
        public double GivePercent() { return Percent; }
    }

}
