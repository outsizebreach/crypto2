using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace myproject2
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }
        int i = 1;
        private void button1_Click(object sender, EventArgs e)
        {
            DateTime Date = new DateTime(int.Parse(year.Text), int.Parse(mounth.Text), int.Parse(day.Text));

           Driver D =new Driver(name.Text, lastname.Text, phone.Text, address.Text,Date, drivercode.Text,
            mellicode.Text, comboBox1.Text , int.Parse(percent.Text));

            Addlabel.Text = "Done" + i;
            i++;
        }

        private void textBox11_TextChanged(object sender, EventArgs e)
        {

        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
        private void InitializeComboBox()
        {
            comboBox1.Items.AddRange(Enum.GetNames(typeof(Education)));
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form1 form1 = new Form1();
            form1.ShowDialog();
            this.Close();
        }
    }
}
