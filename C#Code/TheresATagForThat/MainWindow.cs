using System;
using Gtk;
using Newtonsoft.Json;
using TheresATagForThat;
using System.IO;
using System.Net.Sockets;
using System.Net;

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
		TestObject temp = new TestObject();
		temp.number = 1;
		temp.Name = this.entry1.Text;
		this.label1.Text = JsonConvert.SerializeObject(temp).ToString();

		var jsonVar = new WebClient().DownloadString("http://api.stackoverflow.com/1.1/questions?body=true&pagesize=100&tagged=c%23&page=1");

		Print jsonVar;

		string jsonStr = JsonConvert.SerializeObject(jsonVar, Formatting.Indented);
		File.WriteAllText(@"test.json", jsonStr);

	}
}
