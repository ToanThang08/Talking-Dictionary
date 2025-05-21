using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SpeakDictionary
{
    public partial class Form1 : Form
    {
        DictionaryManager dictionary;
        SpeakText VietNam;
        SpeakText English;
        bool isLoading1 = true;
        bool isLoading2 = true;
        public Form1()
        {
            InitializeComponent();

            ChangeLoading();

            cbWord.DisplayMember = "Key";

            WebBrowser wbVN = new WebBrowser();
            wbVN.Width = 0;
            wbVN.Height = 0;
            wbVN.Visible = false;
            wbVN.ScriptErrorsSuppressed = true;
            wbVN.Navigate(Cons.VietNamLink);
            wbVN.DocumentCompleted += wbVN_DocumentCompleted;

            this.Controls.Add(wbVN);

            WebBrowser wbEn = new WebBrowser();
            wbEn.Width = 0;
            wbEn.Height = 0;
            wbEn.Visible = false;
            wbEn.ScriptErrorsSuppressed = true;
            wbEn.Navigate(Cons.EnglishLink);
            wbEn.DocumentCompleted += wbEn_DocumentCompleted;
            this.Controls.Add(wbEn);

            VietNam = new SpeakText(wbVN);
            English = new SpeakText(wbEn);

            dictionary = new DictionaryManager();

            dictionary.LoadDataToCombobox(cbWord);
        }

        void wbEn_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            isLoading1 = false;
            ChangeLoading();
        }

        void wbVN_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            isLoading2 = false;
            ChangeLoading();
        }

        void ChangeLoading()
        {
            this.Enabled = !(isLoading1 && isLoading2);
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (MessageBox.Show("Bạn có chắc chắn muốn thoát?", "Thông báo", MessageBoxButtons.OKCancel) != System.Windows.Forms.DialogResult.OK)
            {
                e.Cancel = true;
                return;
            }

            dictionary.Serialize();
        }

        private void cbWord_SelectedIndexChanged(object sender, EventArgs e)
        {
            ComboBox cb = sender as ComboBox;

            if (cb.DataSource == null)
                return;

            DictionaryData data = cb.SelectedItem as DictionaryData;

            txbMeaning.Text = data.Meaning;
            txbExplaination.Text = data.Explaination;
        }

        private void btnSpeakEnglish_Click(object sender, EventArgs e)
        {
            English.Spreak((cbWord.SelectedItem as DictionaryData).Key);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            VietNam.Spreak(txbMeaning.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            VietNam.Spreak(txbExplaination.Text);
        }
    }
}
