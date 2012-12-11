using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Net.Sockets;
using System.Net;
using Newtonsoft.Json;


namespace testGUI
{
    public partial class Form1 : Form
    {
        
        private BackgroundWorker bw = new BackgroundWorker();
        static string questionText = "";
        static bool newTags = false;
        static TagsResponse tagsResponce = new TagsResponse();
        
        public Form1()
        {
            InitializeComponent();
            bw.WorkerReportsProgress = true;
            bw.WorkerSupportsCancellation = true;
            bw.DoWork += new DoWorkEventHandler(bw_DoWork);
            this.timer1.Start();
        }

        void  bw_DoWork(object sender, DoWorkEventArgs e)
        {
            string jsonResponse = sendRequest(questionText).ToString();
            //this.TitleInput.Text = jsonResponse;
            tagsResponce = JsonConvert.DeserializeObject<TagsResponse>(jsonResponse);
            newTags = true;
        }

        private string getQuestion()
        {
            if (this.QuestionInput.Text == null && this.TitleInput.Text == null)
                return "";
            return this.QuestionInput.Text + this.TitleInput.Text;
        }
		
		private string sendRequest (string request)
		{
			try {
				//Set up connection to python server
				TcpClient client = new TcpClient ();
				IPEndPoint serverEndPoint = new IPEndPoint (IPAddress.Parse (this.IpAddress.Text), Int32.Parse (this.PortNumber.Text));
				client.Connect (serverEndPoint);
				NetworkStream clientStream = client.GetStream ();
				//Encode request to send to python
				ASCIIEncoding encoder = new ASCIIEncoding ();
				byte[] buffer = encoder.GetBytes (request);
				byte[] bufferInfo = encoder.GetBytes (request.Length.ToString ());
				//Send length of request string
				clientStream.Write (bufferInfo, 0, bufferInfo.Length);
				clientStream.Flush ();
				//Recieve send command from python
				byte[] readin = new byte[256];
				clientStream.Read (readin, 0, 256);
				clientStream.Flush ();
				//Send request to server
				clientStream.Write (buffer, 0, buffer.Length);
				clientStream.Flush ();
				//Recieve send command from python
				readin = new byte[256];
				clientStream.Read (readin, 0, 256);
				clientStream.Flush ();
				string readinString = System.Text.Encoding.Default.GetString (readin).Replace ("\0", "");
				int responceSize = Convert.ToInt32 (readinString);
				//Send request for send
				buffer = encoder.GetBytes ("send");
				clientStream.Write (buffer, 0, buffer.Length);
				clientStream.Flush ();
				//Recieve server responce
				//Recieve send command from python
				readin = new byte[responceSize];
				clientStream.Read (readin, 0, responceSize);
				clientStream.Flush ();
				client.Close ();
				readinString = System.Text.Encoding.Default.GetString (readin).Replace ("\0", "");
				return readinString;
			} catch {
				return "Failed";
			}
		}

        private void TitleLabel_Click(object sender, EventArgs e)
        {

        }


        private void button2_Click(object sender, EventArgs e)
        {
            if (!bw.IsBusy)
            {
                bw.RunWorkerAsync();
            }
        }
		//Post question button
        private void button1_Click(object sender, EventArgs e)
        {
			this.checkedListBox1.Items.Clear();
			this.QuestionInput.Text = "";
			this.TitleInput.Text = "";
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            questionText = getQuestion();
            if (newTags == true)
            {
                this.checkedListBox1.Items.Clear();
                foreach (var tag in tagsResponce.tags)
                {
                    this.checkedListBox1.Items.Add(tag);
                }
                newTags = false;
            }

            this.Invalidate();
        }
    }
}

