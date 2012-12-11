namespace testGUI
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.button2 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.checkedListBox1 = new System.Windows.Forms.CheckedListBox();
            this.QuestionInput = new System.Windows.Forms.RichTextBox();
            this.TitleInput = new System.Windows.Forms.TextBox();
            this.TitleLabel = new System.Windows.Forms.Label();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.PortNumber = new System.Windows.Forms.TextBox();
            this.IpAddress = new System.Windows.Forms.TextBox();
            this.PortNumberLabel = new System.Windows.Forms.Label();
            this.IpAddressLabel = new System.Windows.Forms.Label();
            this.NumberOfTagsLabel = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.tabPage2.SuspendLayout();
            this.SuspendLayout();
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Location = new System.Drawing.Point(1, 3);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(635, 389);
            this.tabControl1.TabIndex = 0;
            // 
            // tabPage1
            // 
            this.tabPage1.BackColor = System.Drawing.Color.WhiteSmoke;
            this.tabPage1.Controls.Add(this.button2);
            this.tabPage1.Controls.Add(this.label1);
            this.tabPage1.Controls.Add(this.button1);
            this.tabPage1.Controls.Add(this.checkedListBox1);
            this.tabPage1.Controls.Add(this.QuestionInput);
            this.tabPage1.Controls.Add(this.TitleInput);
            this.tabPage1.Controls.Add(this.TitleLabel);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(627, 363);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "Tag Generator";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(273, 334);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(169, 23);
            this.button2.TabIndex = 6;
            this.button2.Text = "Generate Tags";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(493, 16);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(84, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "Generated Tags";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(448, 334);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(169, 23);
            this.button1.TabIndex = 4;
            this.button1.Text = "Reset Form";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // checkedListBox1
            // 
            this.checkedListBox1.FormattingEnabled = true;
            this.checkedListBox1.Location = new System.Drawing.Point(448, 38);
            this.checkedListBox1.Name = "checkedListBox1";
            this.checkedListBox1.Size = new System.Drawing.Size(170, 289);
            this.checkedListBox1.TabIndex = 3;
            // 
            // QuestionInput
            // 
            this.QuestionInput.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.QuestionInput.Location = new System.Drawing.Point(12, 38);
            this.QuestionInput.Name = "QuestionInput";
            this.QuestionInput.Size = new System.Drawing.Size(430, 290);
            this.QuestionInput.TabIndex = 2;
            this.QuestionInput.Text = "";
            // 
            // TitleInput
            // 
            this.TitleInput.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.TitleInput.Location = new System.Drawing.Point(60, 11);
            this.TitleInput.Name = "TitleInput";
            this.TitleInput.Size = new System.Drawing.Size(382, 20);
            this.TitleInput.TabIndex = 1;
            // 
            // TitleLabel
            // 
            this.TitleLabel.AutoSize = true;
            this.TitleLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.TitleLabel.Location = new System.Drawing.Point(8, 9);
            this.TitleLabel.Name = "TitleLabel";
            this.TitleLabel.Size = new System.Drawing.Size(46, 20);
            this.TitleLabel.TabIndex = 0;
            this.TitleLabel.Text = "Title :";
            // 
            // tabPage2
            // 
            this.tabPage2.BackColor = System.Drawing.Color.WhiteSmoke;
            this.tabPage2.Controls.Add(this.PortNumber);
            this.tabPage2.Controls.Add(this.IpAddress);
            this.tabPage2.Controls.Add(this.PortNumberLabel);
            this.tabPage2.Controls.Add(this.IpAddressLabel);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(627, 363);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "Settings";
            // 
            // PortNumber
            // 
            this.PortNumber.Location = new System.Drawing.Point(70, 35);
            this.PortNumber.Name = "PortNumber";
            this.PortNumber.Size = new System.Drawing.Size(100, 20);
            this.PortNumber.TabIndex = 3;
            this.PortNumber.Text = "8080";
            // 
            // IpAddress
            // 
            this.IpAddress.Location = new System.Drawing.Point(70, 9);
            this.IpAddress.Name = "IpAddress";
            this.IpAddress.Size = new System.Drawing.Size(100, 20);
            this.IpAddress.TabIndex = 2;
            this.IpAddress.Text = "127.0.0.1";
            // 
            // PortNumberLabel
            // 
            this.PortNumberLabel.AutoSize = true;
            this.PortNumberLabel.Location = new System.Drawing.Point(7, 38);
            this.PortNumberLabel.Name = "PortNumberLabel";
            this.PortNumberLabel.Size = new System.Drawing.Size(36, 13);
            this.PortNumberLabel.TabIndex = 1;
            this.PortNumberLabel.Text = "Port #";
            // 
            // IpAddressLabel
            // 
            this.IpAddressLabel.AutoSize = true;
            this.IpAddressLabel.Location = new System.Drawing.Point(7, 12);
            this.IpAddressLabel.Name = "IpAddressLabel";
            this.IpAddressLabel.Size = new System.Drawing.Size(57, 13);
            this.IpAddressLabel.TabIndex = 0;
            this.IpAddressLabel.Text = "Ip Address";
            // 
            // NumberOfTagsLabel
            // 
            this.NumberOfTagsLabel.AutoSize = true;
            this.NumberOfTagsLabel.Location = new System.Drawing.Point(7, 64);
            this.NumberOfTagsLabel.Name = "NumberOfTagsLabel";
            this.NumberOfTagsLabel.Size = new System.Drawing.Size(36, 13);
            this.NumberOfTagsLabel.TabIndex = 1;
            this.NumberOfTagsLabel.Text = "# of Tags";
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(635, 392);
            this.Controls.Add(this.tabControl1);
            this.Name = "Form1";
            this.Text = "There\'s A Tag For That";
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage1.PerformLayout();
            this.tabPage2.ResumeLayout(false);
            this.tabPage2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.TextBox PortNumber;
        private System.Windows.Forms.TextBox IpAddress;
        private System.Windows.Forms.Label PortNumberLabel;
        private System.Windows.Forms.Label IpAddressLabel;
        private System.Windows.Forms.Label TitleLabel;
        public System.Windows.Forms.RichTextBox QuestionInput;
        private System.Windows.Forms.TextBox TitleInput;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.CheckedListBox checkedListBox1;
        private System.Windows.Forms.Button button2;
		private System.Windows.Forms.Label NumberOfTagsLabel;
        private System.Windows.Forms.Timer timer1;


    }
}

