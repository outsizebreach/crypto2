using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace myproject2
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime Date = new DateTime(int.Parse(year.Text), int.Parse(mounth.Text), int.Parse(day.Text));
            DateTime Date1 = new DateTime(int.Parse(year1.Text), int.Parse(mounth1.Text), int.Parse(day1.Text));
            Car C = new Car(Date, comboBox1.Text, model.Text, int.Parse(code.Text), comboBox2.Text, Date1, insuranceNum.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            showForm showForm = new showForm();
            showForm.Show();
            this.Hide();
        }
    }
}
