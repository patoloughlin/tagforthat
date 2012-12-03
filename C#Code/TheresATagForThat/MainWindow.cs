using System;
using Gtk;
using Newtonsoft.Json;
using TheresATagForThat;
using System.IO;
using System.Net.Sockets;
using System.Net;
using System.Text;

public partial class MainWindow: Gtk.Window
{	
	public MainWindow (): base (Gtk.WindowType.Toplevel)
	{
		Build ();
	}
	
	protected void OnDeleteEvent (object sender, DeleteEventArgs a)
	{
		Application.Quit ();
		a.RetVal = true;
	}

	protected void OnClickButtonClicked (object sender, EventArgs e)
	{
		string jsonResponse = sendRequest(this.entry1.Text).ToString();
		this.label1.Text = jsonResponse;

	}
	private string sendRequest(string request)
	{
		try
		{
			//Set up connection to python server
			TcpClient client = new TcpClient();
			IPEndPoint serverEndPoint = new IPEndPoint(IPAddress.Parse(this.IpAddress.Text), Int32.Parse(this.Port.Text));
			client.Connect(serverEndPoint);
			NetworkStream clientStream = client.GetStream();
			//Encode request to send to python
			ASCIIEncoding encoder = new ASCIIEncoding();
			byte[] buffer = encoder.GetBytes(request);
			byte[] bufferInfo = encoder.GetBytes(request.Length.ToString());
			//Send length of request string
			clientStream.Write(bufferInfo, 0, bufferInfo.Length);
			clientStream.Flush();
			//Recieve send command from python
			byte[] readin = new byte[256];
			clientStream.Read(readin, 0, 256);
			clientStream.Flush();
			//Send request to server
			clientStream.Write(buffer, 0, buffer.Length);
			clientStream.Flush();
			//Recieve send command from python
			readin = new byte[256];
			clientStream.Read(readin, 0, 256);
			clientStream.Flush();
			string readinString = System.Text.Encoding.Default.GetString(readin).Replace("\0", "");
			int responceSize = Convert.ToInt32(readinString);
			//Send request for send
			buffer = encoder.GetBytes("send");
			clientStream.Write(buffer, 0, buffer.Length);
			clientStream.Flush();
			//Recieve server responce
			//Recieve send command from python
			readin = new byte[responceSize];
			clientStream.Read(readin, 0, responceSize);
			clientStream.Flush();
			client.Close();
			readinString = System.Text.Encoding.Default.GetString(readin).Replace("\0", "");
			return readinString;
		}
		catch
		{
			return "Failed";
		}
	}
}
